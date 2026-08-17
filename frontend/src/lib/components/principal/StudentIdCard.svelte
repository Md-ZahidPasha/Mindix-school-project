<script lang="ts">
	import { onMount } from 'svelte';
	import QRCode from 'qrcode';

	interface Props {
		code: string;
		name?: string | null;
		rollNumber?: string | null;
		className?: string | null;
		section?: string | null;
		institutionName?: string;
	}

	let {
		code,
		name,
		rollNumber,
		className,
		section,
		institutionName = 'School ID Card'
	}: Props = $props();

	let qrDataUrl = $state('');
	let error = $state('');

	onMount(() => {
		QRCode.toDataURL(code, { width: 220, margin: 1 })
			.then((url) => {
				qrDataUrl = url;
			})
			.catch((err) => {
				error = err instanceof Error ? err.message : 'Could not generate QR code.';
			});
	});

	const initials = $derived(
		(name || code)
			.split(/\s+/)
			.filter(Boolean)
			.map((p) => p[0]?.toUpperCase())
			.join('')
			.slice(0, 2)
	);
</script>

<section class="id-card">
	<div class="id-head">
		<h3>{institutionName}</h3>
	</div>

	<div class="id-body">
		<div class="id-photo">{initials}</div>

		<div class="id-info">
			<strong>{name || code}</strong>
			<span>ID: {code}</span>
			{#if rollNumber}<span>Roll: {rollNumber}</span>{/if}
			{#if className}<span>Class: {className}{#if section} - {section}{/if}</span>{/if}
		</div>
	</div>

	<div class="id-qr">
		{#if qrDataUrl}
			<img src={qrDataUrl} alt={`QR code for ${code}`} />
		{:else if error}
			<p class="qr-error">{error}</p>
		{:else}
			<p class="qr-loading">Generating…</p>
		{/if}
		<p class="qr-hint">Scan this QR to mark attendance</p>
	</div>
</section>

<style>
	.id-card {
		margin-bottom: 18px;
		padding: 22px;
		background: white;
		border: 1px solid #e5eaf2;
		border-radius: 16px;
		box-shadow: 0 4px 14px rgba(15, 23, 42, 0.03);
	}

	.id-head h3 {
		margin: 0 0 16px;
		color: #14213d;
		font-size: 16px;
	}

	.id-body {
		display: flex;
		align-items: center;
		gap: 16px;
	}

	.id-photo {
		width: 62px;
		height: 62px;
		display: flex;
		align-items: center;
		justify-content: center;
		flex-shrink: 0;
		background: #eaf1ff;
		color: #2563eb;
		border-radius: 50%;
		font-size: 19px;
		font-weight: 700;
	}

	.id-info {
		display: flex;
		flex-direction: column;
		gap: 3px;
		min-width: 0;
	}

	.id-info strong {
		color: #14213d;
		font-size: 16px;
	}

	.id-info span {
		color: #64748b;
		font-size: 12px;
	}

	.id-qr {
		display: flex;
		flex-direction: column;
		align-items: center;
		margin-top: 18px;
		padding-top: 18px;
		border-top: 1px dashed #e5eaf2;
	}

	.id-qr img {
		width: 160px;
		height: 160px;
		image-rendering: pixelated;
	}

	.qr-error,
	.qr-loading {
		height: 160px;
		display: flex;
		align-items: center;
		justify-content: center;
		color: #64748b;
		font-size: 13px;
	}

	.qr-error {
		color: #dc2626;
	}

	.qr-hint {
		margin: 10px 0 0;
		color: #94a3b8;
		font-size: 12px;
	}
</style>