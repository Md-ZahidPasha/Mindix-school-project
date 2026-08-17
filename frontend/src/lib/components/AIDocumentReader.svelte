<script lang="ts">
	import { Upload, FileText, Sparkles } from '@lucide/svelte';
	import { API } from '$lib/config/api';

	let selectedFile = $state<File | null>(null);

    let fileInput: HTMLInputElement;

	let isReading = $state(false);
let statusMessage = $state('');
let statusType = $state<'success' | 'error' | 'info' | ''>('');
let extracted = $state<Record<string, unknown> | null>(null);
    
	function handleFileChange(event: Event) {
		const input = event.target as HTMLInputElement;

		if (input.files?.length) {
			selectedFile = input.files[0];
		}
	}
	async function readDocument() {

	if (!selectedFile) {

		statusType = 'error';
		statusMessage = 'Please select a document first.';
		return;

	}

	isReading = true;

	statusType = 'info';
	statusMessage = 'Reading document...';

	try {
		const token = localStorage.getItem('access_token');
		if (!token) throw new Error('Please sign in again to analyze a document.');
		const form = new FormData(); form.append('file', selectedFile);
		const response = await fetch(API.documentExtract, { method: 'POST', headers: { Authorization: `Bearer ${token}` }, body: form });
		const result = await response.json();
		if (!response.ok) throw new Error(result.detail || 'Document analysis failed.');
		extracted = result.data;
		statusType = 'success'; statusMessage = `Extracted ${result.data.document_type || 'document'} details. Review the fields below.`;
	} catch (error) {
		statusType = 'error'; statusMessage = error instanceof Error ? error.message : 'Document analysis failed.';
	} finally { isReading = false; }

}
</script>

<section class="reader-card">

	<h2>AI Document Reader</h2>

	<p class="subtitle">
		Upload a resume, application form or scanned document.
		AI will extract the principal details automatically.
	</p>

	<div class="upload-box">

		<Upload size={42} />

		<h3>Drag & Drop</h3>

		<p>or choose a file</p>

        <input
	bind:this={fileInput}
	type="file"
	accept=".pdf,.jpg,.jpeg,.png"
	onchange={handleFileChange}
	hidden
/>

<button
	type="button"
	class="browse-btn"
	onclick={() => fileInput.click()}
>

	Browse Documents

</button>

		<span class="formats">

			PDF • JPG • PNG

		</span>

	</div>

	<div class="selected-file">

		<FileText size={18} />

		<span>

			{selectedFile ? selectedFile.name : 'No file selected'}

		</span>

	</div>

	<button
	class="reader-btn"
	type="button"
	onclick={readDocument}
	disabled={isReading}
>

	{#if isReading}

	Reading...

{:else}

	<Sparkles size={18} />

	Read & Autofill

{/if}

	</button>

	{#if statusMessage}

	<p class={`status ${statusType}`}>

		{statusMessage}

	</p>

	{/if}

	{#if extracted}
		<div class="extracted"><strong>Extracted fields</strong>{#each Object.entries((extracted.data as Record<string, unknown>) || {}) as [key, value]}<div><span>{key.replaceAll('_', ' ')}</span><input value={String(value)} aria-label={key} /></div>{/each}</div>
	{/if}

</section>

<style lang="scss">

.reader-card{

	background:white;

	border:1px solid #E2E8F0;

	border-radius:24px;

	padding:28px;

	box-shadow:0 10px 25px rgba(15,23,42,.05);

}

.reader-card h2{

	font-size:24px;

	font-weight:700;

	margin-bottom:12px;

	color:#0F172A;

}
.extracted { margin-top: 20px; padding: 16px; border-radius: 12px; background: #f8fafc; border: 1px solid #e2e8f0; }
.extracted > strong { display: block; margin-bottom: 10px; color: #0f172a; }
.extracted div { display: grid; grid-template-columns: 1fr 2fr; gap: 10px; margin-top: 8px; align-items: center; font-size: 13px; }
.extracted span { text-transform: capitalize; color: #475569; }
.extracted input { min-width: 0; padding: 8px; border: 1px solid #cbd5e1; border-radius: 7px; }

.subtitle{

	color:#64748B;

	line-height:1.6;

	margin-bottom:24px;

}

.upload-box{

	border:2px dashed #CBD5E1;

	border-radius:18px;

	padding:32px 20px;

	text-align:center;

	display:flex;

	flex-direction:column;

	align-items:center;

	gap:14px;

}

.upload-box input{

	width:100%;

}

.formats{

	font-size:13px;

	color:#64748B;

	font-weight:600;

}

.browse-btn{

	background:#2563EB;

	color:white;

	border:none;

	padding:12px 24px;

	border-radius:12px;

	font-size:14px;

	font-weight:600;

	cursor:pointer;

	transition:.25s;

}

.browse-btn:hover{

	background:#1D4ED8;

}

.selected-file{

	margin-top:22px;

	padding:14px;

	background:#F8FAFC;

	border-radius:12px;

	display:flex;

	align-items:center;

	gap:10px;

	color:#334155;

}

.reader-btn{

	margin-top:24px;

	width:100%;

	height:52px;

	border:none;

	border-radius:14px;

	background:#2563EB;

	color:white;

	font-size:15px;

	font-weight:700;

	display:flex;

	align-items:center;

	justify-content:center;

	gap:10px;

	cursor:pointer;

	transition:.25s;

}

.reader-btn:hover{

	background:#1D4ED8;

}

.reader-btn:disabled{

	background:#94A3B8;

	cursor:not-allowed;

}

.status{

	margin-top:18px;

	font-size:14px;

	font-weight:600;

	text-align:center;

}

.status.error{

	color:#DC2626;

}

.status.info{

	color:#2563EB;

}

.status.success{

	color:#16A34A;

}

</style>
