<script lang="ts">
	import Navbar from '$lib/components/layout/Navbar.svelte';
	import Footer from '$lib/components/layout/Footer.svelte';

	import WelcomePanel from './components/WelcomePanel.svelte';
	import RegisterForm from './components/RegisterForm.svelte';
</script>

<svelte:head>
	<title>Register Institution | PaperBuddy</title>
</svelte:head>

<Navbar />

<section class="register-page">

	<div class="container">

		<div class="page-header">

			<div class="page-badge">
				🚀 Get Started
			</div>

			<h1>
				Register Your Institution
			</h1>

			<p>
				Create your school's PaperBuddy workspace in minutes and
				begin managing admissions, attendance, academics,
				library, examinations and AI-powered automation.
			</p>

		</div>

		<div class="register-container">

			<div class="welcome-column">

				<WelcomePanel />

			</div>

			<div class="form-column">

				<RegisterForm />

			</div>

		</div>

	</div>

</section>

<Footer />

<style lang="scss">
@use '$lib/styles/_colors' as c;

.register-page{

	min-height:calc(100vh - 160px);

	padding:60px 0;

	background:linear-gradient(
	180deg,
	#f8fbff,
	#eef5ff
	);

}

.container{

	max-width:1400px;

	margin:auto;

}

.page-header{

	max-width:760px;

	margin:0 auto 55px;

	text-align:center;

}

.page-badge{

	display:inline-flex;

	align-items:center;

	padding:10px 22px;

	border-radius:999px;

	background:rgba(37,99,235,.08);

	color:c.$primary;

	font-size:14px;

	font-weight:600;

	margin-bottom:22px;

}

.page-header h1{

	font-size:48px;

	font-weight:800;

	color:c.$text-primary;

	margin-bottom:18px;

}

.page-header p{

	font-size:18px;

	line-height:1.8;

	color:c.$text-secondary;

}

.register-container{

	display:grid;

	grid-template-columns:40% 60%;

	gap:32px;

	align-items:stretch;

}

.welcome-column{

	display:flex;

}

.form-column{

	display:flex;

}

.welcome-column :global(.welcome-panel){

	width:100%;

	height:100%;

}

.form-column :global(.register-card){

	width:100%;

	height:100%;
    }

@media(max-width:1100px){

	.register-container{

		grid-template-columns:1fr;

		gap:28px;

	}

	.welcome-column{

		display:none;

	}

	.page-header{

		margin-bottom:40px;

	}

}

@media(max-width:768px){

	.register-page{

		padding:40px 0;

	}

	.container{

		padding:0 18px;

	}

	.page-header h1{

		font-size:36px;

	}

	.page-header p{

		font-size:16px;

	}

	.page-header{

		margin-bottom:32px;

	}

}

</style>