<script lang="ts">
	const overviewItems = [
		{
			title: 'Students',
			value: '1,240',
			description: 'Registered students',
			icon: '♧'
		},
		{
			title: 'Teachers',
			value: '68',
			description: 'Teaching staff',
			icon: '♙'
		},
		{
			title: 'Staff',
			value: '24',
			description: 'Non-teaching staff',
			icon: '▣'
		},
		{
			title: 'Classes',
			value: '32',
			description: 'Active classes',
			icon: '▦'
		},
		{
			title: 'Departments',
			value: '8',
			description: 'Institution departments',
			icon: '▤'
		}
	];
</script>

<section class="overview-section">
	<div class="section-heading">
		<div>
			<h2>School Overview</h2>
			<p>Overview of your institution.</p>
		</div>
	</div>

	<div class="overview-grid">
		{#each overviewItems as item}
			<div class="overview-card">
				<div class="overview-icon">
					{item.icon}
				</div>

				<div class="overview-content">
					<p class="title">{item.title}</p>
					<h3>{item.value}</h3>
					<p class="description">{item.description}</p>
				</div>
			</div>
		{/each}
	</div>
</section>

<style>
	.overview-section {
		margin-top: 24px;
	}

	.section-heading {
		margin-bottom: 14px;
	}

	.section-heading h2 {
		margin: 0;
		color: #14213d;
		font-size: 20px;
	}

	.section-heading p {
		margin: 5px 0 0;
		color: #64748b;
		font-size: 13px;
	}

	.overview-grid {
		display: grid;
		grid-template-columns: repeat(5, 1fr);
		gap: 14px;
	}

	.overview-card {
		display: flex;
		align-items: center;
		gap: 12px;
		min-height: 105px;
		padding: 16px;
		background: white;
		border: 1px solid #e5eaf2;
		border-radius: 14px;
		box-shadow: 0 4px 14px rgba(15, 23, 42, 0.03);
		box-sizing: border-box;
	}

	.overview-icon {
		width: 44px;
		height: 44px;
		flex-shrink: 0;
		display: flex;
		align-items: center;
		justify-content: center;
		background: #eaf1ff;
		color: #2563eb;
		border-radius: 11px;
		font-size: 20px;
	}

	.overview-content .title {
		margin: 0;
		color: #64748b;
		font-size: 12px;
	}

	.overview-content h3 {
		margin: 3px 0;
		color: #14213d;
		font-size: 22px;
	}

	.overview-content .description {
		margin: 0;
		color: #64748b;
		font-size: 11px;
	}

	@media (max-width: 1100px) {
		.overview-grid {
			grid-template-columns: repeat(3, 1fr);
		}
	}

	@media (max-width: 700px) {
		.overview-grid {
			grid-template-columns: repeat(2, 1fr);
		}
	}

	@media (max-width: 480px) {
		.overview-grid {
			grid-template-columns: 1fr;
		}
	}
</style>