<script lang="ts">
	import Button from '$lib/components/ui/Button.svelte';
</script>

<div class="hero-content">

	<div class="badge">
		✨ AI-Powered School Operations Platform
	</div>

	<h1>
		Manage Your Institution
		<span>Smarter</span>
	</h1>

	<p>
		PaperBuddy brings admissions, attendance, academics,
		examinations, library, communication and AI-powered
		automation together in one intelligent platform built
		for modern schools.
	</p>
<div class="hero-buttons">

	<a href="/register" class="btn-primary">
		Register Institution
	</a>

	<a href="#modules" class="btn-secondary">
		Explore Demo
	</a>

</div>

</div>

<style lang="scss">
@use '$lib/styles/_colors' as c;

.hero-content{

	max-width:820px;

	margin:auto;

	text-align:center;

}

.badge{

	display:inline-flex;

	align-items:center;

	padding:12px 24px;

	border-radius:999px;

	background:rgba(37,99,235,.08);

	color:c.$primary;

	font-weight:600;

	font-size:15px;

	margin-bottom:30px;

}

h1{

	font-size:68px;

	font-weight:800;

	line-height:1.1;

	color:c.$text-primary;

	margin-bottom:28px;

}

h1 span{

	color:c.$primary;

}

p{

	max-width:760px;

	margin:auto;

	font-size:20px;

	line-height:1.9;

	color:c.$text-secondary;

	margin-bottom:42px;

}

.hero-buttons{

	display:flex;

	justify-content:center;

	align-items:center;

	gap:20px;

	margin-top:10px;

	flex-wrap:wrap;

}

.hero-buttons a{

	text-decoration:none;

	font-weight:600;

	font-size:16px;

	padding:15px 30px;

	border-radius:14px;

	min-width:220px;

	text-align:center;

	transition:all .3s ease;

}

.btn-primary{

	background:#2563EB;

	color:white;

	box-shadow:0 12px 30px rgba(37,99,235,.22);

}

.btn-primary:hover{

	background:#1D4ED8;

	transform:translateY(-2px);

}

.btn-secondary{

	background:white;

	color:#0F172A;

	border:1px solid #E2E8F0;

	box-shadow:0 8px 20px rgba(15,23,42,.05);

}

.btn-secondary:hover{

	border-color:#2563EB;

	color:#2563EB;

	transform:translateY(-2px);

}

@media(max-width:768px){

	h1{

		font-size:42px;

	}

	p{

		font-size:17px;

	}

	.hero-buttons{

		flex-direction:column;

	}

}
</style>