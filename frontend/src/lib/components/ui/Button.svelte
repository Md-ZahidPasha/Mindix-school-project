<script lang="ts">
	type Variant =
		| 'primary'
		| 'secondary'
		| 'outline'
		| 'ghost'
		| 'success'
		| 'danger';

	type Size =
		| 'sm'
		| 'md'
		| 'lg';

	let {
		variant = 'primary',
		size = 'md',
		type = 'button',
		disabled = false,
		loading = false,
		fullWidth = false,
		onclick,
		children
	}: {
		variant?: Variant;
		size?: Size;
		type?: 'button' | 'submit' | 'reset';
		disabled?: boolean;
		loading?: boolean;
		fullWidth?: boolean;
		onclick?: (event: MouseEvent) => void;
		children?: import('svelte').Snippet;
	} = $props();
</script>

<button
	type={type}
	class={`btn ${variant} ${size} ${fullWidth ? 'full' : ''}`}
	disabled={disabled || loading}
	onclick={onclick}
>
	{#if loading}
		<span class="loader"></span>
	{/if}

	{@render children?.()}
</button>

<style lang="scss">
@use '$lib/styles/_colors' as c;
@use '$lib/styles/_variables' as v;
@use '$lib/styles/_typography' as t;

.btn {
	display: inline-flex;
	align-items: center;
	justify-content: center;
	gap: 10px;

	border: none;
	outline: none;
	cursor: pointer;

	border-radius: v.$radius-lg;

	font-family: t.$font-family;
	@include t.button-text;

	transition: all v.$transition-normal;

	padding: 14px 28px;

	user-select: none;

	&:disabled {
		opacity: 0.6;
		cursor: not-allowed;
		transform: none;
		box-shadow: none;
	}
}

/* Width */

.full {
	width: 100%;
}

/* Sizes */

.sm {
	padding: 10px 18px;
	font-size: 14px;
}

.md {
	padding: 14px 28px;
	font-size: 15px;
}

.lg {
	padding: 18px 36px;
	font-size: 16px;
}

/* Primary */

.primary {
	background: c.$primary-gradient;
	color: white;
	box-shadow: v.$shadow-md;
}

.primary:hover:not(:disabled) {
	transform: translateY(-2px);
	box-shadow: v.$shadow-lg;
}

/* Secondary */

.secondary {
	background: c.$secondary;
	color: white;
	box-shadow: v.$shadow-md;
}

.secondary:hover:not(:disabled) {
	transform: translateY(-2px);
	box-shadow: v.$shadow-lg;
}

/* Outline */

.outline {
	background: white;
	color: c.$primary;
	border: 1px solid c.$border;
}

.outline:hover:not(:disabled) {
	background: c.$hover;
}

/* Ghost */

.ghost {
	background: transparent;
	color: c.$text-primary;
}

.ghost:hover:not(:disabled) {
	background: c.$surface-alt;
}

/* Success */

.success {
	background: c.$success;
	color: white;
	box-shadow: v.$shadow-md;
}

.success:hover:not(:disabled) {
	transform: translateY(-2px);
	box-shadow: v.$shadow-lg;
}

/* Danger */

.danger {
	background: c.$danger;
	color: white;
	box-shadow: v.$shadow-md;
}

.danger:hover:not(:disabled) {
	transform: translateY(-2px);
	box-shadow: v.$shadow-lg;
}

/* Loader */

.loader {
	width: 18px;
	height: 18px;

	border: 2px solid rgba(255, 255, 255, 0.35);
	border-top: 2px solid white;

	border-radius: 50%;

	animation: spin 0.8s linear infinite;
}

@keyframes spin {
	from {
		transform: rotate(0deg);
	}

	to {
		transform: rotate(360deg);
	}
}
</style>