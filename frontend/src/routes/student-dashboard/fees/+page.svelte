<script lang="ts">
    import {
        CreditCard,
        Wallet,
        Clock,
        CalendarDays,
        Receipt,
        Search
    } from '@lucide/svelte';
</script>

<svelte:head>
    <title>Fees & Payments | PaperBuddy</title>
</svelte:head>

<div class="fees-page">
    <!-- =========================
         PAGE HEADER
         ========================= -->

    <div class="page-header">
        <div>
            <h1>Fees & Payments</h1>
            <p>View your fee details and payment history.</p>
        </div>

        <div class="search-box">
            <Search size={17} />

            <input
                type="text"
                placeholder="Search payments..."
                aria-label="Search payments"
            />
        </div>
    </div>

    <!-- =========================
         SUMMARY CARDS
         ========================= -->

    <div class="summary-grid">
        <div class="summary-card">
            <div class="summary-icon">
                <Wallet size={21} />
            </div>

            <div>
                <span>Total Fees</span>
                <strong>—</strong>
            </div>
        </div>

        <div class="summary-card">
            <div class="summary-icon paid-icon">
                <CreditCard size={21} />
            </div>

            <div>
                <span>Paid</span>
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
            <div class="summary-icon due-icon">
                <CalendarDays size={21} />
            </div>

            <div>
                <span>Next Due Date</span>
                <strong>—</strong>
            </div>
        </div>
    </div>

    <!-- =========================
         FEE DETAILS
         ========================= -->

    <section class="fees-card">
        <div class="card-header">
            <div>
                <h2>Fee Details</h2>
                <p>Your current fee information.</p>
            </div>
        </div>

        <div class="empty-state">
            <div class="empty-icon">
                <Wallet size={30} />
            </div>

            <h3>No fee information available</h3>

            <p>
                Your fee details will appear here when they are available
                from the institution.
            </p>
        </div>
    </section>

    <!-- =========================
         PAYMENT HISTORY
         ========================= -->

    <section class="fees-card">
        <div class="card-header">
            <div>
                <h2>Payment History</h2>
                <p>View your previous fee payments.</p>
            </div>
        </div>

        <div class="empty-state">
            <div class="empty-icon payment-empty-icon">
                <Receipt size={30} />
            </div>

            <h3>No payment history available</h3>

            <p>
                Your fee payment records will appear here after payments
                are recorded.
            </p>
        </div>
    </section>
</div>

<style>
    .fees-page {
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

    .paid-icon {
        color: #16a34a;
        background: #f0fdf4;
    }

    .pending-icon {
        color: #d97706;
        background: #fffbeb;
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
       FEES CARDS
       ========================= */

    .fees-card {
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

    .payment-empty-icon {
        color: #16a34a;
        background: #f0fdf4;
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
        .fees-page {
            padding: 24px;
        }

        .summary-grid {
            grid-template-columns: repeat(2, 1fr);
        }
    }

    @media (max-width: 700px) {
        .fees-page {
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

        .fees-card {
            padding: 18px;
        }
    }
</style>