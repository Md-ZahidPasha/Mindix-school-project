<script lang="ts">
	import { Eye, EyeOff } from '@lucide/svelte';

    let teacherName = $state('');
    let email = $state('');
    let phone = $state('');
    let gender = $state('');
    let dob = $state('');
    let subject = $state('');
    let qualification = $state('');
    let experience = $state('');
    let teacherId = $state('');
    let password = $state('');
    let confirmPassword = $state('');

	let showPassword = $state(false);
	let showConfirmPassword = $state(false);
    let profileImage = $state<string | null>(null);

    let errors = $state({
	teacherName: '',
	email: '',
	phone: '',
	gender: '',
	dob: '',
	subject: '',
	qualification: '',
	experience: '',
    teacherId: '',
	password: '',
	confirmPassword: ''
});
function handleImageChange(event: Event) {
	const input = event.target as HTMLInputElement;

	if (input.files?.length) {
		profileImage = URL.createObjectURL(input.files[0]);
	}
}

let imageInput: HTMLInputElement;

function validateForm() {
	errors.teacherName = teacherName.trim()
		? ''
		: 'Teacher name is required';

	errors.email = email.trim()
		? /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)
			? ''
			: 'Enter a valid email'
		: 'Email is required';

	errors.phone = /^[0-9]{10}$/.test(phone)
		? ''
		: 'Phone must contain exactly 10 digits';

	errors.gender = gender
		? ''
		: 'Please select gender';

	errors.dob = dob
		? ''
		: 'Date of birth is required';

	errors.subject = subject.trim()
		? ''
		: 'Subject is required';

	errors.qualification = qualification.trim()
		? ''
		: 'Qualification is required';

	errors.experience =
		experience !== '' && Number(experience) >= 0
			? ''
			: 'Enter valid experience';

    errors.teacherId = teacherId.trim()
		? ''
		: 'Teacher ID is required';

	errors.password =
		password.length >= 8
			? ''
			: 'Password must contain at least 8 characters';

	errors.confirmPassword =
		confirmPassword
			? password === confirmPassword
				? ''
				: 'Passwords do not match'
			: 'Please confirm your password';

	return Object.values(errors).every(value => value === '');
}

function handleSubmit() {

	if (!validateForm()) {
		return;
	}

	// Backend API will be added here later

	console.log({
		teacherName,
		email,
		phone,
		gender,
		dob,
		qualification,
        teacherId,
		experience,
		password
	});

}

</script>

<section class="form-card">

	<h2>Teacher Details</h2>
    <div class="photo-section">

	{#if profileImage}

		<img
			src={profileImage}
			alt="Teacher"
			class="profile-photo"
		/>

	{:else}

		<div class="photo-placeholder">

			👤

		</div>

	{/if}

	<input
		bind:this={imageInput}
		type="file"
		accept=".jpg,.jpeg,.png"
		onchange={handleImageChange}
		hidden
	/>

	<button
		type="button"
		class="upload-photo-btn"
		onclick={() => imageInput.click()}
	>

		Upload Teacher Photo

	</button>

</div>

	<div class="form-grid">

		<div class="form-group">

			<label for="teacherName">Teacher Name</label>

			<input
				id="teacherName"
				class:error-input={!!errors.teacherName}
				type="text"
				bind:value={teacherName}
				placeholder="Enter Teacher Name"
			/>
{#if errors.teacherName}
	<p class="error">{errors.teacherName}</p>
{/if}
		</div>

        <div class="form-group">

	<label for="subject">Subject</label>

	<input
		id="subject"
		type="text"
		bind:value={subject}
		placeholder="e.g. Mathematics"
	/>

	{#if errors.subject}
		<p class="error-message">{errors.subject}</p>
	{/if}

</div>

		<div class="form-group">

			<label for="email">Email Address</label>

			<input
				id="email"
				class:error-input={!!errors.email}
				type="email"
				bind:value={email}
				placeholder="teacher@school.com"
			/>
{#if errors.email}
	<p class="error">{errors.email}</p>
{/if}

		</div>

<div class="form-group">

	<label for="phone">Phone Number</label>

	<input
		id="phone"
		class:error-input={!!errors.phone}
		type="tel"
		bind:value={phone}
		placeholder="9876543210"
	/>
{#if errors.phone}
	<p class="error">{errors.phone}</p>
{/if}

</div>

<div class="form-group">

	<label for="gender">Gender</label>

	<select
		id="gender"
		class:error-input={!!errors.gender}
		bind:value={gender}
	>
		<option value="">Select Gender</option>
{#if errors.gender}
	<p class="error">{errors.gender}</p>
{/if}

		<option value="Male">Male</option>
		<option value="Female">Female</option>
		<option value="Other">Other</option>

	</select>

</div>

<div class="form-group">

	<label for="dob">Date of Birth</label>

	<input
		id="dob"
		class:error-input={!!errors.dob}
		type="date"
		bind:value={dob}
	/>
{#if errors.dob}
	<p class="error">{errors.dob}</p>
{/if}
</div>

<div class="form-group">

	<label for="qualification">Qualification</label>

	<input
		id="qualification"
	    class:error-input={!!errors.qualification}
		type="text"
		bind:value={qualification}
		placeholder="M.Ed / Ph.D"
	/>
{#if errors.qualification}
	<p class="error">{errors.qualification}</p>
{/if}

</div>

<div class="form-group">

	<label for="experience">Experience (Years)</label>

	<input
		id="experience"
		type="number"
		bind:value={experience}
		placeholder="10"
	/>

	{#if errors.experience}
		<p class="error-message">{errors.experience}</p>
	{/if}

</div>

<div class="form-group">

	<label for="teacherId">Create Teacher ID</label>

	<input
		id="teacherId"
		type="text"
		bind:value={teacherId}
		placeholder="Create Teacher ID"
	/>

	{#if errors.teacherId}
		<p class="error-message">{errors.teacherId}</p>
	{/if}

</div>

<div class="form-group">

	<label for="password">Password</label>

	<div class="password-field">

{#if errors.password}
	<p class="error">{errors.password}</p>
{/if}
		<input
			id="password"
			class:error-input={!!errors.password}
			type={showPassword ? 'text' : 'password'}
			bind:value={password}
			placeholder="Create Password"
		/>

		<button
			type="button"
			class="eye-button"
			onclick={() => showPassword = !showPassword}
		>
			{#if showPassword}
				<EyeOff size={18} />
			{:else}
				<Eye size={18} />
			{/if}
		</button>

	</div>

</div>

<div class="form-group">

	<label for="confirmPassword">Confirm Password</label>

	<div class="password-field">

		<input
			id="confirmPassword"
			class:error-input={!!errors.confirmPassword}
			type={showConfirmPassword ? 'text' : 'password'}
			bind:value={confirmPassword}
			placeholder="Confirm Password"
		/>
{#if errors.confirmPassword}
	<p class="error">{errors.confirmPassword}</p>
{/if}

		<button
			type="button"
			class="eye-button"
			onclick={() => showConfirmPassword = !showConfirmPassword}
		>
			{#if showConfirmPassword}
				<EyeOff size={18} />
			{:else}
				<Eye size={18} />
			{/if}
		</button>

	</div>

</div>


	</div>

	<div class="button-row">
<button
	type="button"
	class="submit-btn"
	onclick={handleSubmit}
>
	Create Teacher Account
</button>

</div>

</section>

<style lang="scss">

.form-card{

	background:white;

	border:1px solid #E2E8F0;

	border-radius:24px;

	padding:32px;

	box-shadow:0 10px 25px rgba(15,23,42,.05);

}

.form-card h2{

	font-size:24px;

	font-weight:700;

	color:#0F172A;

	margin-bottom:28px;

}

.form-grid{

	display:grid;

	grid-template-columns:repeat(2,1fr);

	gap:22px;

}

.form-group{

	display:flex;

	flex-direction:column;

	gap:8px;

}

label{

	font-size:14px;

	font-weight:600;

	color:#334155;

}

input,
select{

	width:100%;

	height:50px;

	padding:0 16px;

	border:1px solid #CBD5E1;

	border-radius:12px;

	font-size:15px;

	background:white;

	outline:none;

	transition:.25s;

	box-sizing:border-box;

}

input:focus,
select:focus{

	border-color:#2563EB;

	box-shadow:0 0 0 3px rgba(37,99,235,.12);

}

.password-field{

	position:relative;

}

.password-field input{

	padding-right:48px;

}

.eye-button{

	position:absolute;

	right:14px;

	top:50%;

	transform:translateY(-50%);

	background:none;

	border:none;

	cursor:pointer;

	color:#64748B;

	display:flex;

	align-items:center;

	justify-content:center;

}

@media(max-width:900px){

	.form-grid{

		grid-template-columns:1fr;

	}

	.button-row{

		justify-content:center;

	}

	.submit-btn{

		width:100%;

	}

}

.photo-section{

	display:flex;

	flex-direction:column;

	align-items:center;

	margin-bottom:28px;

}

.photo-placeholder,
.profile-photo{

	width:120px;

	height:120px;

	border-radius:50%;

	border:2px dashed #CBD5E1;

	display:flex;

	align-items:center;

	justify-content:center;

	font-size:52px;

	background:#F8FAFC;

	object-fit:cover;

	margin-bottom:16px;

}

.upload-photo-btn{

	background:#2563EB;

	color:white;

	border:none;

	padding:12px 24px;

	border-radius:12px;

	cursor:pointer;

	font-weight:600;

	transition:.25s;

}

.upload-photo-btn:hover{

	background:#1D4ED8;

}

.button-row{

	margin-top:32px;

	display:flex;

	justify-content:center;

}

.submit-btn{

	width:100%;

	height:52px;

	background:#2563EB;

	color:white;

	border:none;

	border-radius:12px;

	font-size:16px;

	font-weight:700;

	cursor:pointer;

	transition:.25s;

}

.submit-btn:hover{

	background:#1D4ED8;

}

.error{

	color:#DC2626;

	font-size:13px;

	font-weight:500;

	margin-top:6px;

}

input.error-input,
select.error-input{

	border-color:#DC2626;

	box-shadow:0 0 0 3px rgba(220,38,38,.12);

}

</style>