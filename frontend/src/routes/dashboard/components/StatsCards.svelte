<script lang="ts">
	import {
		GraduationCap,
		Users,
		Building2
	} from '@lucide/svelte';

	import type { DashboardData } from '$lib/services/dashboard';

	let { dashboardData }: { dashboardData: DashboardData } = $props();

	const stats = $derived([
		{
			title: 'Students',
			value: dashboardData.students,
			icon: GraduationCap
		},
		{
			title: 'Teachers',
			value: dashboardData.teachers,
			icon: Users
		},
		{
			title: 'Parents',
			value: dashboardData.parents,
			icon: Users
		},
		{
			title: 'Classes',
			value: dashboardData.classes,
			icon: Building2
		}
	]);
</script>

<section class="stats">

	{#each stats as stat}

		<div class="card">

			<div class="icon">

				<stat.icon size={28} />

			</div>

			<div class="info">

				<h2>{stat.value}</h2>

				<p>{stat.title}</p>

			</div>

		</div>

	{/each}

</section>

<style lang="scss">
@use '$lib/styles/_colors' as c;

.stats{

	display:grid;

	grid-template-columns:repeat(4,1fr);

	gap:24px;

	margin-bottom:32px;

}

.card{

	background:white;

	border-radius:22px;

	padding:28px;

	border:1px solid c.$border;

	display:flex;

	align-items:center;

	gap:18px;

	box-shadow:0 10px 25px rgba(15,23,42,.05);

	transition:.3s;

}

.card:hover{

	transform:translateY(-4px);

	box-shadow:0 20px 40px rgba(37,99,235,.12);

}

.icon{

	width:64px;

	height:64px;

	border-radius:18px;

	background:#EEF4FF;

	color:#2563EB;

	display:flex;

	align-items:center;

	justify-content:center;

}

.info h2{

	margin:0;

	font-size:32px;

	font-weight:800;

	color:c.$text-primary;

}

.info p{

	margin-top:6px;

	font-size:15px;

	color:c.$text-secondary;

}

@media(max-width:1100px){

	.stats{

		grid-template-columns:repeat(2,1fr);

	}

}

@media(max-width:700px){

	.stats{

		grid-template-columns:1fr;

	}

}
</style>