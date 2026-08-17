<script lang="ts">
	import { onMount } from 'svelte';
	import { getTeacherStudents, getTeacherClasses } from '$lib/services/teacherApi';
	import { API } from '$lib/config/api';
	import { apiFetch } from '$lib/services/apiClient';
	import {
		ClipboardCheck,
		Loader2,
		AlertCircle,
		CheckCircle2,
		XCircle
	} from '@lucide/svelte';

	let students = $state<any[]>([]);
	let classes = $state<any[]>([]);
	let loading = $state(true);
	let error = $state('');
	let saving = $state(false);
	let savedMessage = $state('');
	let selectedClass = $state<string>('all');

	const attendanceDate = new Date().toISOString().slice(0, 10);

	const statusMap = $state<Record<string, string>>({});

	const filteredStudents = $derived(
		selectedClass === 'all'
			? students
			: students.filter((s) => s.class_id === selectedClass)
	);

	async function loadData() {
		try {
			loading = true;
			error = '';
			[students, classes] = await Promise.all([
				getTeacherStudents(),
				getTeacherClasses()
			]);
			for (const s of students) {
				statusMap[s.id] = 'present';
			}
		} catch (err) {
			console.error('Failed to load data:', err);
			error = 'Unable to load students.';
		} finally {
			loading = false;
		}
	}

	onMount(loadData);

	function setStatus(id: string, status: string) {
		statusMap[id] = status;
	}

	function markAll(status: string) {
		for (const s of filteredStudents) {
			statusMap[s.id] = status;
		}
	}

	async function submitAttendance() {
		saving = true;
		savedMessage = '';
		const institution_id = localStorage.getItem('institution_id');
		const teacher_id = localStorage.getItem('teacher_id');
		let ok = 0;

		for (const s of filteredStudents) {
			try {
				await apiFetch(`${API.baseUrl}/api/attendance`, {
					method: 'POST',
					body: JSON.stringify({
						student_id: s.id,
						class_id: s.class_id,
						attendance_date: attendanceDate,
						status: statusMap[s.id] ?? 'present',
						institution_id,
						attendance_type: 'student',
						teacher_id,
						attendance_mode: 'full_day'
					})
				});
				ok += 1;
			} catch (err) {
				console.error('Failed to save attendance for', s.full_name, err);
			}
		}

		saving = false;
		savedMessage = `Saved attendance for ${ok} of ${filteredStudents.length} students.`;
	}
</script>

<svelte:head>
	<title>Attendance | PaperBuddy</title>
</svelte:head>

<div class="attendance-page">
	<div class="page-header">
		<div>
			<h1>Mark Attendance</h1>
			<p>Record today's attendance for your students.</p>
		</div>

		<div class="controls">
			<select
				bind:value={selectedClass}
				aria-label="Select class"
			>
				<option value="all">All Classes</option>
				{#each classes as cls}
					<option value={cls.id}>{cls.class_name} {cls.section ?? ''}</option>
				{/each}
			</select>

			<button
				class="btn-outline"
				type="button"
				onclick={() => markAll('present')}
			>
				All Present
			</button>

			<button
				class="btn-outline"
				type="button"
				onclick={() => markAll('absent')}
			>
				All Absent
			</button>
		</div>
	</div>

	{#if loading}
		<div class="state-card">
			<Loader2 class="spin" size={24} />
			<p>Loading students...</p>
		</div>
	{:else if error}
		<div class="state-card error-card">
			<AlertCircle size={24} />
			<p>{error}</p>
		</div>
	{:else if filteredStudents.length === 0}
		<div class="state-card">
			<ClipboardCheck size={24} />
			<p>No students to mark attendance for.</p>
		</div>
	{:else}
		<div class="attendance-table">
			<div class="table-header">
				<span>Student</span>
				<span>Class</span>
				<span>Status</span>
			</div>

			{#each filteredStudents as student}
				<div class="table-row">
					<div class="student-cell">
						<div class="avatar">
							{(student.full_name ?? 'S').charAt(0).toUpperCase()}
						</div>
						<div>
							<strong>{student.full_name ?? '-'}</strong>
							<span>{student.roll_number ?? '-'}</span>
						</div>
					</div>

					<span>{student.class_name ?? '-'} {student.section ?? ''}</span>

					<div class="status-actions">
						<button
							class:selected={statusMap[student.id] === 'present'}
							class="status-btn present"
							type="button"
							onclick={() => setStatus(student.id, 'present')}
						>
							<CheckCircle2 size={16} />
							Present
						</button>
						<button
							class:selected={statusMap[student.id] === 'absent'}
							class="status-btn absent"
							type="button"
							onclick={() => setStatus(student.id, 'absent')}
						>
							<XCircle size={16} />
							Absent
						</button>
					</div>
				</div>
			{/each}
		</div>

		<div class="save-bar">
			{#if savedMessage}
				<span class="saved">{savedMessage}</span>
			{/if}

			<button
				class="btn-primary"
				type="button"
				onclick={submitAttendance}
				disabled={saving}
			>
				{saving ? 'Saving...' : `Save Attendance (${filteredStudents.length})`}
			</button>
		</div>
	{/if}
</div>

<style>
	.attendance-page {
		padding: 36px;
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

	.controls {
		display: flex;
		align-items: center;
		gap: 10px;
		flex-wrap: wrap;
	}

	select {
		height: 42px;
		padding: 0 12px;
		background: white;
		border: 1px solid #e2e8f0;
		border-radius: 10px;
		font-size: 13px;
		color: #0f172a;
	}

	.btn-outline {
		height: 42px;
		padding: 0 14px;
		background: white;
		border: 1px solid #e2e8f0;
		border-radius: 10px;
		font-size: 13px;
		font-weight: 700;
		color: #2563eb;
		cursor: pointer;
		transition: 0.2s;
	}

	.btn-outline:hover {
		background: #eef4ff;
	}

	.attendance-table {
		background: white;
		border: 1px solid #e2e8f0;
		border-radius: 16px;
		overflow: hidden;
	}

	.table-header,
	.table-row {
		display: grid;
		grid-template-columns: 1.4fr 0.8fr 1.2fr;
		align-items: center;
		gap: 15px;
		padding: 14px 20px;
	}

	.table-header {
		background: #f8fafc;
		font-size: 12px;
		font-weight: 700;
		color: #64748b;
	}

	.table-row {
		border-top: 1px solid #e2e8f0;
		font-size: 13px;
		color: #475569;
	}

	.student-cell {
		display: flex;
		align-items: center;
		gap: 12px;
	}

	.avatar {
		width: 38px;
		height: 38px;
		flex-shrink: 0;
		display: flex;
		align-items: center;
		justify-content: center;
		background: #eef4ff;
		color: #2563eb;
		font-size: 15px;
		font-weight: 800;
		border-radius: 10px;
	}

	.student-cell strong {
		display: block;
		color: #0f172a;
	}

	.student-cell span {
		display: block;
		margin-top: 2px;
		font-size: 12px;
		color: #94a3b8;
	}

	.status-actions {
		display: flex;
		gap: 8px;
	}

	.status-btn {
		display: flex;
		align-items: center;
		gap: 6px;
		padding: 8px 12px;
		background: #f8fafc;
		border: 1px solid #e2e8f0;
		border-radius: 9px;
		font-size: 12px;
		font-weight: 700;
		color: #64748b;
		cursor: pointer;
		transition: 0.2s;
	}

	.status-btn.present.selected {
		background: #ecfdf5;
		border-color: #6ee7b7;
		color: #059669;
	}

	.status-btn.absent.selected {
		background: #fef2f2;
		border-color: #fca5a5;
		color: #dc2626;
	}

	.save-bar {
		display: flex;
		align-items: center;
		justify-content: flex-end;
		gap: 16px;
		margin-top: 20px;
	}

	.saved {
		font-size: 13px;
		font-weight: 700;
		color: #059669;
	}

	.btn-primary {
		padding: 13px 22px;
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

	@media (max-width: 800px) {
		.table-header,
		.table-row {
			grid-template-columns: 1fr;
			gap: 8px;
		}
	}
</style>