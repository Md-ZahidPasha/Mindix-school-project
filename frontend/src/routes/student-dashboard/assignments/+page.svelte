<script lang="ts">
    import {
        ClipboardCheck,
        CalendarDays,
        Clock,
        FileText,
        Search
    } from '@lucide/svelte';
</script>

<svelte:head>
    <title>Assignments | PaperBuddy</title>
</svelte:head>

<div class="assignments-page">
    <!-- =========================
         PAGE HEADER
         ========================= -->

    <div class="page-header">
        <div>
            <h1>Assignments</h1>
            <p>View and manage your academic assignments.</p>
        </div>

        <div class="search-box">
            <Search size={17} />
            <input
                type="text"
                placeholder="Search assignments..."
                aria-label="Search assignments"
            />
        </div>
    </div>

    <!-- =========================
         SUMMARY
         ========================= -->

    <div class="summary-grid">
        <div class="summary-card">
            <div class="summary-icon">
                <ClipboardCheck size={21} />
            </div>

            <div>
                <span>Total Assignments</span>
                <strong>—</strong>
            </div>
        </div>

        <div class="summary-card">
            <div class="summary-icon pending-icon">
                <Clock size={21} />
            </div>

            <div>
                <span>Pending</span>
                <strong>—</strong>
            </div>
        </div>

        <div class="summary-card">
            <div class="summary-icon completed-icon">
                <FileText size={21} />
            </div>

            <div>
                <span>Completed</span>
                <strong>—</strong>
            </div>
        </div>

        <div class="summary-card">
            <div class="summary-icon due-icon">
                <CalendarDays size={21} />
            </div>

            <div>
                <span>Upcoming Due</span>
                <strong>—</strong>
            </div>
        </div>
    </div>

    <!-- =========================
         ASSIGNMENTS
         ========================= -->

    <section class="assignments-card">
        <div class="card-header">
            <div>
                <h2>My Assignments</h2>
                <p>Assignments assigned to your class.</p>
            </div>

            <div class="filter">
                <span>All</span>
            </div>
        </div>

        <div class="empty-state">
            <div class="empty-icon">
                <ClipboardCheck size={30} />
            </div>

            <h3>No assignments available</h3>

            <p>
                Your assignments will appear here when they are assigned
                by your teachers.
            </p>
        </div>
    </section>
</div>

<style>
    .assignments-page {
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

    .pending-icon {
        color: #d97706;
        background: #fffbeb;
    }

    .completed-icon {
        color: #16a34a;
        background: #f0fdf4;
    }

    .due-icon {
        color: #7c3aed;
        background: #f5f3ff;
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
       ASSIGNMENTS CARD
       ========================= */

    .assignments-card {
        min-height: 420px;
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

    .filter {
        padding: 8px 14px;
        color: #2563eb;
        background: #eff6ff;
        border-radius: 8px;
        font-size: 11px;
        font-weight: 700;
    }

    /* =========================
       EMPTY STATE
       ========================= */

    .empty-state {
        display: flex;
        align-items: center;
        flex-direction: column;
        justify-content: center;
        min-height: 320px;
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
        .assignments-page {
            padding: 24px;
        }

        .summary-grid {
            grid-template-columns: repeat(2, 1fr);
        }
    }

    @media (max-width: 700px) {
        .assignments-page {
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

        .assignments-card {
            padding: 18px;
        }
    }
</style>