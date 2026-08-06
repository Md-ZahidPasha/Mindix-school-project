<script lang="ts">
import { Eye, EyeOff } from '@lucide/svelte';

	let institutionName = $state('');
	let institutionType = $state('');
	let adminName = $state('');
	let email = $state('');
	let phone = $state('');
	let password = $state('');
	let confirmPassword = $state('');
    let showPassword = $state(false);
    let showConfirmPassword = $state(false);
</script>

<section class="register-card">

	<div class="card-header">

		<h2>Register Your Institution</h2>

		<p>
			Create your PaperBuddy workspace and start managing your
			school with AI.
		</p>

	</div>

<form
	class="register-form"
	onsubmit={(e) => e.preventDefault()}
>

	<div class="form-grid">

		<div class="form-group">

			<label for="institutionName">
				Institution Name
			</label>

			<input
				id="institutionName"
				type="text"
				bind:value={institutionName}
				placeholder="ABC Public School"
			/>

		</div>

		<div class="form-group">

			<label for="institutionType">
				Institution Type
			</label>

			<select
				id="institutionType"
				bind:value={institutionType}
			>

				<option value="">
					Select Institution Type
				</option>

				<option>School</option>

				<option>Junior College</option>

				<option>College</option>

				<option>University</option>

			</select>

		</div>

		<div class="form-group">

			<label for="adminName">
				Principal / Admin Name
			</label>

			<input
				id="adminName"
				type="text"
				bind:value={adminName}
				placeholder="John Doe"
			/>

		</div>

		<div class="form-group">

			<label for="phone">
				Phone Number
			</label>

			<input
				id="phone"
				type="tel"
				bind:value={phone}
				placeholder="+91 9876543210"
			/>

		</div>

		<div class="form-group full">

			<label for="email">
				Email Address
			</label>

			<input
				id="email"
				type="email"
				bind:value={email}
				placeholder="admin@school.com"
			/>

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
			placeholder="Create Password"
		/>

		<button
			type="button"
			class="eye-btn"
			onclick={() => showPassword = !showPassword}
		>

			{#if showPassword}
				<EyeOff size={20} />
			{:else}
				<Eye size={20} />
			{/if}

		</button>

	</div>

</div>

<div class="form-group">

	<label for="confirmPassword">
		Confirm Password
	</label>

	<div class="password-wrapper">

		<input
			id="confirmPassword"
			type={showConfirmPassword ? 'text' : 'password'}
			bind:value={confirmPassword}
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

</div>

	</div>

	<button
		type="submit"
		class="submit-btn"
	>
		🚀 Create Institution
	</button>

</form>

</section>

<style lang="scss">
@use '$lib/styles/_colors' as c;

.register-card{

	height:100%;

	background:white;

	border-radius:24px;

	padding:42px;

	border:1px solid c.$border;

	box-shadow:0 20px 50px rgba(15,23,42,.08);

	display:flex;

	flex-direction:column;

	justify-content:space-between;

}

.card-header{

	margin-bottom:32px;

}

.card-header h2{

	font-size:32px;

	font-weight:800;

	color:c.$text-primary;

	margin-bottom:10px;

}

.card-header p{

	font-size:16px;

	line-height:1.7;

	color:c.$text-secondary;

}

.register-form{

	display:flex;

	flex-direction:column;

	gap:20px;

}

.form-group{

	display:flex;

	flex-direction:column;

	gap:8px;

}

.form-grid{

	display:grid;

	grid-template-columns:1fr 1fr;

	gap:20px;

}

.full{

	grid-column:1 / -1;

}

@media(max-width:768px){

	.form-grid{

		grid-template-columns:1fr;

	}

	.full{

		grid-column:auto;

	}

}

label{

	font-size:14px;

	font-weight:600;

	color:c.$text-primary;

}

input,
select{

	width:100%;

	padding:15px 50px 15px 18px;

	border-radius:14px;

	border:1px solid c.$border;

	font-size:15px;

	background:white;

	outline:none;

	transition:.25s;
    }

    .password-wrapper{

	position:relative;

}

.eye-btn{

	position:absolute;

	top:50%;

	right:16px;

	transform:translateY(-50%);

	background:none;

	border:none;

	cursor:pointer;

	display:flex;

	align-items:center;

	justify-content:center;

	color:#64748B;

	padding:4px;

	transition:.25s;

}

.eye-btn:hover{

	color:#2563EB;

}


input:focus,
select:focus{

	border-color:c.$primary;

	box-shadow:0 0 0 4px rgba(37,99,235,.10);

}

.submit-btn{

	width:100%;

	height:56px;

	margin-top:10px;

	border:none;

	border-radius:14px;

	background:linear-gradient(135deg,#2563EB,#4F46E5);

	color:#ffffff;

	font-size:16px;

	font-weight:700;

	cursor:pointer;

	display:flex;

	align-items:center;

	justify-content:center;

	transition:all .3s ease;

	box-shadow:0 12px 28px rgba(37,99,235,.25);

}

.submit-btn:hover{

	background:linear-gradient(135deg,#1D4ED8,#4338CA);

	transform:translateY(-2px);

	box-shadow:0 18px 36px rgba(37,99,235,.35);

}
	
.submit-btn:active{

	transform:translateY(0);

}

::placeholder{

	color:c.$text-muted;

}

@media(max-width:768px){

	.register-card{

		padding:28px;

		border-radius:20px;

	}

	.card-header h2{

		font-size:28px;

	}

}

</style>