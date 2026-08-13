<script lang="ts">
    import {
        Library as LibraryIcon,
        BookOpen,
        BookMarked,
        RotateCcw,
        CalendarDays,
        AlertCircle,
        Search
    } from '@lucide/svelte';
</script>

<svelte:head>
    <title>Library | PaperBuddy</title>
</svelte:head>

<div class="library-page">
    <!-- =========================
         PAGE HEADER
         ========================= -->

    <div class="page-header">
        <div>
            <h1>Library</h1>
            <p>View your borrowed books and library activity.</p>
        </div>

        <div class="search-box">
            <Search size={17} />

            <input
                type="text"
                placeholder="Search books..."
                aria-label="Search books"
            />
        </div>
    </div>

    <!-- =========================
         SUMMARY CARDS
         ========================= -->

    <div class="summary-grid">
        <div class="summary-card">
            <div class="summary-icon">
                <BookOpen size={21} />
            </div>

            <div>
                <span>Borrowed Books</span>
                <strong>—</strong>
            </div>
        </div>

        <div class="summary-card">
            <div class="summary-icon returned-icon">
                <RotateCcw size={21} />
            </div>

            <div>
                <span>Returned Books</span>
                <strong>—</strong>
            </div>
        </div>

        <div class="summary-card">
            <div class="summary-icon due-icon">
                <CalendarDays size={21} />
            </div>

            <div>
                <span>Due Books</span>
                <strong>—</strong>
            </div>
        </div>

        <div class="summary-card">
            <div class="summary-icon overdue-icon">
                <AlertCircle size={21} />
            </div>

            <div>
                <span>Overdue Books</span>
                <strong>—</strong>
            </div>
        </div>
    </div>

    <!-- =========================
         CURRENTLY BORROWED
         ========================= -->

    <section class="library-card">
        <div class="card-header">
            <div>
                <h2>Currently Borrowed</h2>
                <p>Books currently issued to you.</p>
            </div>
        </div>

        <div class="empty-state">
            <div class="empty-icon">
                <BookMarked size={30} />
            </div>

            <h3>No borrowed books</h3>

            <p>
                Your currently borrowed books will appear here when
                library records are available.
            </p>
        </div>
    </section>

    <!-- =========================
         LIBRARY ACTIVITY
         ========================= -->

    <section class="library-card">
        <div class="card-header">
            <div>
                <h2>Library Activity</h2>
                <p>Your book issue and return information.</p>
            </div>
        </div>

        <div class="empty-state">
            <div class="empty-icon activity-icon">
                <LibraryIcon size={30} />
            </div>

            <h3>No library activity available</h3>

            <p>
                Your library activity, due dates and fines will appear
                here when records are available.
            </p>
        </div>
    </section>
</div>

<style>
    .library-page {
        min-height: 100vh;
        padding: 36px;
        box-sizing: border-box;
        background: #f8fafc;
    }

    /* =========================
       PAGE HEADER
       ========================= */

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

    /* =========================
       SUMMARY CARDS
       ========================= */

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

    /* =========================
       LIBRARY CARDS
       ========================= */

    .library-card {
        min-height: 360px;
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

    /* =========================
       EMPTY STATE
       ========================= */

    .empty-state {
        display: flex;
        align-items: center;
        flex-direction: column;
        justify-content: center;
        min-height: 260px;
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

    /* =========================
       RESPONSIVE
       ========================= */

    @media (max-width: 1100px) {
        .library-page {
            padding: 24px;
        }

        .summary-grid {
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

        .summary-grid {
            grid-template-columns: 1fr;
        }

        .library-card {
            padding: 18px;
        }
    }
</style>