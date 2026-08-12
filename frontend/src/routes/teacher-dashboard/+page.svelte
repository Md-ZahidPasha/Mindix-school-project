<script lang="ts">
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
		BookMarked,
		Bot,
		ArrowRight,
		MoreHorizontal
	} from '@lucide/svelte';

	const teacherName = 'Teacher';

	const today = new Date();

	const currentDate = today.toLocaleDateString('en-US', {
		weekday: 'long',
		day: 'numeric',
		month: 'long',
		year: 'numeric'
	});

	const stats = [
		{
			title: 'My Students',
			value: '128',
			icon: GraduationCap
		},
		{
			title: 'My Classes',
			value: '6',
			icon: BookOpen
		},
		{
			title: "Today's Classes",
			value: '4',
			icon: Clock3
		},
		{
			title: 'Pending Tasks',
			value: '8',
			icon: CheckCircle2
		},
		{
			title: "Today's Attendance",
			value: '94%',
			icon: ClipboardCheck
		},
		{
			title: 'Pending Assignments',
			value: '12',
			icon: BookMarked
		},
		{
			title: 'Leave Balance',
			value: '14',
			icon: CalendarDays
		},
		{
			title: 'Upcoming Exams',
			value: '3',
			icon: CalendarDays
		}
	];

	const schedule = [
		{
			time: '09:00 AM',
			className: '10th',
			subject: 'Mathematics',
			room: 'Room 204'
		},
		{
			time: '10:00 AM',
			className: '9th',
			subject: 'Mathematics',
			room: 'Room 105'
		},
		{
			time: '11:30 AM',
			className: '10th',
			subject: 'Mathematics',
			room: 'Room 204'
		},
		{
			time: '02:00 PM',
			className: '8th',
			subject: 'Mathematics',
			room: 'Room 108'
		}
	];

	const classes = [
		{
			className: '10th',
			section: 'A',
			students: 32,
			subject: 'Mathematics'
		},
		{
			className: '10th',
			section: 'B',
			students: 30,
			subject: 'Mathematics'
		},
		{
			className: '9th',
			section: 'A',
			students: 34,
			subject: 'Mathematics'
		},
		{
			className: '8th',
			section: 'B',
			students: 32,
			subject: 'Mathematics'
		}
	];

	const assignments = [
		{
			title: 'Quadratic Equations',
			className: '10th A',
			due: 'Today',
			status: 'Pending'
		},
		{
			title: 'Algebra Practice',
			className: '9th A',
			due: 'Tomorrow',
			status: 'Submitted'
		},
		{
			title: 'Geometry Worksheet',
			className: '8th B',
			due: '18 Aug',
			status: 'To Evaluate'
		}
	];

	const exams = [
		{
			subject: 'Mathematics',
			className: '10th',
			date: '20 Aug',
			time: '10:00 AM'
		},
		{
			subject: 'Mathematics',
			className: '9th',
			date: '23 Aug',
			time: '09:00 AM'
		},
		{
			subject: 'Mathematics',
			className: '8th',
			date: '26 Aug',
			time: '11:00 AM'
		}
	];

	const syllabus = [
		{
			className: '10th A',
			subject: 'Mathematics',
			topic: 'Quadratic Equations',
			completed: '8 topics',
			remaining: '4 topics',
			target: '30 Aug',
			progress: 67
		},
		{
			className: '9th A',
			subject: 'Mathematics',
			topic: 'Polynomials',
			completed: '6 topics',
			remaining: '3 topics',
			target: '28 Aug',
			progress: 72
		}
	];

    const leaveRequests = [
	{
		type: 'Casual Leave',
		from: '18 Aug',
		to: '19 Aug',
		status: 'Pending'
	},
	{
		type: 'Medical Leave',
		from: '21 Aug',
		to: '22 Aug',
		status: 'Approved'
	}
];

	const aiPrompts = [
		'Show students with attendance below 75%',
		'Show pending assignments',
		'Generate class performance summary',
		'Show syllabus progress'
	];
</script>

<div class="dashboard">

	<aside class="sidebar">

		<div class="brand">
			<div class="brand-icon">
				<GraduationCap size={25} />
			</div>

			<div>
				<h2>PaperBuddy</h2>
				<span>Teacher Portal</span>
			</div>
		</div>

		<nav class="navigation">

			<a href="/teacher-dashboard" class="nav-item active">
				<GraduationCap size={19} />
				<span>Dashboard</span>
			</a>

			<a href="/teacher-dashboard" class="nav-item">
				<UserCircle2 size={19} />
				<span>My Profile</span>
			</a>

			<a href="/teacher-dashboard" class="nav-item">
				<Users size={19} />
				<span>My Classes</span>
			</a>

			<a href="/teacher-dashboard" class="nav-item">
				<GraduationCap size={19} />
				<span>My Students</span>
			</a>

			<a href="/teacher-dashboard" class="nav-item">
				<ClipboardCheck size={19} />
				<span>Attendance</span>
			</a>

			<a href="/teacher-dashboard" class="nav-item">
				<CalendarDays size={19} />
				<span>Timetable</span>
			</a>

			<a href="/teacher-dashboard" class="nav-item">
				<BookOpen size={19} />
				<span>Assignments</span>
			</a>

			<a href="/teacher-dashboard" class="nav-item">
				<CheckCircle2 size={19} />
				<span>Exams & Results</span>
			</a>

			<a href="/teacher-dashboard" class="nav-item">
				<CalendarDays size={19} />
				<span>Apply Leave</span>
			</a>

			<a href="/teacher-dashboard" class="nav-item">
				<BookMarked size={19} />
				<span>Syllabus Plan</span>
			</a>

			<a href="/teacher-dashboard" class="nav-item">
				<BookOpen size={19} />
				<span>Library</span>
			</a>

			<a href="/teacher-dashboard" class="nav-item">
				<Bell size={19} />
				<span>Notifications</span>
			</a>

			<a href="/teacher-dashboard" class="nav-item">
				<Bot size={19} />
				<span>AI Assistant</span>
			</a>

			<a href="/teacher-dashboard" class="nav-item">
				<ClipboardCheck size={19} />
				<span>Reports</span>
			</a>

			<a href="/teacher-dashboard" class="nav-item">
				<MoreHorizontal size={19} />
				<span>Settings</span>
			</a>

		</nav>

		<button class="logout" type="button">
			<ArrowRight size={19} />
			<span>Logout</span>
		</button>

	</aside>

	<main class="main-content">

		<header class="header">

			<div class="welcome">

				<h1>Welcome, {teacherName} 👋</h1>

				<p>
					Here's what's happening with your classes today.
				</p>

				<span>{currentDate}</span>

			</div>

			<div class="header-actions">

				<div class="search-box">
					<Search size={18} />

					<input
						type="text"
						placeholder="Search..."
					/>
				</div>

				<button
					class="icon-button"
					type="button"
					aria-label="Notifications"
				>
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

		<section class="stats-grid">

			{#each stats as stat}

				<div class="stat-card">

					<div class="stat-icon">
						<stat.icon size={24} />
					</div>

					<div>
						<span>{stat.title}</span>
						<strong>{stat.value}</strong>
					</div>

				</div>

			{/each}

		</section>

		<section class="content-grid">

			<div class="large-card schedule-card">

				<div class="section-header">

					<div>
						<h2>Today's Schedule</h2>
						<p>Your classes for today</p>
					</div>

					<button type="button">
						View Timetable
						<ArrowRight size={16} />
					</button>

				</div>

				<div class="schedule-list">

					{#each schedule as item}

						<div class="schedule-row">

							<div class="time">
								<Clock3 size={17} />
								<span>{item.time}</span>
							</div>

							<div>
								<strong>{item.className} Class</strong>
								<span>{item.subject}</span>
							</div>

							<div class="room">
								{item.room}
							</div>

						</div>

					{/each}

				</div>

			</div>

			<div class="large-card attendance-card">

				<div class="section-header">
					<div>
						<h2>Attendance Overview</h2>
						<p>Today's class attendance</p>
					</div>
				</div>

				<div class="attendance-value">
					<strong>94%</strong>
					<span>Today's Attendance</span>
				</div>

				<div class="attendance-bar">
					<div style="width: 94%"></div>
				</div>

				<div class="attendance-stats">

					<div>
						<strong>120</strong>
						<span>Present</span>
					</div>

					<div>
						<strong>8</strong>
						<span>Absent</span>
					</div>

					<div>
						<strong>3</strong>
						<span>Late</span>
					</div>

				</div>

				<div class="warning">
					<ClipboardCheck size={18} />

					<span>
						5 students are below the 75% attendance threshold.
					</span>
				</div>

			</div>

		</section>

		<section class="large-card">

			<div class="section-header">

				<div>
					<h2>My Classes</h2>
					<p>Your assigned classes and students</p>
				</div>

				<button type="button">
					View All
					<ArrowRight size={16} />
				</button>

			</div>

			<div class="classes-grid">

				{#each classes as item}

					<div class="class-card">

						<div class="class-icon">
							<GraduationCap size={23} />
						</div>

						<div class="class-info">

							<strong>
								{item.className} - {item.section}
							</strong>

							<span>{item.subject}</span>

							<p>
								<Users size={15} />
								{item.students} students
							</p>

						</div>

					</div>

				{/each}

			</div>

		</section>

		<section class="content-grid">

			<div class="large-card">

				<div class="section-header">

					<div>
						<h2>Assignments</h2>
						<p>Track your assignments</p>
					</div>

					<button type="button">
						View All
						<ArrowRight size={16} />
					</button>

				</div>

				<div class="table">

					<div class="table-header">
						<span>Assignment</span>
						<span>Class</span>
						<span>Due Date</span>
						<span>Status</span>
					</div>

					{#each assignments as item}

						<div class="table-row">

							<strong>{item.title}</strong>

							<span>{item.className}</span>

							<span>{item.due}</span>

							<span
								class:pending={item.status === 'Pending'}
								class:submitted={item.status === 'Submitted'}
							>
								{item.status}
							</span>

						</div>

					{/each}

				</div>

			</div>

			<div class="large-card">

				<div class="section-header">

					<div>
						<h2>Upcoming Exams</h2>
						<p>Next scheduled examinations</p>
					</div>

				</div>

				<div class="exam-list">

					{#each exams as exam}

						<div class="exam-item">

							<div class="exam-icon">
								<CalendarDays size={20} />
							</div>

							<div>
								<strong>{exam.subject}</strong>
								<span>
									{exam.className} • {exam.date} • {exam.time}
								</span>
							</div>

						</div>

					{/each}

				</div>

			</div>

		</section>

		<section class="large-card">

			<div class="section-header">

				<div>
					<h2>Syllabus Plan</h2>
					<p>Track syllabus progress by class and subject</p>
				</div>

				<button type="button">
					View Plan
					<ArrowRight size={16} />
				</button>

			</div>

			<div class="syllabus-list">

				{#each syllabus as item}

					<div class="syllabus-item">

						<div class="syllabus-main">

							<div>
								<strong>
									{item.className} • {item.subject}
								</strong>

								<span>
									Current Topic: {item.topic}
								</span>
							</div>

							<strong>{item.progress}%</strong>

						</div>

						<div class="progress-bar">
							<div style={`width: ${item.progress}%`}></div>
						</div>

						<div class="syllabus-meta">

							<span>Completed: {item.completed}</span>
							<span>Remaining: {item.remaining}</span>
							<span>Target: {item.target}</span>

						</div>

					</div>

				{/each}

			</div>

		</section>

		<section class="content-grid">

			<div class="large-card">

				<div class="section-header">

					<div>
						<h2>Apply Leave</h2>
						<p>Manage your leave requests</p>
					</div>

					<button type="button">
						Apply Leave
						<ArrowRight size={16} />
					</button>

				</div>

				<div class="leave-balance">

					<div>
						<span>Available Leave</span>
						<strong>14 Days</strong>
					</div>

					<div>
						<span>Pending Requests</span>
						<strong>2</strong>
					</div>

				</div>

				<div class="leave-list">

					{#each leaveRequests as request}

						<div class="leave-item">

							<div>
								<strong>{request.type}</strong>

								<span>
									{request.type} • {request.from} - {request.to}
								</span>
							</div>

							<span class="leave-status">
								{request.status}
							</span>

						</div>

					{/each}

				</div>

			</div>

			<div class="large-card ai-card">

				<div class="ai-heading">

					<div class="ai-icon">
						<Bot size={24} />
					</div>

					<div>
						<h2>AI Assistant</h2>
						<p>Ask PaperBuddy anything about your classes.</p>
					</div>

				</div>

				<div class="prompt-list">

					{#each aiPrompts as prompt}

						<button type="button" class="prompt">
							{prompt}
							<ArrowRight size={15} />
						</button>

					{/each}

				</div>

			</div>

		</section>

	</main>

</div>

<style lang="scss">
/* =========================================
   DASHBOARD
   ========================================= */

.dashboard {
	display: flex;
	min-height: 100vh;
	background: #F8FAFC;
}


/* =========================================
   SIDEBAR
   ========================================= */

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
    box-sizing: border-box
    ;
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

.nav-item.active svg {
	color: white;
	stroke: white;
}


/* LOGOUT */

.logout {
	width: 100%;

	display: flex;
	align-items: center;

	gap: 14px;

	padding: 14px 18px;

	margin-top: 18px;

	border: none;

	border-radius: 14px;

	background: white;

	color: #FCA5A5;

	font-size: 15px;

	font-weight: 600;

	cursor: pointer;

	transition: 0.25s;
}

.logout svg {
	color: #FCA5A5;
	stroke: #FCA5A5;
}

.logout:hover {
	background: #FEF2F2;
}


/* =========================================
   MAIN CONTENT
   ========================================= */

.main-content {
	flex: 1;

	margin-left: 280px;

	padding: 36px;

	max-width: 1700px;
}


/* =========================================
   HEADER
   ========================================= */

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


/* SEARCH */

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

	color: #0F172A;
}


/* NOTIFICATION */

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

	transition: 0.25s;
}

.icon-button:hover {
	background: #EEF4FF;

	color: #2563EB;
}


/* PROFILE */

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


/* =========================================
   KPI CARDS
   ========================================= */

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

	border: 1px solid #E2E8F0;

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

	font-size: 26px;

	font-weight: 800;

	color: #0F172A;
}


/* =========================================
   GRID
   ========================================= */

.content-grid {
	display: grid;

	grid-template-columns: 1.6fr 1.4fr;

	gap: 28px;

	margin-bottom: 28px;
}


/* =========================================
   LARGE CARDS
   ========================================= */

.large-card {
	background: white;

	border: 1px solid #E2E8F0;

	border-radius: 18px;

	padding: 24px;

	box-shadow: 0 4px 15px rgba(15, 23, 42, 0.04);

	margin-bottom: 28px;
}


/* =========================================
   SECTION HEADER
   ========================================= */

.section-header {
	display: flex;

	align-items: center;

	justify-content: space-between;

	gap: 20px;

	margin-bottom: 22px;
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

	font-size: 14px;

	font-weight: 700;

	cursor: pointer;
}


/* =========================================
   SCHEDULE
   ========================================= */

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

.schedule-row > div:nth-child(2) span {
	display: block;

	margin-top: 3px;

	font-size: 13px;

	color: #64748B;
}

.room {
	text-align: right;

	font-size: 13px;

	color: #64748B;
}


/* =========================================
   ATTENDANCE
   ========================================= */

.attendance-value {
	margin-bottom: 14px;
}

.attendance-value strong {
	display: block;

	font-size: 38px;

	font-weight: 800;

	color: #2563EB;
}

.attendance-value span {
	font-size: 13px;

	color: #64748B;
}

.attendance-bar {
	width: 100%;

	height: 9px;

	background: #E2E8F0;

	border-radius: 20px;

	overflow: hidden;

	margin-bottom: 20px;
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

	margin-bottom: 18px;
}

.attendance-stats > div {
	padding: 12px;

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

.warning {
	display: flex;

	align-items: center;

	gap: 8px;

	padding: 12px;

	background: #FFF7ED;

	border-radius: 10px;

	color: #C2410C;

	font-size: 12px;
}


/* =========================================
   MY CLASSES
   ========================================= */

.classes-grid {
	display: grid;

	grid-template-columns: repeat(4, 1fr);

	gap: 16px;
}

.class-card {
	padding: 18px;

	background: #F8FAFC;

	border: 1px solid #E2E8F0;

	border-radius: 14px;

	transition: 0.25s;
}

.class-card:hover {
	border-color: #BFDBFE;

	background: #F5F9FF;
}

.class-icon {
	width: 44px;
	height: 44px;

	display: flex;

	align-items: center;
	justify-content: center;

	background: #EEF4FF;

	color: #2563EB;

	border-radius: 12px;

	margin-bottom: 14px;
}

.class-info > strong {
	display: block;

	font-size: 15px;

	color: #0F172A;
}

.class-info > span {
	display: block;

	margin-top: 4px;

	font-size: 13px;

	color: #64748B;
}

.class-info p {
	display: flex;

	align-items: center;

	gap: 6px;

	margin: 12px 0 0;

	font-size: 12px;

	color: #64748B;
}


/* =========================================
   ASSIGNMENTS TABLE
   ========================================= */

.table {
	width: 100%;
}

.table-header,
.table-row {
	display: grid;

	grid-template-columns: 1.5fr 0.8fr 0.8fr 0.9fr;

	align-items: center;

	gap: 15px;

	padding: 14px 10px;
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

	color: #475569;
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


/* =========================================
   EXAMS
   ========================================= */

.exam-list {
	display: flex;

	flex-direction: column;

	gap: 12px;
}

.exam-item {
	display: flex;

	align-items: center;

	gap: 14px;

	padding: 14px;

	background: #F8FAFC;

	border-radius: 12px;
}

.exam-icon {
	width: 42px;
	height: 42px;

	flex-shrink: 0;

	display: flex;

	align-items: center;
	justify-content: center;

	background: #EEF4FF;

	color: #2563EB;

	border-radius: 11px;
}

.exam-item strong {
	display: block;

	font-size: 14px;

	color: #0F172A;
}

.exam-item span {
	display: block;

	margin-top: 4px;

	font-size: 12px;

	color: #64748B;
}


/* =========================================
   SYLLABUS
   ========================================= */

.syllabus-list {
	display: flex;

	flex-direction: column;

	gap: 16px;
}

.syllabus-item {
	padding: 18px;

	background: #F8FAFC;

	border: 1px solid #E2E8F0;

	border-radius: 14px;
}

.syllabus-main {
	display: flex;

	align-items: center;

	justify-content: space-between;

	gap: 20px;

	margin-bottom: 12px;
}

.syllabus-main strong {
	display: block;

	font-size: 15px;

	color: #0F172A;
}

.syllabus-main span {
	display: block;

	margin-top: 5px;

	font-size: 13px;

	color: #64748B;
}

.syllabus-main > strong:last-child {
	color: #2563EB;

	font-size: 20px;
}

.progress-bar {
	width: 100%;

	height: 8px;

	background: #E2E8F0;

	border-radius: 20px;

	overflow: hidden;
}

.progress-bar div {
	height: 100%;

	background: #2563EB;

	border-radius: 20px;
}

.syllabus-meta {
	display: flex;

	flex-wrap: wrap;

	gap: 20px;

	margin-top: 10px;

	font-size: 12px;

	color: #64748B;
}


/* =========================================
   APPLY LEAVE
   ========================================= */

.leave-balance {
	display: grid;

	grid-template-columns: 1fr 1fr;

	gap: 16px;

	margin-bottom: 20px;
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
	display: block;

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

	gap: 20px;

	padding: 16px 0;

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

.leave-item > div > span {
	display: block;

	margin-top: 5px;

	font-size: 12px;

	color: #64748B;
}

.leave-status {
	padding: 7px 11px;

	border-radius: 9px;

	background: #FFF7ED;

	color: #EA580C;

	font-size: 11px;

	font-weight: 700;
}

.leave-item:nth-child(2) .leave-status {
	background: #ECFDF5;

	color: #059669;
}


/* =========================================
   AI ASSISTANT
   ========================================= */

.ai-card {
	background: linear-gradient(
		135deg,
		#EEF4FF,
		#FFFFFF
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
	margin: 0 0 5px;

	font-size: 21px;

	color: #0F172A;
}

.ai-heading p {
	margin: 0;

	font-size: 13px;

	color: #64748B;
}

.prompt-list {
	display: flex;

	flex-direction: column;

	gap: 9px;
}

.prompt {
	width: 100%;

	display: flex;

	align-items: center;

	justify-content: space-between;

	gap: 10px;

	padding: 12px 14px;

	background: white;

	border: 1px solid #D8E5FF;

	border-radius: 10px;

	color: #2563EB;

	font-size: 12px;

	text-align: left;

	cursor: pointer;

	transition: 0.2s;
}

.prompt:hover {
	background: #2563EB;

	color: white;
}


/* =========================================
   RESPONSIVE
   ========================================= */

@media (max-width: 1350px) {
	.stats-grid {
		grid-template-columns: repeat(2, 1fr);
	}

	.classes-grid {
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

		min-height: auto;
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

	.classes-grid {
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
		min-width: 600px;
	}

	.leave-balance {
		grid-template-columns: 1fr;
	}
}
</style>