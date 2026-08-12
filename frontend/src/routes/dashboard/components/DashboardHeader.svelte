<script lang="ts">
	import {
		Search,
		Bell,
		UserCircle2
	} from '@lucide/svelte';

	let {
		institutionName = ''
	}: {
		institutionName?: string;
	} = $props();

	const today = new Date();

	const options: Intl.DateTimeFormatOptions = {
		weekday: 'long',
		day: 'numeric',
		month: 'long',
		year: 'numeric'
	};

	const currentDate = today.toLocaleDateString(
		'en-US',
		options
	);

	const userRole =
		typeof window !== 'undefined'
			? localStorage.getItem('user_role') || 'Admin'
			: 'Admin';
</script>

<header class="header">

	<div class="left">

		<h1>Welcome Back 👋</h1>

		<p>{currentDate}</p>

	</div>

	<div class="right">

		<div class="search-box">

			<Search size={18} />

			<input
				type="text"
				placeholder="Search..."
			/>

		</div>

		<button
			type="button"
			class="icon-btn"
			aria-label="Notifications"
		>

			<Bell size={20} />

		</button>

		<div class="profile">

			<UserCircle2 size={38} />

			<div>

				<h4>{userRole}</h4>

				<p>{institutionName || 'PaperBuddy'}</p>

			</div>

		</div>

	</div>

</header>

<style lang="scss">
@use '$lib/styles/_colors' as c;

.header{

	display:flex;

	align-items:center;

	justify-content:space-between;

	margin-bottom:40px;

}

.left h1{

	font-size:34px;

	font-weight:800;

	color:c.$text-primary;

	margin-bottom:8px;

}

.left p{

	color:c.$text-secondary;

	font-size:15px;

}

.right{

	display:flex;

	align-items:center;

	gap:18px;

}

.search-box{

	width:320px;

	height:48px;

	background:white;

	border:1px solid c.$border;

	border-radius:14px;

	display:flex;

	align-items:center;

	padding:0 16px;

	gap:12px;

}

.search-box input{

	flex:1;

	border:none;

	outline:none;

	background:none;

	font-size:15px;

}

.icon-btn{

	width:48px;

	height:48px;

	border:none;

	border-radius:14px;

	background:white;

	border:1px solid c.$border;

	cursor:pointer;

	display:flex;

	align-items:center;

	justify-content:center;

	transition:.25s;

}

.icon-btn:hover{

	background:#EEF4FF;

	color:#2563EB;

}

.profile{

	display:flex;

	align-items:center;

	gap:12px;

	background:white;

	border:1px solid c.$border;

	padding:8px 14px;

	border-radius:16px;

}

.profile h4{

	margin:0;

	font-size:15px;

	font-weight:700;

	color:c.$text-primary;

}

.profile p{

	margin:2px 0 0;

	font-size:13px;

	color:c.$text-secondary;

}
</style>