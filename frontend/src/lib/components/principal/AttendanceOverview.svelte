<script lang="ts">
	type AttendanceType = 'students' | 'teachers' | 'employees';

	let attendanceType = $state<AttendanceType>('students');

	let title = $derived(
		attendanceType === 'students'
			? 'Overall Student Attendance'
			: attendanceType === 'teachers'
				? 'Overall Teacher Attendance'
				: 'Overall Employee / Staff Attendance'
	);

	let subtitle = $derived(
		attendanceType === 'students'
			? 'Attendance summary for the selected class, section and class time.'
			: attendanceType === 'teachers'
				? 'Attendance summary for teachers assigned to the selected class and section.'
				: 'Attendance summary for the selected department.'
	);

	let overallAttendance = $state(92.4);
	let total = $state(40);
	let present = $state(185);
	let absent = $state(12);
	let leave = $state(3);

	function updateAttendance(
		type: AttendanceType,
		attendance: number,
		totalCount: number,
		presentCount: number,
		absentCount: number,
		leaveCount: number
	) {
		attendanceType = type;
		overallAttendance = attendance;
		total = totalCount;
		present = presentCount;
		absent = absentCount;
		leave = leaveCount;
	}
</script>

<section class="attendance-overview">
	<div class="overview-header">
		<div>
			<h2>{title}</h2>
			<p>{subtitle}</p>
		</div>

		<div class="attendance-percentage">
			<span>Overall Attendance</span>
			<strong>{overallAttendance}%</strong>
		</div>
	</div>

	<div class="summary-grid">
		<div class="summary-card">
			<span class="summary-label">
				{attendanceType === 'employees' ? 'Total Staff' : attendanceType === 'teachers' ? 'Total Teachers' : 'Total Students'}
			</span>

			<strong>{total}</strong>
		</div>

		<div class="summary-card">
			<span class="summary-label">
				{attendanceType === 'employees' ? 'Present Days' : 'Present'}
			</span>

			<strong>{present}</strong>
		</div>

		<div class="summary-card">
			<span class="summary-label">
				{attendanceType === 'employees' ? 'Absent Days' : 'Absent'}
			</span>

			<strong>{absent}</strong>
		</div>

		<div class="summary-card">
			<span class="summary-label">
				{attendanceType === 'employees' ? 'Leave Days' : 'Leave'}
			</span>

			<strong>{leave}</strong>
		</div>
	</div>

	<div class="demo-switcher">
		<button
			type="button"
			class:active={attendanceType === 'students'}
			onclick={() => updateAttendance('students', 92.4, 40, 185, 12, 3)}
		>
			Student Data
		</button>

		<button
			type="button"
			class:active={attendanceType === 'teachers'}
			onclick={() => updateAttendance('teachers', 94.2, 6, 113, 3, 4)}
		>
			Teacher Data
		</button>

		<button
			type="button"
			class:active={attendanceType === 'employees'}
			onclick={() => updateAttendance('employees', 93.8, 8, 145, 3, 7)}
		>
			Staff Data
		</button>
	</div>
</section>

<style>
	.attendance-overview {
		margin-top: 24px;
	}

	.overview-header {
		display: flex;
		align-items: center;
		justify-content: space-between;
		gap: 20px;
		margin-bottom: 16px;
	}

	.overview-header h2 {
		margin: 0;
		color: #14213d;
		font-size: 20px;
	}

	.overview-header p {
		margin: 5px 0 0;
		color: #64748b;
		font-size: 13px;
	}

	.attendance-percentage {
		min-width: 170px;
		padding: 15px 18px;
		border: 1px solid #dbe3ef;
		border-radius: 12px;
		background: #f8fafc;
		text-align: right;
	}

	.attendance-percentage span {
		display: block;
		margin-bottom: 4px;
		color: #64748b;
		font-size: 11px;
	}

	.attendance-percentage strong {
		color: #2563eb;
		font-size: 24px;
	}

	.summary-grid {
		display: grid;
		grid-template-columns: repeat(4, 1fr);
		gap: 14px;
	}

	.summary-card {
		padding: 18px;
		border: 1px solid #e5eaf2;
		border-radius: 13px;
		background: white;
		box-shadow: 0 4px 14px rgba(15, 23, 42, 0.03);
	}

	.summary-label {
		display: block;
		margin-bottom: 8px;
		color: #64748b;
		font-size: 12px;
	}

	.summary-card strong {
		color: #14213d;
		font-size: 23px;
	}

	.demo-switcher {
		display: flex;
		gap: 8px;
		margin-top: 14px;
	}

	.demo-switcher button {
		padding: 7px 11px;
		border: 1px solid #dbe3ef;
		border-radius: 8px;
		background: white;
		color: #64748b;
		font-size: 11px;
		font-weight: 600;
		cursor: pointer;
	}

	.demo-switcher button.active {
		border-color: #2563eb;
		background: #2563eb;
		color: white;
	}

	@media (max-width: 800px) {
		.overview-header {
			align-items: flex-start;
			flex-direction: column;
		}

		.attendance-percentage {
			width: 100%;
			box-sizing: border-box;
			text-align: left;
		}

		.summary-grid {
			grid-template-columns: repeat(2, 1fr);
		}
	}

	@media (max-width: 500px) {
		.summary-grid {
			grid-template-columns: 1fr;
		}

		.demo-switcher {
			flex-wrap: wrap;
		}
	}
</style>