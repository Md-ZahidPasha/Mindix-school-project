<script lang="ts">
	import PrincipalSidebar from '$lib/components/principal/PrincipalSidebar.svelte';
	import PrincipalStats from '$lib/components/principal/PrincipalStats.svelte';
	import SchoolOverview from '$lib/components/principal/SchoolOverview.svelte';
</script>

<div class="principal-layout">
	<PrincipalSidebar />

	<main class="main-content">
		<header class="top-header">
			<div>
				<h1>Welcome, Principal</h1>
				<p>Here's what's happening in your institution today.</p>
			</div>

			<div class="header-right">
				<div class="search-box">
					<span>⌕</span>
					<input type="text" placeholder="Search anything..." />
				</div>

				<button class="notification" aria-label="Notifications">
					🔔
					<span>5</span>
				</button>

				<div class="profile">
					<div class="profile-avatar">P</div>

					<div>
						<strong>Principal</strong>
						<small>School Name</small>
					</div>

					<span>⌄</span>
				</div>
			</div>
		</header>

		<section class="welcome-section">
			<h2>Principal Dashboard</h2>
			<p>Manage and monitor your institution from one place.</p>
		</section>
        <PrincipalStats />
        <SchoolOverview />
	</main>
</div>

<style>
	.principal-layout {
		display: flex;
		min-height: 100vh;
		background: #f7f9fc;
	}

	.main-content {
		flex: 1;
		padding: 28px 32px;
	}

	.top-header {
		display: flex;
		align-items: center;
		justify-content: space-between;
		gap: 24px;
	}

	.top-header h1 {
		margin: 0;
		font-size: 30px;
		color: #14213d;
	}

	.top-header p {
		margin: 7px 0 0;
		color: #64748b;
		font-size: 15px;
	}

	.header-right {
		display: flex;
		align-items: center;
		gap: 18px;
	}

	.search-box {
		width: 280px;
		height: 44px;
		display: flex;
		align-items: center;
		gap: 10px;
		padding: 0 14px;
		background: white;
		border: 1px solid #dbe3ef;
		border-radius: 12px;
	}

	.search-box span {
		font-size: 22px;
		color: #64748b;
	}

	.search-box input {
		width: 100%;
		border: none;
		outline: none;
		font-size: 14px;
	}

	.notification {
		position: relative;
		border: none;
		background: transparent;
		font-size: 20px;
		cursor: pointer;
	}

	.notification span {
		position: absolute;
		top: -7px;
		right: -8px;
		width: 18px;
		height: 18px;
		display: flex;
		align-items: center;
		justify-content: center;
		background: #ef4444;
		color: white;
		border-radius: 50%;
		font-size: 10px;
	}

	.profile {
		display: flex;
		align-items: center;
		gap: 10px;
	}

	.profile-avatar {
		width: 42px;
		height: 42px;
		display: flex;
		align-items: center;
		justify-content: center;
		background: #e8f0ff;
		color: #2563eb;
		border-radius: 50%;
		font-weight: 700;
	}

	.profile strong {
		display: block;
		color: #14213d;
		font-size: 14px;
	}

	.profile small {
		display: block;
		margin-top: 3px;
		color: #64748b;
	}

	.profile > span {
		color: #475569;
	}

	.welcome-section {
		margin-top: 35px;
		padding: 30px;
		background: white;
		border: 1px solid #e5eaf2;
		border-radius: 18px;
	}

	.welcome-section h2 {
		margin: 0;
		color: #14213d;
	}

	.welcome-section p {
		margin: 8px 0 0;
		color: #64748b;
	}

	@media (max-width: 900px) {
		.header-right {
			flex-wrap: wrap;
			justify-content: flex-end;
		}

		.search-box {
			width: 220px;
		}
	}
</style>