<script lang="ts">
	import { GraduationCap, Menu, X } from '@lucide/svelte';

	let isMenuOpen = $state(false);

	function toggleMenu() {
		isMenuOpen = !isMenuOpen;
	}
</script>

<nav class="navbar">

	<div class="container navbar-container">

		<!-- Logo -->
		<a href="#hero" class="logo">

			<div class="logo-icon">
				<GraduationCap size={22}/>
			</div>

			<span class="logo-text">
				PaperBuddy
			</span>

		</a>

		<!-- Desktop Navigation -->
		<div class="nav-center">

			<a href="/#modules">
				Platform Modules
			</a>

			<a href="/login">
				Login
			</a>

			<a
				href="/register"
				class="register-btn"
			>
				Register Institution
			</a>

		</div>

		<!-- Mobile Menu Button -->
		<button
			class="menu-btn"
			onclick={toggleMenu}
			aria-label="Toggle Menu"
		>

			{#if isMenuOpen}
				<X size={24}/>
			{:else}
				<Menu size={24}/>
			{/if}

		</button>

	</div>

	<!-- Mobile Menu -->

	{#if isMenuOpen}

		<div class="mobile-menu">

			<a
				href="#/modules"
				onclick={() => isMenuOpen = false}
			>
				Platform Modules
			</a>

			<a
				href="/login"
				onclick={() => isMenuOpen = false}
			>
				Login
			</a>

			<a
				href="/register"
				class="mobile-register"
				onclick={() => isMenuOpen = false}
			>
				Register Institution
			</a>

		</div>

	{/if}

</nav>

<style lang="scss">
@use '$lib/styles/_colors' as c;

.navbar{

	position:sticky;

	top:0;

	z-index:1000;

	height:78px;

	background:rgba(255,255,255,.90);

	backdrop-filter:blur(18px);

	-webkit-backdrop-filter:blur(18px);

	border-bottom:1px solid rgba(226,232,240,.8);

	box-shadow:0 4px 20px rgba(15,23,42,.04);

}

.navbar-container{

	height:100%;

	display:flex;

	align-items:center;

	justify-content:space-between;

}

.logo{

	display:flex;

	align-items:center;

	gap:14px;

	text-decoration:none;

	color:c.$text-primary;

}

.logo-icon{

	width:46px;

	height:46px;

	display:flex;

	align-items:center;

	justify-content:center;

	border-radius:14px;

	background:c.$primary-gradient;

	color:white;

	flex-shrink:0;

}

.logo-text{

	font-size:2rem;

	font-weight:800;

	letter-spacing:-0.5px;

}

.nav-center{

	display:flex;

	align-items:center;

	gap:36px;

	margin-left:auto;

}

.nav-center a{

	text-decoration:none;

	font-size:15px;

	font-weight:600;

	color:c.$text-secondary;

	transition:all .25s ease;

}

.nav-center a:hover{

	color:c.$primary;

}

.register-btn{

	display:inline-flex;

	align-items:center;

	justify-content:center;

	padding:12px 24px;

	border-radius:14px;

	background:#2563EB;

	color:white !important;

	font-weight:600;

	white-space:nowrap;

	box-shadow:0 10px 24px rgba(37,99,235,.18);

	transition:all .25s ease;

}

.register-btn:hover{

	background:#1D4ED8;

	transform:translateY(-2px);

}
.menu-btn{

	display:none;

	width:42px;

	height:42px;

	border:none;

	background:transparent;

	cursor:pointer;

	align-items:center;

	justify-content:center;

	border-radius:10px;

	transition:all .25s ease;

}

.menu-btn:hover{

	background:#f1f5f9;

}

.mobile-menu{

	display:none;

}

@media (max-width:900px){

	.nav-center{

		display:none;

	}

	.menu-btn{

		display:flex;

	}

	.mobile-menu{

		display:flex;

		flex-direction:column;

		gap:18px;

		padding:24px;

		background:white;

		border-top:1px solid c.$border;

	}

	.mobile-menu a{

		text-decoration:none;

		font-size:16px;

		font-weight:600;

		color:c.$text-primary;

	}

	.mobile-register{

		display:flex;

		align-items:center;

		justify-content:center;

		background:#2563EB;

		color:white !important;

		padding:14px;

		border-radius:14px;

		margin-top:10px;

	}

}

@media (max-width:1200px){

	.nav-center{

		gap:24px;

	}

}

</style>