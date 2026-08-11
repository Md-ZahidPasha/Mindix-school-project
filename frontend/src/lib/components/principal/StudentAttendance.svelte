<script lang="ts">
	import AttendanceOverview from '$lib/components/principal/AttendanceOverview.svelte';
	import AttendanceTable from '$lib/components/principal/AttendanceTable.svelte';

	let showResults = $state(false);
	let selectedPeriod = $state('last-month');
	let startDate = $state('');
	let endDate = $state('');

	function viewStudentAttendance() {
		showResults = true;
	}
</script>

<section class="student-attendance">
	<div class="section-header">
		<div>
			<h2>Student Attendance</h2>
			<p>
				View attendance for students of a selected class, section and class time.
			</p>
		</div>
	</div>

	<div class="selection-card">
		<div class="field">
			<label for="student-class">Class</label>

			<select id="student-class">
				<option value="">Select Class</option>
				<option value="class-1">Class 1</option>
				<option value="class-2">Class 2</option>
				<option value="class-3">Class 3</option>
				<option value="class-4">Class 4</option>
				<option value="class-5">Class 5</option>
				<option value="class-6">Class 6</option>
				<option value="class-7">Class 7</option>
				<option value="class-8">Class 8</option>
				<option value="class-9">Class 9</option>
				<option value="class-10">Class 10</option>
				<option value="class-11">Class 11</option>
				<option value="class-12">Class 12</option>
			</select>
		</div>

		<div class="field">
			<label for="student-section">Section</label>

			<select id="student-section">
				<option value="">Select Section</option>
				<option value="a">Section A</option>
				<option value="b">Section B</option>
				<option value="c">Section C</option>
				<option value="d">Section D</option>
			</select>
		</div>

		<div class="field">
			<label for="student-class-time">Class Time</label>

			<select id="student-class-time">
				<option value="">Select Class Time</option>
				<option value="8-9">8:00 AM – 9:00 AM</option>
				<option value="9-10">9:00 AM – 10:00 AM</option>
				<option value="10-11">10:00 AM – 11:00 AM</option>
				<option value="11-12">11:00 AM – 12:00 PM</option>
				<option value="12-1">12:00 PM – 1:00 PM</option>
				<option value="2-3">2:00 PM – 3:00 PM</option>
				<option value="3-4">3:00 PM – 4:00 PM</option>
				<option value="full-day">Full Day</option>
				<option value="half-day">Half Day</option>
			</select>
		</div>

		<div class="field">
			<label for="student-period">Attendance Period</label>

			<select
				id="student-period"
				bind:value={selectedPeriod}
			>
				<option value="today">Today</option>
				<option value="this-week">This Week</option>
				<option value="last-week">Last Week</option>
				<option value="this-month">This Month</option>
				<option value="last-month">Last Month</option>
				<option value="custom">Custom Date Range</option>
			</select>
		</div>

		{#if selectedPeriod === 'custom'}
			<div class="field">
				<label for="student-start-date">Start Date</label>

				<input
					id="student-start-date"
					type="date"
					bind:value={startDate}
				/>
			</div>

			<div class="field">
				<label for="student-end-date">End Date</label>

				<input
					id="student-end-date"
					type="date"
					bind:value={endDate}
				/>
			</div>
		{/if}

		<button type="button" class="view-button" onclick={viewStudentAttendance}>
			View Attendance
		</button>
	</div>

	{#if showResults}
		<div class="result-heading">
			<div>
				<h3>Class 9 - Section A</h3>

				{#if selectedPeriod === 'custom'}
					<p>{startDate || 'Start Date'} → {endDate || 'End Date'}</p>
				{:else}
					<p>9:00 AM – 10:00 AM · Last Month</p>
				{/if}
			</div>
		</div>

		<AttendanceOverview />

		<AttendanceTable />
	{/if}
</section>

<style>
	.student-attendance {
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

	.field label {
		display: block;
		margin-bottom: 7px;
		color: #334155;
		font-size: 12px;
		font-weight: 600;
	}

	select,
	input {
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

	select:focus,
	input:focus {
		border-color: #2563eb;
		box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.1);
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