<script lang="ts">
	import {
		Library as LibraryIcon,
		BookOpen,
		Plus,
		Search,
		RefreshCw,
		AlertCircle,
		Trash2
	} from '@lucide/svelte';
	import {
		getBooks,
		createBook,
		deleteBook,
		getBorrowed,
		getOverdueBooks,
		getLibraryStats,
		type Book,
		type Transaction,
		type LibraryStats
	} from '$lib/services/library';

	let books = $state<Book[]>([]);
	let borrowed = $state<Transaction[]>([]);
	let overdue = $state<Transaction[]>([]);
	let stats = $state<LibraryStats | null>(null);
	let searchQuery = $state('');
	let isLoading = $state(true);
	let error = $state('');
	let success = $state('');

	let showAddForm = $state(false);
	let newTitle = $state('');
	let newAuthor = $state('');
	let newIsbn = $state('');
	let newCopies = $state(1);

	async function loadAll() {
		isLoading = true;
		error = '';
		try {
			const [booksResult, borrowedResult, overdueResult, statsResult] = await Promise.all([
				getBooks(),
				getBorrowed(),
				getOverdueBooks(),
				getLibraryStats()
			]);
			books = booksResult;
			borrowed = borrowedResult;
			overdue = overdueResult;
			stats = statsResult;
		} catch (err) {
			error = err instanceof Error ? err.message : 'Unable to load library data.';
		} finally {
			isLoading = false;
		}
	}

	async function addBook() {
		if (!newTitle.trim()) {
			error = 'Book title is required.';
			return;
		}
		error = '';
		success = '';
		try {
			await createBook({
				title: newTitle.trim(),
				author: newAuthor.trim() || undefined,
				isbn: newIsbn.trim() || undefined,
				total_copies: newCopies
			});
			success = 'Book added to the library.';
			showAddForm = false;
			newTitle = '';
			newAuthor = '';
			newIsbn = '';
			newCopies = 1;
			await loadAll();
		} catch (err) {
			error = err instanceof Error ? err.message : 'Unable to add book.';
		}
	}

	async function removeBook(id: string) {
		error = '';
		success = '';
		try {
			await deleteBook(id);
			success = 'Book removed from the library.';
			await loadAll();
		} catch (err) {
			error = err instanceof Error ? err.message : 'Unable to remove book.';
		}
	}

	const filteredBooks = $derived(
		searchQuery
			? books.filter((b) =>
					`${b.title} ${b.author} ${b.isbn || ''}`.toLowerCase().includes(searchQuery.toLowerCase())
				)
			: books
	);

	function fmtDate(value: string | null | undefined): string {
		if (!value) return '—';
		const d = new Date(value);
		if (isNaN(d.getTime())) return value;
		return d.toLocaleDateString();
	}

	$effect(() => {
		loadAll();
	});
</script>

<div class="library-page">
	<div class="page-header">
		<div class="title-section">
			<div class="title-icon">
				<LibraryIcon size={26} />
			</div>
			<div>
				<h1>Library Management</h1>
				<p>Manage books, borrowed items and overdue returns</p>
			</div>
		</div>
		<div class="header-actions">
			<div class="search-box">
				<Search size={17} />
				<input type="text" placeholder="Search books..." bind:value={searchQuery} />
			</div>
			<button class="refresh-btn" type="button" onclick={loadAll}><RefreshCw size={15} /> Refresh</button>
			<button class="add-btn" type="button" onclick={() => (showAddForm = !showAddForm)}>
				<Plus size={16} /> Add Book
			</button>
		</div>
	</div>

	{#if error}
		<div class="error-box">{error}</div>
	{/if}
	{#if success}
		<div class="success-box">{success}</div>
	{/if}

	{#if showAddForm}
		<section class="card add-card">
			<h2>Add a New Book</h2>
			<div class="form-grid">
				<div class="form-group">
					<label>Title</label>
					<input type="text" bind:value={newTitle} placeholder="Book title" />
				</div>
				<div class="form-group">
					<label>Author</label>
					<input type="text" bind:value={newAuthor} placeholder="Author name" />
				</div>
				<div class="form-group">
					<label>ISBN</label>
					<input type="text" bind:value={newIsbn} placeholder="ISBN (optional)" />
				</div>
				<div class="form-group">
					<label>Copies</label>
					<input type="number" bind:value={newCopies} min={1} />
				</div>
			</div>
			<button class="primary-btn" type="button" onclick={addBook}>Add Book</button>
		</section>
	{/if}

	<div class="summary-grid">
		<div class="summary-card">
			<div class="summary-icon"><BookOpen size={20} /></div>
			<div><span>Total Titles</span><strong>{stats?.total_books ?? '—'}</strong></div>
		</div>
		<div class="summary-card">
			<div class="summary-icon available-icon"><BookOpen size={20} /></div>
			<div><span>Available Copies</span><strong>{stats?.available_copies ?? '—'}</strong></div>
		</div>
		<div class="summary-card">
			<div class="summary-icon issued-icon"><BookOpen size={20} /></div>
			<div><span>Issued Books</span><strong>{stats?.issued_books ?? '—'}</strong></div>
		</div>
		<div class="summary-card">
			<div class="summary-icon overdue-icon"><AlertCircle size={20} /></div>
			<div><span>Overdue</span><strong>{stats?.overdue_books ?? '—'}</strong></div>
		</div>
	</div>

	<section class="card">
		<h2>Catalog ({filteredBooks.length})</h2>
		{#if isLoading}
			<p class="empty">Loading...</p>
		{:else if filteredBooks.length === 0}
			<p class="empty">No books in the library catalog.</p>
		{:else}
			<table class="data-table">
				<thead>
					<tr>
						<th>Title</th>
						<th>Author</th>
						<th>ISBN</th>
						<th>Copies</th>
						<th>Available</th>
						<th></th>
					</tr>
				</thead>
				<tbody>
					{#each filteredBooks as book}
						<tr>
							<td><strong>{book.title}</strong></td>
							<td>{book.author || '—'}</td>
							<td>{book.isbn || '—'}</td>
							<td>{book.total_copies ?? 0}</td>
							<td>
								<span class="availability {(book.available_copies ?? 0) > 0 ? 'in' : 'out'}">
									{(book.available_copies ?? 0) > 0 ? 'In stock' : 'Out of stock'}
								</span>
							</td>
							<td>
								<button class="delete-btn" type="button" onclick={() => removeBook(book.id)}>
									<Trash2 size={14} />
								</button>
							</td>
						</tr>
					{/each}
				</tbody>
			</table>
		{/if}
	</section>

	<section class="card">
		<h2>Currently Issued</h2>
		{#if isLoading}
			<p class="empty">Loading...</p>
		{:else if borrowed.length === 0}
			<p class="empty">No books are currently issued.</p>
		{:else}
			<table class="data-table">
				<thead>
					<tr>
						<th>Book</th>
						<th>Student</th>
						<th>Issued</th>
						<th>Due</th>
						<th>Status</th>
					</tr>
				</thead>
				<tbody>
					{#each borrowed as tx}
						<tr>
							<td>{tx.book_title || '—'}</td>
							<td>{tx.student_name || tx.student_roll || '—'}</td>
							<td>{fmtDate(tx.issue_date)}</td>
							<td>{fmtDate(tx.due_date)}</td>
							<td>
								<span class="availability {(tx.days_overdue ?? 0) > 0 ? 'out' : 'in'}">
									{(tx.days_overdue ?? 0) > 0 ? `${tx.days_overdue}d overdue` : 'Issued'}
								</span>
							</td>
						</tr>
					{/each}
				</tbody>
			</table>
		{/if}
	</section>

	<section class="card">
		<h2>Overdue Books ({overdue.length})</h2>
		{#if isLoading}
			<p class="empty">Loading...</p>
		{:else if overdue.length === 0}
			<p class="empty">No overdue books. Great job!</p>
		{:else}
			<table class="data-table">
				<thead>
					<tr>
						<th>Book</th>
						<th>Student</th>
						<th>Due</th>
						<th>Days Overdue</th>
						<th>Fine</th>
					</tr>
				</thead>
				<tbody>
					{#each overdue as tx}
						<tr>
							<td>{tx.book_title || '—'}</td>
							<td>{tx.student_name || tx.student_roll || '—'}</td>
							<td>{fmtDate(tx.due_date)}</td>
							<td>{tx.days_overdue ?? 0}</td>
							<td>₹{tx.fine ?? 0}</td>
						</tr>
					{/each}
				</tbody>
			</table>
		{/if}
	</section>
</div>

<style>
	.library-page {
		min-height: 100vh;
		padding: 36px;
		box-sizing: border-box;
		background: #f8fafc;
	}

	.page-header {
		display: flex;
		align-items: center;
		justify-content: space-between;
		gap: 20px;
		margin-bottom: 24px;
		flex-wrap: wrap;
	}

	.title-section {
		display: flex;
		align-items: center;
		gap: 14px;
	}

	.title-icon {
		display: flex;
		align-items: center;
		justify-content: center;
		width: 50px;
		height: 50px;
		color: #2563eb;
		background: #eff6ff;
		border-radius: 13px;
	}

	.page-header h1 {
		margin: 0;
		color: #0f172a;
		font-size: 28px;
		font-weight: 800;
	}

	.page-header p {
		margin: 5px 0 0;
		color: #64748b;
		font-size: 13px;
	}

	.header-actions {
		display: flex;
		align-items: center;
		gap: 10px;
		flex-wrap: wrap;
	}

	.search-box {
		display: flex;
		align-items: center;
		gap: 9px;
		width: 240px;
		padding: 10px 13px;
		box-sizing: border-box;
		color: #64748b;
		background: white;
		border: 1px solid #e2e8f0;
		border-radius: 10px;
	}

	.search-box input {
		width: 100%;
		padding: 0;
		color: #0f172a;
		background: transparent;
		border: none;
		outline: none;
		font-size: 12px;
	}

	.refresh-btn,
	.add-btn {
		display: flex;
		align-items: center;
		gap: 6px;
		padding: 10px 14px;
		border-radius: 10px;
		font-size: 13px;
		font-weight: 600;
		cursor: pointer;
	}

	.refresh-btn {
		border: 1px solid #e2e8f0;
		background: white;
		color: #334155;
	}

	.add-btn {
		border: none;
		background: #2563eb;
		color: white;
	}

	.primary-btn {
		padding: 10px 18px;
		border: none;
		border-radius: 10px;
		background: #2563eb;
		color: white;
		font-size: 13px;
		font-weight: 600;
		cursor: pointer;
	}

	.error-box {
		padding: 12px 16px;
		margin-bottom: 16px;
		background: #fef2f2;
		border: 1px solid #fecaca;
		border-radius: 10px;
		color: #b91c1c;
		font-size: 13px;
	}

	.success-box {
		padding: 12px 16px;
		margin-bottom: 16px;
		background: #f0fdf4;
		border: 1px solid #bbf7d0;
		border-radius: 10px;
		color: #15803d;
		font-size: 13px;
	}

	.card {
		padding: 24px;
		background: white;
		border: 1px solid #e2e8f0;
		border-radius: 16px;
		margin-bottom: 20px;
	}

	.card h2 {
		margin: 0 0 16px;
		color: #0f172a;
		font-size: 17px;
		font-weight: 700;
	}

	.add-card {
		border-color: #bfdbfe;
		background: #f8faff;
	}

	.form-grid {
		display: grid;
		grid-template-columns: repeat(4, 1fr);
		gap: 14px;
		margin-bottom: 16px;
	}

	.form-group {
		display: flex;
		flex-direction: column;
		gap: 7px;
	}

	.form-group label {
		color: #0f172a;
		font-size: 13px;
		font-weight: 600;
	}

	.form-group input {
		height: 44px;
		padding: 0 12px;
		border: 1px solid #cbd5e1;
		border-radius: 10px;
		background: white;
		color: #0f172a;
		font-size: 13px;
		outline: none;
	}

	.summary-grid {
		display: grid;
		grid-template-columns: repeat(4, 1fr);
		gap: 16px;
		margin-bottom: 20px;
	}

	.summary-card {
		display: flex;
		align-items: center;
		gap: 14px;
		padding: 20px;
		background: white;
		border: 1px solid #e2e8f0;
		border-radius: 15px;
	}

	.summary-icon {
		display: flex;
		align-items: center;
		justify-content: center;
		width: 44px;
		height: 44px;
		border-radius: 11px;
		flex-shrink: 0;
		color: #2563eb;
		background: #eff6ff;
	}

	.available-icon {
		color: #16a34a;
		background: #f0fdf4;
	}

	.issued-icon {
		color: #d97706;
		background: #fffbeb;
	}

	.overdue-icon {
		color: #dc2626;
		background: #fef2f2;
	}

	.summary-card span {
		display: block;
		margin-bottom: 5px;
		color: #64748b;
		font-size: 11px;
	}

	.summary-card strong {
		color: #0f172a;
		font-size: 22px;
		font-weight: 800;
	}

	.data-table {
		width: 100%;
		border-collapse: collapse;
		font-size: 12px;
	}

	.data-table th,
	.data-table td {
		padding: 11px 12px;
		text-align: left;
		border-bottom: 1px solid #e2e8f0;
	}

	.data-table th {
		color: #64748b;
		font-size: 11px;
		text-transform: uppercase;
		letter-spacing: 0.4px;
	}

	.data-table td {
		color: #334155;
	}

	.data-table td strong {
		color: #0f172a;
	}

	.availability {
		padding: 4px 10px;
		border-radius: 20px;
		font-size: 11px;
		font-weight: 700;
	}

	.availability.in {
		background: #dcfce7;
		color: #15803d;
	}

	.availability.out {
		background: #fee2e2;
		color: #b91c1c;
	}

	.delete-btn {
		display: flex;
		align-items: center;
		justify-content: center;
		padding: 6px;
		border: 1px solid #fecaca;
		border-radius: 7px;
		background: white;
		color: #dc2626;
		cursor: pointer;
	}

	.empty {
		color: #94a3b8;
		font-size: 13px;
		text-align: center;
		padding: 24px 0;
	}

	@media (max-width: 900px) {
		.library-page {
			padding: 18px;
		}

		.summary-grid,
		.form-grid {
			grid-template-columns: repeat(2, 1fr);
		}

		.search-box {
			width: 100%;
		}
	}
</style>