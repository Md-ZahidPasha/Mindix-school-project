<script lang="ts">
	import PrincipalForm from './components/PrincipalForm.svelte';
	import AIDocumentReader from '$lib/components/AIDocumentReader.svelte';
    
</script>

<section class="principal-page">

	<div class="page-header">

		<h1>Add Principal</h1>

		<p>
			Create the principal account for your institution.
		</p>

	</div>

	<div class="page-grid">

        <PrincipalForm />

        <AIDocumentReader />		

	</div>

	

</section>

<style lang="scss">

.principal-page{

	max-width:1450px;

	margin:0 auto;

	padding:40px 32px;

	background:#F8FAFC;

	min-height:100vh;

}

.page-header{

	margin-bottom:32px;

}

.page-header h1{

	font-size:36px;

	font-weight:700;

	color:#0F172A;

	margin-bottom:8px;

}

.page-header p{

	font-size:16px;

	color:#64748B;

}

.page-grid{

	display:grid;

	grid-template-columns:2fr 1fr;

	gap:30px;

	align-items:start;

}

.page-footer{

	margin-top:36px;

	display:flex;

	justify-content:center;

}

@media(max-width:1000px){

	.page-grid{

		grid-template-columns:1fr;

	}

}
</style>