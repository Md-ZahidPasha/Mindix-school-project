<script lang="ts">
    import {
        FileText,
        GraduationCap,
        Trophy,
        BarChart3,
        CalendarDays,
        Search
    } from '@lucide/svelte';
</script>

<svelte:head>
    <title>Exams & Results | PaperBuddy</title>
</svelte:head>

<div class="exams-page">
    <!-- =========================
         PAGE HEADER
         ========================= -->

    <div class="page-header">
        <div>
            <h1>Exams & Results</h1>
            <p>View your upcoming examinations and academic results.</p>
        </div>

        <div class="search-box">
            <Search size={17} />

            <input
                type="text"
                placeholder="Search exams..."
                aria-label="Search exams"
            />
        </div>
    </div>

    <!-- =========================
         SUMMARY CARDS
         ========================= -->

    <div class="summary-grid">
        <div class="summary-card">
            <div class="summary-icon">
                <FileText size={21} />
            </div>

            <div>
                <span>Total Exams</span>
                <strong>—</strong>
            </div>
        </div>

        <div class="summary-card">
            <div class="summary-icon upcoming-icon">
                <CalendarDays size={21} />
            </div>

            <div>
                <span>Upcoming Exams</span>
                <strong>—</strong>
            </div>
        </div>

        <div class="summary-card">
            <div class="summary-icon result-icon">
                <GraduationCap size={21} />
            </div>

            <div>
                <span>Results Available</span>
                <strong>—</strong>
            </div>
        </div>

        <div class="summary-card">
            <div class="summary-icon percentage-icon">
                <BarChart3 size={21} />
            </div>

            <div>
                <span>Latest Percentage</span>
                <strong>—</strong>
            </div>
        </div>
    </div>

    <!-- =========================
         UPCOMING EXAMS
         ========================= -->

    <section class="exams-card">
        <div class="card-header">
            <div>
                <h2>Upcoming Exams</h2>
                <p>Your scheduled examinations.</p>
            </div>

            <div class="filter">
                All Exams
            </div>
        </div>

        <div class="empty-state">
            <div class="empty-icon">
                <CalendarDays size={30} />
            </div>

            <h3>No upcoming exams</h3>

            <p>
                Upcoming examination details will appear here when they
                are available.
            </p>
        </div>
    </section>

    <!-- =========================
         RESULTS
         ========================= -->

    <section class="exams-card">
        <div class="card-header">
            <div>
                <h2>Results</h2>
                <p>View your examination results and performance.</p>
            </div>
        </div>

        <div class="empty-state">
            <div class="empty-icon result-empty-icon">
                <Trophy size={30} />
            </div>

            <h3>No results available</h3>

            <p>
                Your examination results will appear here after they are
                published by the institution.
            </p>
        </div>
    </section>
</div>

<style>
    .exams-page {
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

    .upcoming-icon {
        color: #d97706;
        background: #fffbeb;
    }

    .result-icon {
        color: #16a34a;
        background: #f0fdf4;
    }

    .percentage-icon {
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
       EXAMS CARDS
       ========================= */

    .exams-card {
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

    .result-empty-icon {
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
        .exams-page {
            padding: 24px;
        }

        .summary-grid {
            grid-template-columns: repeat(2, 1fr);
        }
    }

    @media (max-width: 700px) {
        .exams-page {
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

        .exams-card {
            padding: 18px;
        }
    }
</style>