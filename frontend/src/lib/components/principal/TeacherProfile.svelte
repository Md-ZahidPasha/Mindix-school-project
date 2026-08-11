<script lang="ts">
	let teacher = {
		name: 'Rahul Verma',
		teacherId: 'TCH102',
		email: 'rahul.verma@example.com',
		phone: '+91 98765 43210',
		gender: 'Male',
		dob: '12 August 1988',
		qualification: 'M.Sc. Mathematics, B.Ed.',
		experience: '8 Years',
		specialization: 'Mathematics',
		department: 'Mathematics',
		joiningDate: '10 June 2018',
		assignedClasses: '8-A, 9-A, 10-B',
		subjects: 'Mathematics',
		attendance: '95%',
		present: '190',
		absent: '7',
		leave: '3',
		leaveStatus: 'No Pending Leave'
	};
</script>

<section class="teacher-profile">
	<div class="profile-heading">
		<div>
			<h2>Teacher Profile</h2>
			<p>Complete information about the selected teacher.</p>
		</div>
	</div>

	<!-- Profile Header -->
	<div class="profile-card profile-header">
		<div class="teacher-photo">
			<span>RV</span>
		</div>

		<div class="teacher-main-info">
			<h3>{teacher.name}</h3>

			<p>
				Teacher ID:
				<strong>{teacher.teacherId}</strong>
			</p>

			<div class="teacher-tags">
				<span>{teacher.department}</span>
				<span>{teacher.specialization}</span>
				<span>{teacher.experience}</span>
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
				<span>Teacher ID</span>
				<strong>{teacher.teacherId}</strong>
			</div>

			<div>
				<span>Teacher Name</span>
				<strong>{teacher.name}</strong>
			</div>

			<div>
				<span>Email Address</span>
				<strong>{teacher.email}</strong>
			</div>

			<div>
				<span>Phone Number</span>
				<strong>{teacher.phone}</strong>
			</div>

			<div>
				<span>Gender</span>
				<strong>{teacher.gender}</strong>
			</div>

			<div>
				<span>Date of Birth</span>
				<strong>{teacher.dob}</strong>
			</div>
		</div>
	</div>

	<!-- Professional Details -->
	<div class="profile-card">
		<div class="card-heading">
			<h3>Professional Details</h3>
		</div>

		<div class="details-grid">
			<div>
				<span>Qualification</span>
				<strong>{teacher.qualification}</strong>
			</div>

			<div>
				<span>Experience</span>
				<strong>{teacher.experience}</strong>
			</div>

			<div>
				<span>Specialization</span>
				<strong>{teacher.specialization}</strong>
			</div>

			<div>
				<span>Department</span>
				<strong>{teacher.department}</strong>
			</div>

			<div>
				<span>Joining Date</span>
				<strong>{teacher.joiningDate}</strong>
			</div>
		</div>
	</div>

	<!-- Teaching Details -->
	<div class="profile-card">
		<div class="card-heading">
			<h3>Teaching Details</h3>
		</div>

		<div class="details-grid">
			<div>
				<span>Assigned Classes</span>
				<strong>{teacher.assignedClasses}</strong>
			</div>

			<div>
				<span>Subjects</span>
				<strong>{teacher.subjects}</strong>
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
				<strong>{teacher.attendance}</strong>
			</div>

			<div class="attendance-item">
				<span>Present</span>
				<strong>{teacher.present}</strong>
			</div>

			<div class="attendance-item">
				<span>Absent</span>
				<strong>{teacher.absent}</strong>
			</div>

			<div class="attendance-item">
				<span>Leave</span>
				<strong>{teacher.leave}</strong>
			</div>
		</div>
	</div>

	<!-- Leave -->
	<div class="profile-card">
		<div class="card-heading">
			<h3>Leave Information</h3>
		</div>

		<div class="leave-status">
			<span>Status</span>
			<strong>{teacher.leaveStatus}</strong>
		</div>
	</div>
</section>

<style>
	.teacher-profile {
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

	.teacher-photo {
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

	.teacher-main-info h3 {
		margin: 0;
		color: #14213d;
		font-size: 22px;
	}

	.teacher-main-info p {
		margin: 6px 0 10px;
		color: #64748b;
		font-size: 13px;
	}

	.teacher-main-info strong {
		color: #2563eb;
	}

	.teacher-tags {
		display: flex;
		flex-wrap: wrap;
		gap: 8px;
	}

	.teacher-tags span {
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