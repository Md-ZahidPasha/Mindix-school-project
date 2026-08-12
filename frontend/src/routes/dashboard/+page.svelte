<script lang="ts">
	import { onMount } from 'svelte';

	import DashboardSidebar from './components/DashboardSidebar.svelte';
	import DashboardHeader from './components/DashboardHeader.svelte';
	import AIBanner from './components/AIBanner.svelte';
	import StatsCards from './components/StatsCards.svelte';
	import QuickActions from './components/QuickActions.svelte';
	import RecentActivity from './components/RecentActivity.svelte';

	import {
		getDashboard,
		type DashboardData
	} from '$lib/services/dashboard';

	let dashboardData = $state<DashboardData | null>(null);
	let isLoading = $state(true);
	let serverError = $state('');

	async function loadDashboard() {
		isLoading = true;
		serverError = '';

		try {
			dashboardData = await getDashboard();
		} catch (error) {
			serverError =
				error instanceof Error
					? error.message
					: 'Unable to load dashboard data.';
		} finally {
			isLoading = false;
		}
	}

	onMount(() => {
		loadDashboard();
	});
</script>

<div class="dashboard">

	<DashboardSidebar />

	<div class="main-content">

		{#if isLoading}

			<div class="status-card">
				<p>Loading dashboard...</p>
			</div>

		{:else if serverError}

			<div class="status-card error">

				<p>{serverError}</p>

				<button type="button" onclick={loadDashboard}>
					Try Again
				</button>

			</div>

		{:else if dashboardData}

			<DashboardHeader
				institutionName={dashboardData.institution_name}
			/>

			<AIBanner />

			<StatsCards dashboardData={dashboardData} />

			<div class="bottom-grid">

				<div class="left-column">

					<QuickActions />

				</div>

				<div class="right-column">

					<RecentActivity />

				</div>

			</div>

		{/if}

	</div>

</div>

<style lang="scss">

.dashboard{

	display:flex;

	min-height:100vh;

	background:#F8FAFC;

}

.main-content{

	flex:1;

	padding:36px;

	margin-left:300px;

}

.bottom-grid {

	display: grid;

	grid-template-columns: 1.6fr 1.4fr;

	gap: 28px;

	align-items: stretch;

}

.left-column {

	display: flex;

	flex-direction: column;

}

.right-column {

	display: flex;

	flex-direction: column;

}

.status-card {

	background: white;

	border: 1px solid #E2E8F0;

	border-radius: 18px;

	padding: 30px;

	text-align: center;

	color: #475569;

	margin-bottom: 30px;

}

.status-card.error {

	border-color: #FECACA;

	background: #FEF2F2;

	color: #DC2626;

}

.status-card button {

	margin-top: 14px;

	padding: 10px 18px;

	border: none;

	border-radius: 10px;

	background: #2563EB;

	color: white;

	font-weight: 600;

	cursor: pointer;

}

@media(max-width:1100px){

	.main-content{

		margin-left:0;

		padding:20px;

	}

	.bottom-grid{

		grid-template-columns:1fr;

	}

}

</style>