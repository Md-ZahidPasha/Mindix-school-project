<script lang="ts">
	let student = {
		name: 'Aarav Sharma',
		studentId: 'STU1024',
		admissionNo: 'ADM20240024',
		email: 'aarav@example.com',
		phone: '+91 98765 43210',
		gender: 'Male',
		dob: '15 March 2012',
		className: '9',
		section: 'A',
		rollNo: '24',
		previousSchool: 'Green Valley School',
		previousMarks: '86%',
		fatherName: 'Rajesh Sharma',
		fatherOccupation: 'Business',
		motherName: 'Priya Sharma',
		motherOccupation: 'Teacher',
		parentPhone: '+91 98765 43211',
		attendance: '92%',
		present: '184',
		absent: '12',
		leave: '4'
	};
</script>

<section class="student-profile">
	<div class="profile-heading">
		<div>
			<h2>Student Profile</h2>
			<p>Complete information about the selected student.</p>
		</div>
	</div>

	<!-- Profile Header -->
	<div class="profile-card profile-header">
		<div class="student-photo">
			<span>AS</span>
		</div>

		<div class="student-main-info">
			<h3>{student.name}</h3>

			<p>
				Student ID:
				<strong>{student.studentId}</strong>
			</p>

			<div class="student-tags">
				<span>Class {student.className}</span>
				<span>Section {student.section}</span>
				<span>Roll No. {student.rollNo}</span>
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
				<span>Admission No.</span>
				<strong>{student.admissionNo}</strong>
			</div>

			<div>
				<span>Student Name</span>
				<strong>{student.name}</strong>
			</div>

			<div>
				<span>Email Address</span>
				<strong>{student.email}</strong>
			</div>

			<div>
				<span>Phone Number</span>
				<strong>{student.phone}</strong>
			</div>

			<div>
				<span>Gender</span>
				<strong>{student.gender}</strong>
			</div>

			<div>
				<span>Date of Birth</span>
				<strong>{student.dob}</strong>
			</div>
		</div>
	</div>

	<!-- Academic Details -->
	<div class="profile-card">
		<div class="card-heading">
			<h3>Academic Details</h3>
		</div>

		<div class="details-grid">
			<div>
				<span>Class / Grade</span>
				<strong>{student.className}</strong>
			</div>

			<div>
				<span>Section</span>
				<strong>{student.section}</strong>
			</div>

			<div>
				<span>Student ID / Roll No.</span>
				<strong>{student.studentId} / {student.rollNo}</strong>
			</div>

			<div>
				<span>Previous School</span>
				<strong>{student.previousSchool}</strong>
			</div>

			<div>
				<span>Previous Academic Marks</span>
				<strong>{student.previousMarks}</strong>
			</div>
		</div>
	</div>

	<!-- Parent Details -->
	<div class="profile-card">
		<div class="card-heading">
			<h3>Parent Details</h3>
		</div>

		<div class="details-grid">
			<div>
				<span>Father Name</span>
				<strong>{student.fatherName}</strong>
			</div>

			<div>
				<span>Father Occupation</span>
				<strong>{student.fatherOccupation}</strong>
			</div>

			<div>
				<span>Mother Name</span>
				<strong>{student.motherName}</strong>
			</div>

			<div>
				<span>Mother Occupation</span>
				<strong>{student.motherOccupation}</strong>
			</div>

			<div>
				<span>Parent Phone</span>
				<strong>{student.parentPhone}</strong>
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
				<strong>{student.attendance}</strong>
			</div>

			<div class="attendance-item">
				<span>Present</span>
				<strong>{student.present}</strong>
			</div>

			<div class="attendance-item">
				<span>Absent</span>
				<strong>{student.absent}</strong>
			</div>

			<div class="attendance-item">
				<span>Leave</span>
				<strong>{student.leave}</strong>
			</div>
		</div>
	</div>
</section>

<style>
	.student-profile {
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

	.student-photo {
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

	.student-main-info h3 {
		margin: 0;
		color: #14213d;
		font-size: 22px;
	}

	.student-main-info p {
		margin: 6px 0 10px;
		color: #64748b;
		font-size: 13px;
	}

	.student-main-info strong {
		color: #2563eb;
	}

	.student-tags {
		display: flex;
		flex-wrap: wrap;
		gap: 8px;
	}

	.student-tags span {
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
	.attendance-item span {
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