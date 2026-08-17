<script lang="ts">
	import { CalendarDays, CheckCircle2, XCircle, Clock, Users, RefreshCw, Sparkles } from '@lucide/svelte';
	import { getLeaveApplications, updateLeaveApplication, type LeaveApplication } from '$lib/services/leave';
	import { suggestSubstitutes, confirmSubstitution, type SubstituteSuggestion } from '$lib/services/substitution';

	let leaves = $state<LeaveApplication[]>([]);
	let isLoading = $state(true);
	let error = $state('');
	let success = $state('');

	let suggestions = $state<SubstituteSuggestion[]>([]);
	let suggestionsLoading = $state(false);
	let selectedLeave = $state<string | null>(null);

	async function load() {
		isLoading = true;
		error = '';
		try {
			const institutionId = localStorage.getItem('institution_id');
			if (!institutionId) throw new Error('Institution scope is missing. Please sign in again.');
			leaves = await getLeaveApplications(institutionId);
		} catch (err) {
			error = err instanceof Error ? err.message : 'Unable to load leave applications.';
		} finally {
			isLoading = false;
		}
	}

	async function review(leave: LeaveApplication, status: string) {
		error = '';
		success = '';
		try {
			const institutionId = localStorage.getItem('institution_id');
			await updateLeaveApplication(leave.id, institutionId!, { status });
			success = `Leave ${status} successfully.`;
			await load();
		} catch (err) {
			error = err instanceof Error ? err.message : 'Unable to update leave status.';
		}
	}

	async function getSuggestions(leave: LeaveApplication) {
		error = '';
		success = '';
		suggestionsLoading = true;
		selectedLeave = leave.id;
		suggestions = [];
		try {
			suggestions = await suggestSubstitutes(leave.id);
			if (suggestions.length === 0) {
				success = 'No substitute teachers are available for this leave.';
			}
		} catch (err) {
			error = err instanceof Error ? err.message : 'Unable to suggest substitutes.';
		} finally {
			suggestionsLoading = false;
		}
	}

	async function confirm(suggestion: SubstituteSuggestion) {
		error = '';
		success = '';
		try {
			await confirmSubstitution({
				leave_application_id: suggestion.leave_application_id,
				teacher_id: suggestion.teacher_id || undefined,
				substitute_teacher_id: suggestion.substitute_teacher_id,
				class_id: suggestion.class_id,
				subject_id: suggestion.subject_id || undefined,
				day_of_week: suggestion.day_of_week,
				period: suggestion.period
			});
			success = `Substitution confirmed — ${suggestion.substitute_name} will cover the class.`;
			suggestions = [];
			selectedLeave = null;
		} catch (err) {
			error = err instanceof Error ? err.message : 'Unable to confirm substitution.';
		}
	}

	function fmtDate(value: string): string {
		const d = new Date(value);
		if (isNaN(d.getTime())) return value;
		return d.toLocaleDateString();
	}

	const pending = $derived(leaves.filter((l) => (l.status || '').toLowerCase() === 'pending'));
	const approved = $derived(leaves.filter((l) => (l.status || '').toLowerCase() === 'approved'));
	const rejected = $derived(leaves.filter((l) => (l.status || '').toLowerCase() === 'rejected'));

	$effect(() => {
		load();
	});
</script>

<div class="leave-page">
	<div class="page-header">
		<div class="title-section">
			<div class="title-icon">
				<CalendarDays size={26} />
			</div>
			<div>
				<h1>Leave & Substitution</h1>
				<p>Review leave applications and assign substitute teachers</p>
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
		<h2>Leave Applications</h2>
		{#if isLoading}
			<p class="empty">Loading...</p>
		{:else if leaves.length === 0}
			<p class="empty">No leave applications yet.</p>
		{:else}
			<div class="leave-list">
				{#each leaves as leave}
					{@const status = (leave.status || 'pending').toLowerCase()}
					<div class="leave-item">
						<div class="leave-icon"><CalendarDays size={19} /></div>
						<div class="leave-info">
							<strong>{leave.leave_type}</strong>
							<span>{fmtDate(leave.start_date)} → {fmtDate(leave.end_date)}</span>
							<span class="reason">{leave.reason || 'No reason provided'}</span>
							<span class="applied">Applied: {leave.created_at ? fmtDate(leave.created_at) : '—'}</span>
						</div>
						<div class="leave-status">
							<span class="status-badge status-{status}">
								{(leave.status || 'pending').toUpperCase()}
							</span>
						</div>
						{#if status === 'pending'}
							<div class="actions">
								<button class="approve-btn" type="button" onclick={() => review(leave, 'approved')}>
									<CheckCircle2 size={14} /> Approve
								</button>
								<button class="reject-btn" type="button" onclick={() => review(leave, 'rejected')}>
									<XCircle size={14} /> Reject
								</button>
								<button class="suggest-btn" type="button" onclick={() => getSuggestions(leave)}>
									<Users size={14} /> Substitute
								</button>
							</div>
						{/if}
					</div>
				{/each}
			</div>
		{/if}
	</section>

	{#if selectedLeave}
		<section class="card suggestions-card">
			<div class="suggestions-header">
				<div class="title-section">
					<div class="title-icon sparkle-icon">
						<Sparkles size={20} />
					</div>
					<div>
						<h2>Suggested Substitutes</h2>
						<p>Smart substitution suggestions for this leave</p>
					</div>
				</div>
				<button class="close-btn" type="button" onclick={() => (selectedLeave = null)}>×</button>
			</div>

			{#if suggestionsLoading}
				<p class="empty">Finding substitutes...</p>
			{:else if suggestions.length === 0}
				<p class="empty">No substitute suggestions available.</p>
			{:else}
				<div class="suggestion-list">
					{#each suggestions as suggestion}
						<div class="suggestion-item">
							<div class="suggestion-icon"><Users size={18} /></div>
							<div class="suggestion-info">
								<strong>{suggestion.substitute_name}</strong>
								<span>
									{suggestion.subject_name || 'Subject'} · {suggestion.class_name || 'Class'} · Day {suggestion.day_of_week} · Period {suggestion.period}
								</span>
								<span class="reason">{suggestion.reason}</span>
							</div>
							<button class="confirm-btn" type="button" onclick={() => confirm(suggestion)}>
								Assign
							</button>
						</div>
					{/each}
				</div>
			{/if}
		</section>
	{/if}
</div>

<style>
	.leave-page {
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

	.sparkle-icon {
		color: #7c3aed;
		background: #f5f3ff;
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
		margin-bottom: 20px;
	}

	.card h2 {
		margin: 0 0 16px;
		color: #0f172a;
		font-size: 17px;
		font-weight: 700;
	}

	.suggestions-card {
		border-color: #ddd6fe;
		background: #fafaff;
	}

	.suggestions-header {
		display: flex;
		align-items: flex-start;
		justify-content: space-between;
		gap: 15px;
		margin-bottom: 16px;
	}

	.close-btn {
		width: 32px;
		height: 32px;
		border: 1px solid #e2e8f0;
		border-radius: 8px;
		background: white;
		color: #64748b;
		font-size: 20px;
		line-height: 1;
		cursor: pointer;
		flex-shrink: 0;
	}

	.leave-list,
	.suggestion-list {
		display: flex;
		flex-direction: column;
		gap: 10px;
	}

	.leave-item {
		display: flex;
		align-items: center;
		gap: 14px;
		padding: 14px;
		border: 1px solid #e2e8f0;
		border-radius: 12px;
		background: #f8fafc;
		flex-wrap: wrap;
	}

	.leave-icon {
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

	.leave-info {
		flex: 1;
		display: flex;
		flex-direction: column;
		gap: 3px;
		min-width: 0;
	}

	.leave-info strong {
		color: #0f172a;
		font-size: 14px;
	}

	.leave-info span {
		color: #64748b;
		font-size: 12px;
	}

	.reason {
		color: #334155 !important;
	}

	.applied {
		color: #94a3b8 !important;
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

	.status-approved {
		background: #dcfce7;
		color: #15803d;
	}

	.status-rejected {
		background: #fee2e2;
		color: #b91c1c;
	}

	.actions {
		display: flex;
		gap: 8px;
		flex-shrink: 0;
		flex-wrap: wrap;
	}

	.approve-btn,
	.reject-btn,
	.suggest-btn,
	.confirm-btn {
		display: flex;
		align-items: center;
		gap: 5px;
		padding: 8px 12px;
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

	.suggest-btn {
		border: 1px solid #ddd6fe;
		background: white;
		color: #7c3aed;
	}

	.suggestion-item {
		display: flex;
		align-items: center;
		gap: 14px;
		padding: 14px;
		border: 1px solid #e2e8f0;
		border-radius: 12px;
		background: white;
	}

	.suggestion-icon {
		display: flex;
		align-items: center;
		justify-content: center;
		width: 42px;
		height: 42px;
		border-radius: 10px;
		color: #7c3aed;
		background: #f5f3ff;
		flex-shrink: 0;
	}

	.suggestion-info {
		flex: 1;
		display: flex;
		flex-direction: column;
		gap: 3px;
		min-width: 0;
	}

	.suggestion-info strong {
		color: #0f172a;
		font-size: 14px;
	}

	.suggestion-info span {
		color: #64748b;
		font-size: 12px;
	}

	.confirm-btn {
		border: none;
		background: #7c3aed;
		color: white;
		flex-shrink: 0;
	}

	.empty {
		color: #94a3b8;
		font-size: 13px;
		text-align: center;
		padding: 24px 0;
	}

	@media (max-width: 900px) {
		.leave-page {
			padding: 18px;
		}

		.summary-grid {
			grid-template-columns: 1fr;
		}

		.actions {
			width: 100%;
		}
	}
</style>