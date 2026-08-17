<script lang="ts">
	import { onMount, onDestroy } from 'svelte';
	import jsQR from 'jsqr';
	import { scanLookup, scanRecord, type ScanLookupResult } from '$lib/services/attendance';

	let videoEl = $state<HTMLVideoElement | null>(null);
	let stream: MediaStream | null = null;
	let rafId: number | null = null;
	let canvas = $state<HTMLCanvasElement | null>(null);
	let cameraOn = $state(false);
	let cameraError = $state('');
	let scanning = $state(false);
	let manualId = $state('');
	let result: ScanLookupResult | null = $state(null);
	let feedback = $state('');
	let feedbackType = $state<'success' | 'error' | 'info'>('info');
	let recorded = $state(false);

	onMount(() => {
		canvas = document.createElement('canvas');
	});

	onDestroy(() => {
		if (stream) {
			stream.getTracks().forEach((t) => t.stop());
		}
		if (rafId !== null) {
			cancelAnimationFrame(rafId);
		}
	});

	async function startCamera() {
		cameraError = '';
		try {
			stream = await navigator.mediaDevices.getUserMedia({
				video: { facingMode: 'environment' }
			});
			if (videoEl) {
				videoEl.srcObject = stream;
				await videoEl.play();
			}
			cameraOn = true;
			loop();
		} catch (error) {
			cameraError =
				error instanceof Error
					? error.message
					: 'Camera is not available. Use the student ID input below.';
			feedback = cameraError;
			feedbackType = 'error';
		}
	}

	function stopCamera() {
		if (stream) {
			stream.getTracks().forEach((t) => t.stop());
		}
		stream = null;
		cameraOn = false;
		if (rafId !== null) {
			cancelAnimationFrame(rafId);
			rafId = null;
		}
	}

	function loop() {
		if (!videoEl || !canvas || videoEl.readyState < videoEl.HAVE_ENOUGH_DATA) {
			rafId = requestAnimationFrame(loop);
			return;
		}
		canvas.width = videoEl.videoWidth;
		canvas.height = videoEl.videoHeight;
		const ctx = canvas.getContext('2d', { willReadFrequently: true });
		if (!ctx) {
			rafId = requestAnimationFrame(loop);
			return;
		}
		ctx.drawImage(videoEl, 0, 0, canvas.width, canvas.height);
		const imageData = ctx.getImageData(0, 0, canvas.width, canvas.height);
		const code = jsQR(imageData.data, imageData.width, imageData.height, {
			inversionAttempts: 'dontInvert'
		});
		if (code?.data) {
			handleCode(code.data);
			return;
		}
		rafId = requestAnimationFrame(loop);
	}

	function handleCode(value: string) {
		if (scanning) return;
		const code = value.trim();
		if (!code) return;
		scanning = true;
		if (rafId !== null) {
			cancelAnimationFrame(rafId);
			rafId = null;
		}
		processId(code);
	}

	function processId(id: string) {
		const institutionId = localStorage.getItem('institution_id') || '';
		if (!institutionId) {
			showFeedback('Institution context is missing. Please log in again.', 'error');
			scanning = false;
			return;
		}
		scanLookup(id, institutionId)
			.then((data) => {
				result = data;
				recorded = false;
				if (data.already_marked) {
					showFeedback(
						`${data.full_name || data.code} was already marked (${data.today_status || 'present'}) today.`,
						'info'
					);
				} else {
					showFeedback(`Student identified: ${data.full_name || data.code}`, 'success');
				}
			})
			.catch((error) => {
				result = null;
				showFeedback(error instanceof Error ? error.message : 'Student not found.', 'error');
			})
			.finally(() => {
				scanning = false;
			});
	}

	async function doRecord() {
		if (!result) return;
		const institutionId = localStorage.getItem('institution_id') || '';
		try {
			const res = await scanRecord(result.student_id, institutionId);
			recorded = true;
			showFeedback(res.message, 'success');
		} catch (error) {
			showFeedback(error instanceof Error ? error.message : 'Failed to record attendance.', 'error');
		}
	}

	function onManualSubmit() {
		const id = manualId.trim();
		if (!id) {
			showFeedback('Enter a student ID or roll number.', 'error');
			return;
		}
		if (scanning) return;
		scanning = true;
		processId(id);
	}

	function resetScan() {
		result = null;
		recorded = false;
		feedback = '';
		if (cameraOn) {
			rafId = requestAnimationFrame(loop);
		}
	}

	function showFeedback(message: string, type: 'success' | 'error' | 'info') {
		feedback = message;
		feedbackType = type;
	}
</script>

<section class="qr-scanner">
	<div class="section-header">
		<div>
			<h2>QR / Student-ID Attendance</h2>
			<p>Scan a student QR code or enter a student ID / roll number to mark attendance.</p>
		</div>
	</div>

	<div class="scanner-grid">
		<div class="camera-card">
			<div class="video-wrap">
				{#if cameraOn}
					<video bind:this={videoEl} autoplay muted playsinline></video>
				{:else}
					<div class="placeholder">
						<span>Camera is off</span>
					</div>
				{/if}
			</div>

			<div class="camera-actions">
				{#if cameraOn}
					<button type="button" class="action-button secondary" onclick={stopCamera}>
						Stop Camera
					</button>
				{:else}
					<button type="button" class="action-button" onclick={startCamera}>
						Start Camera
					</button>
				{/if}
				{#if result}
					<button type="button" class="action-button secondary" onclick={resetScan}>
						Scan Next
					</button>
				{/if}
			</div>
		</div>

		<div class="manual-card">
			<label for="student-id-input">Student ID / Roll Number</label>
			<div class="input-row">
				<input
					id="student-id-input"
					type="text"
					placeholder="e.g. STU001 or 564"
					bind:value={manualId}
					onkeydown={(e) => {
						if (e.key === 'Enter') onManualSubmit();
					}}
				/>
				<button type="button" class="action-button" onclick={onManualSubmit} disabled={scanning}>
					{scanning ? 'Checking…' : 'Identify'}
				</button>
			</div>
			<p class="hint">Works with the ID printed on the student's ID card.</p>
		</div>
	</div>

	{#if feedback}
		<div class={`feedback ${feedbackType}`}>{feedback}</div>
	{/if}

	{#if result}
		<div class="result-card">
			<div class="result-head">
				<div>
					<h3>{result.full_name || result.code}</h3>
					<p>
						{result.code}
						{#if result.roll_number} · Roll {result.roll_number}{/if}
						{#if result.class_name} · {result.class_name}{#if result.section} - {result.section}{/if}{/if}
					</p>
				</div>
				{#if result.already_marked}
					<span class="badge marked">Already Marked ({result.today_status || 'present'})</span>
				{:else}
					<span class="badge">Present</span>
				{/if}
			</div>
			<div class="result-actions">
				{#if result.already_marked || recorded}
					<button type="button" class="action-button secondary" disabled>
						{recorded ? 'Attendance Recorded' : 'Already Recorded'}
					</button>
				{:else}
					<button type="button" class="action-button" onclick={doRecord}>
						Record Attendance
					</button>
				{/if}
			</div>
		</div>
	{/if}
</section>

<style>
	.qr-scanner {
		margin-top: 24px;
	}

	.section-header {
		margin-bottom: 14px;
	}

	.section-header h2 {
		margin: 0;
		color: #14213d;
		font-size: 20px;
	}

	.section-header p {
		margin: 5px 0 0;
		color: #64748b;
		font-size: 13px;
	}

	.scanner-grid {
		display: grid;
		grid-template-columns: 1.2fr 1fr;
		gap: 18px;
	}

	.camera-card,
	.manual-card,
	.result-card {
		background: white;
		border: 1px solid #e5eaf2;
		border-radius: 16px;
		box-shadow: 0 4px 14px rgba(15, 23, 42, 0.03);
	}

	.camera-card {
		padding: 14px;
	}

	.video-wrap {
		position: relative;
		width: 100%;
		aspect-ratio: 4 / 3;
		border-radius: 12px;
		overflow: hidden;
		background: #0f172a;
	}

	.video-wrap video {
		width: 100%;
		height: 100%;
		object-fit: cover;
	}

	.placeholder {
		width: 100%;
		height: 100%;
		display: flex;
		align-items: center;
		justify-content: center;
		color: #94a3b8;
		font-size: 13px;
	}

	.camera-actions {
		display: flex;
		gap: 10px;
		margin-top: 12px;
	}

	.manual-card {
		padding: 22px;
		align-self: start;
	}

	.manual-card label {
		display: block;
		margin-bottom: 7px;
		color: #334155;
		font-size: 12px;
		font-weight: 600;
	}

	.input-row {
		display: flex;
		gap: 10px;
	}

	.input-row input {
		flex: 1;
		height: 42px;
		padding: 0 11px;
		box-sizing: border-box;
		border: 1px solid #dbe3ef;
		border-radius: 9px;
		color: #1e293b;
		font-size: 13px;
		outline: none;
	}

	.input-row input:focus {
		border-color: #2563eb;
		box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.1);
	}

	.hint {
		margin: 10px 0 0;
		color: #64748b;
		font-size: 12px;
	}

	.action-button {
		height: 42px;
		padding: 0 18px;
		border: none;
		border-radius: 9px;
		background: #2563eb;
		color: white;
		font-size: 13px;
		font-weight: 600;
		cursor: pointer;
	}

	.action-button:hover {
		background: #1d4ed8;
	}

	.action-button:disabled {
		background: #94a3b8;
		cursor: not-allowed;
	}

	.action-button.secondary {
		background: #f1f5f9;
		color: #334155;
	}

	.action-button.secondary:hover {
		background: #e2e8f0;
	}

	.feedback {
		margin-top: 16px;
		padding: 12px 16px;
		border-radius: 10px;
		font-size: 13px;
	}

	.feedback.success {
		background: #ecfdf5;
		color: #047857;
		border: 1px solid #a7f3d0;
	}

	.feedback.error {
		background: #fef2f2;
		color: #b91c1c;
		border: 1px solid #fecaca;
	}

	.feedback.info {
		background: #eff6ff;
		color: #1d4ed8;
		border: 1px solid #bfdbfe;
	}

	.result-card {
		margin-top: 18px;
		padding: 20px;
	}

	.result-head {
		display: flex;
		align-items: center;
		justify-content: space-between;
		gap: 12px;
	}

	.result-head h3 {
		margin: 0;
		color: #14213d;
		font-size: 18px;
	}

	.result-head p {
		margin: 5px 0 0;
		color: #64748b;
		font-size: 13px;
	}

	.badge {
		padding: 6px 12px;
		border-radius: 999px;
		background: #d1fae5;
		color: #065f46;
		font-size: 12px;
		font-weight: 600;
		white-space: nowrap;
	}

	.badge.marked {
		background: #fef9c3;
		color: #854d0e;
	}

	.result-actions {
		margin-top: 16px;
	}

	@media (max-width: 900px) {
		.scanner-grid {
			grid-template-columns: 1fr;
		}
	}
</style>