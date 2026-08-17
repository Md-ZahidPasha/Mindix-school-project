<script lang="ts">
	import { onMount } from 'svelte';
	import { getBooks, type Book } from '$lib/services/library';
	import { Search, BookOpen, Loader2, AlertCircle } from '@lucide/svelte';

	let books = $state<Book[]>([]);
	let loading = $state(true);
	let error = $state('');
	let search = $state('');

	const filteredBooks = $derived(
		search.trim()
			? books.filter(
					(b) =>
						`${b.title ?? ''} ${b.author ?? ''} ${b.isbn ?? ''}`
							.toLowerCase()
							.includes(search.toLowerCase())
				)
			: books
	);

	async function loadBooks() {
		try {
			loading = true;
			error = '';
			books = await getBooks();
		} catch (err) {
			console.error('Failed to load books:', err);
			error = 'Unable to load library books.';
		} finally {
			loading = false;
		}
	}

	onMount(loadBooks);
</script>

<svelte:head>
	<title>Library | PaperBuddy</title>
</svelte:head>

<div class="library-page">
	<div class="page-header">
		<div>
			<h1>Library</h1>
			<p>Browse books available in the school library.</p>
		</div>

		<div class="search-box">
			<Search size={18} />
			<input type="text" placeholder="Search books..." bind:value={search} />
		</div>
	</div>

	{#if loading}
		<div class="state-card">
			<Loader2 class="spin" size={24} />
			<p>Loading books...</p>
		</div>
	{:else if error}
		<div class="state-card error-card">
			<AlertCircle size={24} />
			<p>{error}</p>
		</div>
	{:else if filteredBooks.length === 0}
		<div class="state-card">
			<BookOpen size={24} />
			<p>No books found.</p>
		</div>
	{:else}
		<div class="books-grid">
			{#each filteredBooks as book}
				<div class="book-card">
					<div class="book-icon">
						<BookOpen size={24} />
					</div>

					<div class="book-info">
						<strong>{book.title ?? '-'}</strong>
						<span>{book.author ?? 'Unknown Author'}</span>
						{#if book.isbn}
							<span class="isbn">ISBN: {book.isbn}</span>
						{/if}
					</div>

					<div class="book-meta">
						<span
							class:low={(book.available_copies ?? 0) <= 0}
						>
							{(book.available_copies ?? 0)} / {book.total_copies ?? 0} available
						</span>
					</div>
				</div>
			{/each}
		</div>
	{/if}
</div>

<style>
	.library-page {
		padding: 36px;
	}

	.page-header {
		display: flex;
		align-items: center;
		justify-content: space-between;
		flex-wrap: wrap;
		gap: 20px;
		margin-bottom: 28px;
	}

	.page-header h1 {
		margin: 0 0 8px;
		font-size: 30px;
		font-weight: 800;
		color: #0f172a;
	}

	.page-header p {
		margin: 0;
		font-size: 15px;
		color: #64748b;
	}

	.search-box {
		width: 260px;
		height: 44px;
		display: flex;
		align-items: center;
		gap: 10px;
		padding: 0 14px;
		background: white;
		border: 1px solid #e2e8f0;
		border-radius: 12px;
	}

	.search-box svg {
		color: #64748b;
	}

	.search-box input {
		width: 100%;
		border: none;
		outline: none;
		background: transparent;
		font-size: 14px;
		color: #0f172a;
	}

	.books-grid {
		display: grid;
		grid-template-columns: repeat(3, 1fr);
		gap: 18px;
	}

	.book-card {
		display: flex;
		flex-direction: column;
		gap: 14px;
		padding: 22px;
		background: white;
		border: 1px solid #e2e8f0;
		border-radius: 16px;
		box-shadow: 0 4px 15px rgba(15, 23, 42, 0.04);
		transition: 0.25s;
	}

	.book-card:hover {
		border-color: #bfdbfe;
		transform: translateY(-2px);
	}

	.book-icon {
		width: 48px;
		height: 48px;
		display: flex;
		align-items: center;
		justify-content: center;
		background: #eef4ff;
		color: #2563eb;
		border-radius: 12px;
	}

	.book-info strong {
		display: block;
		font-size: 15px;
		color: #0f172a;
	}

	.book-info span {
		display: block;
		margin-top: 4px;
		font-size: 13px;
		color: #64748b;
	}

	.book-info .isbn {
		font-size: 11px;
		color: #94a3b8;
	}

	.book-meta span {
		display: inline-block;
		padding: 6px 10px;
		background: #ecfdf5;
		color: #059669;
		border-radius: 8px;
		font-size: 11px;
		font-weight: 700;
	}

	.book-meta span.low {
		background: #fef2f2;
		color: #dc2626;
	}

	.state-card {
		display: flex;
		align-items: center;
		justify-content: center;
		gap: 10px;
		padding: 40px;
		background: white;
		border: 1px solid #e2e8f0;
		border-radius: 18px;
		color: #64748b;
	}

	.state-card p {
		margin: 0;
	}

	.error-card {
		color: #dc2626;
	}

	.spin {
		animation: spin 1s linear infinite;
	}

	@keyframes spin {
		to {
			transform: rotate(360deg);
		}
	}

	@media (max-width: 1100px) {
		.books-grid {
			grid-template-columns: repeat(2, 1fr);
		}
	}

	@media (max-width: 700px) {
		.books-grid {
			grid-template-columns: 1fr;
		}
	}
</style>