<script lang="ts">
	const stats = [
		{
			title: 'Total Students',
			value: '1,240',
			description: 'View all students',
			icon: '♧',
			type: 'students'
		},
		{
			title: 'Total Teachers',
			value: '68',
			description: 'View all teachers',
			icon: '♙',
			type: 'teachers'
		},
		{
			title: 'Total Staff',
			value: '24',
			description: 'View all staff',
			icon: '▣',
			type: 'staff'
		},
		{
			title: 'Attendance Overview',
			value: '92.4%',
			description: 'Today',
			icon: '☑',
			type: 'attendance'
		},
		{
			title: 'Pending Teacher Leave',
			value: '5',
			description: 'Needs attention',
			icon: '▢',
			type: 'leave'
		},
		{
			title: 'Pending Requests',
			value: '8',
			description: 'View requests',
			icon: '♢',
			type: 'requests'
		}
	];
</script>

<section class="stats-grid">
	{#each stats as stat}
		<div class="stat-card {stat.type}">
			<div class="stat-icon">
				{stat.icon}
			</div>

			<div class="stat-content">
				<p class="stat-title">{stat.title}</p>

				<h2>{stat.value}</h2>

				<p class="stat-description">{stat.description}</p>
			</div>
		</div>
	{/each}
</section>

<style>
	.stats-grid {
		display: grid;
		grid-template-columns: repeat(3, 1fr);
		gap: 18px;
		margin-top: 28px;
	}

	.stat-card {
		min-height: 130px;
		display: flex;
		align-items: center;
		gap: 18px;
		padding: 20px;
		background: white;
		border: 1px solid #e5eaf2;
		border-radius: 16px;
		box-sizing: border-box;
		box-shadow: 0 5px 18px rgba(15, 23, 42, 0.04);
	}

	.stat-icon {
		width: 54px;
		height: 54px;
		flex-shrink: 0;
		display: flex;
		align-items: center;
		justify-content: center;
		border-radius: 14px;
		background: #eaf1ff;
		color: #2563eb;
		font-size: 24px;
	}

	.stat-title {
		margin: 0;
		color: #64748b;
		font-size: 13px;
		font-weight: 500;
	}

	.stat-content h2 {
		margin: 5px 0;
		color: #14213d;
		font-size: 27px;
		line-height: 1.1;
	}

	.stat-description {
		margin: 0;
		color: #2563eb;
		font-size: 12px;
	}

	.teachers .stat-icon {
		background: #e9f8ef;
		color: #16a34a;
	}

	.teachers .stat-description {
		color: #16a34a;
	}

	.staff .stat-icon {
		background: #f2eaff;
		color: #7c3aed;
	}

	.staff .stat-description {
		color: #7c3aed;
	}

	.attendance .stat-icon {
		background: #e8f3ff;
		color: #2563eb;
	}

	.leave .stat-icon {
		background: #fff0e6;
		color: #ea580c;
	}

	.leave .stat-description {
		color: #ea580c;
	}

	.requests .stat-icon {
		background: #ffecef;
		color: #e11d48;
	}

	.requests .stat-description {
		color: #e11d48;
	}

	@media (max-width: 1100px) {
		.stats-grid {
			grid-template-columns: repeat(2, 1fr);
		}
	}

	@media (max-width: 650px) {
		.stats-grid {
			grid-template-columns: 1fr;
		}
	}
</style>