<script lang="ts">
	import {
		LayoutDashboard,
		UserCircle,
		BookOpen,
		CalendarCheck,
		CalendarDays,
		ClipboardCheck,
		GraduationCap,
		IndianRupee,
		Library,
		Award,
		Bell,
		Bot,
		BarChart3,
		Settings,
		LogOut,
		Search,
		Clock,
		ArrowRight,
		CheckCircle2,
		AlertCircle,
		FileText
	} from '@lucide/svelte';

	const menuItems = [
		{ icon: LayoutDashboard, label: 'Dashboard', active: true },
		{ icon: UserCircle, label: 'My Profile', active: false },
		{ icon: BookOpen, label: 'My Classes', active: false },
		{ icon: CalendarCheck, label: 'Attendance', active: false },
		{ icon: CalendarDays, label: 'Timetable', active: false },
		{ icon: GraduationCap, label: 'Exams & Results', active: false },
		{ icon: ClipboardCheck, label: 'Assignments', active: false },
		{ icon: IndianRupee, label: 'Fees', active: false },
		{ icon: Library, label: 'Library', active: false },
		{ icon: Award, label: 'Certificates', active: false },
		{ icon: Bell, label: 'Notifications', active: false },
		{ icon: Bot, label: 'AI Assistant', active: false },
		{ icon: BarChart3, label: 'Reports', active: false },
		{ icon: Settings, label: 'Settings', active: false }
	];

	const timetable = [
		{
			time: '09:00 AM',
			subject: 'Mathematics',
			teacher: 'Mr. Ravi Kumar',
			room: 'Room 204'
		},
		{
			time: '10:00 AM',
			subject: 'Physics',
			teacher: 'Mrs. Anjali Sharma',
			room: 'Room 105'
		},
		{
			time: '11:30 AM',
			subject: 'Biology',
			teacher: 'Mr. Arjun Rao',
			room: 'Lab 2'
		},
		{
			time: '02:00 PM',
			subject: 'English',
			teacher: 'Mrs. Priya Singh',
			room: 'Room 108'
		}
	];

	const exams = [
		{
			subject: 'Mathematics',
			date: '20 Aug',
			time: '10:00 AM',
			room: 'Room 204'
		},
		{
			subject: 'Physics',
			date: '23 Aug',
			time: '10:00 AM',
			room: 'Room 105'
		},
		{
			subject: 'Biology',
			date: '26 Aug',
			time: '02:00 PM',
			room: 'Lab 2'
		}
	];

	const results = [
		{ subject: 'Mathematics', marks: '92 / 100', grade: 'A+' },
		{ subject: 'Physics', marks: '86 / 100', grade: 'A' },
		{ subject: 'Biology', marks: '95 / 100', grade: 'A+' },
		{ subject: 'English', marks: '82 / 100', grade: 'A' }
	];

	const assignments = [
		{
			name: 'Quadratic Equations',
			subject: 'Mathematics',
			due: 'Today',
			status: 'Pending'
		},
		{
			name: 'Motion & Laws',
			subject: 'Physics',
			due: 'Tomorrow',
			status: 'Submitted'
		},
		{
			name: 'Cellular Structure',
			subject: 'Biology',
			due: '18 Aug',
			status: 'Pending'
		}
	];
</script>


<div class="dashboard">

	<!-- =========================
	     SIDEBAR
	     ========================= -->

	<aside class="sidebar">

		<div class="brand">

			<div class="brand-icon">
				<BookOpen size={28} />
			</div>

			<div>
				<h2>PaperBuddy</h2>
				<span>Student Portal</span>
			</div>

		</div>


		<nav class="navigation">

			{#each menuItems as item}

				<a
					href="/student-dashboard"
					class:active={item.active}
					class="nav-item"
				>
					<item.icon size={21} />
					<span>{item.label}</span>
				</a>

			{/each}

		</nav>


		<div class="profile-card">

			<div class="avatar">
				👨‍🎓
			</div>

			<div>
				<strong>Rahul Kumar</strong>
				<span>10th - A</span>
			</div>

		</div>


		<button class="logout">
			<LogOut size={20} />
			<span>Logout</span>
		</button>

	</aside>


	<!-- =========================
	     MAIN CONTENT
	     ========================= -->

	<main class="main-content">


		<!-- HEADER -->

		<header class="header">

			<div class="welcome">

				<h1>Welcome, Student 👋</h1>

				<p>
					Here's what's happening with your academics today.
				</p>

				<span>Tuesday, August 11, 2026</span>

			</div>


			<div class="header-actions">

				<div class="search-box">

					<Search size={18} />

					<input
						type="text"
						placeholder="Search..."
					/>

				</div>


				<button class="icon-button">
					<Bell size={20} />
				</button>


				<div class="profile">

					<UserCircle size={36} />

					<div>
						<strong>Rahul Kumar</strong>
						<span>Student</span>
					</div>

				</div>

			</div>

		</header>


		<!-- =========================
		     KPI CARDS
		     ========================= -->

		<section class="stats-grid">

			<div class="stat-card">
				<div class="stat-icon">
					<GraduationCap size={23} />
				</div>

				<div>
					<span>My Class</span>
					<strong>10th - A</strong>
				</div>
			</div>


			<div class="stat-card">
				<div class="stat-icon">
					<CalendarCheck size={23} />
				</div>

				<div>
					<span>Attendance</span>
					<strong>92%</strong>
				</div>
			</div>


			<div class="stat-card">
				<div class="stat-icon">
					<FileText size={23} />
				</div>

				<div>
					<span>Upcoming Exams</span>
					<strong>3</strong>
				</div>
			</div>


			<div class="stat-card">
				<div class="stat-icon">
					<ClipboardCheck size={23} />
				</div>

				<div>
					<span>Pending Assignments</span>
					<strong>4</strong>
				</div>
			</div>


			<div class="stat-card">
				<div class="stat-icon">
					<BarChart3 size={23} />
				</div>

				<div>
					<span>Last Exams Percentage</span>
					<strong>78%</strong>
				</div>
			</div>


			<div class="stat-card">
				<div class="stat-icon">
					<Library size={23} />
				</div>

				<div>
					<span>Books Issued</span>
					<strong>3</strong>
				</div>
			</div>


			<div class="stat-card">
				<div class="stat-icon">
					<IndianRupee size={23} />
				</div>

				<div>
					<span>Fee Due</span>
					<strong>₹4,500</strong>
				</div>
			</div>


			<div class="stat-card">
				<div class="stat-icon">
					<Award size={23} />
				</div>

				<div>
					<span>Certificates</span>
					<strong>5</strong>
				</div>
			</div>

		</section>


		<!-- =========================
		     TIMETABLE + ATTENDANCE
		     ========================= -->

		<div class="content-grid">


			<section class="large-card">

				<div class="section-header">

					<div>
						<h2>Today's Timetable</h2>
						<p>Your classes for today</p>
					</div>

					<button>
						View Timetable
						<ArrowRight size={17} />
					</button>

				</div>


				<div class="schedule-list">

					{#each timetable as item}

						<div class="schedule-row">

							<div class="time">
								<Clock size={17} />
								{item.time}
							</div>

							<div>
								<strong>{item.subject}</strong>
								<span>{item.teacher}</span>
							</div>

							<div class="room">
								{item.room}
							</div>

						</div>

					{/each}

				</div>

			</section>


			<section class="large-card">

				<div class="section-header">

					<div>
						<h2>Attendance Overview</h2>
						<p>Your monthly attendance</p>
					</div>

				</div>


				<div class="attendance-value">

					<strong>92%</strong>

					<span>Overall Attendance</span>

				</div>


				<div class="attendance-bar">
					<div style="width: 92%;"></div>
				</div>


				<div class="attendance-stats">

					<div>
						<strong>82</strong>
						<span>Present</span>
					</div>

					<div>
						<strong>5</strong>
						<span>Absent</span>
					</div>

					<div>
						<strong>2</strong>
						<span>Late</span>
					</div>

				</div>


				<div class="attendance-note">
					<CheckCircle2 size={17} />
					<span>Your attendance is above the 75% requirement.</span>
				</div>

			</section>

		</div>


		<!-- =========================
		     UPCOMING EXAMS + RESULTS
		     ========================= -->

		<div class="content-grid">


			<section class="large-card">

				<div class="section-header">

					<div>
						<h2>Upcoming Exams</h2>
						<p>Your upcoming examination schedule</p>
					</div>

					<button>
						View All
						<ArrowRight size={17} />
					</button>

				</div>


				<div class="exam-list">

					{#each exams as exam}

						<div class="exam-item">

							<div class="exam-icon">
								<GraduationCap size={21} />
							</div>

							<div class="exam-info">

								<strong>{exam.subject}</strong>

								<span>
									{exam.date} • {exam.time} • {exam.room}
								</span>

							</div>

						</div>

					{/each}

				</div>

			</section>


			<section class="large-card">

				<div class="section-header">

					<div>
						<h2>Recent Results</h2>
						<p>Your latest academic performance</p>
					</div>

					<button>
						View All
						<ArrowRight size={17} />
					</button>

				</div>


				<div class="results-list">

					{#each results as result}

						<div class="result-row">

							<div>
								<strong>{result.subject}</strong>
								<span>{result.marks}</span>
							</div>

							<div class="grade">
								{result.grade}
							</div>

						</div>

					{/each}

				</div>

			</section>

		</div>


		<!-- =========================
		     ASSIGNMENTS
		     ========================= -->

		<section class="large-card">

			<div class="section-header">

				<div>
					<h2>Assignments</h2>
					<p>Track your assignments</p>
				</div>

				<button>
					View All
					<ArrowRight size={17} />
				</button>

			</div>


			<div class="table">

				<div class="table-header">

					<span>Assignment</span>
					<span>Subject</span>
					<span>Due Date</span>
					<span>Status</span>

				</div>


				{#each assignments as assignment}

					<div class="table-row">

						<strong>{assignment.name}</strong>

						<span>{assignment.subject}</span>

						<span>{assignment.due}</span>

						<span
							class:pending={assignment.status === 'Pending'}
							class:submitted={assignment.status === 'Submitted'}
						>
							{assignment.status}
						</span>

					</div>

				{/each}

			</div>

		</section>


		<!-- =========================
		     APPLY LEAVE
		     ========================= -->

		<section class="large-card">

			<div class="section-header">

				<div>
					<h2>Apply Leave</h2>
					<p>Manage your leave requests</p>
				</div>

				<button class="apply-button">
					Apply Leave
					<ArrowRight size={17} />
				</button>

			</div>


			<div class="leave-balance">

				<div>
					<span>Available Leave</span>
					<strong>12 Days</strong>
				</div>

				<div>
					<span>Pending Requests</span>
					<strong>1</strong>
				</div>

			</div>


			<div class="leave-list">

				<div class="leave-item">

					<div>
						<strong>Casual Leave</strong>
						<span>18 Aug - 19 Aug</span>
					</div>

					<span class="leave-status">
						Pending
					</span>

				</div>


				<div class="leave-item">

					<div>
						<strong>Medical Leave</strong>
						<span>02 Aug - 03 Aug</span>
					</div>

					<span class="leave-status approved">
						Approved
					</span>

				</div>

			</div>

		</section>


		<!-- =========================
		     AI ASSISTANT
		     ========================= -->

		<section class="large-card ai-card">

			<div class="ai-heading">

				<div class="ai-icon">
					<Bot size={24} />
				</div>

				<div>
					<h2>AI Assistant</h2>
					<p>Ask PaperBuddy about your academics.</p>
				</div>

			</div>


			<div class="prompt-list">

				<button class="prompt">
					<span>What exams do I have this week?</span>
					<ArrowRight size={16} />
				</button>

				<button class="prompt">
					<span>Show my pending assignments.</span>
					<ArrowRight size={16} />
				</button>

				<button class="prompt">
					<span>Why is my attendance low?</span>
					<ArrowRight size={16} />
				</button>

				<button class="prompt">
					<span>Show my academic performance.</span>
					<ArrowRight size={16} />
				</button>

			</div>

		</section>

	</main>

</div>


<style lang="scss">
.dashboard {
	display: flex;
	min-height: 100vh;
	background: #F8FAFC;
}


/* =========================
   SIDEBAR
   ========================= */

.sidebar {
	width: 280px;
	height: 100vh;

	position: fixed;
	left: 0;
	top: 0;

	background: #15315B;

	display: flex;
	flex-direction: column;

	padding: 28px 20px;

	box-sizing: border-box;

	z-index: 10;

	overflow: hidden;
}


/* BRAND */

.brand {
	display: flex;
	align-items: center;
	gap: 14px;

	margin-bottom: 36px;
}

.brand-icon {
	width: 52px;
	height: 52px;

	display: flex;
	align-items: center;
	justify-content: center;

	background: #2563EB;

	color: white;

	border-radius: 14px;
}

.brand h2 {
	margin: 0;

	font-size: 24px;
	font-weight: 800;

	color: white;
}

.brand span {
	display: block;

	margin-top: 3px;

	font-size: 12px;

	color: rgba(255, 255, 255, 0.75);
}


/* NAVIGATION */

.navigation {
	flex: 1;

	display: flex;
	flex-direction: column;

	gap: 6px;

	overflow-y: auto;

	padding-right: 6px;

	scrollbar-width: none;
}

.navigation::-webkit-scrollbar {
	display: none;
}

.nav-item {
	width: 100%;
	box-sizing: border-box;

	display: flex;
	align-items: center;

	gap: 14px;

	padding: 13px 14px;

	border-radius: 13px;

	text-decoration: none;

	color: white;

	font-size: 15px;

	font-weight: 600;

	transition: 0.25s;
}

.nav-item svg {
	color: white;
	stroke: white;
}

.nav-item:hover {
	background: rgba(255, 255, 255, 0.08);
	color: white;
}

.nav-item.active {
	background: #2563EB;

	color: white;

	box-shadow: 0 10px 25px rgba(37, 99, 235, 0.25);
}


/* PROFILE */

.profile-card {
	display: flex;
	align-items: center;
	gap: 12px;

	padding: 14px;

	margin-top: 14px;

	background: rgba(255, 255, 255, 0.08);

	border: 1px solid rgba(255, 255, 255, 0.12);

	border-radius: 15px;

	color: white;
}

.avatar {
	width: 44px;
	height: 44px;

	display: flex;
	align-items: center;
	justify-content: center;

	border-radius: 50%;

	background: #2563EB;

	font-size: 20px;
}

.profile-card strong {
	display: block;

	font-size: 14px;
}

.profile-card span {
	display: block;

	margin-top: 3px;

	font-size: 12px;

	color: rgba(255, 255, 255, 0.7);
}


/* LOGOUT */

.logout {
	width: 100%;

	display: flex;
	align-items: center;

	gap: 14px;

	padding: 14px 18px;

	margin-top: 14px;

	border: none;

	border-radius: 14px;

	background: white;

	color: #FCA5A5;

	font-size: 15px;

	font-weight: 600;

	cursor: pointer;
}

.logout svg {
	color: #FCA5A5;
}


/* =========================
   MAIN
   ========================= */

.main-content {
	flex: 1;

	margin-left: 280px;

	padding: 36px;

	max-width: 1700px;
}


/* =========================
   HEADER
   ========================= */

.header {
	display: flex;

	align-items: center;

	justify-content: space-between;

	gap: 30px;

	margin-bottom: 32px;
}

.welcome h1 {
	margin: 0 0 8px;

	font-size: 34px;

	font-weight: 800;

	color: #0F172A;
}

.welcome p {
	margin: 0 0 6px;

	font-size: 16px;

	color: #64748B;
}

.welcome span {
	font-size: 14px;

	color: #94A3B8;
}

.header-actions {
	display: flex;
	align-items: center;

	gap: 14px;
}

.search-box {
	width: 280px;
	height: 46px;

	display: flex;
	align-items: center;

	gap: 10px;

	padding: 0 14px;

	background: white;

	border: 1px solid #E2E8F0;

	border-radius: 12px;
}

.search-box svg {
	color: #64748B;
}

.search-box input {
	width: 100%;

	border: none;
	outline: none;

	background: transparent;

	font-size: 14px;
}

.icon-button {
	width: 46px;
	height: 46px;

	display: flex;
	align-items: center;
	justify-content: center;

	background: white;

	border: 1px solid #E2E8F0;

	border-radius: 12px;

	color: #475569;

	cursor: pointer;
}

.profile {
	display: flex;
	align-items: center;

	gap: 10px;

	padding: 7px 12px;

	background: white;

	border: 1px solid #E2E8F0;

	border-radius: 14px;
}

.profile > svg {
	color: #2563EB;
}

.profile strong {
	display: block;

	font-size: 14px;

	color: #0F172A;
}

.profile span {
	display: block;

	margin-top: 2px;

	font-size: 12px;

	color: #64748B;
}


/* =========================
   KPI CARDS
   ========================= */

.stats-grid {
	display: grid;

	grid-template-columns: repeat(4, 1fr);

	gap: 18px;

	margin-bottom: 28px;
}

.stat-card {
	display: flex;
	align-items: center;

	gap: 15px;

	padding: 20px;

	background: white;

	border: 1px solid #E2E8F0;

	border-radius: 18px;

	box-shadow: 0 4px 15px rgba(15, 23, 42, 0.04);
}

.stat-icon {
	width: 46px;
	height: 46px;

	flex-shrink: 0;

	display: flex;
	align-items: center;
	justify-content: center;

	background: #EEF4FF;

	color: #2563EB;

	border-radius: 13px;
}

.stat-card span {
	display: block;

	margin-bottom: 5px;

	font-size: 13px;

	color: #64748B;
}

.stat-card strong {
	display: block;

	font-size: 24px;

	font-weight: 800;

	color: #0F172A;
}


/* =========================
   CARDS
   ========================= */

.content-grid {
	display: grid;

	grid-template-columns: 1.6fr 1.4fr;

	gap: 28px;

	margin-bottom: 28px;
}

.large-card {
	background: white;

	border: 1px solid #E2E8F0;

	border-radius: 18px;

	padding: 24px;

	box-shadow: 0 4px 15px rgba(15, 23, 42, 0.04);

	margin-bottom: 28px;
}

.section-header {
	display: flex;
	align-items: center;

	justify-content: space-between;

	gap: 20px;

	margin-bottom: 20px;
}

.section-header h2 {
	margin: 0 0 5px;

	font-size: 21px;

	font-weight: 800;

	color: #0F172A;
}

.section-header p {
	margin: 0;

	font-size: 14px;

	color: #64748B;
}

.section-header button {
	display: flex;
	align-items: center;

	gap: 7px;

	border: none;

	background: transparent;

	color: #2563EB;

	font-weight: 700;

	cursor: pointer;
}


/* =========================
   TIMETABLE
   ========================= */

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

	background: #F8FAFC;

	border: 1px solid #E2E8F0;

	border-radius: 13px;
}

.time {
	display: flex;
	align-items: center;

	gap: 7px;

	color: #2563EB;

	font-size: 13px;

	font-weight: 700;
}

.schedule-row strong {
	display: block;

	font-size: 14px;

	color: #0F172A;
}

.schedule-row span {
	display: block;

	margin-top: 4px;

	font-size: 12px;

	color: #64748B;
}

.room {
	text-align: right;

	font-size: 13px;

	color: #64748B;
}


/* =========================
   ATTENDANCE
   ========================= */

.attendance-value strong {
	display: block;

	font-size: 38px;

	color: #2563EB;
}

.attendance-value span {
	font-size: 13px;

	color: #64748B;
}

.attendance-bar {
	height: 9px;

	margin: 15px 0 20px;

	background: #E2E8F0;

	border-radius: 20px;

	overflow: hidden;
}

.attendance-bar div {
	height: 100%;

	background: #2563EB;

	border-radius: 20px;
}

.attendance-stats {
	display: grid;

	grid-template-columns: repeat(3, 1fr);

	gap: 10px;
}

.attendance-stats div {
	padding: 13px;

	text-align: center;

	background: #F8FAFC;

	border-radius: 12px;
}

.attendance-stats strong {
	display: block;

	font-size: 18px;

	color: #0F172A;
}

.attendance-stats span {
	font-size: 12px;

	color: #64748B;
}

.attendance-note {
	display: flex;

	align-items: center;

	gap: 8px;

	margin-top: 16px;

	padding: 11px;

	background: #ECFDF5;

	color: #059669;

	border-radius: 10px;

	font-size: 12px;
}


/* =========================
   EXAMS
   ========================= */

.exam-list {
	display: flex;

	flex-direction: column;

	gap: 12px;
}

.exam-item {
	display: flex;

	align-items: center;

	gap: 14px;

	padding: 15px;

	background: #F8FAFC;

	border: 1px solid #E2E8F0;

	border-radius: 13px;
}

.exam-icon {
	width: 43px;
	height: 43px;

	display: flex;

	align-items: center;
	justify-content: center;

	background: #EEF4FF;

	color: #2563EB;

	border-radius: 12px;
}

.exam-info strong {
	display: block;

	font-size: 14px;

	color: #0F172A;
}

.exam-info span {
	display: block;

	margin-top: 4px;

	font-size: 12px;

	color: #64748B;
}


/* =========================
   RESULTS
   ========================= */

.results-list {
	display: flex;

	flex-direction: column;
}

.result-row {
	display: flex;

	align-items: center;

	justify-content: space-between;

	padding: 14px 0;

	border-bottom: 1px solid #E2E8F0;
}

.result-row:last-child {
	border-bottom: none;
}

.result-row strong {
	display: block;

	font-size: 14px;

	color: #0F172A;
}

.result-row span {
	display: block;

	margin-top: 4px;

	font-size: 12px;

	color: #64748B;
}

.grade {
	padding: 7px 11px;

	background: #ECFDF5;

	color: #059669;

	border-radius: 9px;

	font-size: 12px;

	font-weight: 800;
}


/* =========================
   ASSIGNMENTS
   ========================= */

.table {
	width: 100%;
}

.table-header,
.table-row {
	display: grid;

	grid-template-columns: 1.5fr 1fr 0.8fr 0.8fr;

	align-items: center;

	gap: 15px;

	padding: 14px 12px;
}

.table-header {
	background: #F8FAFC;

	border-radius: 10px;

	font-size: 12px;

	font-weight: 700;

	color: #64748B;
}

.table-row {
	border-bottom: 1px solid #E2E8F0;

	font-size: 13px;

	color: #64748B;
}

.table-row strong {
	color: #0F172A;
}

.table-row > span:last-child {
	width: fit-content;

	padding: 6px 10px;

	border-radius: 8px;

	background: #EEF4FF;

	color: #2563EB;

	font-size: 11px;

	font-weight: 700;
}

.table-row > span.pending {
	background: #FFF7ED;

	color: #EA580C;
}

.table-row > span.submitted {
	background: #ECFDF5;

	color: #059669;
}


/* =========================
   LEAVE
   ========================= */

.apply-button {
	color: #2563EB !important;
}

.leave-balance {
	display: grid;

	grid-template-columns: 1fr 1fr;

	gap: 16px;

	margin-bottom: 18px;
}

.leave-balance > div {
	padding: 18px;

	background: #F8FAFC;

	border-radius: 14px;
}

.leave-balance span {
	display: block;

	margin-bottom: 7px;

	font-size: 13px;

	color: #64748B;
}

.leave-balance strong {
	font-size: 24px;

	color: #0F172A;
}

.leave-list {
	display: flex;

	flex-direction: column;
}

.leave-item {
	display: flex;

	align-items: center;

	justify-content: space-between;

	padding: 15px 0;

	border-bottom: 1px solid #E2E8F0;
}

.leave-item:last-child {
	border-bottom: none;
}

.leave-item strong {
	display: block;

	font-size: 14px;

	color: #0F172A;
}

.leave-item div span {
	display: block;

	margin-top: 4px;

	font-size: 12px;

	color: #64748B;
}

.leave-status {
	padding: 7px 10px;

	background: #FFF7ED;

	color: #EA580C;

	border-radius: 9px;

	font-size: 11px;

	font-weight: 700;
}

.leave-status.approved {
	background: #ECFDF5;

	color: #059669;
}


/* =========================
   AI ASSISTANT
   ========================= */

.ai-card {
	background: linear-gradient(
		135deg,
		#EEF4FF,
		white
	);

	border-color: #D8E5FF;
}

.ai-heading {
	display: flex;

	align-items: center;

	gap: 14px;

	margin-bottom: 20px;
}

.ai-icon {
	width: 48px;
	height: 48px;

	display: flex;

	align-items: center;
	justify-content: center;

	background: #2563EB;

	color: white;

	border-radius: 13px;
}

.ai-heading h2 {
	margin: 0 0 4px;

	font-size: 21px;

	color: #0F172A;
}

.ai-heading p {
	margin: 0;

	font-size: 13px;

	color: #64748B;
}

.prompt-list {
	display: grid;

	grid-template-columns: 1fr 1fr;

	gap: 10px;
}

.prompt {
	display: flex;

	align-items: center;

	justify-content: space-between;

	gap: 10px;

	padding: 13px 14px;

	background: white;

	border: 1px solid #D8E5FF;

	border-radius: 10px;

	color: #2563EB;

	font-size: 12px;

	text-align: left;

	cursor: pointer;
}

.prompt:hover {
	background: #2563EB;

	color: white;
}


/* =========================
   RESPONSIVE
   ========================= */

@media (max-width: 1350px) {
	.stats-grid {
		grid-template-columns: repeat(2, 1fr);
	}
}

@media (max-width: 1100px) {
	.sidebar {
		width: 250px;
	}

	.main-content {
		margin-left: 250px;

		padding: 24px;
	}

	.content-grid {
		grid-template-columns: 1fr;
	}
}

@media (max-width: 800px) {
	.sidebar {
		position: relative;

		width: 100%;

		height: auto;

		max-height: none;
	}

	.dashboard {
		display: block;
	}

	.main-content {
		margin-left: 0;

		padding: 20px;
	}

	.header {
		flex-direction: column;

		align-items: flex-start;
	}

	.header-actions {
		width: 100%;
	}

	.search-box {
		flex: 1;

		width: auto;
	}

	.stats-grid {
		grid-template-columns: 1fr;
	}

	.content-grid {
		grid-template-columns: 1fr;
	}

	.schedule-row {
		grid-template-columns: 1fr;

		gap: 8px;
	}

	.room {
		text-align: left;
	}

	.table {
		overflow-x: auto;
	}

	.table-header,
	.table-row {
		min-width: 650px;
	}

	.leave-balance {
		grid-template-columns: 1fr;
	}

	.prompt-list {
		grid-template-columns: 1fr;
	}
}
</style>