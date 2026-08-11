<script lang="ts">
	import PrincipalSidebar from '$lib/components/principal/PrincipalSidebar.svelte';
	import EmployeeAccess from '$lib/components/principal/EmployeeAccess.svelte';
</script>

<div class="principal-layout">
	<PrincipalSidebar />

	<main class="main-content">
		<header class="page-header">
			<div>
				<h1>Employees / Staff</h1>
				<p>Search and view complete employee information.</p>
			</div>
		</header>

		<EmployeeAccess />
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
		box-sizing: border-box;
	}

	.page-header {
		margin-bottom: 24px;
	}

	.page-header h1 {
		margin: 0;
		color: #14213d;
		font-size: 30px;
	}

	.page-header p {
		margin: 7px 0 0;
		color: #64748b;
		font-size: 15px;
	}

	@media (max-width: 700px) {
		.main-content {
			padding: 20px;
		}

		.page-header h1 {
			font-size: 25px;
		}
	}
</style>