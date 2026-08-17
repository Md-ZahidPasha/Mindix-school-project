<script lang="ts">
	import { onMount } from 'svelte';
	import {
		getLeaveApplications,
		createLeaveApplication,
		type LeaveApplication
	} from '$lib/services/leave';
	import {
		CalendarClock,
		Loader2,
		AlertCircle,
		Plus
	} from '@lucide/svelte';

	let leaveRequests = $state<LeaveApplication[]>([]);
	let loading = $state(true);
	let error = $state('');
	let saving = $state(false);
	let savedMessage = $state('');
	let showForm = $state(false);

	let leaveType = $state('Casual Leave');
	let startDate = $state('');
	let endDate = $state('');
	let reason = $state('');

	const myLeave = $derived(
		leaveRequests.filter(
			(l) => l.user_id === localStorage.getItem('user_id')
		)
	);

	const pendingCount = $derived(
		myLeave.filter((l) => (l.status ?? '').toLowerCase() === 'pending').length
	);

	async function loadLeave() {
		try {
			loading = true;
			error = '';
			const institution_id = localStorage.getItem('institution_id');
			if (!institution_id) throw new Error('Missing institution context.');
			leaveRequests = await getLeaveApplications(institution_id);
		} catch (err) {
			console.error('Failed to load leave requests:', err);
			error = 'Unable to load leave requests.';
		} finally {
			loading = false;
		}
	}

	onMount(loadLeave);

	function formatDate(value: string): string {
		const date = new Date(value);
		return date.toLocaleDateString('en-US', {
			day: 'numeric',
			month: 'short',
			year: 'numeric'
		});
	}

	async function submitLeave() {
		if (!startDate || !endDate) {
			savedMessage = 'Please select both start and end dates.';
			return;
		}
		if (new Date(endDate) < new Date(startDate)) {
			savedMessage = 'End date cannot be before the start date.';
			return;
		}

		saving = true;
		savedMessage = '';
		try {
			await createLeaveApplication({
				user_id: localStorage.getItem('user_id')!,
				institution_id: localStorage.getItem('institution_id')!,
				leave_type: leaveType,
				start_date: startDate,
				end_date: endDate,
				reason: reason || undefined
			});
			savedMessage = 'Leave request submitted successfully.';
			showForm = false;
			reason = '';
			await loadLeave();
		} catch (err) {
			console.error('Failed to submit leave:', err);
			savedMessage = err instanceof Error ? err.message : 'Failed to submit leave request.';
		} finally {
			saving = false;
		}
	}
</script>

<svelte:head>
	<title>Apply Leave | PaperBuddy</title>
</svelte:head>

<div class="leave-page">
	<div class="page-header">
		<div>
			<h1>Apply Leave</h1>
			<p>Manage your leave requests.</p>
		</div>

		<button
			class="btn-primary"
			type="button"
			onclick={() => {
				showForm = !showForm;
				savedMessage = '';
			}}
		>
			<Plus size={18} />
			{showForm ? 'Close Form' : 'Apply Leave'}
		</button>
	</div>

	{#if showForm}
		<section class="form-card">
			<h2>New Leave Request</h2>

			<div class="form-grid">
				<label>
					<span>Leave Type</span>
					<select bind:value={leaveType}>
						<option>Casual Leave</option>
						<option>Sick Leave</option>
						<option>Medical Leave</option>
						<option>Earned Leave</option>
						<option>Emergency Leave</option>
					</select>
				</label>

				<label>
					<span>Start Date</span>
					<input type="date" bind:value={startDate} />
				</label>

				<label>
					<span>End Date</span>
					<input type="date" bind:value={endDate} />
				</label>

				<label class="full">
					<span>Reason</span>
					<textarea
						bind:value={reason}
						rows="3"
						placeholder="Optional reason for leave..."
					></textarea>
				</label>
			</div>

			<div class="form-actions">
				{#if savedMessage}
					<span class:error-msg={savedMessage.includes('Failed') || savedMessage.includes('select')} class="saved">
						{savedMessage}
					</span>
				{/if}

				<button
					class="btn-primary"
					type="button"
					onclick={submitLeave}
					disabled={saving}
				>
					{saving ? 'Submitting...' : 'Submit Request'}
				</button>
			</div>
		</section>
	{/if}

	<div class="summary-cards">
		<div class="summary-card">
			<span>My Leave Requests</span>
			<strong>{myLeave.length}</strong>
		</div>
		<div class="summary-card">
			<span>Pending Requests</span>
			<strong>{pendingCount}</strong>
		</div>
	</div>

	{#if loading}
		<div class="state-card">
			<Loader2 class="spin" size={24} />
			<p>Loading leave requests...</p>
		</div>
	{:else if error}
		<div class="state-card error-card">
			<AlertCircle size={24} />
			<p>{error}</p>
		</div>
	{:else if myLeave.length === 0}
		<div class="state-card">
			<CalendarClock size={24} />
			<p>No leave requests yet.</p>
		</div>
	{:else}
		<div class="leave-list">
			{#each myLeave as request}
				<div class="leave-item">
					<div class="leave-info">
						<strong>{request.leave_type}</strong>
						<span>
							{formatDate(request.start_date)} - {formatDate(request.end_date)}
						</span>
						{#if request.reason}
							<p class="reason">{request.reason}</p>
						{/if}
					</div>
					<span class="leave-status">
						{request.status ?? 'Pending'}
					</span>
				</div>
			{/each}
		</div>
	{/if}
</div>

<style>
	.leave-page {
		padding: 36px;
		max-width: 1000px;
	}

	.page-header {
		display: flex;
		align-items: center;
		justify-content: space-between;
		flex-wrap: wrap;
		gap: 20px;
		margin-bottom: 28px;
	}

	.page-header h1 {
		margin: 0 0 8px;
		font-size: 30px;
		font-weight: 800;
		color: #0f172a;
	}

	.page-header p {
		margin: 0;
		font-size: 15px;
		color: #64748b;
	}

	.btn-primary {
		display: inline-flex;
		align-items: center;
		gap: 8px;
		padding: 12px 20px;
		background: #2563eb;
		border: none;
		border-radius: 11px;
		color: white;
		font-size: 14px;
		font-weight: 700;
		cursor: pointer;
		transition: 0.2s;
	}

	.btn-primary:hover {
		background: #1d4ed8;
	}

	.btn-primary:disabled {
		opacity: 0.6;
		cursor: not-allowed;
	}

	.form-card {
		background: white;
		border: 1px solid #e2e8f0;
		border-radius: 16px;
		padding: 24px;
		margin-bottom: 28px;
	}

	.form-card h2 {
		margin: 0 0 20px;
		font-size: 18px;
		font-weight: 800;
		color: #0f172a;
	}

	.form-grid {
		display: grid;
		grid-template-columns: 1fr 1fr;
		gap: 16px;
	}

	.form-grid label {
		display: flex;
		flex-direction: column;
		gap: 7px;
	}

	.form-grid label.full {
		grid-column: 1 / -1;
	}

	.form-grid label > span {
		font-size: 12px;
		font-weight: 700;
		color: #475569;
	}

	.form-grid select,
	.form-grid input,
	.form-grid textarea {
		padding: 11px 12px;
		background: #f8fafc;
		border: 1px solid #e2e8f0;
		border-radius: 10px;
		font-size: 14px;
		color: #0f172a;
		font-family: inherit;
	}

	.form-grid textarea {
		resize: vertical;
	}

	.form-actions {
		display: flex;
		align-items: center;
		justify-content: flex-end;
		gap: 16px;
		margin-top: 18px;
	}

	.saved {
		font-size: 13px;
		font-weight: 700;
		color: #059669;
	}

	.saved.error-msg {
		color: #dc2626;
	}

	.summary-cards {
		display: grid;
		grid-template-columns: 1fr 1fr;
		gap: 18px;
		margin-bottom: 28px;
	}

	.summary-card {
		padding: 20px;
		background: white;
		border: 1px solid #e2e8f0;
		border-radius: 14px;
	}

	.summary-card span {
		display: block;
		margin-bottom: 6px;
		font-size: 13px;
		color: #64748b;
	}

	.summary-card strong {
		font-size: 26px;
		font-weight: 800;
		color: #0f172a;
	}

	.leave-list {
		background: white;
		border: 1px solid #e2e8f0;
		border-radius: 16px;
		overflow: hidden;
	}

	.leave-item {
		display: flex;
		align-items: center;
		justify-content: space-between;
		gap: 20px;
		padding: 18px 22px;
		border-bottom: 1px solid #e2e8f0;
	}

	.leave-item:last-child {
		border-bottom: none;
	}

	.leave-info strong {
		display: block;
		font-size: 15px;
		color: #0f172a;
	}

	.leave-info span {
		display: block;
		margin-top: 4px;
		font-size: 13px;
		color: #64748b;
	}

	.leave-info .reason {
		margin: 6px 0 0;
		font-size: 12px;
		color: #94a3b8;
	}

	.leave-status {
		padding: 7px 12px;
		border-radius: 9px;
		background: #fff7ed;
		color: #ea580c;
		font-size: 11px;
		font-weight: 700;
		white-space: nowrap;
	}

	.leave-status {
		text-transform: capitalize;
	}

	.state-card {
		display: flex;
		align-items: center;
		justify-content: center;
		gap: 10px;
		padding: 40px;
		background: white;
		border: 1px solid #e2e8f0;
		border-radius: 18px;
		color: #64748b;
	}

	.state-card p {
		margin: 0;
	}

	.error-card {
		color: #dc2626;
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
		.form-grid {
			grid-template-columns: 1fr;
		}
	}
</style>