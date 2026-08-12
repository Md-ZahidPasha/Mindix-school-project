<script lang="ts">
	import { Eye, EyeOff } from '@lucide/svelte';

	let employeeName = $state('');
	let email = $state('');
	let phone = $state('');
	let gender = $state('');
	let dob = $state('');
	let work = $state('');
	let qualification = $state('');
	let experience = $state('');
	let employeeId = $state('');
	let password = $state('');
	let confirmPassword = $state('');

	let showPassword = $state(false);
	let showConfirmPassword = $state(false);
	let profileImage = $state<string | null>(null);

	let errors = $state({
		employeeName: '',
		email: '',
		phone: '',
		gender: '',
		dob: '',
		work: '',
		qualification: '',
		experience: '',
		employeeId: '',
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
		errors.employeeName = employeeName.trim()
			? ''
			: 'Employee name is required';

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

		errors.work = work.trim()
			? ''
			: 'Work is required';

		errors.qualification = qualification.trim()
			? ''
			: 'Qualification is required';

		errors.experience =
			experience !== '' && Number(experience) >= 0
				? ''
				: 'Enter valid experience';

		errors.employeeId = employeeId.trim()
			? ''
			: 'Employee ID is required';

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
			employeeName,
			email,
			phone,
			gender,
			dob,
			work,
			qualification,
			experience,
			employeeId,
			password
		});
	}
</script>
<div class="form-card">

	<h2>Employee Details</h2>

	<div class="photo-section">

		{#if profileImage}
			<img
				src={profileImage}
				alt="Employee profile"
				class="profile-photo"
			/>
		{:else}
			<div class="photo-placeholder">
				👤
			</div>
		{/if}

		<button
			type="button"
			class="upload-photo-btn"
			onclick={() => imageInput?.click()}
		>
			Upload Photo
		</button>

		<input
			bind:this={imageInput}
			type="file"
			accept="image/*"
			hidden
			onchange={handleImageChange}
		/>

	</div>

	<div class="form-grid">

		<!-- Employee Name -->
		<div class="form-group">
			<label for="employeeName">Employee Name</label>

			<input
				id="employeeName"
				type="text"
				bind:value={employeeName}
				class:error-input={errors.employeeName}
				placeholder="Enter employee name"
			/>

			{#if errors.employeeName}
				<p class="error">{errors.employeeName}</p>
			{/if}
		</div>

		<!-- Email -->
		<div class="form-group">
			<label for="email">Email Address</label>

			<input
				id="email"
				type="email"
				bind:value={email}
				class:error-input={errors.email}
				placeholder="Enter email address"
			/>

			{#if errors.email}
				<p class="error">{errors.email}</p>
			{/if}
		</div>

		<!-- Phone -->
		<div class="form-group">
			<label for="phone">Phone Number</label>

			<input
				id="phone"
				type="tel"
				bind:value={phone}
				class:error-input={errors.phone}
				placeholder="Enter 10-digit phone number"
			/>

			{#if errors.phone}
				<p class="error">{errors.phone}</p>
			{/if}
		</div>

		<!-- Gender -->
		<div class="form-group">
			<label for="gender">Gender</label>

			<select
				id="gender"
				bind:value={gender}
				class:error-input={errors.gender}
			>
				<option value="">Select Gender</option>
				<option value="Male">Male</option>
				<option value="Female">Female</option>
				<option value="Other">Other</option>
			</select>

			{#if errors.gender}
				<p class="error">{errors.gender}</p>
			{/if}
		</div>

		<!-- Date of Birth -->
		<div class="form-group">
			<label for="dob">Date of Birth</label>

			<input
				id="dob"
				type="date"
				bind:value={dob}
				class:error-input={errors.dob}
			/>

			{#if errors.dob}
				<p class="error">{errors.dob}</p>
			{/if}
		</div>

		<!-- Work -->
		<div class="form-group">
			<label for="work">Work</label>

			<input
				id="work"
				type="text"
				bind:value={work}
				class:error-input={errors.work}
				placeholder="e.g. Driver, Watchman, Librarian, Lab Assistant"
			/>

			{#if errors.work}
				<p class="error">{errors.work}</p>
			{/if}
		</div>

		<!-- Qualification -->
		<div class="form-group">
			<label for="qualification">Qualification</label>

			<input
				id="qualification"
				type="text"
				bind:value={qualification}
				class:error-input={errors.qualification}
				placeholder="Enter qualification"
			/>

			{#if errors.qualification}
				<p class="error">{errors.qualification}</p>
			{/if}
		</div>

		<!-- Experience -->
		<div class="form-group">
			<label for="experience">Experience (Years)</label>

			<input
				id="experience"
				type="number"
				min="0"
				bind:value={experience}
				class:error-input={errors.experience}
				placeholder="e.g. 5"
			/>

			{#if errors.experience}
				<p class="error">{errors.experience}</p>
			{/if}
		</div>

		<!-- Employee ID -->
		<div class="form-group">
			<label for="employeeId">Create Employee ID</label>

			<input
				id="employeeId"
				type="text"
				bind:value={employeeId}
				class:error-input={errors.employeeId}
				placeholder="Create employee ID"
			/>

			{#if errors.employeeId}
				<p class="error">{errors.employeeId}</p>
			{/if}
		</div>

		<!-- Password -->
		<div class="form-group">
			<label for="password">Password</label>

			<div class="password-field">

				<input
					id="password"
					type={showPassword ? 'text' : 'password'}
					bind:value={password}
					class:error-input={errors.password}
					placeholder="Create password"
				/>

				<button
					type="button"
					class="eye-button"
					aria-label={showPassword ? 'Hide password' : 'Show password'}
					onclick={() => (showPassword = !showPassword)}
				>
					{#if showPassword}
						<EyeOff size={20} />
					{:else}
						<Eye size={20} />
					{/if}
				</button>

			</div>

			{#if errors.password}
				<p class="error">{errors.password}</p>
			{/if}
		</div>

		<!-- Confirm Password -->
		<div class="form-group confirm-password">
			<label for="confirmPassword">Confirm Password</label>

			<div class="password-field">

				<input
					id="confirmPassword"
					type={showConfirmPassword ? 'text' : 'password'}
					bind:value={confirmPassword}
					class:error-input={errors.confirmPassword}
					placeholder="Confirm password"
				/>

				<button
					type="button"
					class="eye-button"
					aria-label={
						showConfirmPassword
							? 'Hide confirm password'
							: 'Show confirm password'
					}
					onclick={() =>
						(showConfirmPassword = !showConfirmPassword)}
				>
					{#if showConfirmPassword}
						<EyeOff size={20} />
					{:else}
						<Eye size={20} />
					{/if}
				</button>

			</div>

			{#if errors.confirmPassword}
				<p class="error">{errors.confirmPassword}</p>
			{/if}
		</div>

	</div>

	<div class="button-row">

		<button
			type="button"
			class="submit-btn"
			onclick={handleSubmit}
		>
			Create Employee Account
		</button>

	</div>

</div>
<style lang="scss">
	.form-card {
		background: white;
		border: 1px solid #E2E8F0;
		border-radius: 24px;
		padding: 32px;
		box-shadow: 0 10px 25px rgba(15,23,42,.05);
	}

	.form-card h2 {
		font-size: 24px;
		font-weight: 700;
		color: #0F172A;
		margin-bottom: 28px;
	}

	.form-grid {
		display: grid;
		grid-template-columns: repeat(2, 1fr);
		gap: 22px;
	}

	.form-group {
		display: flex;
		flex-direction: column;
		gap: 8px;
	}

	label {
		font-size: 14px;
		font-weight: 600;
		color: #334155;
	}

	input,
	select {
		width: 100%;
		height: 50px;
		padding: 0 16px;
		border: 1px solid #CBD5E1;
		border-radius: 12px;
		font-size: 15px;
		background: white;
		outline: none;
		transition: .25s;
		box-sizing: border-box;
	}

	input:focus,
	select:focus {
		border-color: #2563EB;
		box-shadow: 0 0 0 3px rgba(37,99,235,.12);
	}

	.password-field {
		position: relative;
	}

	.password-field input {
		padding-right: 48px;
	}

	.eye-button {
		position: absolute;
		right: 14px;
		top: 50%;
		transform: translateY(-50%);
		background: none;
		border: none;
		cursor: pointer;
		color: #64748B;
		display: flex;
		align-items: center;
		justify-content: center;
	}

	.photo-section {
		display: flex;
		flex-direction: column;
		align-items: center;
		margin-bottom: 28px;
	}

	.photo-placeholder,
	.profile-photo {
		width: 120px;
		height: 120px;
		border-radius: 50%;
		border: 2px dashed #CBD5E1;
		display: flex;
		align-items: center;
		justify-content: center;
		font-size: 52px;
		background: #F8FAFC;
		object-fit: cover;
		margin-bottom: 16px;
	}

	.upload-photo-btn {
		background: #2563EB;
		color: white;
		border: none;
		padding: 12px 24px;
		border-radius: 12px;
		cursor: pointer;
		font-weight: 600;
		transition: .25s;
	}

	.upload-photo-btn:hover {
		background: #1D4ED8;
	}

	.button-row {
		margin-top: 32px;
		display: flex;
		justify-content: center;
	}

	.submit-btn {
		width: 100%;
		height: 52px;
		background: #2563EB;
		color: white;
		border: none;
		border-radius: 12px;
		font-size: 16px;
		font-weight: 700;
		cursor: pointer;
		transition: .25s;
	}

	.submit-btn:hover {
		background: #1D4ED8;
	}

	.error {
		color: #DC2626;
		font-size: 13px;
		font-weight: 500;
		margin-top: 6px;
	}

	input.error-input,
	select.error-input {
		border-color: #DC2626;
		box-shadow: 0 0 0 3px rgba(220,38,38,.12);
	}

	@media (max-width: 900px) {
		.form-grid {
			grid-template-columns: 1fr;
		}

		.button-row {
			justify-content: center;
		}

		.submit-btn {
			width: 100%;
		}
	}
</style>