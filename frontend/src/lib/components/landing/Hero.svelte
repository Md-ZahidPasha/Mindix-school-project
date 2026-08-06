<script lang="ts">
	import HeroContent from './HeroContent.svelte';
</script>

<section id="hero" class="hero">

	<div class="gradient gradient-1"></div>

	<div class="gradient gradient-2"></div>

	<div class="container hero-container">

		<HeroContent />

	</div>

</section>

<style lang="scss">
.hero{

	position:relative;

	overflow:hidden;

	min-height:calc(100vh - 78px);

	display:flex;

	align-items:center;

	background:
	linear-gradient(
	180deg,
	#ffffff 0%,
	#f8fbff 45%,
	#eef5ff 100%
	);

}

.hero-container{

	position:relative;

	z-index:2;

	display:flex;

	justify-content:center;

	padding:100px 0 120px;

}

.gradient{

	position:absolute;

	border-radius:50%;

	filter:blur(90px);

	opacity:.45;

}

.gradient-1{

	width:420px;

	height:420px;

	background:#2563eb;

	top:-140px;

	right:-120px;

}

.gradient-2{

	width:350px;

	height:350px;

	background:#4f46e5;

	left:-120px;

	bottom:-100px;

}

@media(max-width:768px){

	.hero{

		min-height:auto;

		padding:80px 0;

	}

	.hero-container{

		padding:60px 0;

	}

	.gradient{

		display:none;

	}

}
</style>