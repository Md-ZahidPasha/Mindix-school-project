<script lang="ts">
	import { onMount } from 'svelte';
	import { getTeacherTimetable } from '$lib/services/teacherApi';
	import {
		CalendarDays,
		Loader2,
		AlertCircle
	} from '@lucide/svelte';

	let slots = $state<any[]>([]);
	let loading = $state(true);
	let error = $state('');

	const days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'];

	const grouped = $derived.by(() => {
		const map: Record<string, any[]> = {};
		for (const day of days) map[day] = [];
		for (const slot of slots) {
			const day = slot.day ?? '';
			if (!map[day]) map[day] = [];
			map[day].push(slot);
		}
		return days.filter((d) => map[d].length > 0).map((d) => ({ day: d, slots: map[d] }));
	});

	async function loadTimetable() {
		try {
			loading = true;
			error = '';
			slots = await getTeacherTimetable();
		} catch (err) {
			console.error('Failed to load teacher timetable:', err);
			error = 'Unable to load timetable.';
		} finally {
			loading = false;
		}
	}

	onMount(loadTimetable);
</script>

<svelte:head>
	<title>My Timetable | PaperBuddy</title>
</svelte:head>

<div class="timetable-page">
	<div class="page-header">
		<div>
			<h1>My Timetable</h1>
			<p>Your teaching schedule.</p>
		</div>
	</div>

	{#if loading}
		<div class="state-card">
			<Loader2 class="spin" size={24} />
			<p>Loading timetable...</p>
		</div>
	{:else if error}
		<div class="state-card error-card">
			<AlertCircle size={24} />
			<p>{error}</p>
		</div>
	{:else if grouped.length === 0}
		<div class="state-card">
			<CalendarDays size={24} />
			<p>No timetable generated yet.</p>
		</div>
	{:else}
		<div class="days-grid">
			{#each grouped as group}
				<div class="day-card">
					<div class="day-header">
						<h2>{group.day}</h2>
					</div>

					<div class="slot-list">
						{#each group.slots as slot}
							<div class="slot">
								<div class="period">
									<span>Period</span>
									<strong>{slot.period}</strong>
								</div>

								<div class="slot-info">
									<strong>{slot.subject ?? '-'}</strong>
									<span>
										{slot.class_name ?? 'Class'} {slot.section ?? ''}
									</span>
									{#if slot.room}
										<span class="room">Room: {slot.room}</span>
									{/if}
								</div>
							</div>
						{/each}
					</div>
				</div>
			{/each}
		</div>
	{/if}
</div>

<style>
	.timetable-page {
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

	.days-grid {
		display: grid;
		grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
		gap: 18px;
	}

	.day-card {
		background: white;
		border: 1px solid #e2e8f0;
		border-radius: 16px;
		padding: 20px;
		box-shadow: 0 4px 15px rgba(15, 23, 42, 0.04);
	}

	.day-header h2 {
		margin: 0 0 16px;
		font-size: 17px;
		font-weight: 800;
		color: #2563eb;
	}

	.slot-list {
		display: flex;
		flex-direction: column;
		gap: 10px;
	}

	.slot {
		display: flex;
		align-items: center;
		gap: 14px;
		padding: 12px;
		background: #f8fafc;
		border: 1px solid #e2e8f0;
		border-radius: 12px;
	}

	.period {
		width: 54px;
		height: 48px;
		flex-shrink: 0;
		display: flex;
		flex-direction: column;
		align-items: center;
		justify-content: center;
		background: #eef4ff;
		border-radius: 10px;
		color: #2563eb;
	}

	.period span {
		font-size: 9px;
		font-weight: 700;
	}

	.period strong {
		font-size: 16px;
	}

	.slot-info strong {
		display: block;
		font-size: 14px;
		color: #0f172a;
	}

	.slot-info span {
		display: block;
		margin-top: 3px;
		font-size: 12px;
		color: #64748b;
	}

	.slot-info .room {
		margin-top: 5px;
		font-size: 11px;
		font-weight: 700;
		color: #2563eb;
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
</style>