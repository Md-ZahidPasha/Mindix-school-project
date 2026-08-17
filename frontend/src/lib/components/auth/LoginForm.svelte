<script lang="ts">
	import { Eye, EyeOff } from '@lucide/svelte';
	import { API } from '$lib/config/api';

	let selectedRole = $state('Admin');
	let showPassword = $state(false);
	let isLoading = $state(false);
	let serverError = $state('');

	let loginId = $state('');
	let password = $state('');
	let institutionName = $state('');

	let errors = $state({
		loginId: '',
		password: '',
		institutionName: ''
	});

	function validateForm(): boolean {
		errors.loginId = '';
		errors.password = '';
		errors.institutionName = '';
		serverError = '';

		if (
			(selectedRole === 'Staff' || selectedRole === 'Employee') &&
			!institutionName.trim()
		) {
			errors.institutionName = 'Institution name is required';
		}

		if (!loginId.trim()) {
			if (selectedRole === 'Admin') {
				errors.loginId = 'Institution name is required';
			} else if (selectedRole === 'Student') {
				errors.loginId = 'Student ID is required';
			} else if (selectedRole === 'Parent') {
				errors.loginId = 'Parent ID is required';
			} else if (selectedRole === 'Staff') {
				errors.loginId = 'Email is required';
			} else {
				errors.loginId = 'Employee email is required';
			}
		}

		if (!password.trim()) {
			errors.password = 'Password is required';
		}

		return Object.values(errors).every(
			(error) => error === ''
		);
	}

	async function handleSubmit() {
		if (!validateForm()) {
			return;
		}

		isLoading = true;
		serverError = '';

		try {
			let loginEndpoint = API.login;

			let requestBody: Record<string, string>;

			// ==========================================
			// ADMIN LOGIN
			// ==========================================
			if (selectedRole === 'Admin') {
				loginEndpoint = API.login;

				requestBody = {
					institution_name: loginId.trim(),
					password: password
				};
			}

			// ==========================================
			// STUDENT LOGIN
			// ==========================================
			else if (selectedRole === 'Student') {
				loginEndpoint = API.login.replace(
					/\/login$/,
					'/student-login'
				);

				requestBody = {
					student_id: loginId.trim(),
					password: password
				};
			}

			// ==========================================
			// PARENT LOGIN
			// ==========================================
			else if (selectedRole === 'Parent') {
				loginEndpoint = API.login.replace(
					/\/login$/,
					'/parent-login'
				);

				requestBody = {
					parent_id: loginId.trim(),
					password: password
				};
			}

			// ==========================================
			// STAFF / EMPLOYEE LOGIN
			// ==========================================
			else {
				loginEndpoint = API.login.replace(
					/\/login$/,
					'/staff-login'
				);

				requestBody = {
					institution_name: institutionName.trim(),
					email: loginId.trim(),
					password: password
				};
			}

			const response = await fetch(
				loginEndpoint,
				{
					method: 'POST',
					headers: {
						'Content-Type': 'application/json'
					},
					body: JSON.stringify(requestBody)
				}
			);

			const result = await response.json();

			if (!response.ok) {
				throw new Error(
					result.detail ||
						'Invalid ID or password.'
				);
			}

			/*
			 * Store common authentication information.
			 */

			localStorage.setItem(
				'access_token',
				result.access_token
			);

			localStorage.setItem(
				'token_type',
				result.token_type || 'bearer'
			);

			localStorage.setItem(
				'user_id',
				result.user_id
			);

			localStorage.setItem(
				'user_role',
				result.role
			);

			localStorage.setItem(
				'institution_id',
				result.institution_id
			);

			localStorage.setItem(
				'full_name',
				result.full_name || ''
			);

			if (result.employee_id) {
				localStorage.setItem(
					'employee_id',
					result.employee_id
				);
			}

			if (result.teacher_id) {
				localStorage.setItem(
					'teacher_id',
					result.teacher_id
				);
			}

			// ==========================================
			// STUDENT-SPECIFIC INFORMATION
			// ==========================================

			if (selectedRole === 'Student') {
				localStorage.setItem(
					'student_id',
					result.student_id
				);

				window.location.href =
					'/student-dashboard';

				return;
			}

			// ==========================================
			// PARENT-SPECIFIC INFORMATION
			// ==========================================

			if (selectedRole === 'Parent') {
				localStorage.setItem(
					'parent_id',
					result.parent_id
				);

				window.location.href =
					'/parent-dashboard';

				return;
			}

			// ==========================================
			// ADMIN-SPECIFIC INFORMATION
			// ==========================================

			localStorage.setItem(
				'institution_name',
				result.institution_name
			);

			/*
			 * Redirect according to role.
			 */

			switch (result.role?.toLowerCase()) {
				case 'principal':
					window.location.href =
						'/principal-dashboard';
					break;

				case 'teacher':
					window.location.href =
						'/teacher-dashboard';
					break;

				case 'staff':
					window.location.href =
						'/employee-dashboard';
					break;

				case 'employee':
					window.location.href =
						'/employee-dashboard';
					break;

				case 'admin':
					window.location.href =
						'/dashboard';
					break;

				default:
					serverError =
						`Login successful, but dashboard for role "${result.role}" is not available yet.`;
					break;
			}
		} catch (error) {
			serverError =
				error instanceof Error
					? error.message
					: 'Unable to connect to the server.';
		} finally {
			isLoading = false;
		}
	}

	function changeRole(role: string) {
		selectedRole = role;

		loginId = '';
		password = '';
		institutionName = '';

		errors.loginId = '';
		errors.password = '';
		errors.institutionName = '';
		serverError = '';

		showPassword = false;
	}
</script>

<div class="login-card">

	<div class="login-header">
		<h1>Welcome Back!</h1>
		<p>Sign in to continue to your account</p>
	</div>

	<div class="role-section">

		<p class="role-label">Login as</p>

		<div class="role-tabs">

			<button
				type="button"
				class:active={selectedRole === 'Admin'}
				onclick={() => changeRole('Admin')}
			>
				Admin
			</button>

			<button
				type="button"
				class:active={selectedRole === 'Staff'}
				onclick={() => changeRole('Staff')}
			>
				Principal / Teacher
			</button>

			<button
				type="button"
				class:active={selectedRole === 'Student'}
				onclick={() => changeRole('Student')}
			>
				Student
			</button>

			<button
				type="button"
				class:active={selectedRole === 'Parent'}
				onclick={() => changeRole('Parent')}
			>
				Parent
			</button>

			<button
				type="button"
				class:active={selectedRole === 'Employee'}
				onclick={() => changeRole('Employee')}
			>
				Employee
			</button>

		</div>

	</div>

	<form
		class="login-form"
		onsubmit={(event) => {
			event.preventDefault();
			handleSubmit();
		}}
	>

		{#if selectedRole === 'Staff' || selectedRole === 'Employee'}
			<div class="form-group">

				<label for="institutionName">
					Institution Name
				</label>

				<input
					id="institutionName"
					type="text"
					bind:value={institutionName}
					disabled={isLoading}
					oninput={() => {
						errors.institutionName = '';
						serverError = '';
					}}
					placeholder="Enter your institution name"
				/>

				{#if errors.institutionName}
					<p class="error-message">
						{errors.institutionName}
					</p>
				{/if}

			</div>
		{/if}

		<div class="form-group">

			<label for="loginId">
				{selectedRole === 'Admin'
					? 'Institution Name'
					: selectedRole === 'Student'
						? 'Student ID'
						: selectedRole === 'Parent'
							? 'Parent ID'
							: selectedRole === 'Staff'
								? 'Email'
								: 'Email'}
			</label>

			<input
				id="loginId"
				type="text"
				bind:value={loginId}
				disabled={isLoading}
				oninput={() => {
					errors.loginId = '';
					serverError = '';
				}}
				placeholder={
					selectedRole === 'Admin'
						? 'Enter institution name'
						: selectedRole === 'Student'
							? 'Enter student ID (e.g. STU001)'
							: selectedRole === 'Parent'
								? 'Enter parent ID (e.g. PAR001)'
								: selectedRole === 'Staff'
									? 'Enter your email'
									: 'Enter your email'
				}
			/>

			{#if errors.loginId}
				<p class="error-message">
					{errors.loginId}
				</p>
			{/if}

		</div>

		<div class="form-group">

			<label for="password">
				Password
			</label>

			<div class="password-wrapper">

				<input
					id="password"
					type={showPassword ? 'text' : 'password'}
					bind:value={password}
					disabled={isLoading}
					oninput={() => {
						errors.password = '';
						serverError = '';
					}}
					placeholder="Enter your password"
				/>

				<button
					type="button"
					class="eye-btn"
					aria-label={
						showPassword
							? 'Hide password'
							: 'Show password'
					}
					onclick={() =>
						(showPassword = !showPassword)}
					disabled={isLoading}
				>
					{#if showPassword}
						<EyeOff size={19} />
					{:else}
						<Eye size={19} />
					{/if}
				</button>

			</div>

			{#if errors.password}
				<p class="error-message">
					{errors.password}
				</p>
			{/if}

		</div>

		{#if serverError}
			<div class="server-error">
				{serverError}
			</div>
		{/if}

		<div class="login-options">

			<label class="remember">

				<input
					type="checkbox"
					disabled={isLoading}
				/>

				<span>Remember me</span>

			</label>

			<button
				type="button"
				class="forgot-btn"
				disabled={isLoading}
			>
				Forgot Password?
			</button>

		</div>

		<button
			type="submit"
			class="login-btn"
			disabled={isLoading}
		>
			{#if isLoading}
				Logging in...
			{:else}
				Login
			{/if}
		</button>

	</form>

</div>

<style lang="scss">

	.login-card {
		width: 100%;
		max-width: 720px;
		margin: 0 auto;
		background: white;
		border: 1px solid #E2E8F0;
		border-radius: 24px;
		padding: 42px;
		box-shadow: 0 20px 50px rgba(15, 23, 42, .08);
	}

	.login-header {
		text-align: center;
		margin-bottom: 34px;
	}

	.login-header h1 {
		margin: 0;
		color: #0F172A;
		font-size: 32px;
		font-weight: 800;
	}

	.login-header p {
		margin: 10px 0 0;
		color: #64748B;
		font-size: 15px;
	}

	.role-section {
		margin-bottom: 28px;
	}

	.role-label {
		display: block;
		margin-bottom: 10px;
		color: #0F172A;
		font-size: 14px;
		font-weight: 600;
	}

	.role-tabs {
		display: grid;
		grid-template-columns: repeat(5, 1fr);
		gap: 8px;
	}

	.role-tabs button {
		min-height: 44px;
		padding: 10px 12px;

		border: 1px solid #E2E8F0;
		border-radius: 10px;

		background: #F8FAFC;
		color: #475569;

		font-size: 13px;
		font-weight: 600;

		cursor: pointer;
		transition: all .2s ease;
	}

	.role-tabs button:hover {
		background: #EFF6FF;
		border-color: #93C5FD;
		color: #2563EB;
	}

	.role-tabs button.active {
		background: #2563EB;
		border-color: #2563EB;
		color: white;
		box-shadow: 0 4px 10px rgba(37, 99, 235, .18);
	}

	.login-form {
		display: flex;
		flex-direction: column;
		gap: 22px;
	}

	.form-group {
		display: flex;
		flex-direction: column;
		gap: 8px;
	}

	.form-group label {
		color: #0F172A;
		font-size: 14px;
		font-weight: 600;
	}

	.form-group input {
		width: 100%;
		height: 54px;
		padding: 0 16px;
		box-sizing: border-box;
		border: 1px solid #E2E8F0;
		border-radius: 12px;
		background: white;
		color: #0F172A;
		font-size: 15px;
		outline: none;
		transition: .2s;
	}

	.form-group input:focus {
		border-color: #2563EB;
		box-shadow: 0 0 0 4px rgba(37, 99, 235, .10);
	}

	.form-group input:disabled {
		background: #F8FAFC;
		cursor: not-allowed;
	}

	.login-options {
		display: flex;
		align-items: center;
		justify-content: space-between;
		gap: 16px;
	}

	.remember {
		display: flex;
		align-items: center;
		gap: 8px;
		color: #475569;
		font-size: 13px;
		cursor: pointer;
	}

	.remember input {
		width: 16px;
		height: 16px;
		accent-color: #2563EB;
	}

	.forgot-btn {
		border: none;
		background: transparent;
		color: #2563EB;
		font-size: 13px;
		font-weight: 600;
		cursor: pointer;
	}

	.forgot-btn:hover {
		text-decoration: underline;
	}

	.login-btn {
		width: 100%;
		height: 54px;
		border: none;
		border-radius: 12px;
		background: #2563EB;
		color: white;
		font-size: 15px;
		font-weight: 700;
		cursor: pointer;
		transition: .2s;
	}

	.login-btn:hover {
		background: #1D4ED8;
	}

	.login-btn:disabled {
		opacity: .7;
		cursor: not-allowed;
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

		color: #64748B;

		padding: 5px;
		display: flex;
		align-items: center;
		justify-content: center;

		cursor: pointer;
	}

	.eye-btn:hover {
		color: #2563EB;
	}

	.eye-btn:disabled {
		cursor: not-allowed;
	}

	.error-message {
		margin: -2px 0 0;
		color: #DC2626;
		font-size: 13px;
		font-weight: 500;
	}

	.server-error {
		padding: 12px 14px;
		border: 1px solid #FECACA;
		border-radius: 10px;
		background: #FEF2F2;
		color: #DC2626;
		font-size: 13px;
		font-weight: 500;
	}

	@media (max-width: 700px) {

		.login-card {
			padding: 30px 22px;
		}

		.role-tabs {
			grid-template-columns: repeat(2, 1fr);
		}

		.role-tabs button:last-child {
			grid-column: 1 / -1;
		}

		.login-header h1 {
			font-size: 28px;
		}

	}

</style>