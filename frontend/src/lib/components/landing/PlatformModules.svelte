<script lang="ts">
	import {
		FileText,
		CalendarDays,
		LayoutDashboard,
		Library,
		Users,
		Award,
		Brain,
		ClipboardCheck,
		UserSquare2,
		Trophy,
		Fingerprint,
		BarChart3
	} from '@lucide/svelte';

	const modules = [
		{
			title: 'AI Document Reader',
			description: 'Extract student details using AI.',
			icon: FileText
		},
		{
			title: 'Smart Timetable',
			description: 'Generate and manage schedules.',
			icon: CalendarDays
		},
		{
			title: 'Admin Dashboard',
			description: 'Monitor your institution easily.',
			icon: LayoutDashboard
		},
		{
			title: 'Digital Library',
			description: 'Manage books and transactions.',
			icon: Library
		},
		{
			title: 'Parent Portal',
			description: 'Connect parents with students.',
			icon: Users
		},
		{
			title: 'Certificates',
			description: 'Issue and approve certificates.',
			icon: Award
		},
		{
			title: 'AI Exam Tutor',
			description: 'AI-powered learning assistant.',
			icon: Brain
		},
		{
			title: 'Leave Workflow',
			description: 'Leave approval management.',
			icon: ClipboardCheck
		},
		{
			title: 'Bio-data Profiles',
			description: 'Student & staff information.',
			icon: UserSquare2
		},
		{
			title: 'Merit System',
			description: 'Recognize achievements.',
			icon: Trophy
		},
		{
			title: 'Auto Attendance',
			description: 'RFID & Face Attendance Ready.',
			icon: Fingerprint
		},
		{
			title: 'Smart Staffing',
			description: 'AI staffing recommendations.',
			icon: BarChart3
		}
	];
</script>

<section
	id="modules"
	class="modules"
>

	<div class="container">

		<div class="section-title">

			<h2>Platform Modules</h2>

			<p>
				Everything your institution needs in one intelligent platform.
			</p>

		</div>

		<div class="grid">

			{#each modules as module}

				<div class="card">

					<div class="icon">

						<module.icon size={30} />

					</div>

					<h3>{module.title}</h3>

					<p>{module.description}</p>

				</div>

			{/each}

		</div>

	</div>

</section>

<style lang="scss">
@use '$lib/styles/_colors' as c;

.modules{

	padding:100px 0;

	background:#f8fafc;

}


.section-title {

	text-align:center;

	max-width:700px;

	margin:0 auto 70px;

}

.section-title h2{

	font-size:42px;

	font-weight:800;

	color:c.$text-primary;

	margin-bottom:16px;

}

.section-title p{

	font-size:18px;

	line-height:1.8;

	color:c.$text-secondary;

}

.grid{

	display:grid;

	grid-template-columns:repeat(4,1fr);

	gap:28px;

}

.card{

	background:white;

	padding:32px;

	border-radius:22px;

	border:1px solid c.$border;

	transition:all .3s ease;

	box-shadow:0 8px 24px rgba(15,23,42,.05);

	text-align:center;

}

.card:hover{

	transform:translateY(-8px);

	border-color:c.$primary;

	box-shadow:0 20px 40px rgba(37,99,235,.12);

}

.icon{

	width:72px;

	height:72px;

	margin:0 auto 22px;

	display:flex;

	align-items:center;

	justify-content:center;

	border-radius:18px;

	background:rgba(37,99,235,.08);

	color:c.$primary;

}

.card h3{

	font-size:20px;

    font-weight: 700;

	margin-bottom:12px;

	color:c.$text-primary;

    margin-bottom:12px;

}

.card p{

	font-size:15px;

	line-height:1.7;

	color:c.$text-secondary;

}

@media(max-width:1100px){

	.grid{

		grid-template-columns:repeat(2,1fr);

	}

}

@media(max-width:700px){

	.grid{

		grid-template-columns:1fr;

	}

}
</style>