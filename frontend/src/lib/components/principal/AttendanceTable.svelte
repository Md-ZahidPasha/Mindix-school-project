<script lang="ts">
	type AttendanceType = 'students' | 'teachers' | 'employees';

	type AttendanceRow = {
		name: string;
		id: string;
		role?: string;
		total: number;
		attended: number;
		leave: number;
		absent: number;
		percentage: number;
	};

	let attendanceType = $state<AttendanceType>('students');

	let rows = $state<AttendanceRow[]>([
		{
			name: 'Rahul Sharma',
			id: 'STU1024',
			total: 20,
			attended: 19,
			leave: 1,
			absent: 0,
			percentage: 95
		},
		{
			name: 'Aisha Khan',
			id: 'STU1025',
			total: 20,
			attended: 18,
			leave: 0,
			absent: 2,
			percentage: 90
		},
		{
			name: 'Ahmed Ali',
			id: 'STU1026',
			total: 20,
			attended: 20,
			leave: 0,
			absent: 0,
			percentage: 100
		},
		{
			name: 'Priya Sharma',
			id: 'STU1027',
			total: 20,
			attended: 17,
			leave: 1,
			absent: 2,
			percentage: 85
		}
	]);

	let tableTitle = $derived(
		attendanceType === 'students'
			? 'Student Attendance'
			: attendanceType === 'teachers'
				? 'Teacher Attendance'
				: 'Employee / Staff Attendance'
	);

	let idLabel = $derived(
		attendanceType === 'students'
			? 'Student ID'
			: attendanceType === 'teachers'
				? 'Teacher ID'
				: 'Employee ID'
	);

	let totalLabel = $derived(
		attendanceType === 'employees'
			? 'Working Days'
			: 'Total Classes'
	);

	let attendedLabel = $derived(
		attendanceType === 'employees'
			? 'Present'
			: 'Attended'
	);

	function loadStudentData() {
		attendanceType = 'students';

		rows = [
			{
				name: 'Rahul Sharma',
				id: 'STU1024',
				total: 20,
				attended: 19,
				leave: 1,
				absent: 0,
				percentage: 95
			},
			{
				name: 'Aisha Khan',
				id: 'STU1025',
				total: 20,
				attended: 18,
				leave: 0,
				absent: 2,
				percentage: 90
			},
			{
				name: 'Ahmed Ali',
				id: 'STU1026',
				total: 20,
				attended: 20,
				leave: 0,
				absent: 0,
				percentage: 100
			},
			{
				name: 'Priya Sharma',
				id: 'STU1027',
				total: 20,
				attended: 17,
				leave: 1,
				absent: 2,
				percentage: 85
			}
		];
	}

	function loadTeacherData() {
		attendanceType = 'teachers';

		rows = [
			{
				name: 'Rahul Verma',
				id: 'TCH102',
				total: 24,
				attended: 23,
				leave: 1,
				absent: 0,
				percentage: 95.8
			},
			{
				name: 'Sana Khan',
				id: 'TCH103',
				total: 20,
				attended: 19,
				leave: 0,
				absent: 1,
				percentage: 95
			},
			{
				name: 'Ahmed Ali',
				id: 'TCH104',
				total: 18,
				attended: 17,
				leave: 1,
				absent: 0,
				percentage: 94.4
			},
			{
				name: 'Priya Sharma',
				id: 'TCH105',
				total: 22,
				attended: 20,
				leave: 1,
				absent: 1,
				percentage: 90.9
			}
		];
	}

	function loadEmployeeData() {
		attendanceType = 'employees';

		rows = [
			{
				name: 'Ahmed Khan',
				id: 'EMP102',
				role: 'Library Assistant',
				total: 25,
				attended: 24,
				leave: 1,
				absent: 0,
				percentage: 96
			},
			{
				name: 'Sara Ali',
				id: 'EMP103',
				role: 'Accountant',
				total: 25,
				attended: 23,
				leave: 1,
				absent: 1,
				percentage: 92
			},
			{
				name: 'Arif Hussain',
				id: 'EMP104',
				role: 'Office Assistant',
				total: 25,
				attended: 22,
				leave: 2,
				absent: 1,
				percentage: 88
			},
			{
				name: 'Fatima Noor',
				id: 'EMP105',
				role: 'Receptionist',
				total: 25,
				attended: 24,
				leave: 0,
				absent: 1,
				percentage: 96
			}
		];
	}
</script>

<section class="attendance-table-section">
	<div class="table-header">
		<div>
			<h2>{tableTitle}</h2>
			<p>Detailed attendance records for the selected period.</p>
		</div>
	</div>

	<div class="table-wrapper">
		<table>
			<thead>
				<tr>
					<th>Name</th>
					<th>{idLabel}</th>

					{#if attendanceType === 'employees'}
						<th>Role</th>
					{/if}

					<th>{totalLabel}</th>
					<th>{attendedLabel}</th>
					<th>Leave</th>
					<th>Absent</th>
					<th>Attendance %</th>
				</tr>
			</thead>

			<tbody>
				{#each rows as row}
					<tr>
						<td>
							<strong>{row.name}</strong>
						</td>

						<td>{row.id}</td>

						{#if attendanceType === 'employees'}
							<td>{row.role}</td>
						{/if}

						<td>{row.total}</td>
						<td>{row.attended}</td>
						<td>{row.leave}</td>
						<td>{row.absent}</td>

						<td>
							<span
								class:excellent={row.percentage >= 95}
								class:good={row.percentage >= 90 && row.percentage < 95}
								class:warning={row.percentage < 90}
								class="percentage"
							>
								{row.percentage}%
							</span>
						</td>
					</tr>
				{/each}
			</tbody>
		</table>
	</div>

	<div class="demo-controls">
		<button type="button" onclick={loadStudentData}>Student Data</button>
		<button type="button" onclick={loadTeacherData}>Teacher Data</button>
		<button type="button" onclick={loadEmployeeData}>Staff Data</button>
	</div>
</section>

<style>
	.attendance-table-section {
		margin-top: 24px;
	}

	.table-header {
		margin-bottom: 14px;
	}

	.table-header h2 {
		margin: 0;
		color: #14213d;
		font-size: 20px;
	}

	.table-header p {
		margin: 5px 0 0;
		color: #64748b;
		font-size: 13px;
	}

	.table-wrapper {
		width: 100%;
		overflow-x: auto;
		background: white;
		border: 1px solid #e5eaf2;
		border-radius: 16px;
		box-shadow: 0 4px 14px rgba(15, 23, 42, 0.03);
	}

	table {
		width: 100%;
		min-width: 760px;
		border-collapse: collapse;
	}

	th,
	td {
		padding: 15px 16px;
		border-bottom: 1px solid #eef2f7;
		text-align: left;
		white-space: nowrap;
	}

	th {
		background: #f8fafc;
		color: #64748b;
		font-size: 11px;
		font-weight: 700;
		text-transform: uppercase;
		letter-spacing: 0.02em;
	}

	td {
		color: #475569;
		font-size: 13px;
	}

	tbody tr:last-child td {
		border-bottom: none;
	}

	tbody tr:hover {
		background: #fafcff;
	}

	td strong {
		color: #1e293b;
		font-size: 13px;
	}

	.percentage {
		display: inline-flex;
		align-items: center;
		justify-content: center;
		min-width: 58px;
		padding: 5px 8px;
		border-radius: 7px;
		font-size: 11px;
		font-weight: 700;
	}

	.percentage.excellent {
		background: #ecfdf3;
		color: #15803d;
	}

	.percentage.good {
		background: #eff6ff;
		color: #2563eb;
	}

	.percentage.warning {
		background: #fff7ed;
		color: #c2410c;
	}

	.demo-controls {
		display: flex;
		gap: 8px;
		margin-top: 12px;
	}

	.demo-controls button {
		padding: 7px 11px;
		border: 1px solid #dbe3ef;
		border-radius: 8px;
		background: white;
		color: #64748b;
		font-size: 11px;
		font-weight: 600;
		cursor: pointer;
	}

	.demo-controls button:hover {
		background: #f8fafc;
	}

	@media (max-width: 600px) {
		.demo-controls {
			flex-wrap: wrap;
		}
	}
</style>