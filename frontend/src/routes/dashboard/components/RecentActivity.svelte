<script lang="ts">
	import {
		CheckCircle2,
		UserPlus,
		GraduationCap,
		CalendarCheck,
		FileText
	} from '@lucide/svelte';

    const activities = [
	{
		icon: CheckCircle2,
		title: 'Institution Registered',
		time: 'Today • 10:30 AM'
	},
	{
		icon: UserPlus,
		title: 'Teacher Added',
		time: 'Today • 09:45 AM'
	},
	{
		icon: GraduationCap,
		title: 'Student Enrolled',
		time: 'Yesterday • 04:15 PM'
	},
	{
		icon: CalendarCheck,
		title: 'Attendance Updated',
		time: 'Yesterday • 11:20 AM'
	},
	{
		icon: FileText,
		title: 'Exam Schedule Published',
		time: '2 Days Ago'
	}
];
</script>

<section class="activity">

<div class="section-header">

	<div class="title-row">

		<h2>Notifications & Activity</h2>

		<span class="badge">

			5 New

		</span>

	</div>

	<p>Stay updated with institution events.</p>

</div>

	<div class="activity-list">

		{#each activities as activity}

			<div class="activity-item">

	<div class="icon">

		<activity.icon size={20} />

	</div>

	<div class="content">

		<h4>{activity.title}</h4>

		<p>PaperBuddy System</p>

	</div>

	<span class="time">

		{activity.time}

	</span>

</div>

		{/each}

	</div>

</section>

<style lang="scss">
@use '$lib/styles/_colors' as c;

.activity{

	background:white;

	border:1px solid c.$border;

	border-radius:24px;

	padding:28px;

	box-shadow:0 10px 25px rgba(15,23,42,.05);
    
	height: 100%;

	box-sizing: border-box;

	display: flex;

	flex-direction: column;
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

	font-size:14px;

	color:c.$text-secondary;

}

.activity-list{

	display:flex;

	flex-direction:column;

	gap: 28px;

	flex: 1;

	justify-content: flex-start;

}

.activity-item{

	display:grid;

	grid-template-columns:52px 1fr auto;

	align-items:center;

	gap:12px;

	padding: 14px 12px;

	border-radius:16px;

	border:1px solid transparent;

	transition:.3s;

}

.activity-item:hover{

	transform:translateY(-3px);

	border-color:#2563EB;

	box-shadow:0 12px 24px rgba(37,99,235,.08);

}

.icon{

	width: 46px;

	height:46px;

	border-radius:16px;

	background:#EEF4FF;

	color:#2563EB;

	display:flex;

	align-items:center;

	justify-content:center;

}

.content{

	display:flex;

	flex-direction:column;

	gap:4px;

}

.content h4{

	margin:0;

	font-size:16px;

	font-weight:700;

	color:c.$text-primary;

}

.content p{

	margin:0;

	font-size:13px;

	color:c.$text-secondary;

}

.time{

	font-size:12px;

	font-weight:600;

	color:#64748B;

}

.content span{

	margin-top:4px;

	font-size:13px;

	color:c.$text-secondary;

}
.title-row{

	display:flex;

	align-items:center;

	justify-content:space-between;

	margin-bottom:8px;

}

.badge{

	background:#2563EB;

	color:white;

	font-size:12px;

	font-weight:700;

	padding:6px 12px;

	border-radius:999px;

}
</style>