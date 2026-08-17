<script lang="ts">
	import { FileText, CheckCircle2, XCircle, Clock, ShieldCheck, RefreshCw } from '@lucide/svelte';
	import {
		getCertificates,
		reviewCertificate,
		type Certificate
	} from '$lib/services/certificates';

	let certificates = $state<Certificate[]>([]);
	let isLoading = $state(true);
	let error = $state('');
	let success = $state('');

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

	async function approve(cert: Certificate) {
		error = '';
		success = '';
		try {
			const number = `CERT-${Date.now().toString().slice(-8)}`;
			await reviewCertificate(cert.id, {
				status: 'approved',
				certificate_number: number,
				issue_date: new Date().toISOString().slice(0, 10)
			});
			success = `Certificate approved (${number}).`;
			await load();
		} catch (err) {
			error = err instanceof Error ? err.message : 'Unable to approve certificate.';
		}
	}

	async function reject(cert: Certificate) {
		const reason = window.prompt('Reason for rejection:', 'Documentation incomplete');
		if (reason === null) return;
		error = '';
		success = '';
		try {
			await reviewCertificate(cert.id, { status: 'rejected', rejection_reason: reason });
			success = 'Certificate request rejected.';
			await load();
		} catch (err) {
			error = err instanceof Error ? err.message : 'Unable to reject certificate.';
		}
	}

	const pending = $derived(certificates.filter((c) => (c.status || '').toLowerCase() === 'pending'));
	const approved = $derived(certificates.filter((c) => ['approved', 'issued'].includes((c.status || '').toLowerCase())));
	const rejected = $derived(certificates.filter((c) => (c.status || '').toLowerCase() === 'rejected'));

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
				<p>Review and approve student certificate requests</p>
			</div>
		</div>
		<button class="refresh-btn" type="button" onclick={load}>
			<RefreshCw size={15} /> Refresh
		</button>
	</div>

	{#if error}
		<div class="error-box">{error}</div>
	{/if}
	{#if success}
		<div class="success-box">{success}</div>
	{/if}

	<div class="summary-grid">
		<div class="summary-card">
			<div class="summary-icon pending-icon"><Clock size={20} /></div>
			<div><span>Pending</span><strong>{pending.length}</strong></div>
		</div>
		<div class="summary-card">
			<div class="summary-icon approved-icon"><CheckCircle2 size={20} /></div>
			<div><span>Approved</span><strong>{approved.length}</strong></div>
		</div>
		<div class="summary-card">
			<div class="summary-icon rejected-icon"><XCircle size={20} /></div>
			<div><span>Rejected</span><strong>{rejected.length}</strong></div>
		</div>
	</div>

	<section class="card">
		<h2>Certificate Requests</h2>
		{#if isLoading}
			<p class="empty">Loading...</p>
		{:else if certificates.length === 0}
			<p class="empty">No certificate requests yet.</p>
		{:else}
			<div class="cert-list">
				{#each certificates as cert}
					{@const status = (cert.status || 'pending').toLowerCase()}
					<div class="cert-item">
						<div class="cert-icon"><FileText size={20} /></div>
						<div class="cert-info">
							<strong>{cert.student_name || 'Unknown student'}</strong>
							<span>Roll: {cert.student_roll || '—'} · Class: {cert.class_name || '—'} {cert.section || ''}</span>
							<span class="cert-type">{cert.certificate_name}{cert.purpose ? ` · ${cert.purpose}` : ''}</span>
							{#if cert.rejection_reason}
								<span class="reject-reason">Reason: {cert.rejection_reason}</span>
							{/if}
						</div>
						<div class="cert-status">
							<span class="status-badge status-{status}">
								{(cert.status || 'pending').toUpperCase()}
							</span>
							{#if cert.certificate_number}
								<span class="cert-no"><ShieldCheck size={13} /> {cert.certificate_number}</span>
							{/if}
							<span class="cert-date">{cert.created_at ? new Date(cert.created_at).toLocaleDateString() : ''}</span>
						</div>
						{#if status === 'pending'}
							<div class="actions">
								<button class="approve-btn" type="button" onclick={() => approve(cert)}>Approve</button>
								<button class="reject-btn" type="button" onclick={() => reject(cert)}>Reject</button>
							</div>
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

	.refresh-btn {
		display: flex;
		align-items: center;
		gap: 6px;
		padding: 10px 16px;
		border: 1px solid #e2e8f0;
		border-radius: 10px;
		background: white;
		color: #334155;
		font-size: 13px;
		font-weight: 600;
		cursor: pointer;
	}

	.summary-grid {
		display: grid;
		grid-template-columns: repeat(3, 1fr);
		gap: 16px;
		margin-bottom: 20px;
	}

	.summary-card {
		display: flex;
		align-items: center;
		gap: 14px;
		padding: 20px;
		background: white;
		border: 1px solid #e2e8f0;
		border-radius: 15px;
	}

	.summary-icon {
		display: flex;
		align-items: center;
		justify-content: center;
		width: 44px;
		height: 44px;
		border-radius: 11px;
		flex-shrink: 0;
	}

	.pending-icon {
		color: #d97706;
		background: #fffbeb;
	}

	.approved-icon {
		color: #16a34a;
		background: #f0fdf4;
	}

	.rejected-icon {
		color: #dc2626;
		background: #fef2f2;
	}

	.summary-card span {
		display: block;
		margin-bottom: 5px;
		color: #64748b;
		font-size: 11px;
	}

	.summary-card strong {
		color: #0f172a;
		font-size: 22px;
		font-weight: 800;
	}

	.card {
		padding: 24px;
		background: white;
		border: 1px solid #e2e8f0;
		border-radius: 16px;
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
		min-width: 0;
	}

	.cert-info strong {
		color: #0f172a;
		font-size: 14px;
	}

	.cert-info span {
		color: #64748b;
		font-size: 12px;
	}

	.cert-type {
		color: #334155 !important;
	}

	.reject-reason {
		color: #b91c1c !important;
	}

	.cert-status {
		display: flex;
		flex-direction: column;
		align-items: flex-end;
		gap: 5px;
	}

	.status-badge {
		padding: 5px 10px;
		border-radius: 20px;
		font-size: 11px;
		font-weight: 700;
	}

	.status-pending {
		background: #fef3c7;
		color: #b45309;
	}

	.status-approved,
	.status-issued {
		background: #dcfce7;
		color: #15803d;
	}

	.status-rejected {
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

	.cert-date {
		color: #94a3b8;
		font-size: 11px;
	}

	.actions {
		display: flex;
		gap: 8px;
		flex-shrink: 0;
	}

	.approve-btn,
	.reject-btn {
		padding: 8px 13px;
		border-radius: 9px;
		font-size: 12px;
		font-weight: 600;
		cursor: pointer;
	}

	.approve-btn {
		border: none;
		background: #16a34a;
		color: white;
	}

	.reject-btn {
		border: 1px solid #fecaca;
		background: white;
		color: #dc2626;
	}

	.empty {
		color: #94a3b8;
		font-size: 13px;
		text-align: center;
		padding: 30px 0;
	}

	@media (max-width: 900px) {
		.cert-page {
			padding: 18px;
		}

		.summary-grid {
			grid-template-columns: 1fr;
		}

		.cert-item {
			flex-wrap: wrap;
		}

		.cert-status {
			align-items: flex-start;
		}
	}
</style>