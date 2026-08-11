<script lang="ts">
	let employee = {
		name: 'Ahmed Khan',
		employeeId: 'EMP102',
		email: 'ahmed.khan@example.com',
		phone: '+91 98765 43210',
		gender: 'Male',
		dob: '20 February 1985',
		role: 'Library Assistant',
		department: 'Library',
		qualification: 'B.A.',
		experience: '6 Years',
		joiningDate: '15 June 2020',
		assignedDuties: 'Library management and student support',
		attendance: '94%',
		present: '188',
		absent: '8',
		leave: '4',
		leaveStatus: 'No Pending Leave'
	};
</script>

<section class="employee-profile">
	<div class="profile-heading">
		<div>
			<h2>Employee Profile</h2>
			<p>Complete information about the selected employee.</p>
		</div>
	</div>

	<!-- Profile Header -->
	<div class="profile-card profile-header">
		<div class="employee-photo">
			<span>AK</span>
		</div>

		<div class="employee-main-info">
			<h3>{employee.name}</h3>

			<p>
				Employee ID:
				<strong>{employee.employeeId}</strong>
			</p>

			<div class="employee-tags">
				<span>{employee.role}</span>
				<span>{employee.department}</span>
				<span>{employee.experience}</span>
			</div>
		</div>
	</div>

	<!-- Personal Details -->
	<div class="profile-card">
		<div class="card-heading">
			<h3>Personal Details</h3>
		</div>

		<div class="details-grid">
			<div>
				<span>Employee ID</span>
				<strong>{employee.employeeId}</strong>
			</div>

			<div>
				<span>Employee Name</span>
				<strong>{employee.name}</strong>
			</div>

			<div>
				<span>Email Address</span>
				<strong>{employee.email}</strong>
			</div>

			<div>
				<span>Phone Number</span>
				<strong>{employee.phone}</strong>
			</div>

			<div>
				<span>Gender</span>
				<strong>{employee.gender}</strong>
			</div>

			<div>
				<span>Date of Birth</span>
				<strong>{employee.dob}</strong>
			</div>
		</div>
	</div>

	<!-- Work Details -->
	<div class="profile-card">
		<div class="card-heading">
			<h3>Work Details</h3>
		</div>

		<div class="details-grid">
			<div>
				<span>Role</span>
				<strong>{employee.role}</strong>
			</div>

			<div>
				<span>Department</span>
				<strong>{employee.department}</strong>
			</div>

			<div>
				<span>Qualification</span>
				<strong>{employee.qualification}</strong>
			</div>

			<div>
				<span>Experience</span>
				<strong>{employee.experience}</strong>
			</div>

			<div>
				<span>Joining Date</span>
				<strong>{employee.joiningDate}</strong>
			</div>

			<div>
				<span>Assigned Duties</span>
				<strong>{employee.assignedDuties}</strong>
			</div>
		</div>
	</div>

	<!-- Attendance -->
	<div class="profile-card">
		<div class="card-heading">
			<h3>Attendance</h3>
		</div>

		<div class="attendance-grid">
			<div class="attendance-item">
				<span>Overall Attendance</span>
				<strong>{employee.attendance}</strong>
			</div>

			<div class="attendance-item">
				<span>Present</span>
				<strong>{employee.present}</strong>
			</div>

			<div class="attendance-item">
				<span>Absent</span>
				<strong>{employee.absent}</strong>
			</div>

			<div class="attendance-item">
				<span>Leave</span>
				<strong>{employee.leave}</strong>
			</div>
		</div>
	</div>

	<!-- Leave Information -->
	<div class="profile-card">
		<div class="card-heading">
			<h3>Leave Information</h3>
		</div>

		<div class="leave-status">
			<span>Status</span>
			<strong>{employee.leaveStatus}</strong>
		</div>
	</div>
</section>

<style>
	.employee-profile {
		margin-top: 24px;
	}

	.profile-heading {
		margin-bottom: 14px;
	}

	.profile-heading h2 {
		margin: 0;
		color: #14213d;
		font-size: 20px;
	}

	.profile-heading p {
		margin: 5px 0 0;
		color: #64748b;
		font-size: 13px;
	}

	.profile-card {
		margin-bottom: 18px;
		padding: 22px;
		background: white;
		border: 1px solid #e5eaf2;
		border-radius: 16px;
		box-shadow: 0 4px 14px rgba(15, 23, 42, 0.03);
	}

	.profile-header {
		display: flex;
		align-items: center;
		gap: 18px;
	}

	.employee-photo {
		width: 78px;
		height: 78px;
		display: flex;
		align-items: center;
		justify-content: center;
		flex-shrink: 0;
		background: #eaf1ff;
		color: #2563eb;
		border-radius: 50%;
		font-size: 23px;
		font-weight: 700;
	}

	.employee-main-info h3 {
		margin: 0;
		color: #14213d;
		font-size: 22px;
	}

	.employee-main-info p {
		margin: 6px 0 10px;
		color: #64748b;
		font-size: 13px;
	}

	.employee-main-info strong {
		color: #2563eb;
	}

	.employee-tags {
		display: flex;
		flex-wrap: wrap;
		gap: 8px;
	}

	.employee-tags span {
		padding: 5px 9px;
		background: #f1f5f9;
		color: #475569;
		border-radius: 7px;
		font-size: 11px;
		font-weight: 600;
	}

	.card-heading {
		margin-bottom: 18px;
	}

	.card-heading h3 {
		margin: 0;
		color: #14213d;
		font-size: 16px;
	}

	.details-grid {
		display: grid;
		grid-template-columns: repeat(3, 1fr);
		gap: 20px;
	}

	.details-grid div {
		min-width: 0;
	}

	.details-grid span,
	.attendance-item span,
	.leave-status span {
		display: block;
		margin-bottom: 5px;
		color: #64748b;
		font-size: 12px;
	}

	.details-grid strong {
		display: block;
		color: #1e293b;
		font-size: 14px;
		word-break: break-word;
	}

	.attendance-grid {
		display: grid;
		grid-template-columns: repeat(4, 1fr);
		gap: 14px;
	}

	.attendance-item {
		padding: 16px;
		background: #f8fafc;
		border-radius: 12px;
	}

	.attendance-item strong {
		color: #14213d;
		font-size: 22px;
	}

	.leave-status {
		padding: 16px;
		background: #f8fafc;
		border-radius: 12px;
	}

	.leave-status strong {
		color: #16a34a;
		font-size: 14px;
	}

	@media (max-width: 900px) {
		.details-grid {
			grid-template-columns: repeat(2, 1fr);
		}

		.attendance-grid {
			grid-template-columns: repeat(2, 1fr);
		}
	}

	@media (max-width: 600px) {
		.profile-header {
			align-items: flex-start;
		}

		.details-grid,
		.attendance-grid {
			grid-template-columns: 1fr;
		}
	}
</style>