<script lang="ts">
	import AttendanceOverview from '$lib/components/principal/AttendanceOverview.svelte';
	import AttendanceTable from '$lib/components/principal/AttendanceTable.svelte';

	let showResults = $state(false);

	function viewEmployeeAttendance() {
		showResults = true;
	}
</script>

<section class="employee-attendance">
	<div class="section-header">
		<div>
			<h2>Employee / Staff Attendance</h2>
			<p>
				View attendance of employees and staff for a selected department.
			</p>
		</div>
	</div>

	<div class="selection-card">
		<div class="field">
			<label for="employee-department">Department</label>

			<select id="employee-department">
				<option value="">Select Department</option>
				<option value="all">All Departments</option>
				<option value="administration">Administration</option>
				<option value="library">Library</option>
				<option value="accounts">Accounts</option>
				<option value="transport">Transport</option>
				<option value="office">Office</option>
				<option value="security">Security</option>
				<option value="maintenance">Maintenance</option>
				<option value="other">Other</option>
			</select>
		</div>

		<div class="field">
			<label for="employee-period">Attendance Period</label>

			<select id="employee-period">
				<option value="today">Today</option>
				<option value="this-week">This Week</option>
				<option value="last-week">Last Week</option>
				<option value="this-month">This Month</option>
				<option value="last-month" selected>Last Month</option>
				<option value="custom">Custom Date Range</option>
			</select>
		</div>

		<div class="field info-field">
			<span class="field-label">Employees Included</span>

			<span class="field-info">
				All employees assigned to the selected department
			</span>
		</div>

		<div class="field info-field">
			<span class="field-label">Attendance Type</span>

			<span class="field-info">
				Working days, present, leave and absent records
			</span>
		</div>

		<button type="button" class="view-button" onclick={viewEmployeeAttendance}>
			View Employee Attendance
		</button>
	</div>

	{#if showResults}
		<div class="result-heading">
			<div>
				<h3>Library Department</h3>
				<p>All employees in this department · Last Month</p>
			</div>
		</div>

		<AttendanceOverview />

		<AttendanceTable />
	{/if}
</section>

<style>
	.employee-attendance {
		margin-top: 24px;
	}

	.section-header {
		margin-bottom: 14px;
	}

	.section-header h2 {
		margin: 0;
		color: #14213d;
		font-size: 20px;
	}

	.section-header p {
		margin: 5px 0 0;
		color: #64748b;
		font-size: 13px;
	}

	.selection-card {
		display: grid;
		grid-template-columns: repeat(4, 1fr);
		gap: 16px;
		padding: 22px;
		background: white;
		border: 1px solid #e5eaf2;
		border-radius: 16px;
		box-shadow: 0 4px 14px rgba(15, 23, 42, 0.03);
	}

	.field {
		min-width: 0;
	}

	.field label,
	.field-label {
		display: block;
		margin-bottom: 7px;
		color: #334155;
		font-size: 12px;
		font-weight: 600;
	}

	select {
		width: 100%;
		height: 42px;
		padding: 0 11px;
		box-sizing: border-box;
		border: 1px solid #dbe3ef;
		border-radius: 9px;
		background: white;
		color: #1e293b;
		font-size: 13px;
		outline: none;
	}

	select:focus {
		border-color: #2563eb;
		box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.1);
	}

	.info-field {
		padding: 11px 13px;
		border: 1px solid #e5eaf2;
		border-radius: 9px;
		background: #f8fafc;
	}

	.field-info {
		display: block;
		color: #64748b;
		font-size: 11px;
		line-height: 1.4;
	}

	.view-button {
		grid-column: span 4;
		height: 42px;
		border: none;
		border-radius: 9px;
		background: #2563eb;
		color: white;
		font-size: 13px;
		font-weight: 600;
		cursor: pointer;
	}

	.view-button:hover {
		background: #1d4ed8;
	}

	.result-heading {
		display: flex;
		align-items: center;
		justify-content: space-between;
		margin-top: 24px;
		padding: 18px 20px;
		background: #f8fafc;
		border: 1px solid #e5eaf2;
		border-radius: 13px;
	}

	.result-heading h3 {
		margin: 0;
		color: #14213d;
		font-size: 16px;
	}

	.result-heading p {
		margin: 5px 0 0;
		color: #64748b;
		font-size: 12px;
	}

	@media (max-width: 900px) {
		.selection-card {
			grid-template-columns: repeat(2, 1fr);
		}

		.view-button {
			grid-column: span 2;
		}
	}

	@media (max-width: 550px) {
		.selection-card {
			grid-template-columns: 1fr;
		}

		.view-button {
			grid-column: span 1;
		}
	}
</style>