<script lang="ts">
	import { onMount } from 'svelte';
	import { getTeacherClasses } from '$lib/services/teacherApi';
	import {
		GraduationCap,
		Users,
		BookOpen,
		Loader2,
		AlertCircle
	} from '@lucide/svelte';

	let classes = $state<any[]>([]);
	let loading = $state(true);
	let error = $state('');

	async function loadClasses() {
		try {
			loading = true;
			error = '';
			classes = await getTeacherClasses();
		} catch (err) {
			console.error('Failed to load teacher classes:', err);
			error = 'Unable to load classes.';
		} finally {
			loading = false;
		}
	}

	onMount(loadClasses);
</script>

<svelte:head>
	<title>My Classes | PaperBuddy</title>
</svelte:head>

<div class="classes-page">
	<div class="page-header">
		<div>
			<h1>My Classes</h1>
			<p>Classes you are assigned to teach.</p>
		</div>
	</div>

	{#if loading}
		<div class="state-card">
			<Loader2 class="spin" size={24} />
			<p>Loading classes...</p>
		</div>
	{:else if error}
		<div class="state-card error-card">
			<AlertCircle size={24} />
			<p>{error}</p>
		</div>
	{:else if classes.length === 0}
		<div class="state-card">
			<BookOpen size={24} />
			<p>No classes assigned yet.</p>
		</div>
	{:else}
		<div class="classes-grid">
			{#each classes as cls}
				<div class="class-card">
					<div class="class-icon">
						<GraduationCap size={24} />
					</div>

					<div class="class-info">
						<strong>
							{cls.class_name} {cls.section ?? ''}
						</strong>
						<span>Assigned Class</span>
						<p>
							<Users size={15} />
							{cls.student_count ?? 0} students
						</p>
					</div>
				</div>
			{/each}
		</div>
	{/if}
</div>

<style>
	.classes-page {
		padding: 36px;
	}

	.page-header {
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

	.classes-grid {
		display: grid;
		grid-template-columns: repeat(3, 1fr);
		gap: 18px;
	}

	.class-card {
		padding: 22px;
		background: white;
		border: 1px solid #e2e8f0;
		border-radius: 16px;
		box-shadow: 0 4px 15px rgba(15, 23, 42, 0.04);
		transition: 0.25s;
	}

	.class-card:hover {
		border-color: #bfdbfe;
		background: #f5f9ff;
		transform: translateY(-2px);
	}

	.class-icon {
		width: 48px;
		height: 48px;
		display: flex;
		align-items: center;
		justify-content: center;
		background: #eef4ff;
		color: #2563eb;
		border-radius: 12px;
		margin-bottom: 16px;
	}

	.class-info > strong {
		display: block;
		font-size: 17px;
		color: #0f172a;
	}

	.class-info > span {
		display: block;
		margin-top: 4px;
		font-size: 13px;
		color: #64748b;
	}

	.class-info p {
		display: flex;
		align-items: center;
		gap: 6px;
		margin: 14px 0 0;
		font-size: 13px;
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
		.classes-grid {
			grid-template-columns: repeat(2, 1fr);
		}
	}

	@media (max-width: 700px) {
		.classes-grid {
			grid-template-columns: 1fr;
		}
	}
</style>