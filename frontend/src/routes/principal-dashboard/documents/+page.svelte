<script lang="ts">
	import PrincipalSidebar from '$lib/components/principal/PrincipalSidebar.svelte';
	import { extractDocument, type ExtractResult } from '$lib/services/documents';
	import { FileUp, Loader2, Sparkles } from '@lucide/svelte';

	let file = $state<File | null>(null);
	let loading = $state(false);
	let error = $state('');
	let result: ExtractResult | null = $state(null);

	async function handleExtract() {
		error = '';
		result = null;
		if (!file) {
			error = 'Please choose a document first.';
			return;
		}
		loading = true;
		try {
			result = await extractDocument(file);
		} catch (err) {
			error = err instanceof Error ? err.message : 'Failed to process document.';
		} finally {
			loading = false;
		}
	}

	function formatValue(value: unknown): string {
		if (value === null || value === undefined) return '—';
		if (typeof value === 'object') return JSON.stringify(value, null, 2);
		return String(value);
	}
</script>

<div class="principal-layout">
	<PrincipalSidebar />

	<main class="main-content">
		<header class="page-header">
			<div>
				<h1>AI Document Reader</h1>
				<p>Upload a document and let AI extract structured information from it.</p>
			</div>
		</header>

		<div class="reader-card">
			<div class="drop-zone">
				<label for="doc-file" class="file-label">
					<FileUp size={30} />
					<span>{file ? file.name : 'Click to choose a document (PDF, image, doc)'}</span>
				</label>
				<input
					id="doc-file"
					type="file"
					accept=".pdf,.png,.jpg,.jpeg,.doc,.docx,.txt"
					onchange={(e) => {
						const target = e.currentTarget as HTMLInputElement;
						file = target.files?.[0] ?? null;
						error = '';
						result = null;
					}}
				/>
			</div>

			{#if error}
				<div class="alert error">{error}</div>
			{/if}

			<button type="button" class="extract-button" onclick={handleExtract} disabled={loading || !file}>
				{#if loading}
					<Loader2 size={18} class="spin" />
					Processing…
				{:else}
					<Sparkles size={18} />
					Extract with AI
				{/if}
			</button>
		</div>

		{#if result}
			<div class="result-card">
				<div class="result-head">
					<div>
						<h3>Extracted Information</h3>
						<p>{result.filename}</p>
					</div>
					{#if result.data?.document_type}
						<span class="badge">{result.data.document_type}</span>
					{/if}
				</div>

				{#if result.data?.data}
					<div class="data-grid">
						{#each Object.entries(result.data.data) as [key, value]}
							<div class="data-item">
								<span>{key.replace(/_/g, ' ')}</span>
								<pre>{formatValue(value)}</pre>
							</div>
						{/each}
					</div>
				{:else}
					<p class="empty">No structured data was extracted from this document.</p>
				{/if}
			</div>
		{/if}
	</main>
</div>

<style>
	.principal-layout {
		display: flex;
		min-height: 100vh;
		background: #f7f9fc;
	}

	.main-content {
		flex: 1;
		padding: 28px 32px;
		box-sizing: border-box;
	}

	.page-header {
		margin-bottom: 24px;
	}

	.page-header h1 {
		margin: 0;
		color: #14213d;
		font-size: 30px;
	}

	.page-header p {
		margin: 7px 0 0;
		color: #64748b;
		font-size: 15px;
	}

	.reader-card {
		padding: 24px;
		background: white;
		border: 1px solid #e5eaf2;
		border-radius: 16px;
		box-shadow: 0 4px 14px rgba(15, 23, 42, 0.03);
	}

	.drop-zone {
		display: flex;
		align-items: center;
		justify-content: center;
		padding: 34px;
		border: 2px dashed #cbd5e1;
		border-radius: 14px;
		background: #f8fafc;
	}

	.file-label {
		display: flex;
		flex-direction: column;
		align-items: center;
		gap: 12px;
		color: #64748b;
		font-size: 14px;
		cursor: pointer;
		text-align: center;
	}

	.file-label svg {
		color: #2563eb;
	}

	#doc-file {
		display: none;
	}

	.extract-button {
		display: inline-flex;
		align-items: center;
		gap: 8px;
		height: 44px;
		margin-top: 18px;
		padding: 0 24px;
		border: none;
		border-radius: 10px;
		background: #2563eb;
		color: white;
		font-size: 14px;
		font-weight: 600;
		cursor: pointer;
	}

	.extract-button:hover {
		background: #1d4ed8;
	}

	.extract-button:disabled {
		background: #94a3b8;
		cursor: not-allowed;
	}

	.alert {
		margin-top: 14px;
		padding: 12px 16px;
		border-radius: 10px;
		font-size: 13px;
	}

	.alert.error {
		background: #fef2f2;
		color: #b91c1c;
		border: 1px solid #fecaca;
	}

	.result-card {
		margin-top: 18px;
		padding: 22px;
		background: white;
		border: 1px solid #e5eaf2;
		border-radius: 16px;
		box-shadow: 0 4px 14px rgba(15, 23, 42, 0.03);
	}

	.result-head {
		display: flex;
		align-items: center;
		justify-content: space-between;
		gap: 12px;
		margin-bottom: 18px;
	}

	.result-head h3 {
		margin: 0;
		color: #14213d;
		font-size: 18px;
	}

	.result-head p {
		margin: 5px 0 0;
		color: #64748b;
		font-size: 12px;
	}

	.badge {
		padding: 6px 12px;
		border-radius: 999px;
		background: #eef4ff;
		color: #2563eb;
		font-size: 12px;
		font-weight: 600;
		white-space: nowrap;
	}

	.data-grid {
		display: grid;
		grid-template-columns: repeat(2, 1fr);
		gap: 14px;
	}

	.data-item {
		padding: 14px;
		background: #f8fafc;
		border: 1px solid #e5eaf2;
		border-radius: 10px;
		min-width: 0;
	}

	.data-item span {
		display: block;
		margin-bottom: 6px;
		color: #64748b;
		font-size: 11px;
		text-transform: capitalize;
	}

	.data-item pre {
		margin: 0;
		color: #1e293b;
		font-size: 13px;
		white-space: pre-wrap;
		word-break: break-word;
		font-family: inherit;
	}

	.empty {
		color: #64748b;
		font-size: 13px;
	}

	.spin {
		animation: spin 1s linear infinite;
	}

	@keyframes spin {
		to {
			transform: rotate(360deg);
		}
	}

	@media (max-width: 700px) {
		.main-content {
			padding: 20px;
		}

		.data-grid {
			grid-template-columns: 1fr;
		}
	}
</style>