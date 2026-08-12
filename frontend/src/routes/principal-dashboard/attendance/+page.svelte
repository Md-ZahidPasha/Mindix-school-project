<script lang="ts">
	import PrincipalSidebar from '$lib/components/principal/PrincipalSidebar.svelte';
	import AttendanceTypeSelector from '$lib/components/principal/AttendanceTypeSelector.svelte';
	import StudentAttendance from '$lib/components/principal/StudentAttendance.svelte';
	import TeacherAttendance from '$lib/components/principal/TeacherAttendance.svelte';
	import EmployeeAttendance from '$lib/components/principal/EmployeeAttendance.svelte';

	let selectedType = $state<'students' | 'teachers' | 'employees'>('students');
</script>

<div class="principal-layout">
	<PrincipalSidebar />

	<main class="main-content">
		<header class="page-header">
			<div>
				<h1>Attendance</h1>
				<p>View and monitor attendance of students, teachers and employees.</p>
			</div>
		</header>

		<AttendanceTypeSelector bind:selectedType />

		<div class="attendance-content">
			{#if selectedType === 'students'}
				<StudentAttendance />
			{:else if selectedType === 'teachers'}
				<TeacherAttendance />
			{:else}
				<EmployeeAttendance />
			{/if}
		</div>
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
		min-width: 0;
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

	.attendance-content {
		margin-top: 4px;
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