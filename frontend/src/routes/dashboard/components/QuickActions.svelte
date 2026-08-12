<script lang="ts">
	import {
		UserCog,
		Users,
		GraduationCap,
		Briefcase
	} from '@lucide/svelte';

	const actions = [
	{
		title: 'Add Principal',
		description: 'Create principal account.',
		icon: UserCog
	},
	{
		title: 'Add Teacher',
		description: 'Create teacher account.',
		icon: Users
	},
	{
		title: 'Add Student',
		description: 'Enroll new student.',
		icon: GraduationCap
	},
	{
		title: 'Add Employee',
		description: 'Drivers, Lab Assistants, Accountants & Office Staff.',
		icon: Briefcase
	}
];

</script>

<section class="quick-actions">

	<div class="section-header">

		<h2>Add New Members</h2>

<p>Manage your institution by adding new members.</p>

	</div>

	<div class="grid">

		{#each actions as action}

	<div class="action-card">

		<div class="icon">

			<action.icon size={34} />

		</div>

		<h3>{action.title}</h3>

		<p>{action.description}</p>

		<button class="add-btn">

			+ Add

		</button>

	</div>

{/each}

	</div>

</section>

<style lang="scss">
@use '$lib/styles/_colors' as c;

.quick-actions{

	background:white;

	border:1px solid c.$border;

	border-radius:24px;

	padding:28px;

	box-shadow:0 10px 25px rgba(15,23,42,.05);

}

.section-header{

	margin-bottom:24px;

}

.section-header h2{

	font-size:24px;

	font-weight:800;

	color:c.$text-primary;

	margin-bottom:6px;

}

.section-header p{

	color:c.$text-secondary;

	font-size:14px;

}

.grid{

	display:grid;

	grid-template-columns:repeat(2,1fr);

	gap:18px;

}

.action-card{

	border:1px solid c.$border;

	border-radius:22px;

	padding:28px;

	background:white;

	display:flex;

	flex-direction:column;

	align-items:center;

	justify-content:space-between;

	text-align:center;

	min-height:250px;

	transition:.3s;

}

.action-card:hover{

	transform:translateY(-8px);

	border-color:#2563EB;

	box-shadow:0 18px 36px rgba(37,99,235,.15);

}

.icon{

	width:72px;

	height:72px;

	border-radius:20px;

	background:#EEF4FF;

	color:#2563EB;

	display:flex;

	align-items:center;

	justify-content:center;

	margin-bottom:20px;

}

.action-card h3{

	font-size:20px;

	font-weight:700;

	margin-bottom:12px;

	color:c.$text-primary;

}

.action-card p{

	font-size:14px;

	line-height:1.7;

	color:c.$text-secondary;

	margin-bottom:24px;

	min-height:48px;

}

.add-btn{

	width:140px;

	height:44px;

	border:none;

	border-radius:12px;

	background:linear-gradient(135deg,#2563EB,#4F46E5);

	color:white;

	font-size:15px;

	font-weight:700;

	cursor:pointer;

	transition:.3s;

}

.add-btn:hover{

	transform:translateY(-2px);

	box-shadow:0 12px 24px rgba(37,99,235,.25);

}



@media(max-width:900px){

	.grid{

		grid-template-columns:1fr;

	}

}
</style>