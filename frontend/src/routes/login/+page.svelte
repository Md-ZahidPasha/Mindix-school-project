<script lang="ts">
	import Navbar from '$lib/components/layout/Navbar.svelte';
	import Footer from '$lib/components/layout/Footer.svelte';
	import LoginForm from '$lib/components/auth/LoginForm.svelte';
</script>

<Navbar />

<section class="login-page">

	<div class="container">

		<LoginForm />

	</div>

</section>

<Footer />

<style lang="scss">
.login-page{

	min-height:calc(100vh - 160px);

	display:flex;

	align-items:center;

	padding:80px 0;

	background:linear-gradient(
	180deg,
	#ffffff 0%,
	#f8fbff 50%,
	#eef5ff 100%
	);

}

.container{

	width:100%;

	display:flex;

	justify-content:center;

}
</style>