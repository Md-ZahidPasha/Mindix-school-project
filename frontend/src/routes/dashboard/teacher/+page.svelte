<script lang="ts">
	import TeacherForm from './components/TeacherForm.svelte';
	import AIDocumentReader from '$lib/components/AIDocumentReader.svelte';
</script>

<section class="teacher-page">

	<div class="page-header">
		<h1>Add Teacher</h1>
		<p>Create a teacher account.</p>
	</div>

	<div class="page-grid">
		<TeacherForm />
		<AIDocumentReader />
	</div>

</section>

<style lang="scss">
	.teacher-page {
		max-width: 1450px;
		margin: 0 auto;
		padding: 40px 32px;
		background: #F8FAFC;
		min-height: 100vh;
	}

	.page-header {
		margin-bottom: 32px;
	}

	.page-header h1 {
		font-size: 36px;
		font-weight: 700;
		color: #0F172A;
		margin-bottom: 8px;
	}

	.page-header p {
		font-size: 16px;
		color: #64748B;
	}

	.page-grid {
		display: grid;
		grid-template-columns: 2fr 1fr;
		gap: 30px;
		align-items: start;
	}

	@media (max-width: 1000px) {
		.page-grid {
			grid-template-columns: 1fr;
		}
	}
</style>