<script lang="ts">
	import { onMount } from 'svelte';
	import { getTeacherProfile } from '$lib/services/teacherApi';
	import { getTeacherDashboard } from '$lib/services/teacherApi';
	import { Bell, Loader2, AlertCircle, CalendarDays, Users } from '@lucide/svelte';

	let loading = $state(true);
	let error = $state('');
	let items = $state<any[]>([]);

	function formatDate(value: string): string {
		const date = new Date(value);
		return date.toLocaleDateString('en-US', {
			day: 'numeric',
			month: 'short'
		});
	}

	async function loadNotifications() {
		try {
			loading = true;
			error = '';
			const [profile, dashboard] = await Promise.all([
				getTeacherProfile(),
				getTeacherDashboard()
			]);

			const notifications: any[] = [];

			for (const slot of dashboard?.today_schedule ?? []) {
				notifications.push({
					type: 'class',
					icon: CalendarDays,
					title: `${slot.subject} class today`,
					body: `${slot.class_name} ${slot.section ?? ''} • Period ${slot.period}${slot.room ? ` • ${slot.room}` : ''}`,
					time: 'Today'
				});
			}

			const leaveCount = (dashboard?.leave_requests ?? []).length;
			if (leaveCount > 0) {
				notifications.push({
					type: 'leave',
					icon: Bell,
					title: `${leaveCount} leave request${leaveCount > 1 ? 's' : ''}`,
					body: 'Review your recent leave requests.',
					time: 'Recent'
				});
			}

			if ((dashboard?.stats?.students ?? 0) > 0) {
				notifications.push({
					type: 'students',
					icon: Users,
					title: `${dashboard.stats.students} students assigned`,
					body: 'You can mark attendance from the Attendance page.',
					time: 'Info'
				});
			}

			notifications.push({
				type: 'welcome',
				icon: Bell,
				title: `Welcome, ${profile.full_name ?? 'Teacher'}!`,
				body: 'Here is where your updates will appear.',
				time: 'Now'
			});

			items = notifications;
		} catch (err) {
			console.error('Failed to load notifications:', err);
			error = 'Unable to load notifications.';
		} finally {
			loading = false;
		}
	}

	onMount(loadNotifications);
</script>

<svelte:head>
	<title>Notifications | PaperBuddy</title>
</svelte:head>

<div class="notifications-page">
	<div class="page-header">
		<div>
			<h1>Notifications</h1>
			<p>Recent updates for your classes.</p>
		</div>
	</div>

	{#if loading}
		<div class="state-card">
			<Loader2 class="spin" size={24} />
			<p>Loading notifications...</p>
		</div>
	{:else if error}
		<div class="state-card error-card">
			<AlertCircle size={24} />
			<p>{error}</p>
		</div>
	{:else if items.length === 0}
		<div class="state-card">
			<Bell size={24} />
			<p>No notifications yet.</p>
		</div>
	{:else}
		<div class="notifications-list">
			{#each items as item}
				<div class="notification-item">
					<div class="notification-icon">
						<item.icon size={20} />
					</div>

					<div class="notification-body">
						<strong>{item.title}</strong>
						<p>{item.body}</p>
					</div>

					<span class="notification-time">{item.time}</span>
				</div>
			{/each}
		</div>
	{/if}
</div>

<style>
	.notifications-page {
		padding: 36px;
		max-width: 900px;
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

	.notifications-list {
		background: white;
		border: 1px solid #e2e8f0;
		border-radius: 16px;
		overflow: hidden;
	}

	.notification-item {
		display: flex;
		align-items: center;
		gap: 16px;
		padding: 18px 22px;
		border-bottom: 1px solid #e2e8f0;
	}

	.notification-item:last-child {
		border-bottom: none;
	}

	.notification-icon {
		width: 44px;
		height: 44px;
		flex-shrink: 0;
		display: flex;
		align-items: center;
		justify-content: center;
		background: #eef4ff;
		color: #2563eb;
		border-radius: 11px;
	}

	.notification-body {
		flex: 1;
		min-width: 0;
	}

	.notification-body strong {
		display: block;
		font-size: 14px;
		color: #0f172a;
	}

	.notification-body p {
		margin: 4px 0 0;
		font-size: 13px;
		color: #64748b;
	}

	.notification-time {
		flex-shrink: 0;
		font-size: 11px;
		font-weight: 700;
		color: #94a3b8;
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