<script lang="ts">
	import PrincipalSidebar from '$lib/components/principal/PrincipalSidebar.svelte';
	import StudentAccess from '$lib/components/principal/StudentAccess.svelte';
</script>

<div class="principal-layout">
	<PrincipalSidebar />

	<main class="main-content">
		<header class="page-header">
			<div>
				<h1>Students</h1>
				<p>Search and view complete student information.</p>
			</div>
		</header>

		<StudentAccess />
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
		margin-bottom: 4px;
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