<script lang="ts">
	import { onMount } from 'svelte';
	import { CalendarDays, Clock } from '@lucide/svelte';
	import { getTimetable, getDashboard, type StudentDashboard } from '$lib/services/studentApi';

	const DAYS = [
		'Monday',
		'Tuesday',
		'Wednesday',
		'Thursday',
		'Friday',
		'Saturday',
		'Sunday'
	];

	let dashboard = $state<StudentDashboard | null>(null);
	let slots = $state<
		{ day?: string | null; period: number; subject: string; teacher: string; room?: string | null }[]
	>([]);
	let loading = $state(true);
	let error = $state('');

	onMount(async () => {
		try {
			dashboard = await getDashboard();
			slots = dashboard.timetable.slots ?? [];
		} catch (err) {
			error = err instanceof Error ? err.message : 'Could not load your timetable.';
		} finally {
			loading = false;
		}
	});

	const gridDays = $derived(DAYS.filter((day) => slots.some((slot) => slot.day === day)));

	const gridPeriods = $derived.by(() => {
		let max = 0;
		for (const slot of slots) {
			if (slot.period > max) max = slot.period;
		}
		return Array.from({ length: max }, (_, index) => index + 1);
	});

	function slotAt(day: string, period: number) {
		return slots.find((slot) => slot.day === day && slot.period === period);
	}
</script>

<svelte:head>
	<title>My Timetable | PaperBuddy</title>
</svelte:head>

<div class="timetable-page">
	<div class="page-header">
		<div class="title-section">
			<div class="title-icon">
				<CalendarDays size={26} />
			</div>
			<div>
				<h1>My Timetable</h1>
				<p>
					{dashboard ? `${dashboard.student.class ?? ''}${dashboard.student.section ? ` ${dashboard.student.section}` : ''} • ${dashboard.student.name}` : 'Your weekly class schedule'}
				</p>
			</div>
		</div>
	</div>

	{#if loading}
		<div class="status-box">Loading your timetable…</div>
	{:else if error}
		<div class="status-box error">
			{error}
			<button type="button" onclick={() => { loading = true; error = ''; getTimetable().then((data) => { slots = data.slots ?? []; }).finally(() => (loading = false)); }}>
				Try Again
			</button>
		</div>
	{:else if slots.length === 0}
		<div class="status-box">
			<CalendarDays size={22} />
			<p>No timetable has been published for your class yet.</p>
		</div>
	{:else}
		<section class="grid-card">
			<div class="table-scroll">
				<table class="timetable-grid">
					<thead>
						<tr>
							<th class="period-col">Period</th>
							{#each gridDays as day}
								<th>{day}</th>
							{/each}
						</tr>
					</thead>
					<tbody>
						{#each gridPeriods as period}
							<tr>
								<td class="period-col">
									<div class="period-cell">
										<Clock size={13} />
										{period}
									</div>
								</td>
								{#each gridDays as day}
									{@const slot = slotAt(day, period)}
									<td>
										{#if slot}
											<div class="slot">
												<strong>{slot.subject}</strong>
												<span>{slot.teacher}</span>
												{#if slot.room}<span class="room">{slot.room}</span>{/if}
											</div>
										{:else}
											<div class="empty-slot"></div>
										{/if}
									</td>
								{/each}
							</tr>
						{/each}
					</tbody>
				</table>
			</div>
		</section>
	{/if}
</div>

<style>
	.timetable-page {
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
		font-size: 30px;
		font-weight: 800;
	}

	.page-header p {
		margin: 6px 0 0;
		color: #64748b;
		font-size: 13px;
	}

	.status-box {
		display: flex;
		align-items: center;
		flex-direction: column;
		gap: 10px;
		padding: 40px 20px;
		color: #64748b;
		background: white;
		border: 1px solid #e2e8f0;
		border-radius: 16px;
		font-size: 13px;
	}

	.status-box.error {
		color: #b91c1c;
		border-color: #fecaca;
		background: #fef2f2;
	}

	.status-box button {
		padding: 8px 14px;
		color: white;
		background: #2563eb;
		border: none;
		border-radius: 9px;
		cursor: pointer;
		font-size: 12px;
		font-weight: 600;
	}

	.grid-card {
		padding: 26px;
		background: white;
		border: 1px solid #e2e8f0;
		border-radius: 16px;
		box-shadow: 0 5px 18px rgba(15, 23, 42, 0.04);
	}

	.table-scroll {
		overflow-x: auto;
	}

	.timetable-grid {
		width: 100%;
		border-collapse: separate;
		border-spacing: 6px;
	}

	.timetable-grid th {
		padding: 9px 12px;
		color: #475569;
		background: #f1f5f9;
		border-radius: 8px;
		font-size: 11px;
		text-align: left;
		font-weight: 700;
	}

	.timetable-grid .period-col {
		color: #64748b;
		font-size: 11px;
		text-align: center;
	}

	.period-cell {
		display: inline-flex;
		align-items: center;
		gap: 4px;
		color: #2563eb;
		font-weight: 700;
	}

	.slot {
		display: flex;
		flex-direction: column;
		gap: 3px;
		min-width: 128px;
		padding: 9px 11px;
		background: #eff6ff;
		border: 1px solid #dbeafe;
		border-radius: 9px;
		font-size: 10px;
	}

	.slot strong {
		color: #1d4ed8;
		font-size: 11px;
	}

	.slot span {
		color: #475569;
	}

	.slot .room {
		color: #94a3b8;
	}

	.empty-slot {
		min-width: 128px;
		height: 34px;
		background: #f8fafc;
		border: 1px dashed #e2e8f0;
		border-radius: 9px;
	}

	@media (max-width: 640px) {
		.timetable-page {
			padding: 20px;
		}

		.grid-card {
			padding: 16px;
		}
	}
</style>