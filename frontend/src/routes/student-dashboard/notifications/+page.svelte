<script lang="ts">
    import {
        Bell,
        CheckCircle2,
        AlertCircle,
        Info,
        Search
    } from '@lucide/svelte';
</script>

<svelte:head>
    <title>Notifications | PaperBuddy</title>
</svelte:head>

<div class="notifications-page">
    <!-- =========================
         PAGE HEADER
         ========================= -->

    <div class="page-header">
        <div>
            <h1>Notifications</h1>
            <p>Stay updated with important announcements and alerts.</p>
        </div>

        <div class="search-box">
            <Search size={17} />

            <input
                type="text"
                placeholder="Search notifications..."
                aria-label="Search notifications"
            />
        </div>
    </div>

    <!-- =========================
         SUMMARY
         ========================= -->

    <div class="summary-grid">
        <div class="summary-card">
            <div class="summary-icon">
                <Bell size={21} />
            </div>

            <div>
                <span>Total Notifications</span>
                <strong>—</strong>
            </div>
        </div>

        <div class="summary-card">
            <div class="summary-icon unread-icon">
                <AlertCircle size={21} />
            </div>

            <div>
                <span>Unread</span>
                <strong>—</strong>
            </div>
        </div>

        <div class="summary-card">
            <div class="summary-icon read-icon">
                <CheckCircle2 size={21} />
            </div>

            <div>
                <span>Read</span>
                <strong>—</strong>
            </div>
        </div>
    </div>

    <!-- =========================
         NOTIFICATIONS
         ========================= -->

    <section class="notifications-card">
        <div class="card-header">
            <div>
                <h2>All Notifications</h2>
                <p>Your latest school notifications.</p>
            </div>

            <button class="mark-button" type="button">
                Mark all as read
            </button>
        </div>

        <div class="empty-state">
            <div class="empty-icon">
                <Bell size={30} />
            </div>

            <h3>No notifications available</h3>

            <p>
                Your school notifications and important announcements
                will appear here.
            </p>
        </div>
    </section>

    <!-- =========================
         INFORMATION
         ========================= -->

    <section class="info-card">
        <div class="info-icon">
            <Info size={21} />
        </div>

        <div>
            <h3>Stay Updated</h3>

            <p>
                Important information from your school will be displayed
                in this section when notifications are available.
            </p>
        </div>
    </section>
</div>

<style>
    .notifications-page {
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
        grid-template-columns: repeat(3, 1fr);
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

    .unread-icon {
        color: #dc2626;
        background: #fef2f2;
    }

    .read-icon {
        color: #16a34a;
        background: #f0fdf4;
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
       NOTIFICATIONS CARD
       ========================= */

    .notifications-card {
        min-height: 400px;
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

    .mark-button {
        padding: 8px 13px;
        color: #2563eb;
        background: #eff6ff;
        border: none;
        border-radius: 8px;
        font-size: 11px;
        font-weight: 700;
        cursor: pointer;
    }

    .mark-button:hover {
        background: #dbeafe;
    }

    /* =========================
       EMPTY STATE
       ========================= */

    .empty-state {
        display: flex;
        align-items: center;
        flex-direction: column;
        justify-content: center;
        min-height: 290px;
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
       INFORMATION CARD
       ========================= */

    .info-card {
        display: flex;
        align-items: center;
        gap: 15px;
        padding: 20px;
        background: #eff6ff;
        border: 1px solid #dbeafe;
        border-radius: 14px;
    }

    .info-icon {
        display: flex;
        align-items: center;
        justify-content: center;
        width: 44px;
        height: 44px;
        flex-shrink: 0;
        color: #2563eb;
        background: white;
        border-radius: 11px;
    }

    .info-card h3 {
        margin: 0;
        color: #1e3a8a;
        font-size: 13px;
        font-weight: 700;
    }

    .info-card p {
        margin: 5px 0 0;
        color: #64748b;
        font-size: 11px;
        line-height: 1.5;
    }

    /* =========================
       RESPONSIVE
       ========================= */

    @media (max-width: 1100px) {
        .notifications-page {
            padding: 24px;
        }

        .summary-grid {
            grid-template-columns: 1fr;
        }
    }

    @media (max-width: 700px) {
        .notifications-page {
            padding: 18px;
        }

        .page-header {
            align-items: flex-start;
            flex-direction: column;
        }

        .search-box {
            width: 100%;
        }

        .notifications-card {
            padding: 18px;
        }

        .card-header {
            align-items: flex-start;
            flex-direction: column;
        }
    }
</style>