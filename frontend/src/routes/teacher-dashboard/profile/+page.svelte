<script lang="ts">
	import { getTeacherProfile } from '$lib/services/teacherApi';
	import {
		UserCircle,
		Mail,
		Phone,
		GraduationCap,
		CalendarDays,
		BookOpen,
		Briefcase,
		Loader2,
		AlertCircle
	} from '@lucide/svelte';

	let profileData = $state<any>(null);
	let loading = $state(true);
	let error = $state('');

	async function loadProfile() {
		try {
			loading = true;
			error = '';
			profileData = await getTeacherProfile();
		} catch (err) {
			console.error('Failed to load teacher profile:', err);
			error = 'Unable to load profile data.';
		} finally {
			loading = false;
		}
	}

	loadProfile();

	function formatDate(value: string | null): string {
		if (!value) return '-';
		const date = new Date(value);
		if (isNaN(date.getTime())) return value;
		return date.toLocaleDateString('en-US', {
			day: 'numeric',
			month: 'long',
			year: 'numeric'
		});
	}
</script>

<svelte:head>
	<title>My Profile | PaperBuddy</title>
</svelte:head>

<div class="profile-page">
	<div class="page-header">
		<div>
			<h1>My Profile</h1>
			<p>View your personal and professional information.</p>
		</div>
	</div>

	{#if loading}
		<div class="state-card">
			<Loader2 class="spin" size={24} />
			<p>Loading profile...</p>
		</div>
	{:else if error}
		<div class="state-card error-card">
			<AlertCircle size={24} />
			<p>{error}</p>
		</div>
	{:else if profileData}
		<section class="profile-card">
			<div class="profile-top">
				<div class="avatar">
					<UserCircle size={48} />
				</div>

				<div>
					<h2>{profileData.full_name ?? 'Teacher'}</h2>
					<p>Teacher</p>
				</div>
			</div>

			<div class="profile-grid">
				<div class="info-item">
					<div class="icon-box">
						<Mail size={19} />
					</div>
					<div>
						<span>Email</span>
						<strong>{profileData.email ?? '-'}</strong>
					</div>
				</div>

				<div class="info-item">
					<div class="icon-box">
						<Phone size={19} />
					</div>
					<div>
						<span>Phone</span>
						<strong>{profileData.phone ?? '-'}</strong>
					</div>
				</div>

				<div class="info-item">
					<div class="icon-box">
						<Briefcase size={19} />
					</div>
					<div>
						<span>Department</span>
						<strong>{profileData.department_id ? 'Assigned' : '-'}</strong>
					</div>
				</div>

				<div class="info-item">
					<div class="icon-box">
						<BookOpen size={19} />
					</div>
					<div>
						<span>Qualification</span>
						<strong>{profileData.qualification ?? '-'}</strong>
					</div>
				</div>

				<div class="info-item">
					<div class="icon-box">
						<GraduationCap size={19} />
					</div>
					<div>
						<span>Specialization</span>
						<strong>{profileData.specialization ?? '-'}</strong>
					</div>
				</div>

				<div class="info-item">
					<div class="icon-box">
						<CalendarDays size={19} />
					</div>
					<div>
						<span>Joining Date</span>
						<strong>{formatDate(profileData.joining_date)}</strong>
					</div>
				</div>
			</div>

			<div class="subjects-section">
				<h3>Assigned Subjects</h3>
				{#if (profileData.subject_ids ?? []).length === 0}
					<p class="muted">No subjects assigned yet.</p>
				{:else}
					<div class="subject-chips">
						{#each profileData.subject_ids as _sid, index}
							<span class="chip">Subject {index + 1}</span>
						{/each}
					</div>
				{/if}
			</div>
		</section>
	{/if}
</div>

<style>
	.profile-page {
		padding: 36px;
		max-width: 900px;
	}

	.page-header {
		margin-bottom: 28px;
	}

	.page-header h1 {
		margin: 0 0 8px;
		font-size: 30px;
		font-weight: 800;
		color: #0f172a;
	}

	.page-header p {
		margin: 0;
		font-size: 15px;
		color: #64748b;
	}

	.profile-card {
		background: white;
		border: 1px solid #e2e8f0;
		border-radius: 18px;
		padding: 28px;
		box-shadow: 0 4px 15px rgba(15, 23, 42, 0.04);
	}

	.profile-top {
		display: flex;
		align-items: center;
		gap: 16px;
		margin-bottom: 26px;
	}

	.avatar {
		width: 68px;
		height: 68px;
		display: flex;
		align-items: center;
		justify-content: center;
		background: #eef4ff;
		color: #2563eb;
		border-radius: 16px;
	}

	.profile-top h2 {
		margin: 0 0 5px;
		font-size: 22px;
		font-weight: 800;
		color: #0f172a;
	}

	.profile-top p {
		margin: 0;
		font-size: 14px;
		color: #64748b;
	}

	.profile-grid {
		display: grid;
		grid-template-columns: 1fr 1fr;
		gap: 16px;
	}

	.info-item {
		display: flex;
		align-items: center;
		gap: 14px;
		padding: 16px;
		background: #f8fafc;
		border: 1px solid #e2e8f0;
		border-radius: 12px;
	}

	.icon-box {
		width: 40px;
		height: 40px;
		flex-shrink: 0;
		display: flex;
		align-items: center;
		justify-content: center;
		background: white;
		color: #2563eb;
		border-radius: 10px;
	}

	.info-item span {
		display: block;
		font-size: 12px;
		color: #64748b;
		margin-bottom: 4px;
	}

	.info-item strong {
		display: block;
		font-size: 14px;
		color: #0f172a;
	}

	.subjects-section {
		margin-top: 24px;
	}

	.subjects-section h3 {
		margin: 0 0 14px;
		font-size: 16px;
		font-weight: 800;
		color: #0f172a;
	}

	.muted {
		margin: 0;
		font-size: 14px;
		color: #94a3b8;
	}

	.subject-chips {
		display: flex;
		flex-wrap: wrap;
		gap: 10px;
	}

	.chip {
		padding: 8px 14px;
		background: #eef4ff;
		color: #2563eb;
		border-radius: 20px;
		font-size: 13px;
		font-weight: 600;
	}

	.state-card {
		display: flex;
		align-items: center;
		justify-content: center;
		gap: 10px;
		padding: 40px;
		background: white;
		border: 1px solid #e2e8f0;
		border-radius: 18px;
		color: #64748b;
	}

	.state-card p {
		margin: 0;
	}

	.error-card {
		color: #dc2626;
	}

	.spin {
		animation: spin 1s linear infinite;
	}

	@keyframes spin {
		to {
			transform: rotate(360deg);
		}
	}

	@media (max-width: 700px) {
		.profile-grid {
			grid-template-columns: 1fr;
		}
	}
</style>