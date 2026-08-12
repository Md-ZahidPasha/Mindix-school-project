<script lang="ts">
	import { Eye, EyeOff } from '@lucide/svelte';

	let principalName = $state('');
	let email = $state('');
	let phone = $state('');
	let gender = $state('');
	let dob = $state('');
	let qualification = $state('');
	let experience = $state('');
	let principalId = $state('');
	let password = $state('');
	let confirmPassword = $state('');

	let showPassword = $state(false);
	let showConfirmPassword = $state(false);
    let profileImage = $state<string | null>(null);

	let errors = $state({
	principalName: '',
	email: '',
	phone: '',
	gender: '',
	dob: '',
	qualification: '',
	experience: '',
	principalId: '',
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

function validateForm(): boolean {

	errors.principalName = principalName.trim()
		? ''
		: 'Principal name is required';

	errors.email = email.trim()
		? /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)
			? ''
			: 'Please enter a valid email address'
		: 'Email address is required';

	errors.phone = /^[6-9]\d{9}$/.test(phone)
		? ''
		: 'Please enter a valid 10-digit phone number';

	errors.gender = gender
		? ''
		: 'Please select gender';

	errors.dob = dob
		? ''
		: 'Date of birth is required';

	errors.qualification = qualification.trim()
		? ''
		: 'Qualification is required';

	errors.experience =
		experience !== '' && Number(experience) >= 0
			? ''
			: 'Please enter experience';
    
	errors.principalId = principalId.trim()
	? ''
	: 'Principal ID is required';

	errors.password =
		password.length >= 8
			? ''
			: 'Password must be at least 8 characters';

	errors.confirmPassword =
		confirmPassword === ''
			? 'Please confirm your password'
			: password === confirmPassword
				? ''
				: 'Passwords do not match';

	return Object.values(errors).every(error => error === '');

}
function handleSubmit() {

	if (!validateForm()) {
		return;
	}

	// Backend API will be added here later

	console.log({
		principalName,
		principalId,
		email,
		phone,
		gender,
		dob,
		qualification,
		experience,
		password
	});

}

</script>

<section class="form-card">

	<h2>Principal Details</h2>
    <div class="photo-section">

	{#if profileImage}

		<img
			src={profileImage}
			alt="Principal"
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

		Upload Principal Photo

	</button>

</div>

	<div class="form-grid">

		<div class="form-group">

			<label for="principalName">Principal Name</label>

			<input
				id="principalName"
				class:error-input={!!errors.principalName}
				type="text"
				bind:value={principalName}
				placeholder="Enter Principal Name"
			/>
{#if errors.principalName}
	<p class="error">{errors.principalName}</p>
{/if}
		</div>

		<div class="form-group">

			<label for="email">Email Address</label>

			<input
				id="email"
				class:error-input={!!errors.email}
				type="email"
				bind:value={email}
				placeholder="principal@school.com"
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

	<label for="principalId">Create Principal ID</label>

	<input
		id="principalId"
		type="text"
		bind:value={principalId}
		placeholder="Create Principal ID"
	/>

	{#if errors.principalId}
		<p class="error-message">{errors.principalId}</p>
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
	Create Principal Account
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