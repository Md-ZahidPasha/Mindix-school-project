<script lang="ts">
	import {
		LayoutDashboard,
		UserCog,
		GraduationCap,
		Users,
		Building2,
		CalendarCheck,
		FileText,
		Library,
		IndianRupee,
		Bot,
		BarChart3,
		Settings,
		LogOut,
		School
	} from '@lucide/svelte';

	const menuItems = [
		{
			icon: LayoutDashboard,
			label: 'Dashboard',
			active: true
		},
		{
			icon: UserCog,
			label: 'Principal',
			active: false
		},
		{
			icon: Users,
			label: 'Teachers',
			active: false
		},
		{
			icon: GraduationCap,
			label: 'Students',
			active: false
		},
		{
			icon: Users,
			label: 'Parents',
			active: false
		},
		{
			icon: Building2,
			label: 'Classes',
			active: false
		},
		{
			icon: CalendarCheck,
			label: 'Attendance',
			active: false
		},
		{
			icon: FileText,
			label: 'Exams',
			active: false
		},
		{
			icon: Library,
			label: 'Library',
			active: false
		},
		{
			icon: IndianRupee,
			label: 'Fees',
			active: false
		},
		{
			icon: Bot,
			label: 'AI Assistant',
			active: false
		},
		{
			icon: BarChart3,
			label: 'Reports',
			active: false
		},
		{
			icon: Settings,
			label: 'Settings',
			active: false
		}
	];
</script>

<aside class="sidebar">

	<div class="logo">

		<School size={34} />

		<h2>PaperBuddy</h2>

	</div>

	<nav>

		{#each menuItems as item}

			<div
				class:item-active={item.active}
				class="menu-item"
			>

				<item.icon size={22} />

				<span>{item.label}</span>

			</div>

		{/each}

	</nav>

	<div class="profile-card">

		<div class="avatar">
			👤
		</div>

		<div class="profile-info">

			<h4>Admin</h4>

			<p>PaperBuddy Admin</p>

		</div>

	</div>

	<div class="logout">

		<LogOut size={20} />

		<span>Logout</span>

	</div>

</aside>

<style lang="scss">
@use '$lib/styles/_colors' as c;

.sidebar {
	width: 280px;
	height: 100vh;
	position: fixed;
	left: 0;
	top: 0;
	background: white;
	border-right: 1px solid c.$border;
	display: flex;
	flex-direction: column;
	padding: 28px 20px;
	overflow-y: auto;
}

.logo {
	display: flex;
	align-items: center;
	gap: 14px;
	color: c.$primary;
	font-size: 18px;
	font-weight: 800;
	margin-bottom: 40px;
}

.logo h2 {
	margin: 0;
	color: c.$primary;
}

nav {
	flex: 1;
	display: flex;
	flex-direction: column;
	gap: 8px;
	overflow-y: auto;
	padding-right: 6px;
}

.menu-item {
	display: flex;
	align-items: center;
	gap: 14px;
	padding: 14px 18px;
	border-radius: 14px;
	cursor: pointer;
	color: c.$text-secondary;
	transition: .25s;
	font-weight: 600;
}

.menu-item:hover {
	background: #eef4ff;
	color: c.$primary;
}

.item-active {
	background: #2563eb;
	color: white;
	box-shadow: 0 10px 25px rgba(37, 99, 235, .25);
}

.logout {
	display: flex;
	align-items: center;
	gap: 14px;
	padding: 14px 18px;
	border-radius: 14px;
	cursor: pointer;
	color: #ef4444;
	font-weight: 600;
	transition: .25s;
}

.logout:hover {
	background: #fef2f2;
}

.profile-card {
	display: flex;
	align-items: center;
	gap: 12px;
	padding: 16px;
	margin-top: 20px;
	margin-bottom: 16px;
	background: #F8FAFC;
	border: 1px solid c.$border;
	border-radius: 16px;
}

.avatar {
	width: 48px;
	height: 48px;
	border-radius: 50%;
	background: #2563EB;
	color: white;
	display: flex;
	align-items: center;
	justify-content: center;
	font-size: 20px;
}

.profile-info h4 {
	margin: 0;
	font-size: 15px;
	font-weight: 700;
	color: c.$text-primary;
}

.profile-info p {
	margin: 4px 0 0;
	font-size: 13px;
	color: c.$text-secondary;
}
</style>