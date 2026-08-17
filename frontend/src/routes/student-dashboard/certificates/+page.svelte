<script lang="ts">
	import { FileText, Download, CheckCircle2, Clock, XCircle, ShieldCheck } from '@lucide/svelte';
	import {
		getCertificates,
		requestCertificate,
		type Certificate
	} from '$lib/services/certificates';

	let certificates = $state<Certificate[]>([]);
	let isLoading = $state(true);
	let error = $state('');
	let success = $state('');

	let showForm = $state(false);
	let submitting = $state(false);
	let formError = $state('');
	let certificateName = $state('Bonafide');
	let certificateType = $state('bonafide');
	let purpose = $state('');

	const certificateTypes = [
		{ name: 'Bonafide', type: 'bonafide' },
		{ name: 'School Leaving Certificate', type: 'leaving' },
		{ name: 'Character Certificate', type: 'character' },
		{ name: 'Transfer Certificate', type: 'transfer' }
	];

	async function load() {
		isLoading = true;
		error = '';
		try {
			certificates = await getCertificates();
		} catch (err) {
			error = err instanceof Error ? err.message : 'Unable to load certificates.';
		} finally {
			isLoading = false;
		}
	}

	async function submitRequest() {
		formError = '';
		submitting = true;
		try {
			const studentId = localStorage.getItem('student_id');
			const institutionId = localStorage.getItem('institution_id');
			if (!studentId || !institutionId) {
				formError = 'Student scope is missing. Please sign in again.';
				return;
			}
			await requestCertificate({
				student_id: studentId,
				institution_id: institutionId,
				certificate_name: certificateName,
				certificate_type: certificateType,
				purpose: purpose || undefined
			});
			success = 'Certificate request submitted successfully.';
			showForm = false;
			purpose = '';
			await load();
		} catch (err) {
			formError = err instanceof Error ? err.message : 'Unable to submit request.';
		} finally {
			submitting = false;
		}
	}

	function statusIcon(status: string | null | undefined) {
		const s = (status || '').toLowerCase();
		if (s === 'approved' || s === 'issued') return CheckCircle2;
		if (s === 'rejected') return XCircle;
		return Clock;
	}

	function printCertificate(cert: Certificate) {
		const w = window.open('', '_blank');
		if (!w) return;
		w.document.write(`<html><head><title>${cert.certificate_name}</title><style>
			body{font-family:Georgia,serif;margin:0;padding:40px;color:#1e293b;}
			.school{text-align:center;font-size:22px;font-weight:bold;letter-spacing:1px;}
			.addr{text-align:center;color:#64748b;font-size:13px;margin-top:4px;}
			.line{height:2px;background:#2563eb;margin:16px 0 28px;}
			.title{text-align:center;font-size:26px;font-weight:bold;text-decoration:underline;margin-bottom:30px;}
			.body{font-size:15px;line-height:2;max-width:680px;margin:0 auto;}
			.footer{margin-top:50px;max-width:680px;margin-left:auto;margin-right:auto;display:flex;justify-content:space-between;}
			.sign{font-size:14px;}
			</style></head><body>
			<div class="school">${cert.institution_name || ''}</div>
			<div class="addr">${cert.institution_name ? '' : ''}</div>
			<div class="line"></div>
			<div class="title">${cert.certificate_name.toUpperCase()}</div>
			<div class="body">
			<p>Certificate No: <strong>${cert.certificate_number || ''}</strong></p>
			<p>This is to certify that <strong>${cert.student_name || ''}</strong> (Roll No: ${cert.student_roll || ''})
			of <strong>${cert.class_name || ''}</strong> ${cert.section ? 'Section ' + cert.section : ''}
			is a bonafide student of ${cert.institution_name || 'the institution'}.</p>
			<p>Purpose: ${cert.purpose || ''}</p>
			<p>Date of issue: <strong>${cert.issue_date || ''}</strong></p>
			</div>
			<div class="footer"><div class="sign">Student</div><div class="sign">Authorized Signatory</div></div>
			</body></html>`);
		w.document.close();
	}

	$effect(() => {
		load();
	});
</script>

<div class="cert-page">
	<div class="page-header">
		<div class="title-section">
			<div class="title-icon">
				<FileText size={26} />
			</div>
			<div>
				<h1>Certificates</h1>
				<p>Request bonafide and school certificates</p>
			</div>
		</div>
		<button class="primary-btn" type="button" onclick={() => (showForm = !showForm)}>
			{showForm ? 'Cancel' : '+ New Request'}
		</button>
	</div>

	{#if error}
		<div class="error-box">{error}</div>
	{/if}
	{#if success}
		<div class="success-box">{success}</div>
	{/if}

	{#if showForm}
		<section class="card request-card">
			<h2>Request a Certificate</h2>
			<div class="form-grid">
				<div class="form-group">
					<label>Certificate Type</label>
					<select bind:value={certificateName}>
						{#each certificateTypes as t}
							<option value={t.name}>{t.name}</option>
						{/each}
					</select>
				</div>
				<div class="form-group">
					<label>Purpose</label>
					<input type="text" bind:value={purpose} placeholder="e.g. Bank loan, admission, government exam" />
				</div>
			</div>
			{#if formError}<p class="form-error">{formError}</p>{/if}
			<button class="primary-btn" type="button" onclick={submitRequest} disabled={submitting}>
				{submitting ? 'Submitting...' : 'Submit Request'}
			</button>
		</section>
	{/if}

	<section class="card">
		<h2>My Requests</h2>
		{#if isLoading}
			<p class="empty">Loading...</p>
		{:else if certificates.length === 0}
			<p class="empty">No certificate requests yet.</p>
		{:else}
			<div class="cert-list">
				{#each certificates as cert}
					{@const Icon = statusIcon(cert.status)}
					<div class="cert-item">
						<div class="cert-icon"><Icon size={22} /></div>
						<div class="cert-info">
							<strong>{cert.certificate_name}</strong>
							<span>{cert.purpose || 'No purpose specified'}</span>
							{#if cert.rejection_reason}
								<span class="reject-reason">Reason: {cert.rejection_reason}</span>
							{/if}
						</div>
						<div class="cert-status">
							<span class:approved={cert.status === 'approved' || cert.status === 'issued'} class:rejected={cert.status === 'rejected'} class="status-badge">
								{(cert.status || 'pending').toUpperCase()}
							</span>
							<span class="cert-no">
								{#if cert.certificate_number}
									<ShieldCheck size={13} /> {cert.certificate_number}
								{/if}
							</span>
						</div>
						{#if cert.status === 'approved' || cert.status === 'issued'}
							<button class="view-btn" type="button" onclick={() => printCertificate(cert)}>
								<Download size={15} /> View
							</button>
						{/if}
					</div>
				{/each}
			</div>
		{/if}
	</section>
</div>

<style>
	.cert-page {
		min-height: 100vh;
		padding: 36px;
		box-sizing: border-box;
		background: #f8fafc;
	}

	.page-header {
		display: flex;
		align-items: center;
		justify-content: space-between;
		gap: 20px;
		margin-bottom: 24px;
	}

	.title-section {
		display: flex;
		align-items: center;
		gap: 14px;
	}

	.title-icon {
		display: flex;
		align-items: center;
		justify-content: center;
		width: 50px;
		height: 50px;
		color: #2563eb;
		background: #eff6ff;
		border-radius: 13px;
	}

	.page-header h1 {
		margin: 0;
		color: #0f172a;
		font-size: 28px;
		font-weight: 800;
	}

	.page-header p {
		margin: 5px 0 0;
		color: #64748b;
		font-size: 13px;
	}

	.primary-btn {
		padding: 11px 18px;
		border: none;
		border-radius: 10px;
		background: #2563eb;
		color: white;
		font-size: 13px;
		font-weight: 600;
		cursor: pointer;
	}

	.primary-btn:hover:not(:disabled) {
		background: #1d4ed8;
	}

	.primary-btn:disabled {
		opacity: 0.7;
		cursor: not-allowed;
	}

	.card {
		padding: 24px;
		background: white;
		border: 1px solid #e2e8f0;
		border-radius: 16px;
		margin-bottom: 20px;
	}

	.card h2 {
		margin: 0 0 18px;
		color: #0f172a;
		font-size: 17px;
		font-weight: 700;
	}

	.error-box {
		padding: 12px 16px;
		margin-bottom: 16px;
		background: #fef2f2;
		border: 1px solid #fecaca;
		border-radius: 10px;
		color: #b91c1c;
		font-size: 13px;
	}

	.success-box {
		padding: 12px 16px;
		margin-bottom: 16px;
		background: #f0fdf4;
		border: 1px solid #bbf7d0;
		border-radius: 10px;
		color: #15803d;
		font-size: 13px;
	}

	.form-grid {
		display: grid;
		grid-template-columns: 1fr 1fr;
		gap: 14px;
		margin-bottom: 18px;
	}

	.form-group {
		display: flex;
		flex-direction: column;
		gap: 7px;
	}

	.form-group label {
		color: #0f172a;
		font-size: 13px;
		font-weight: 600;
	}

	.form-group select,
	.form-group input {
		height: 44px;
		padding: 0 12px;
		border: 1px solid #cbd5e1;
		border-radius: 10px;
		background: white;
		color: #0f172a;
		font-size: 13px;
		outline: none;
	}

	.form-error {
		color: #dc2626;
		font-size: 13px;
	}

	.cert-list {
		display: flex;
		flex-direction: column;
		gap: 10px;
	}

	.cert-item {
		display: flex;
		align-items: center;
		gap: 14px;
		padding: 14px;
		border: 1px solid #e2e8f0;
		border-radius: 12px;
		background: #f8fafc;
	}

	.cert-icon {
		display: flex;
		align-items: center;
		justify-content: center;
		width: 42px;
		height: 42px;
		border-radius: 10px;
		color: #2563eb;
		background: #eff6ff;
		flex-shrink: 0;
	}

	.cert-info {
		flex: 1;
		display: flex;
		flex-direction: column;
		gap: 3px;
	}

	.cert-info strong {
		color: #0f172a;
		font-size: 14px;
	}

	.cert-info span {
		color: #64748b;
		font-size: 12px;
	}

	.reject-reason {
		color: #b91c1c !important;
	}

	.cert-status {
		display: flex;
		flex-direction: column;
		align-items: flex-end;
		gap: 6px;
	}

	.status-badge {
		padding: 5px 10px;
		border-radius: 20px;
		font-size: 11px;
		font-weight: 700;
		background: #fef3c7;
		color: #b45309;
	}

	.status-badge.approved {
		background: #dcfce7;
		color: #15803d;
	}

	.status-badge.rejected {
		background: #fee2e2;
		color: #b91c1c;
	}

	.cert-no {
		display: flex;
		align-items: center;
		gap: 4px;
		color: #64748b;
		font-size: 11px;
	}

	.view-btn {
		display: flex;
		align-items: center;
		gap: 5px;
		padding: 8px 12px;
		border: 1px solid #2563eb;
		border-radius: 9px;
		background: white;
		color: #2563eb;
		font-size: 12px;
		font-weight: 600;
		cursor: pointer;
		flex-shrink: 0;
	}

	.empty {
		color: #94a3b8;
		font-size: 13px;
		text-align: center;
		padding: 20px 0;
	}

	@media (max-width: 700px) {
		.cert-page {
			padding: 18px;
		}

		.form-grid {
			grid-template-columns: 1fr;
		}

		.cert-item {
			flex-wrap: wrap;
		}
	}
</style>