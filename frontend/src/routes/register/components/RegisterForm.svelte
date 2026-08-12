<script lang="ts">
	import { Eye, EyeOff } from '@lucide/svelte';
    import { registerInstitution } from '$lib/services/institution';
    import { goto } from '$app/navigation';
	// ==========================
	// Form Fields
	// ==========================

	let institutionName = $state('');
	let institutionType = $state('');
	let adminName = $state('');
	let email = $state('');
	let phone = $state('');
	let password = $state('');
	let confirmPassword = $state('');

	// ==========================
	// Password Visibility
	// ==========================

	let showPassword = $state(false);
	let showConfirmPassword = $state(false);

	// ==========================
	// Success Message
	// ==========================

	let successMessage = $state('');

	// ==========================
	// Validation Errors
	// ==========================

	let errors = $state({
		institutionName: '',
		institutionType: '',
		adminName: '',
		email: '',
		phone: '',
		password: '',
		confirmPassword: ''
	});

	// ==========================
	// Email Regex
	// ==========================

	const emailRegex =
		/^[^\s@]+@[^\s@]+\.[^\s@]+$/;

	// ==========================
	// Phone Regex
	// ==========================

	const phoneRegex =
		/^[6-9]\d{9}$/;

	// ==========================
	// Validate Form
	// ==========================

	async function validateForm() {

		successMessage = '';

		errors = {
			institutionName: '',
			institutionType: '',
			adminName: '',
			email: '',
			phone: '',
			password: '',
			confirmPassword: ''
		};

		let isValid = true;

		// --------------------------

		if (!institutionName.trim()) {

			errors.institutionName =
				'Institution Name is required';

			isValid = false;

		}

		// --------------------------

		if (!institutionType) {

			errors.institutionType =
				'Please select Institution Type';

			isValid = false;

		}

		// --------------------------

		if (!adminName.trim()) {

			errors.adminName =
				'Principal / Admin Name is required';

			isValid = false;

		}

		// --------------------------

		if (!email.trim()) {

			errors.email =
				'Email Address is required';

			isValid = false;

		}
		else if (!emailRegex.test(email)) {

			errors.email =
				'Please enter a valid Email Address';

			isValid = false;

		}

		// --------------------------

		if (!phone.trim()) {

			errors.phone =
				'Phone Number is required';

			isValid = false;

		}
		else if (!phoneRegex.test(phone)) {

			errors.phone =
				'Enter a valid 10-digit Mobile Number';

			isValid = false;

		}

		// --------------------------

		if (!password) {

			errors.password =
				'Password is required';

			isValid = false;

		}
		else if (password.length < 8) {

			errors.password =
				'Password must be at least 8 characters';

			isValid = false;

		}

		// --------------------------

		if (!confirmPassword) {

			errors.confirmPassword =
				'Please confirm your Password';

			isValid = false;

		}
		else if (password !== confirmPassword) {

			errors.confirmPassword =
				'Passwords do not match';

			isValid = false;

		}

		// --------------------------

	if (isValid) {

	try {

		const response = await registerInstitution({

			institution_name: institutionName,

			institution_type: institutionType,

			admin_name: adminName,

			email,

			phone,

			password

		});

		successMessage = response.message;

		setTimeout(() => {

			goto('/login');

		}, 1500);

	}
	catch (error) {

		if (error instanceof Error) {

			successMessage = '';

			alert(error.message);

		}

	}

}

return isValid;

	}
</script>
<section class="register-card">

	<div class="card-header">

		<h2>Register Your Institution</h2>

		<p>
			Create your PaperBuddy workspace and start managing your
			institution with AI.
		</p>

	</div>

	<form
		class="register-form"
		onsubmit={(e) => {

			e.preventDefault();

			validateForm();

		}}
	>

		{#if successMessage}

			<div class="success-message">

				{successMessage}

			</div>

		{/if}

		<div class="form-grid">

			<!-- Institution Name -->

			<div class="form-group">

				<label for="institutionName">

					Institution Name

				</label>

				<input
					id="institutionName"
					type="text"
					bind:value={institutionName}
					class:error={!!errors.institutionName}
					placeholder="ABC Public School"
				/>

				{#if errors.institutionName}

					<p class="error-message">

						{errors.institutionName}

					</p>

				{/if}

			</div>

			<!-- Institution Type -->

			<div class="form-group">

				<label for="institutionType">

					Institution Type

				</label>

				<select
					id="institutionType"
					bind:value={institutionType}
					class:error={!!errors.institutionType}
				>

					<option value="">

						Select Institution Type

					</option>

					<option value="School">School</option>

					<option value="Junior College">Junior College</option>

					<option value="College">College</option>

					<option value="University">University</option>

				</select>

				{#if errors.institutionType}

					<p class="error-message">

						{errors.institutionType}

					</p>

				{/if}

			</div>

			<!-- Principal -->

			<div class="form-group">

				<label for="adminName">

					Principal / Admin Name

				</label>

				<input
					id="adminName"
					type="text"
					bind:value={adminName}
					class:error={!!errors.adminName}
					placeholder="John Doe"
				/>

				{#if errors.adminName}

					<p class="error-message">

						{errors.adminName}

					</p>

				{/if}

			</div>

			<!-- Phone -->

			<div class="form-group">

				<label for="phone">

					Phone Number

				</label>

				<input
					id="phone"
					type="tel"
					bind:value={phone}
					class:error={!!errors.phone}
					placeholder="9876543210"
				/>

				{#if errors.phone}

					<p class="error-message">

						{errors.phone}

					</p>

				{/if}

			</div>

			<!-- Email -->

			<div class="form-group full">

				<label for="email">

					Email Address

				</label>

				<input
					id="email"
					type="email"
					bind:value={email}
					class:error={!!errors.email}
					placeholder="admin@school.com"
				/>

				{#if errors.email}

					<p class="error-message">

						{errors.email}

					</p>

				{/if}

			</div>
						<!-- Password -->

			<div class="form-group">

				<label for="password">

					Password

				</label>

				<div class="password-wrapper">

					<input
						id="password"
						type={showPassword ? 'text' : 'password'}
						bind:value={password}
						class:error={!!errors.password}
						placeholder="Create Password"
					/>

					<button
						type="button"
						class="eye-btn"
						onclick={() => showPassword = !showPassword}
						aria-label="Toggle password visibility"
					>

						{#if showPassword}

							<EyeOff size={20} />

						{:else}

							<Eye size={20} />

						{/if}

					</button>

				</div>

				{#if errors.password}

					<p class="error-message">

						{errors.password}

					</p>

				{/if}

			</div>

			<!-- Confirm Password -->

			<div class="form-group">

				<label for="confirmPassword">

					Confirm Password

				</label>

				<div class="password-wrapper">

					<input
						id="confirmPassword"
						type={showConfirmPassword ? 'text' : 'password'}
						bind:value={confirmPassword}
						class:error={!!errors.confirmPassword}
						placeholder="Confirm Password"
					/>

					<button
						type="button"
						class="eye-btn"
						onclick={() => showConfirmPassword = !showConfirmPassword}
						aria-label="Toggle confirm password visibility"
					>

						{#if showConfirmPassword}

							<EyeOff size={20} />

						{:else}

							<Eye size={20} />

						{/if}

					</button>

				</div>

				{#if errors.confirmPassword}

					<p class="error-message">

						{errors.confirmPassword}

					</p>

				{/if}

			</div>

		</div>

		<button
			type="submit"
			class="submit-btn"
		>

			Create Institution

		</button>

	</form>

</section>

<style lang="scss">
@use '$lib/styles/_colors' as c;

.register-card {
	height: 100%;
	background: white;
	border-radius: 24px;
	padding: 42px;
	border: 1px solid c.$border;
	box-shadow: 0 20px 50px rgba(15, 23, 42, .08);
	display: flex;
	flex-direction: column;
	justify-content: space-between;
}

.card-header {
	margin-bottom: 32px;
}

.card-header h2 {
	font-size: 32px;
	font-weight: 800;
	color: c.$text-primary;
	margin-bottom: 10px;
}

.card-header p {
	font-size: 16px;
	line-height: 1.7;
	color: c.$text-secondary;
}

.register-form {
	display: flex;
	flex-direction: column;
	gap: 22px;
}

.form-grid {
	display: grid;
	grid-template-columns: 1fr 1fr;
	gap: 22px;
}

.full {
	grid-column: 1 / -1;
}

.form-group {
	display: flex;
	flex-direction: column;
	gap: 8px;
}

label {
	font-size: 14px;
	font-weight: 600;
	color: c.$text-primary;
}

input,
select {
	width: 100%;
	height: 54px;
	padding: 0 18px;
	border-radius: 14px;
	border: 1px solid c.$border;
	font-size: 15px;
	background: white;
	outline: none;
	transition: .25s;
	box-sizing: border-box;
}

.password-wrapper {
	position: relative;
}

.password-wrapper input {
	padding-right: 52px;
}

.eye-btn {
	position: absolute;
	top: 50%;
	right: 14px;
	transform: translateY(-50%);
	border: none;
	background: transparent;
	cursor: pointer;
	display: flex;
	align-items: center;
	justify-content: center;
	color: #64748b;
	padding: 4px;
}

.eye-btn:hover {
	color: c.$primary;
}

input:focus,
select:focus {
	border-color: c.$primary;
	box-shadow: 0 0 0 4px rgba(37,99,235,.10);
}

.error {
	border-color: #ef4444 !important;
}

.error:focus {
	box-shadow: 0 0 0 4px rgba(239,68,68,.15);
}

.error-message {
	font-size: 13px;
	color: #ef4444;
	font-weight: 500;
	margin-top: -2px;
}

.success-message {
	background: #ecfdf5;
	border: 1px solid #22c55e;
	color: #15803d;
	padding: 14px 18px;
	border-radius: 14px;
	font-size: 14px;
	font-weight: 600;
}

.submit-btn {
	width: 100%;
	height: 56px;
	border: none;
	border-radius: 14px;
	background: linear-gradient(135deg,#2563eb,#4f46e5);
	color: white;
	font-size: 16px;
	font-weight: 700;
	cursor: pointer;
	transition: .3s;
	box-shadow: 0 12px 28px rgba(37,99,235,.25);
}

.submit-btn:hover {
	transform: translateY(-2px);
	box-shadow: 0 18px 36px rgba(37,99,235,.35);
}

.submit-btn:active {
	transform: translateY(0);
}

::placeholder {
	color: c.$text-muted;
}

@media (max-width:768px) {

	.register-card {
		padding: 28px;
		border-radius: 20px;
	}

	.card-header h2 {
		font-size: 28px;
	}

	.form-grid {
		grid-template-columns: 1fr;
	}

	.full {
		grid-column: auto;
	}
}
</style>