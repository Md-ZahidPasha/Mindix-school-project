<script lang="ts">
	import { onMount } from 'svelte';
	import {
		Search,
		Bell,
		UserCircle2,
		GraduationCap,
		BookOpen,
		Clock3,
		CheckCircle2,
		CalendarDays,
		ClipboardCheck,
		Users,
		ArrowRight,
		Loader2,
		AlertCircle
	} from '@lucide/svelte';
	import { getTeacherDashboard } from '$lib/services/teacherApi';

	let dashboardData = $state<any>(null);
	let loading = $state(true);
	let error = $state('');

	const teacherName = $derived(dashboardData?.teacher?.full_name ?? 'Teacher');

	const today = new Date();
	const currentDate = today.toLocaleDateString('en-US', {
		weekday: 'long',
		day: 'numeric',
		month: 'long',
		year: 'numeric'
	});

	async function loadDashboard() {
		try {
			loading = true;
			error = '';
			dashboardData = await getTeacherDashboard();
		} catch (err) {
			console.error('Failed to load teacher dashboard:', err);
			error = 'Unable to load dashboard data.';
		} finally {
			loading = false;
		}
	}

	onMount(loadDashboard);

	function formatDate(value: string): string {
		if (!value) return '-';
		const date = new Date(value);
		return date.toLocaleDateString('en-US', {
			day: 'numeric',
			month: 'short'
		});
	}
</script>

<div class="dashboard">
	<main class="main-content">
		<header class="header">
			<div class="welcome">
				<h1>Welcome, {teacherName} 👋</h1>
				<p>Here's what's happening with your classes today.</p>
				<span>{currentDate}</span>
			</div>

			<div class="header-actions">
				<div class="search-box">
					<Search size={18} />
					<input type="text" placeholder="Search..." />
				</div>

				<button class="icon-button" type="button" aria-label="Notifications">
					<Bell size={20} />
				</button>

				<div class="profile">
					<UserCircle2 size={40} />
					<div>
						<strong>{teacherName}</strong>
						<span>Teacher</span>
					</div>
				</div>
			</div>
		</header>

		{#if loading}
			<div class="state-box">
				<Loader2 class="spin" size={28} />
				<span>Loading dashboard...</span>
			</div>
		{:else if error}
			<div class="state-box error">
				<AlertCircle size={28} />
				<span>{error}</span>
			</div>
		{:else}
			<section class="stats-grid">
				<div class="stat-card">
					<div class="stat-icon">
						<GraduationCap size={24} />
					</div>
					<div>
						<span>My Classes</span>
						<strong>{dashboardData?.stats?.classes ?? 0}</strong>
					</div>
				</div>

				<div class="stat-card">
					<div class="stat-icon">
						<Users size={24} />
					</div>
					<div>
						<span>My Students</span>
						<strong>{dashboardData?.stats?.students ?? 0}</strong>
					</div>
				</div>

				<div class="stat-card">
					<div class="stat-icon">
						<Clock3 size={24} />
					</div>
					<div>
						<span>Today's Classes</span>
						<strong>{dashboardData?.stats?.today_classes ?? 0}</strong>
					</div>
				</div>

				<div class="stat-card">
					<div class="stat-icon">
						<ClipboardCheck size={24} />
					</div>
					<div>
						<span>Attendance Rate</span>
						<strong>{dashboardData?.attendance?.percentage ?? 0}%</strong>
					</div>
				</div>
			</section>

			<section class="content-grid">
				<div class="large-card schedule-card">
					<div class="section-header">
						<div>
							<h2>Today's Schedule</h2>
							<p>Your classes for today</p>
						</div>
						<a href="/teacher-dashboard/timetable" class="link-btn">
							View Timetable
							<ArrowRight size={16} />
						</a>
					</div>

					{#if (dashboardData?.today_schedule ?? []).length === 0}
						<div class="empty">No classes scheduled today.</div>
					{:else}
						<div class="schedule-list">
							{#each dashboardData?.today_schedule ?? [] as item}
								<div class="schedule-row">
									<div class="time">
										<Clock3 size={17} />
										<span>Period {item.period}</span>
									</div>
									<div>
										<strong>{item.class_name} {item.section ?? ''}</strong>
										<span>{item.subject}</span>
									</div>
									<div class="room">{item.room ?? '-'}</div>
								</div>
							{/each}
						</div>
					{/if}
				</div>

				<div class="large-card attendance-card">
					<div class="section-header">
						<div>
							<h2>Attendance Overview</h2>
							<p>Overall attendance of your students</p>
						</div>
					</div>

					<div class="attendance-value">
						<strong>{dashboardData?.attendance?.percentage ?? 0}%</strong>
						<span>Attendance Rate</span>
					</div>

					<div class="attendance-bar">
						<div
							style="width: {Math.min(dashboardData?.attendance?.percentage ?? 0, 100)}%"
						></div>
					</div>

					<div class="attendance-stats">
						<div>
							<strong>{dashboardData?.attendance?.present ?? 0}</strong>
							<span>Present</span>
						</div>
						<div>
							<strong>{dashboardData?.attendance?.absent ?? 0}</strong>
							<span>Absent</span>
						</div>
						<div>
							<strong>{dashboardData?.attendance?.total ?? 0}</strong>
							<span>Total</span>
						</div>
					</div>
				</div>
			</section>

			<section class="content-grid">
				<div class="large-card">
					<div class="section-header">
						<div>
							<h2>Apply Leave</h2>
							<p>Your recent leave requests</p>
						</div>
						<a href="/teacher-dashboard/leave" class="link-btn">
							Apply Leave
							<ArrowRight size={16} />
						</a>
					</div>

					{#if (dashboardData?.leave_requests ?? []).length === 0}
						<div class="empty">No leave requests yet.</div>
					{:else}
						<div class="leave-list">
							{#each dashboardData?.leave_requests ?? [] as request}
								<div class="leave-item">
									<div>
										<strong>{request.leave_type}</strong>
										<span>
											{formatDate(request.start_date)} - {formatDate(request.end_date)}
										</span>
									</div>
									<span class="leave-status">{request.status}</span>
								</div>
							{/each}
						</div>
					{/if}
				</div>

				<div class="large-card">
					<div class="section-header">
						<div>
							<h2>Quick Actions</h2>
							<p>Frequently used tools</p>
						</div>
					</div>

					<div class="quick-actions">
						<a href="/teacher-dashboard/classes" class="quick-action">
							<div class="quick-icon">
								<BookOpen size={20} />
							</div>
							<span>My Classes</span>
						</a>
						<a href="/teacher-dashboard/students" class="quick-action">
							<div class="quick-icon">
								<Users size={20} />
							</div>
							<span>My Students</span>
						</a>
						<a href="/teacher-dashboard/timetable" class="quick-action">
							<div class="quick-icon">
								<CalendarDays size={20} />
							</div>
							<span>Timetable</span>
						</a>
						<a href="/teacher-dashboard/attendance" class="quick-action">
							<div class="quick-icon">
								<ClipboardCheck size={20} />
							</div>
							<span>Attendance</span>
						</a>
					</div>
				</div>
			</section>
		{/if}
	</main>
</div>

<style>
	.dashboard {
		min-height: 100vh;
		background: #f8fafc;
	}

	.main-content {
		padding: 36px;
		max-width: 1500px;
	}

	.header {
		display: flex;
		align-items: center;
		justify-content: space-between;
		gap: 30px;
		margin-bottom: 32px;
	}

	.welcome h1 {
		margin: 0 0 8px;
		font-size: 30px;
		font-weight: 800;
		color: #0f172a;
	}

	.welcome p {
		margin: 0 0 6px;
		font-size: 15px;
		color: #64748b;
	}

	.welcome span {
		font-size: 14px;
		color: #94a3b8;
	}

	.header-actions {
		display: flex;
		align-items: center;
		gap: 14px;
	}

	.search-box {
		width: 260px;
		height: 46px;
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

	.icon-button {
		width: 46px;
		height: 46px;
		display: flex;
		align-items: center;
		justify-content: center;
		background: white;
		border: 1px solid #e2e8f0;
		border-radius: 12px;
		color: #475569;
		cursor: pointer;
		transition: 0.25s;
	}

	.icon-button:hover {
		background: #eef4ff;
		color: #2563eb;
	}

	.profile {
		display: flex;
		align-items: center;
		gap: 10px;
		padding: 7px 12px;
		background: white;
		border: 1px solid #e2e8f0;
		border-radius: 14px;
	}

	.profile > svg {
		color: #2563eb;
	}

	.profile strong {
		display: block;
		font-size: 14px;
		color: #0f172a;
	}

	.profile span {
		display: block;
		margin-top: 2px;
		font-size: 12px;
		color: #64748b;
	}

	.stats-grid {
		display: grid;
		grid-template-columns: repeat(4, 1fr);
		gap: 18px;
		margin-bottom: 28px;
	}

	.stat-card {
		display: flex;
		align-items: center;
		gap: 16px;
		padding: 22px;
		background: white;
		border: 1px solid #e2e8f0;
		border-radius: 18px;
		box-shadow: 0 4px 15px rgba(15, 23, 42, 0.04);
		transition: 0.25s;
	}

	.stat-card:hover {
		transform: translateY(-2px);
		box-shadow: 0 10px 25px rgba(15, 23, 42, 0.08);
	}

	.stat-icon {
		width: 48px;
		height: 48px;
		flex-shrink: 0;
		display: flex;
		align-items: center;
		justify-content: center;
		background: #eef4ff;
		color: #2563eb;
		border-radius: 13px;
	}

	.stat-card span {
		display: block;
		margin-bottom: 5px;
		font-size: 13px;
		color: #64748b;
	}

	.stat-card strong {
		display: block;
		font-size: 26px;
		font-weight: 800;
		color: #0f172a;
	}

	.content-grid {
		display: grid;
		grid-template-columns: 1.6fr 1.4fr;
		gap: 28px;
		margin-bottom: 28px;
	}

	.large-card {
		background: white;
		border: 1px solid #e2e8f0;
		border-radius: 18px;
		padding: 24px;
		box-shadow: 0 4px 15px rgba(15, 23, 42, 0.04);
	}

	.section-header {
		display: flex;
		align-items: center;
		justify-content: space-between;
		gap: 20px;
		margin-bottom: 22px;
	}

	.section-header h2 {
		margin: 0 0 5px;
		font-size: 20px;
		font-weight: 800;
		color: #0f172a;
	}

	.section-header p {
		margin: 0;
		font-size: 14px;
		color: #64748b;
	}

	.link-btn {
		display: flex;
		align-items: center;
		gap: 7px;
		border: none;
		background: transparent;
		color: #2563eb;
		font-size: 14px;
		font-weight: 700;
		cursor: pointer;
		text-decoration: none;
	}

	.schedule-list {
		display: flex;
		flex-direction: column;
		gap: 10px;
	}

	.schedule-row {
		display: grid;
		grid-template-columns: 130px 1fr 120px;
		align-items: center;
		gap: 18px;
		padding: 15px;
		background: #f8fafc;
		border: 1px solid #e2e8f0;
		border-radius: 13px;
	}

	.time {
		display: flex;
		align-items: center;
		gap: 7px;
		color: #2563eb;
		font-size: 13px;
		font-weight: 700;
	}

	.schedule-row strong {
		display: block;
		font-size: 14px;
		color: #0f172a;
	}

	.schedule-row > div:nth-child(2) span {
		display: block;
		margin-top: 3px;
		font-size: 13px;
		color: #64748b;
	}

	.room {
		text-align: right;
		font-size: 13px;
		color: #64748b;
	}

	.attendance-value {
		margin-bottom: 14px;
	}

	.attendance-value strong {
		display: block;
		font-size: 38px;
		font-weight: 800;
		color: #2563eb;
	}

	.attendance-value span {
		font-size: 13px;
		color: #64748b;
	}

	.attendance-bar {
		width: 100%;
		height: 9px;
		background: #e2e8f0;
		border-radius: 20px;
		overflow: hidden;
		margin-bottom: 20px;
	}

	.attendance-bar div {
		height: 100%;
		background: #2563eb;
		border-radius: 20px;
	}

	.attendance-stats {
		display: grid;
		grid-template-columns: repeat(3, 1fr);
		gap: 10px;
	}

	.attendance-stats > div {
		padding: 12px;
		text-align: center;
		background: #f8fafc;
		border-radius: 12px;
	}

	.attendance-stats strong {
		display: block;
		font-size: 18px;
		color: #0f172a;
	}

	.attendance-stats span {
		font-size: 12px;
		color: #64748b;
	}

	.leave-list {
		display: flex;
		flex-direction: column;
	}

	.leave-item {
		display: flex;
		align-items: center;
		justify-content: space-between;
		gap: 20px;
		padding: 16px 0;
		border-bottom: 1px solid #e2e8f0;
	}

	.leave-item:last-child {
		border-bottom: none;
	}

	.leave-item strong {
		display: block;
		font-size: 14px;
		color: #0f172a;
	}

	.leave-item > div > span {
		display: block;
		margin-top: 5px;
		font-size: 12px;
		color: #64748b;
	}

	.leave-status {
		padding: 7px 11px;
		border-radius: 9px;
		background: #fff7ed;
		color: #ea580c;
		font-size: 11px;
		font-weight: 700;
	}

	.quick-actions {
		display: grid;
		grid-template-columns: 1fr 1fr;
		gap: 14px;
	}

	.quick-action {
		display: flex;
		flex-direction: column;
		align-items: flex-start;
		gap: 10px;
		padding: 16px;
		background: #f8fafc;
		border: 1px solid #e2e8f0;
		border-radius: 14px;
		text-decoration: none;
		transition: 0.25s;
	}

	.quick-action:hover {
		border-color: #bfdbfe;
		background: #f5f9ff;
	}

	.quick-icon {
		width: 40px;
		height: 40px;
		display: flex;
		align-items: center;
		justify-content: center;
		background: #eef4ff;
		color: #2563eb;
		border-radius: 11px;
	}

	.quick-action span {
		font-size: 13px;
		font-weight: 700;
		color: #0f172a;
	}

	.empty {
		padding: 24px;
		text-align: center;
		background: #f8fafc;
		border: 1px dashed #e2e8f0;
		border-radius: 12px;
		font-size: 13px;
		color: #64748b;
	}

	.state-box {
		display: flex;
		align-items: center;
		justify-content: center;
		gap: 10px;
		padding: 60px;
		background: white;
		border: 1px solid #e2e8f0;
		border-radius: 18px;
		color: #64748b;
		font-size: 14px;
	}

	.state-box.error {
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
		.stats-grid {
			grid-template-columns: repeat(2, 1fr);
		}

		.content-grid {
			grid-template-columns: 1fr;
		}
	}
</style>