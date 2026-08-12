<script lang="ts">
	import {
		LayoutDashboard,
		Users,
		CalendarCheck,
		BarChart3,
		GraduationCap,
		ClipboardCheck,
		IndianRupee,
		Award,
		Bell,
		Bot,
		UserCircle,
		Settings,
		LogOut,
		Search,
		ArrowRight,
		Clock,
		CheckCircle2,
		AlertCircle,
		BookOpen,
		FileText
	} from '@lucide/svelte';

	const menuItems = [
		{ icon: LayoutDashboard, label: 'Dashboard', active: true },
		{ icon: Users, label: 'My Children', active: false },
		{ icon: CalendarCheck, label: 'Attendance', active: false },
		{ icon: BarChart3, label: 'Academic Performance', active: false },
		{ icon: GraduationCap, label: 'Exams & Results', active: false },
		{ icon: ClipboardCheck, label: 'Assignments', active: false },
		{ icon: IndianRupee, label: 'Fees & Payments', active: false },
		{ icon: Award, label: 'Certificates', active: false },
		{ icon: Bell, label: 'Notices', active: false },
		{ icon: Bell, label: 'Notifications', active: false },
		{ icon: Bot, label: 'AI Assistant', active: false },
		{ icon: UserCircle, label: 'Profile', active: false }
	];

	const children = [
		{
			name: 'Rahul Kumar',
			className: '10th',
			section: 'A',
			attendance: '92%',
			grade: '77%'
		},
		{
			name: 'Ayesha Kumar',
			className: '7th',
			section: 'B',
			attendance: '95%',
			grade: '84%'
		}
	];

	const performance = [
		{ subject: 'Mathematics', marks: '78 / 100', grade: 'A' },
		{ subject: 'Science', marks: '74 / 100', grade: 'A' },
		{ subject: 'English', marks: '81 / 100', grade: 'A+' },
		{ subject: 'Social Studies', marks: '75 / 100', grade: 'A' }
	];

	const exams = [
		{
			subject: 'Mathematics',
			date: '20 Aug',
			time: '10:00 AM',
			syllabus: 'Algebra & Geometry'
		},
		{
			subject: 'Science',
			date: '23 Aug',
			time: '10:00 AM',
			syllabus: 'Light & Human Eye'
		},
		{
			subject: 'English',
			date: '26 Aug',
			time: '10:00 AM',
			syllabus: 'Grammar & Literature'
		}
	];

	const assignments = [
		{
			name: 'Quadratic Equations',
			subject: 'Mathematics',
			due: 'Today',
			status: 'Pending'
		},
		{
			name: 'Cellular Structure',
			subject: 'Biology',
			due: 'Tomorrow',
			status: 'Submitted'
		},
		{
			name: 'Grammar Practice',
			subject: 'English',
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
				<Users size={28} />
			</div>

			<div>
				<h2>PaperBuddy</h2>
				<span>Parent Portal</span>
			</div>

		</div>


		<nav class="navigation">

			{#each menuItems as item}

				<a
					href="/parent-dashboard"
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
				👨‍👩‍👧
			</div>

			<div>
				<strong>Mr. Kumar</strong>
				<span>Parent</span>
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

				<h1>Welcome, Parent 👋</h1>

				<p>
					Stay connected with your child's academic journey.
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
						<strong>Mr. Kumar</strong>
						<span>Parent</span>
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
					<Users size={23} />
				</div>

				<div>
					<span>Children</span>
					<strong>2</strong>
				</div>

			</div>


			<div class="stat-card">

				<div class="stat-icon">
					<CalendarCheck size={23} />
				</div>

				<div>
					<span>Attendance</span>
					<strong>93%</strong>
				</div>

			</div>


			<div class="stat-card">

				<div class="stat-icon">
					<BarChart3 size={23} />
				</div>

				<div>
					<span>Average Grade</span>
					<strong>81%</strong>
				</div>

			</div>


			<div class="stat-card">

				<div class="stat-icon">
					<ClipboardCheck size={23} />
				</div>

				<div>
					<span>Pending Assignments</span>
					<strong>3</strong>
				</div>

			</div>


			<div class="stat-card">

				<div class="stat-icon">
					<GraduationCap size={23} />
				</div>

				<div>
					<span>Upcoming Exams</span>
					<strong>4</strong>
				</div>

			</div>


			<div class="stat-card">

				<div class="stat-icon">
					<IndianRupee size={23} />
				</div>

				<div>
					<span>Pending Fees</span>
					<strong>₹6,500</strong>
				</div>

			</div>


			<div class="stat-card">

				<div class="stat-icon">
					<Award size={23} />
				</div>

				<div>
					<span>Certificates</span>
					<strong>7</strong>
				</div>

			</div>


			<div class="stat-card">

				<div class="stat-icon">
					<Bell size={23} />
				</div>

				<div>
					<span>Notifications</span>
					<strong>5</strong>
				</div>

			</div>

		</section>


		<!-- =========================
		     CHILDREN OVERVIEW
		     ========================= -->

		<section class="large-card">

			<div class="section-header">

				<div>
					<h2>Children Overview</h2>
					<p>Monitor your children's academic progress.</p>
				</div>

				<button>
					View All
					<ArrowRight size={17} />
				</button>

			</div>


			<div class="children-grid">

				{#each children as child}

					<div class="child-card">

						<div class="child-top">

							<div class="child-avatar">
								{child.name.charAt(0)}
							</div>

							<div>
								<strong>{child.name}</strong>

								<span>
									{child.className} - {child.section}
								</span>
							</div>

						</div>


						<div class="child-stats">

							<div>
								<span>Attendance</span>
								<strong>{child.attendance}</strong>
							</div>

							<div>
								<span>Average Grade</span>
								<strong>{child.grade}</strong>
							</div>

						</div>


						<button class="view-profile">
							View Profile
							<ArrowRight size={15} />
						</button>

					</div>

				{/each}

			</div>

		</section>


		<!-- =========================
		     ATTENDANCE + PERFORMANCE
		     ========================= -->

		<div class="content-grid">


			<section class="large-card">

				<div class="section-header">

					<div>
						<h2>Attendance</h2>
						<p>Monthly attendance overview</p>
					</div>

				</div>


				<div class="attendance-value">

					<strong>93%</strong>

					<span>Overall Attendance</span>

				</div>


				<div class="attendance-bar">
					<div style="width: 93%;"></div>
				</div>


				<div class="attendance-stats">

					<div>
						<strong>86</strong>
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
					<span>Attendance is above the required threshold.</span>
				</div>

			</section>


			<section class="large-card">

				<div class="section-header">

					<div>
						<h2>Academic Performance</h2>
						<p>Recent subject performance</p>
					</div>

				</div>


				<div class="performance-list">

					{#each performance as item}

						<div class="performance-row">

							<div>
								<strong>{item.subject}</strong>
								<span>{item.marks}</span>
							</div>

							<div class="grade">
								{item.grade}
							</div>

						</div>

					{/each}

				</div>

			</section>

		</div>


		<!-- =========================
		     UPCOMING EXAMS
		     ========================= -->

		<section class="large-card">

			<div class="section-header">

				<div>
					<h2>Upcoming Exams</h2>
					<p>Keep track of your child's examination schedule.</p>
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
								{exam.date} • {exam.time}
							</span>

						</div>

						<div class="syllabus">
							{exam.syllabus}
						</div>

					</div>

				{/each}

			</div>

		</section>


		<!-- =========================
		     ASSIGNMENTS
		     ========================= -->

		<section class="large-card">

			<div class="section-header">

				<div>
					<h2>Assignments</h2>
					<p>Monitor your child's assignments.</p>
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
		     FEES
		     ========================= -->

		<section class="large-card">

			<div class="section-header">

				<div>
					<h2>Fees</h2>
					<p>Track school fees and payments.</p>
				</div>

				<button>
					View Details
					<ArrowRight size={17} />
				</button>

			</div>


			<div class="fees-grid">

				<div>
					<span>Total Fees</span>
					<strong>₹45,000</strong>
				</div>

				<div>
					<span>Paid</span>
					<strong>₹38,500</strong>
				</div>

				<div>
					<span>Pending</span>
					<strong class="pending-fee">₹6,500</strong>
				</div>

				<div>
					<span>Due Date</span>
					<strong>30 Aug</strong>
				</div>

			</div>

		</section>


		<!-- =========================
		     NOTIFICATIONS
		     ========================= -->

		<section class="large-card">

			<div class="section-header">

				<div>
					<h2>Notifications</h2>
					<p>Important school updates.</p>
				</div>

				<button>
					View All
					<ArrowRight size={17} />
				</button>

			</div>


			<div class="notifications-list">

				<div class="notification-item">

					<div class="notification-icon">
						<Bell size={18} />
					</div>

					<div>
						<strong>School Annual Day</strong>
						<span>Annual Day will be held on 28 August.</span>
					</div>

				</div>


				<div class="notification-item">

					<div class="notification-icon">
						<FileText size={18} />
					</div>

					<div>
						<strong>Exam Schedule Published</strong>
						<span>The upcoming examination schedule is now available.</span>
					</div>

				</div>


				<div class="notification-item">

					<div class="notification-icon">
						<IndianRupee size={18} />
					</div>

					<div>
						<strong>Fee Reminder</strong>
						<span>₹6,500 fee payment is pending.</span>
					</div>

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
					<p>Ask PaperBuddy about your child's academics.</p>
				</div>

			</div>


			<div class="prompt-list">

				<button class="prompt">
					<span>How is my child's attendance?</span>
					<ArrowRight size={16} />
				</button>

				<button class="prompt">
					<span>How is my child's academic performance?</span>
					<ArrowRight size={16} />
				</button>

				<button class="prompt">
					<span>What exams are coming?</span>
					<ArrowRight size={16} />
				</button>

				<button class="prompt">
					<span>Does my child have pending assignments?</span>
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
   KPI
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
   CHILDREN
   ========================= */

.children-grid {
	display: grid;

	grid-template-columns: repeat(2, 1fr);

	gap: 18px;
}

.child-card {
	padding: 20px;

	background: #F8FAFC;

	border: 1px solid #E2E8F0;

	border-radius: 15px;
}

.child-top {
	display: flex;

	align-items: center;

	gap: 13px;

	margin-bottom: 20px;
}

.child-avatar {
	width: 46px;
	height: 46px;

	display: flex;

	align-items: center;
	justify-content: center;

	background: #2563EB;

	color: white;

	border-radius: 50%;

	font-size: 18px;

	font-weight: 700;
}

.child-top strong {
	display: block;

	font-size: 16px;

	color: #0F172A;
}

.child-top span {
	display: block;

	margin-top: 4px;

	font-size: 13px;

	color: #64748B;
}

.child-stats {
	display: grid;

	grid-template-columns: 1fr 1fr;

	gap: 12px;

	margin-bottom: 18px;
}

.child-stats div {
	padding: 12px;

	background: white;

	border-radius: 11px;
}

.child-stats span {
	display: block;

	font-size: 12px;

	color: #64748B;
}

.child-stats strong {
	display: block;

	margin-top: 5px;

	font-size: 19px;

	color: #0F172A;
}

.view-profile {
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
   PERFORMANCE
   ========================= */

.performance-list {
	display: flex;

	flex-direction: column;
}

.performance-row {
	display: flex;

	align-items: center;

	justify-content: space-between;

	padding: 14px 0;

	border-bottom: 1px solid #E2E8F0;
}

.performance-row:last-child {
	border-bottom: none;
}

.performance-row strong {
	display: block;

	font-size: 14px;

	color: #0F172A;
}

.performance-row span {
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

.exam-info {
	flex: 1;
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

.syllabus {
	font-size: 12px;

	color: #64748B;

	text-align: right;
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
   FEES
   ========================= */

.fees-grid {
	display: grid;

	grid-template-columns: repeat(4, 1fr);

	gap: 16px;
}

.fees-grid > div {
	padding: 18px;

	background: #F8FAFC;

	border-radius: 14px;
}

.fees-grid span {
	display: block;

	margin-bottom: 7px;

	font-size: 13px;

	color: #64748B;
}

.fees-grid strong {
	font-size: 22px;

	color: #0F172A;
}

.fees-grid .pending-fee {
	color: #EA580C;
}


/* =========================
   NOTIFICATIONS
   ========================= */

.notifications-list {
	display: flex;

	flex-direction: column;
}

.notification-item {
	display: flex;

	align-items: center;

	gap: 14px;

	padding: 15px 0;

	border-bottom: 1px solid #E2E8F0;
}

.notification-item:last-child {
	border-bottom: none;
}

.notification-icon {
	width: 42px;
	height: 42px;

	display: flex;

	align-items: center;
	justify-content: center;

	flex-shrink: 0;

	background: #EEF4FF;

	color: #2563EB;

	border-radius: 11px;
}

.notification-item strong {
	display: block;

	font-size: 14px;

	color: #0F172A;
}

.notification-item span {
	display: block;

	margin-top: 4px;

	font-size: 12px;

	color: #64748B;
}


/* =========================
   AI
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

	.fees-grid {
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

	.children-grid {
		grid-template-columns: 1fr;
	}
}

@media (max-width: 800px) {
	.sidebar {
		position: relative;

		width: 100%;

		height: auto;
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

	.children-grid {
		grid-template-columns: 1fr;
	}

	.attendance-stats {
		grid-template-columns: 1fr;
	}

	.fees-grid {
		grid-template-columns: 1fr;
	}

	.prompt-list {
		grid-template-columns: 1fr;
	}

	.table {
		overflow-x: auto;
	}

	.table-header,
	.table-row {
		min-width: 650px;
	}
}
</style>