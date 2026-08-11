<script lang="ts">
	let selectedType = $state<'students' | 'teachers' | 'employees'>('students');

	const attendanceTypes = [
		{
			id: 'students',
			label: 'Students',
			icon: '♧'
		},
		{
			id: 'teachers',
			label: 'Teachers',
			icon: '♙'
		},
		{
			id: 'employees',
			label: 'Employees / Staff',
			icon: '▣'
		}
	];

	function selectType(type: 'students' | 'teachers' | 'employees') {
		selectedType = type;
	}
</script>

<section class="type-selector">
	<div class="section-heading">
		<h2>Attendance</h2>
		<p>Select whose attendance you want to view.</p>
	</div>

	<div class="type-grid">
		{#each attendanceTypes as type}
			<button
				type="button"
				class:active={selectedType === type.id}
				class="type-card"
				onclick={() => selectType(type.id as 'students' | 'teachers' | 'employees')}
			>
				<span class="type-icon">{type.icon}</span>

				<span class="type-label">{type.label}</span>

				{#if selectedType === type.id}
					<span class="selected-indicator">✓</span>
				{/if}
			</button>
		{/each}
	</div>
</section>

<style>
	.type-selector {
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

	.type-grid {
		display: grid;
		grid-template-columns: repeat(3, 1fr);
		gap: 16px;
	}

	.type-card {
		position: relative;
		display: flex;
		align-items: center;
		gap: 14px;
		min-height: 78px;
		padding: 16px 18px;
		border: 1px solid #e5eaf2;
		border-radius: 14px;
		background: white;
		color: #334155;
		text-align: left;
		cursor: pointer;
		box-shadow: 0 4px 14px rgba(15, 23, 42, 0.03);
		transition:
			border-color 0.2s ease,
			box-shadow 0.2s ease,
			background 0.2s ease;
	}

	.type-card:hover {
		border-color: #b9cdf5;
	}

	.type-card.active {
		border-color: #2563eb;
		background: #f7faff;
		box-shadow: 0 0 0 2px rgba(37, 99, 235, 0.08);
	}

	.type-icon {
		width: 44px;
		height: 44px;
		display: flex;
		align-items: center;
		justify-content: center;
		flex-shrink: 0;
		border-radius: 11px;
		background: #eaf1ff;
		color: #2563eb;
		font-size: 20px;
	}

	.type-label {
		font-size: 14px;
		font-weight: 600;
	}

	.selected-indicator {
		position: absolute;
		top: 12px;
		right: 12px;
		width: 20px;
		height: 20px;
		display: flex;
		align-items: center;
		justify-content: center;
		border-radius: 50%;
		background: #2563eb;
		color: white;
		font-size: 11px;
		font-weight: 700;
	}

	@media (max-width: 750px) {
		.type-grid {
			grid-template-columns: 1fr;
		}
	}
</style>