<script lang="ts">
	import TeacherProfile from '$lib/components/principal/TeacherProfile.svelte';

	let teacherId = $state('');
	let error = $state('');
	let showProfile = $state(false);

	function searchTeacher() {
		error = '';
		showProfile = false;

		if (!teacherId.trim()) {
			error = 'Teacher ID is required';
			return;
		}

		showProfile = true;

		console.log('Searching teacher:', teacherId);
	}

	function clearSearch() {
		teacherId = '';
		error = '';
		showProfile = false;
	}
</script>

<section class="teacher-access">
	<div class="search-card">
		<div class="search-content">
			<div class="search-icon">♙</div>

			<div class="search-text">
				<h2>Find a Teacher</h2>
				<p>Enter the teacher's ID to view their overall profile.</p>
			</div>
		</div>

		<div class="search-form">
			<div class="input-group">
				<label for="teacher-id">Teacher ID</label>

				<input
					id="teacher-id"
					type="text"
					bind:value={teacherId}
					placeholder="Enter teacher ID"
					oninput={() => {
						error = '';
					}}
				/>

				{#if error}
					<p class="error-message">{error}</p>
				{/if}
			</div>

			<button type="button" onclick={searchTeacher}>
				Search
			</button>
		</div>
		</div>

	{#if showProfile}
		<TeacherProfile />

		<button
			type="button"
			class="clear-button"
			onclick={clearSearch}
		>
			Search Another Teacher
		</button>
	{/if}
</section>

<style>
	.teacher-access {
		margin-top: 0;
	}

	.search-card {
		padding: 24px;
		background: white;
		border: 1px solid #e5eaf2;
		border-radius: 16px;
		box-shadow: 0 4px 14px rgba(15, 23, 42, 0.03);
	}

	.search-content {
		display: flex;
		align-items: center;
		gap: 14px;
		margin-bottom: 22px;
	}

	.search-icon {
		width: 48px;
		height: 48px;
		display: flex;
		align-items: center;
		justify-content: center;
		flex-shrink: 0;
		background: #eaf1ff;
		color: #2563eb;
		border-radius: 12px;
		font-size: 22px;
	}

	.search-text h2 {
		margin: 0;
		color: #14213d;
		font-size: 18px;
	}

	.search-text p {
		margin: 5px 0 0;
		color: #64748b;
		font-size: 13px;
	}

	.search-form {
		display: flex;
		align-items: flex-end;
		gap: 14px;
	}

	.input-group {
		flex: 1;
	}

	label {
		display: block;
		margin-bottom: 7px;
		color: #334155;
		font-size: 13px;
		font-weight: 600;
	}

	input {
		width: 100%;
		height: 44px;
		padding: 0 13px;
		box-sizing: border-box;
		border: 1px solid #dbe3ef;
		border-radius: 10px;
		outline: none;
		color: #14213d;
		font-size: 14px;
		background: white;
	}

	input:focus {
		border-color: #2563eb;
		box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.1);
	}

	input::placeholder {
		color: #94a3b8;
	}

	button {
		height: 44px;
		padding: 0 24px;
		border: none;
		border-radius: 10px;
		background: #2563eb;
		color: white;
		font-size: 14px;
		font-weight: 600;
		cursor: pointer;
	}

	button:hover {
		background: #1d4ed8;
	}

	.error-message {
		margin: 6px 0 0;
		color: #dc2626;
		font-size: 12px;
	}

	@media (max-width: 650px) {
		.search-form {
			flex-direction: column;
			align-items: stretch;
		}

		button {
			width: 100%;
		}
	}
    .clear-button {
	margin-top: 4px;
	padding: 10px 18px;
	border: 1px solid #dbe3ef;
	border-radius: 9px;
	background: white;
	color: #2563eb;
	font-size: 13px;
	font-weight: 600;
	cursor: pointer;
}

.clear-button:hover {
	background: #f8fafc;
}
</style>