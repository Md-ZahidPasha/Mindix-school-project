<script lang="ts">
	import { Upload, FileText, Sparkles } from '@lucide/svelte';

	let selectedFile = $state<File | null>(null);

    let fileInput: HTMLInputElement;

	let isReading = $state(false);
let statusMessage = $state('');
let statusType = $state<'success' | 'error' | 'info' | ''>('');
    
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

	await new Promise(resolve => setTimeout(resolve, 2000));

	isReading = false;

	statusType = 'info';
	statusMessage =
		'AI extraction is not available yet. Waiting for backend integration.';

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