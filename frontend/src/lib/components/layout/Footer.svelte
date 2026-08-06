<footer class="footer">

	<div class="container footer-container">

		<div class="brand">

			<h2>PaperBuddy</h2>

			<p>
				AI-Powered School Operations Platform
			</p>

		</div>

		<div class="copyright">

			<p>
				Built with ❤️ by <strong>Mindix</strong>
			</p>

			<p>
				© 2026 PaperBuddy. All Rights Reserved.
			</p>

		</div>

	</div>

</footer>

<style lang="scss">
@use '$lib/styles/_colors' as c;

.footer{

	margin-top:100px;

	padding:40px 0;

	background:#ffffff;

	border-top:1px solid c.$border;

}

.footer-container{

	display:flex;

	justify-content:space-between;

	align-items:center;

	gap:30px;

	flex-wrap:wrap;

}

.brand h2{

	font-size:26px;

	font-weight:800;

	color:c.$primary;

	margin-bottom:8px;

}

.brand p{

	color:c.$text-secondary;

	font-size:15px;

}

.copyright{

	text-align:right;

}

.copyright p{

	color:c.$text-secondary;

	font-size:14px;

	margin:4px 0;

}

@media(max-width:768px){

	.footer-container{

		flex-direction:column;

		text-align:center;

	}

	.copyright{

		text-align:center;

	}

}
</style>