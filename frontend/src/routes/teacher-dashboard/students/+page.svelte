<script lang="ts">
	import { onMount } from 'svelte';
	import { getTeacherStudents } from '$lib/services/teacherApi';
	import {
		Users,
		Search,
		Mail,
		Loader2,
		AlertCircle
	} from '@lucide/svelte';

	let students = $state<any[]>([]);
	let loading = $state(true);
	let error = $state('');
	let search = $state('');

	const filteredStudents = $derived(
		search.trim()
			? students.filter((s) =>
					`${s.full_name ?? ''} ${s.roll_number ?? ''} ${s.class_name ?? ''}`
						.toLowerCase()
						.includes(search.toLowerCase())
				)
			: students
	);

	async function loadStudents() {
		try {
			loading = true;
			error = '';
			students = await getTeacherStudents();
		} catch (err) {
			console.error('Failed to load teacher students:', err);
			error = 'Unable to load students.';
		} finally {
			loading = false;
		}
	}

	onMount(loadStudents);
</script>

<svelte:head>
	<title>My Students | PaperBuddy</title>
</svelte:head>

<div class="students-page">
	<div class="page-header">
		<div>
			<h1>My Students</h1>
			<p>Students in the classes you teach.</p>
		</div>

		<div class="search-box">
			<Search size={18} />
			<input
				type="text"
				placeholder="Search students..."
				bind:value={search}
			/>
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
			<Users size={24} />
			<p>No students found.</p>
		</div>
	{:else}
		<div class="students-grid">
			{#each filteredStudents as student}
				<div class="student-card">
					<div class="avatar">
						{(student.full_name ?? 'S').charAt(0).toUpperCase()}
					</div>

					<div class="student-info">
						<strong>{student.full_name ?? '-'}</strong>
						<span>{student.class_name ?? '-'} {student.section ?? ''}</span>
					</div>

					<div class="student-meta">
						<span class="badge">Roll {student.roll_number ?? '-'}</span>
						<span class="badge">{student.student_id ?? '-'}</span>
					</div>

					{#if student.email}
						<div class="email">
							<Mail size={14} />
							<span>{student.email}</span>
						</div>
					{/if}
				</div>
			{/each}
		</div>
	{/if}
</div>

<style>
	.students-page {
		padding: 36px;
	}

	.page-header {
		display: flex;
		align-items: center;
		justify-content: space-between;
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

	.search-box {
		width: 260px;
		height: 44px;
		display: flex;
		align-items: center;
		gap: 10px;
		padding: 0 14px;
		background: white;
		border: 1px solid #e2e8f0;
		border-radius: 12px;
	}

	.search-box svg {
		color: #64748b;
	}

	.search-box input {
		width: 100%;
		border: none;
		outline: none;
		background: transparent;
		font-size: 14px;
		color: #0f172a;
	}

	.students-grid {
		display: grid;
		grid-template-columns: repeat(3, 1fr);
		gap: 18px;
	}

	.student-card {
		display: flex;
		flex-direction: column;
		gap: 12px;
		padding: 22px;
		background: white;
		border: 1px solid #e2e8f0;
		border-radius: 16px;
		box-shadow: 0 4px 15px rgba(15, 23, 42, 0.04);
		transition: 0.25s;
	}

	.student-card:hover {
		border-color: #bfdbfe;
		transform: translateY(-2px);
	}

	.avatar {
		width: 52px;
		height: 52px;
		display: flex;
		align-items: center;
		justify-content: center;
		background: #eef4ff;
		color: #2563eb;
		font-size: 22px;
		font-weight: 800;
		border-radius: 14px;
	}

	.student-info strong {
		display: block;
		font-size: 16px;
		color: #0f172a;
	}

	.student-info span {
		display: block;
		margin-top: 4px;
		font-size: 13px;
		color: #64748b;
	}

	.student-meta {
		display: flex;
		flex-wrap: wrap;
		gap: 8px;
	}

	.badge {
		padding: 5px 10px;
		background: #f8fafc;
		border: 1px solid #e2e8f0;
		border-radius: 8px;
		font-size: 11px;
		font-weight: 700;
		color: #475569;
	}

	.email {
		display: flex;
		align-items: center;
		gap: 6px;
		font-size: 12px;
		color: #64748b;
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

	@media (max-width: 1100px) {
		.students-grid {
			grid-template-columns: repeat(2, 1fr);
		}
	}

	@media (max-width: 700px) {
		.students-grid {
			grid-template-columns: 1fr;
		}
	}
</style>