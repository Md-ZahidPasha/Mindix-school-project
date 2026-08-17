<script lang="ts">
    import {
        Library as LibraryIcon,
        BookOpen,
        BookMarked,
        RotateCcw,
        CalendarDays,
        AlertCircle,
        Search,
        LibraryBig
    } from '@lucide/svelte';
    import {
        getBooks,
        getBorrowed,
        getLibraryHistory,
        borrowBook,
        returnBook,
        type Book,
        type Transaction
    } from '$lib/services/library';

    let books = $state<Book[]>([]);
    let borrowed = $state<Transaction[]>([]);
    let history = $state<Transaction[]>([]);
    let searchQuery = $state('');
    let isLoading = $state(true);
    let error = $state('');
    let success = $state('');

    async function loadAll() {
        isLoading = true;
        error = '';
        try {
            const [booksResult, borrowedResult, historyResult] = await Promise.all([
                getBooks(),
                getBorrowed(),
                getLibraryHistory()
            ]);
            books = booksResult;
            borrowed = borrowedResult;
            history = historyResult;
        } catch (err) {
            error = err instanceof Error ? err.message : 'Unable to load library data.';
        } finally {
            isLoading = false;
        }
    }

    async function doBorrow(bookId: string) {
        error = '';
        success = '';
        try {
            await borrowBook('', bookId);
            success = 'Book borrowed successfully.';
            await loadAll();
        } catch (err) {
            error = err instanceof Error ? err.message : 'Unable to borrow book.';
        }
    }

    async function doReturn(transactionId: string) {
        error = '';
        success = '';
        try {
            await returnBook(transactionId);
            success = 'Book returned successfully.';
            await loadAll();
        } catch (err) {
            error = err instanceof Error ? err.message : 'Unable to return book.';
        }
    }

    const filteredBooks = $derived(
        searchQuery
            ? books.filter((b) =>
                  `${b.title} ${b.author} ${b.isbn || ''}`
                      .toLowerCase()
                      .includes(searchQuery.toLowerCase())
              )
            : books
    );

    const returnedCount = $derived(history.filter((h) => (h.status || '').toLowerCase() === 'returned').length);
    const overdueCount = $derived(borrowed.filter((h) => (h.days_overdue ?? 0) > 0).length);

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

<svelte:head>
    <title>Library | PaperBuddy</title>
</svelte:head>

<div class="library-page">
    <div class="page-header">
        <div>
            <h1>Library</h1>
            <p>Browse books, borrow and return from the digital library.</p>
        </div>

        <div class="search-box">
            <Search size={17} />
            <input
                type="text"
                placeholder="Search books..."
                aria-label="Search books"
                bind:value={searchQuery}
            />
        </div>
    </div>

    {#if error}
        <div class="alert error-alert">{error}</div>
    {/if}
    {#if success}
        <div class="alert success-alert">{success}</div>
    {/if}

    <div class="summary-grid">
        <div class="summary-card">
            <div class="summary-icon">
                <BookOpen size={21} />
            </div>
            <div>
                <span>Borrowed Books</span>
                <strong>{borrowed.length}</strong>
            </div>
        </div>

        <div class="summary-card">
            <div class="summary-icon returned-icon">
                <RotateCcw size={21} />
            </div>
            <div>
                <span>Returned Books</span>
                <strong>{returnedCount}</strong>
            </div>
        </div>

        <div class="summary-card">
            <div class="summary-icon due-icon">
                <CalendarDays size={21} />
            </div>
            <div>
                <span>Available Titles</span>
                <strong>{books.filter((b) => (b.available_copies ?? 0) > 0).length}</strong>
            </div>
        </div>

        <div class="summary-card">
            <div class="summary-icon overdue-icon">
                <AlertCircle size={21} />
            </div>
            <div>
                <span>Overdue Books</span>
                <strong>{overdueCount}</strong>
            </div>
        </div>
    </div>

    <section class="library-card">
        <div class="card-header">
            <div>
                <h2>Available Books</h2>
                <p>Books you can borrow from the library.</p>
            </div>
        </div>

        {#if isLoading}
            <p class="muted">Loading...</p>
        {:else if filteredBooks.length === 0}
            <div class="empty-state">
                <div class="empty-icon">
                    <LibraryBig size={30} />
                </div>
                <h3>No books found</h3>
                <p>{searchQuery ? 'Try a different search term.' : 'No books are available in the library yet.'}</p>
            </div>
        {:else}
            <div class="book-grid">
                {#each filteredBooks as book}
                    <div class="book-card">
                        <div class="book-cover">
                            <BookMarked size={22} />
                        </div>
                        <div class="book-body">
                            <strong>{book.title}</strong>
                            <span class="book-author">{book.author || 'Unknown author'}</span>
                            {#if book.isbn}
                                <span class="book-isbn">ISBN: {book.isbn}</span>
                            {/if}
                            <span class="book-copies">
                                {(book.available_copies ?? 0)} / {(book.total_copies ?? 0)} available
                            </span>
                        </div>
                        <button
                            class="borrow-btn"
                            type="button"
                            disabled={(book.available_copies ?? 0) <= 0}
                            onclick={() => doBorrow(book.id)}
                        >
                            {(book.available_copies ?? 0) > 0 ? 'Borrow' : 'Unavailable'}
                        </button>
                    </div>
                {/each}
            </div>
        {/if}
    </section>

    <section class="library-card">
        <div class="card-header">
            <div>
                <h2>Currently Borrowed</h2>
                <p>Books currently issued to you.</p>
            </div>
        </div>

        {#if isLoading}
            <p class="muted">Loading...</p>
        {:else if borrowed.length === 0}
            <div class="empty-state">
                <div class="empty-icon">
                    <BookMarked size={30} />
                </div>
                <h3>No borrowed books</h3>
                <p>Books you borrow will appear here.</p>
            </div>
        {:else}
            <div class="transaction-list">
                {#each borrowed as tx}
                    <div class="transaction-item">
                        <div class="tx-icon">
                            <BookOpen size={19} />
                        </div>
                        <div class="tx-info">
                            <strong>{tx.book_title || 'Book'}</strong>
                            <span>Issued: {fmtDate(tx.issue_date)} · Due: {fmtDate(tx.due_date)}</span>
                            {#if (tx.days_overdue ?? 0) > 0}
                                <span class="overdue-label">{(tx.days_overdue)} day(s) overdue</span>
                            {/if}
                        </div>
                        <button class="return-btn" type="button" onclick={() => doReturn(tx.id)}>
                            Return
                        </button>
                    </div>
                {/each}
            </div>
        {/if}
    </section>

    <section class="library-card">
        <div class="card-header">
            <div>
                <h2>Library Activity</h2>
                <p>Your book issue and return information.</p>
            </div>
        </div>

        {#if isLoading}
            <p class="muted">Loading...</p>
        {:else if history.length === 0}
            <div class="empty-state">
                <div class="empty-icon activity-icon">
                    <LibraryIcon size={30} />
                </div>
                <h3>No library activity available</h3>
                <p>Your issue and return records will appear here.</p>
            </div>
        {:else}
            <table class="history-table">
                <thead>
                    <tr>
                        <th>Book</th>
                        <th>Issued</th>
                        <th>Due</th>
                        <th>Returned</th>
                        <th>Status</th>
                    </tr>
                </thead>
                <tbody>
                    {#each history as tx}
                        <tr>
                            <td>{tx.book_title || '—'}</td>
                            <td>{fmtDate(tx.issue_date)}</td>
                            <td>{fmtDate(tx.due_date)}</td>
                            <td>{fmtDate(tx.return_date)}</td>
                            <td>
                                <span class="status-pill status-{(tx.status || 'issued').toLowerCase()}">
                                    {(tx.status || 'issued').toUpperCase()}
                                </span>
                            </td>
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
        margin-bottom: 28px;
    }

    .page-header h1 {
        margin: 0;
        color: #0f172a;
        font-size: 30px;
        font-weight: 800;
    }

    .page-header p {
        margin: 7px 0 0;
        color: #64748b;
        font-size: 13px;
    }

    .search-box {
        display: flex;
        align-items: center;
        gap: 9px;
        width: 250px;
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

    .search-box input::placeholder {
        color: #94a3b8;
    }

    .alert {
        padding: 12px 16px;
        margin-bottom: 16px;
        border-radius: 10px;
        font-size: 13px;
        font-weight: 500;
    }

    .error-alert {
        background: #fef2f2;
        border: 1px solid #fecaca;
        color: #b91c1c;
    }

    .success-alert {
        background: #f0fdf4;
        border: 1px solid #bbf7d0;
        color: #15803d;
    }

    .muted {
        color: #94a3b8;
        font-size: 13px;
        text-align: center;
        padding: 24px 0;
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
        box-shadow: 0 5px 18px rgba(15, 23, 42, 0.04);
    }

    .summary-icon {
        display: flex;
        align-items: center;
        justify-content: center;
        width: 44px;
        height: 44px;
        flex-shrink: 0;
        color: #2563eb;
        background: #eff6ff;
        border-radius: 11px;
    }

    .returned-icon {
        color: #16a34a;
        background: #f0fdf4;
    }

    .due-icon {
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

    .library-card {
        margin-bottom: 20px;
        padding: 24px;
        background: white;
        border: 1px solid #e2e8f0;
        border-radius: 16px;
        box-shadow: 0 5px 18px rgba(15, 23, 42, 0.04);
    }

    .card-header {
        display: flex;
        align-items: center;
        justify-content: space-between;
        gap: 15px;
        margin-bottom: 20px;
    }

    .card-header h2 {
        margin: 0;
        color: #0f172a;
        font-size: 17px;
        font-weight: 800;
    }

    .card-header p {
        margin: 5px 0 0;
        color: #64748b;
        font-size: 11px;
    }

    .book-grid {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 14px;
    }

    .book-card {
        display: flex;
        align-items: center;
        gap: 12px;
        padding: 14px;
        border: 1px solid #e2e8f0;
        border-radius: 12px;
        background: #f8fafc;
    }

    .book-cover {
        display: flex;
        align-items: center;
        justify-content: center;
        width: 46px;
        height: 60px;
        flex-shrink: 0;
        color: white;
        background: linear-gradient(135deg, #2563eb, #7c3aed);
        border-radius: 8px;
    }

    .book-body {
        flex: 1;
        display: flex;
        flex-direction: column;
        gap: 3px;
        min-width: 0;
    }

    .book-body strong {
        color: #0f172a;
        font-size: 13px;
        white-space: nowrap;
        overflow: hidden;
        text-overflow: ellipsis;
    }

    .book-author,
    .book-isbn,
    .book-copies {
        color: #64748b;
        font-size: 11px;
    }

    .borrow-btn {
        padding: 8px 12px;
        border: none;
        border-radius: 8px;
        background: #2563eb;
        color: white;
        font-size: 12px;
        font-weight: 600;
        cursor: pointer;
        flex-shrink: 0;
    }

    .borrow-btn:disabled {
        background: #cbd5e1;
        cursor: not-allowed;
    }

    .transaction-list {
        display: flex;
        flex-direction: column;
        gap: 10px;
    }

    .transaction-item {
        display: flex;
        align-items: center;
        gap: 14px;
        padding: 13px 14px;
        border: 1px solid #e2e8f0;
        border-radius: 11px;
        background: #f8fafc;
    }

    .tx-icon {
        display: flex;
        align-items: center;
        justify-content: center;
        width: 40px;
        height: 40px;
        flex-shrink: 0;
        color: #2563eb;
        background: #eff6ff;
        border-radius: 10px;
    }

    .tx-info {
        flex: 1;
        display: flex;
        flex-direction: column;
        gap: 3px;
        min-width: 0;
    }

    .tx-info strong {
        color: #0f172a;
        font-size: 14px;
    }

    .tx-info span {
        color: #64748b;
        font-size: 12px;
    }

    .overdue-label {
        color: #dc2626 !important;
        font-weight: 600;
    }

    .return-btn {
        padding: 8px 12px;
        border: 1px solid #16a34a;
        border-radius: 8px;
        background: white;
        color: #16a34a;
        font-size: 12px;
        font-weight: 600;
        cursor: pointer;
        flex-shrink: 0;
    }

    .history-table {
        width: 100%;
        border-collapse: collapse;
        font-size: 12px;
    }

    .history-table th,
    .history-table td {
        padding: 11px 12px;
        text-align: left;
        border-bottom: 1px solid #e2e8f0;
    }

    .history-table th {
        color: #64748b;
        font-size: 11px;
        text-transform: uppercase;
        letter-spacing: 0.4px;
    }

    .history-table td {
        color: #334155;
    }

    .status-pill {
        padding: 4px 10px;
        border-radius: 20px;
        font-size: 11px;
        font-weight: 700;
    }

    .status-issued {
        background: #eff6ff;
        color: #2563eb;
    }

    .status-returned {
        background: #dcfce7;
        color: #15803d;
    }

    .status-overdue {
        background: #fee2e2;
        color: #b91c1c;
    }

    .empty-state {
        display: flex;
        align-items: center;
        flex-direction: column;
        justify-content: center;
        min-height: 220px;
        padding: 30px 20px;
        text-align: center;
    }

    .empty-icon {
        display: flex;
        align-items: center;
        justify-content: center;
        width: 64px;
        height: 64px;
        color: #2563eb;
        background: #eff6ff;
        border-radius: 16px;
    }

    .activity-icon {
        color: #7c3aed;
        background: #f5f3ff;
    }

    .empty-state h3 {
        margin: 16px 0 7px;
        color: #334155;
        font-size: 15px;
        font-weight: 700;
    }

    .empty-state p {
        max-width: 430px;
        margin: 0;
        color: #94a3b8;
        font-size: 11px;
        line-height: 1.6;
    }

    @media (max-width: 1100px) {
        .library-page {
            padding: 24px;
        }

        .summary-grid {
            grid-template-columns: repeat(2, 1fr);
        }

        .book-grid {
            grid-template-columns: repeat(2, 1fr);
        }
    }

    @media (max-width: 700px) {
        .library-page {
            padding: 18px;
        }

        .page-header {
            align-items: flex-start;
            flex-direction: column;
        }

        .search-box {
            width: 100%;
        }

        .summary-grid,
        .book-grid {
            grid-template-columns: 1fr;
        }

        .library-card {
            padding: 18px;
        }
    }
</style>