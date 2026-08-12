<script lang="ts">
	import { Sparkles, ArrowRight } from '@lucide/svelte';
</script>

<section class="banner">

	<div class="content">

		<div class="badge">

			<Sparkles size={18} />

			<span>PaperBuddy AI</span>

		</div>

		<h2>

			Welcome back,
			<br>
			ABC Public School

		</h2>

		<p>

			Manage your institution smarter with AI-powered
			automation, student management and real-time insights.

		</p>

		<button>

			Get Started

			<ArrowRight size={18} />

		</button>

	</div>

</section>

<style lang="scss">
.banner{

	background:linear-gradient(135deg,#2563EB,#4F46E5);

	border-radius:28px;

	padding:40px;

	color:white;

	margin-bottom:32px;

	box-shadow:0 20px 40px rgba(37,99,235,.25);

}

.badge{

	display:inline-flex;

	align-items:center;

	gap:8px;

	background:rgba(255,255,255,.18);

	padding:10px 16px;

	border-radius:999px;

	margin-bottom:24px;

	font-size:14px;

	font-weight:600;

}

.banner h2{

	font-size:38px;

	font-weight:800;

	line-height:1.25;

	margin-bottom:18px;

}

.banner p{

	max-width:620px;

	font-size:17px;

	line-height:1.8;

	opacity:.92;

	margin-bottom:28px;

}

button{

	display:flex;

	align-items:center;

	gap:10px;

	padding:14px 24px;

	border:none;

	border-radius:14px;

	background:white;

	color:#2563EB;

	font-size:15px;

	font-weight:700;

	cursor:pointer;

	transition:.25s;

}

button:hover{

	transform:translateY(-2px);

}
</style>