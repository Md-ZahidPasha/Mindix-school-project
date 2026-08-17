<script lang="ts">
	import StudentProfile from '$lib/components/principal/StudentProfile.svelte';
	import StudentIdCard from '$lib/components/principal/StudentIdCard.svelte';
	import { scanLookup, type ScanLookupResult } from '$lib/services/attendance';

	let studentId = $state('');
	let error = $state('');
	let loading = $state(false);
	let showProfile = $state(false);
	let result: ScanLookupResult | null = $state(null);

	async function searchStudent() {
		error = '';
		showProfile = false;
		result = null;

		const id = studentId.trim();
		if (!id) {
			error = 'Student ID is required';
			return;
		}

		const institutionId = localStorage.getItem('institution_id') || '';
		if (!institutionId) {
			error = 'Institution context is missing. Please log in again.';
			return;
		}

		loading = true;
		try {
			const data = await scanLookup(id, institutionId);
			result = data;
			showProfile = true;
		} catch (err) {
			error = err instanceof Error ? err.message : 'Student not found.';
		} finally {
			loading = false;
		}
	}

	function clearSearch() {
		studentId = '';
		error = '';
		showProfile = false;
		result = null;
	}
</script>

<section class="student-access">
	<div class="section-header">
		<div>
			<h2>Students</h2>
			<p>Search and view complete student information.</p>
		</div>
	</div>

	<div class="search-card">
		<div class="search-content">
			<div class="search-icon">♧</div>

			<div class="search-text">
				<h3>Find a Student</h3>
				<p>Enter the student's ID to view their overall profile.</p>
			</div>
		</div>

		<div class="search-form">
			<div class="input-group">
				<label for="student-id">Student ID</label>

				<input
					id="student-id"
					type="text"
					bind:value={studentId}
					placeholder="Enter student ID"
					oninput={() => {
						error = '';
					}}
					onkeydown={(e) => {
						if (e.key === 'Enter') searchStudent();
					}}
				/>

				{#if error}
					<p class="error-message">{error}</p>
				{/if}
			</div>

			<button type="button" onclick={searchStudent} disabled={loading}>
				{loading ? 'Searching…' : 'Search'}
			</button>
		</div>
	</div>
	{#if showProfile && result}
		<StudentIdCard
			code={result.code}
			name={result.full_name}
			rollNumber={result.roll_number}
			className={result.class_name}
			section={result.section}
		/>
	<StudentProfile />

	<button
		type="button"
		class="clear-button"
		onclick={clearSearch}
	>
		Search Another Student
	</button>
{/if}
</section>

<style>
	.student-access {
		margin-top: 28px;
	}

	.section-header {
		margin-bottom: 14px;
	}

	.section-header h2 {
		margin: 0;
		color: #14213d;
		font-size: 20px;
	}

	.section-header p {
		margin: 5px 0 0;
		color: #64748b;
		font-size: 13px;
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
		background: #eaf1ff;
		color: #2563eb;
		border-radius: 12px;
		font-size: 22px;
	}

	.search-text h3 {
		margin: 0;
		color: #14213d;
		font-size: 16px;
	}

	.search-text p {
		margin: 4px 0 0;
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

	button:disabled {
		background: #94a3b8;
		cursor: not-allowed;
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