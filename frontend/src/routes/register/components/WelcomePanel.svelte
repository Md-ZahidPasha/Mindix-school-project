<section class="welcome-panel">

	<div class="content">

		<div class="logo">

			<div class="logo-icon">
				🎓
			</div>

			<h2>PaperBuddy</h2>

		</div>

		<span class="badge">
			AI-Powered School Operations Platform
		</span>

		<h1>
			Welcome to
			<span>PaperBuddy</span>
		</h1>

		<p>
			Create your institution in just a few minutes and start managing admissions,
			attendance, academics, examinations, library, communication and AI-powered
			automation from one intelligent platform.
		</p>

		<div class="features">

			<div class="feature">
				<span>✓</span>
				AI Document Reader
			</div>

			<div class="feature">
				<span>✓</span>
				Smart Timetable
			</div>

			<div class="feature">
				<span>✓</span>
				Student Management
			</div>

			<div class="feature">
				<span>✓</span>
				Attendance & Leave
			</div>

			<div class="feature">
				<span>✓</span>
				Digital Library
			</div>

			<div class="feature">
				<span>✓</span>
				AI Analytics
			</div>

		</div>

	</div>

</section>

<style lang="scss">
@use '$lib/styles/_colors' as c;

.welcome-panel{

	height:100%;

	padding:50px;

	display:flex;

	align-items:center;

	background:linear-gradient(
	135deg,
	#2563EB,
	#4F46E5
	);

	color:white;

	border-radius:28px;

}

.content{

	max-width:520px;

}

.logo{

	display:flex;

	align-items:center;

	gap:14px;

	margin-bottom:30px;

}

.logo-icon{

	width:54px;

	height:54px;

	border-radius:16px;

	background:rgba(255,255,255,.18);

	display:flex;

	align-items:center;

	justify-content:center;

	font-size:24px;

}

.logo h2{

	font-size:34px;

	font-weight:800;

}

.badge{

	display:inline-block;

	padding:10px 18px;

	border-radius:999px;

	background:rgba(255,255,255,.15);

	margin-bottom:28px;

	font-size:14px;

	font-weight:600;

}

h1{

	font-size:44px;

	font-weight:800;

	line-height:1.15;

	margin-bottom:22px;

}

h1 span{

	color:#BFDBFE;

}

p{

	font-size:18px;

	line-height:1.8;

	color:rgba(255,255,255,.92);

	margin-bottom:36px;

}

.features{

	display:grid;

	grid-template-columns:1fr;

	gap:18px;

}

.feature{

	display:flex;

	align-items:center;

	gap:14px;

	font-size:17px;

	font-weight:500;

}

.feature span{

	width:28px;

	height:28px;

	display:flex;

	align-items:center;

	justify-content:center;

	border-radius:50%;

	background:rgba(255,255,255,.18);

	font-weight:700;

}
</style>