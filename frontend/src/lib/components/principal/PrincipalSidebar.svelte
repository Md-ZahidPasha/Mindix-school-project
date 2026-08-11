<script lang="ts">
	const menuItems = [
		{ label: 'Dashboard', icon: '⌂', active: true },
		{ label: 'School Overview', icon: '▦' },
		{ label: 'Teachers', icon: '♙' },
		{ label: 'Students', icon: '♧' },
		{ label: 'Employees / Staff', icon: '▣' },
		{ label: 'Attendance', icon: '☑' },
		{ label: 'Smart Timetable', icon: '▤' },
		{ label: 'Teacher Leave', icon: '▢' },
		{ label: 'Library', icon: '▥' },
		{ label: 'Certificates', icon: '▤' },
		{ label: 'Notifications', icon: '♢' },
		{ label: 'Reports', icon: '▥' }
	];
</script>

<aside class="sidebar">
	<div class="brand">
		<div class="brand-icon">📖</div>

		<div>
			<h2>PaperBuddy</h2>
			<p>School Management System</p>
		</div>
	</div>

	<nav class="navigation" aria-label="Principal navigation">
		{#each menuItems as item}
	<a
		href={
			item.label === 'Students'
				? '/principal-dashboard/students'
				: item.label === 'Teachers'
					? '/principal-dashboard/teachers'
					: item.label === 'Employees / Staff'
						? '/principal-dashboard/employees'
                        : item.label === 'Attendance'
						? '/principal-dashboard/attendance'
						: '/principal-dashboard'
		}
		class:active={item.active}
		class="nav-item"
	>
		<span class="nav-icon">{item.icon}</span>
		<span>{item.label}</span>
	</a>
{/each}
	</nav>

	<div class="sidebar-bottom">
		<a href="/principal-dashboard/profile" class="profile-link">
			<span class="bottom-icon">◎</span>
			<span>Profile</span>
		</a>

		<button class="logout" type="button">
			<span class="logout-icon">↪</span>
			<span>Logout</span>
		</button>
	</div>
</aside>

<style>
	.sidebar {
		width: 250px;
		min-height: 100vh;
		display: flex;
		flex-direction: column;
		background: #102a56;
		color: white;
		padding: 22px 14px;
		box-sizing: border-box;
	}

	.brand {
		display: flex;
		align-items: center;
		gap: 10px;
		padding: 4px 8px 24px;
	}

	.brand-icon {
		width: 42px;
		height: 42px;
		display: flex;
		align-items: center;
		justify-content: center;
		background: #1f5fe5;
		border-radius: 10px;
		font-size: 22px;
	}

	.brand h2 {
		margin: 0;
		font-size: 21px;
		font-weight: 700;
	}

	.brand p {
		margin: 3px 0 0;
		font-size: 10px;
		color: #d7e2f4;
	}

	.navigation {
		display: flex;
		flex-direction: column;
		gap: 5px;
	}

	.nav-item,
	.profile-link {
		display: flex;
		align-items: center;
		gap: 13px;
		min-height: 44px;
		padding: 0 14px;
		border-radius: 10px;
		color: #e8eef8;
		text-decoration: none;
		font-size: 14px;
		font-weight: 500;
		transition:
			background 0.2s ease,
			color 0.2s ease;
	}

	.nav-item:hover,
	.profile-link:hover {
		background: rgba(255, 255, 255, 0.1);
	}

	.nav-item.active {
		background: #2f68e8;
		color: white;
		font-weight: 600;
	}

	.nav-icon,
	.bottom-icon,
	.logout-icon {
		width: 22px;
		text-align: center;
		font-size: 18px;
	}

	.sidebar-bottom {
		margin-top: auto;
		padding-top: 20px;
		border-top: 1px solid rgba(255, 255, 255, 0.14);
	}

	.profile-link {
		margin-bottom: 8px;
	}

	.logout {
		width: 100%;
		display: flex;
		align-items: center;
		gap: 13px;
		min-height: 44px;
		padding: 0 14px;
		border: none;
		border-radius: 10px;
		background: transparent;
		color: #ff7777;
		font: inherit;
		font-size: 14px;
		font-weight: 500;
		cursor: pointer;
		text-align: left;
	}

	.logout:hover {
		background: rgba(255, 255, 255, 0.08);
	}

	@media (max-width: 900px) {
		.sidebar {
			width: 220px;
		}
	}
</style>