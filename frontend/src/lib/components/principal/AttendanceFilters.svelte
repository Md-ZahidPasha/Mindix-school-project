<script lang="ts">
	type AttendanceType = 'students' | 'teachers' | 'employees';

	let selectedType = $state<AttendanceType>('students');

	let selectedClass = $state('');
	let selectedSection = $state('');
	let selectedClassTime = $state('');
	let selectedDepartment = $state('');
	let selectedPeriod = $state('last-month');

	let fromDate = $state('');
	let toDate = $state('');

	let showCustomDates = $state(false);

	const classes = ['Class 1', 'Class 2', 'Class 3', 'Class 4', 'Class 5', 'Class 6', 'Class 7', 'Class 8', 'Class 9', 'Class 10', 'Class 11', 'Class 12'];

	const sections = ['Section A', 'Section B', 'Section C', 'Section D'];

	const classTimes = [
		'8:00 AM – 9:00 AM',
		'9:00 AM – 10:00 AM',
		'10:00 AM – 11:00 AM',
		'11:00 AM – 12:00 PM',
		'12:00 PM – 1:00 PM',
		'2:00 PM – 3:00 PM',
		'3:00 PM – 4:00 PM'
	];

	const departments = [
		'All Departments',
		'Administration',
		'Library',
		'Accounts',
		'Transport',
		'Office',
		'Security',
		'Maintenance',
		'Other'
	];

	const periods = [
		{ value: 'today', label: 'Today' },
		{ value: 'this-week', label: 'This Week' },
		{ value: 'last-week', label: 'Last Week' },
		{ value: 'this-month', label: 'This Month' },
		{ value: 'last-month', label: 'Last Month' },
		{ value: 'custom', label: 'Custom Date Range' }
	];

	function changePeriod(value: string) {
		selectedPeriod = value;
		showCustomDates = value === 'custom';
	}

	function clearFilters() {
		selectedClass = '';
		selectedSection = '';
		selectedClassTime = '';
		selectedDepartment = '';
		selectedPeriod = 'last-month';
		fromDate = '';
		toDate = '';
		showCustomDates = false;
	}

	function applyFilters() {
		console.log('Attendance filters:', {
			type: selectedType,
			class: selectedClass,
			section: selectedSection,
			classTime: selectedClassTime,
			department: selectedDepartment,
			period: selectedPeriod,
			fromDate,
			toDate
		});
	}

	function setType(type: AttendanceType) {
		selectedType = type;
		clearFilters();
	}
</script>

<section class="attendance-filters">
	<div class="filter-header">
		<div>
			<h2>Attendance Filters</h2>
			<p>Select the required details to view attendance.</p>
		</div>

		<button type="button" class="clear-button" onclick={clearFilters}>
			Clear
		</button>
	</div>

	<div class="type-tabs">
		<button
			type="button"
			class:active={selectedType === 'students'}
			onclick={() => setType('students')}
		>
			Students
		</button>

		<button
			type="button"
			class:active={selectedType === 'teachers'}
			onclick={() => setType('teachers')}
		>
			Teachers
		</button>

		<button
			type="button"
			class:active={selectedType === 'employees'}
			onclick={() => setType('employees')}
		>
			Employees / Staff
		</button>
	</div>

	<div class="filter-card">
		{#if selectedType === 'students' || selectedType === 'teachers'}
			<div class="field">
				<label for="attendance-class">Class</label>

				<select id="attendance-class" bind:value={selectedClass}>
					<option value="">Select Class</option>

					{#each classes as item}
						<option value={item}>{item}</option>
					{/each}
				</select>
			</div>

			<div class="field">
				<label for="attendance-section">Section</label>

				<select id="attendance-section" bind:value={selectedSection}>
					<option value="">Select Section</option>

					{#each sections as item}
						<option value={item}>{item}</option>
					{/each}
				</select>
			</div>
		{/if}

		{#if selectedType === 'students'}
			<div class="field">
				<label for="attendance-time">Class Time</label>

				<select id="attendance-time" bind:value={selectedClassTime}>
					<option value="">Select Class Time</option>

					{#each classTimes as item}
						<option value={item}>{item}</option>
					{/each}
				</select>
			</div>
		{/if}

		{#if selectedType === 'employees'}
			<div class="field">
				<label for="attendance-department">Department</label>

				<select id="attendance-department" bind:value={selectedDepartment}>
					<option value="">Select Department</option>

					{#each departments as item}
						<option value={item}>{item}</option>
					{/each}
				</select>
			</div>
		{/if}

		<div class="field">
			<label for="attendance-period">Attendance Period</label>

			<select
				id="attendance-period"
				value={selectedPeriod}
				onchange={(event) => changePeriod(event.currentTarget.value)}
			>
				{#each periods as period}
					<option value={period.value}>{period.label}</option>
				{/each}
			</select>
		</div>

		{#if showCustomDates}
			<div class="field">
				<label for="from-date">From Date</label>

				<input
					id="from-date"
					type="date"
					bind:value={fromDate}
				/>
			</div>

			<div class="field">
				<label for="to-date">To Date</label>

				<input
					id="to-date"
					type="date"
					bind:value={toDate}
				/>
			</div>
		{/if}

		<div class="filter-actions">
			<button type="button" class="view-button" onclick={applyFilters}>
				View Attendance
			</button>
		</div>
	</div>
</section>

<style>
	.attendance-filters {
		margin-top: 24px;
	}

	.filter-header {
		display: flex;
		align-items: flex-start;
		justify-content: space-between;
		gap: 16px;
		margin-bottom: 14px;
	}

	.filter-header h2 {
		margin: 0;
		color: #14213d;
		font-size: 20px;
	}

	.filter-header p {
		margin: 5px 0 0;
		color: #64748b;
		font-size: 13px;
	}

	.clear-button {
		padding: 8px 14px;
		border: 1px solid #dbe3ef;
		border-radius: 8px;
		background: white;
		color: #64748b;
		font-size: 12px;
		font-weight: 600;
		cursor: pointer;
	}

	.clear-button:hover {
		background: #f8fafc;
	}

	.type-tabs {
		display: flex;
		gap: 8px;
		margin-bottom: 14px;
		overflow-x: auto;
	}

	.type-tabs button {
		padding: 10px 16px;
		border: 1px solid #e5eaf2;
		border-radius: 9px;
		background: white;
		color: #64748b;
		font-size: 13px;
		font-weight: 600;
		white-space: nowrap;
		cursor: pointer;
	}

	.type-tabs button:hover {
		border-color: #b9cdf5;
	}

	.type-tabs button.active {
		border-color: #2563eb;
		background: #2563eb;
		color: white;
	}

	.filter-card {
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

	.filter-actions {
		display: flex;
		align-items: flex-end;
	}

	.view-button {
		width: 100%;
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

	@media (max-width: 1000px) {
		.filter-card {
			grid-template-columns: repeat(2, 1fr);
		}
	}

	@media (max-width: 600px) {
		.filter-card {
			grid-template-columns: 1fr;
		}

		.filter-header {
			flex-direction: column;
		}

		.clear-button {
			align-self: flex-start;
		}

		.type-tabs {
			flex-wrap: wrap;
		}
	}
</style>