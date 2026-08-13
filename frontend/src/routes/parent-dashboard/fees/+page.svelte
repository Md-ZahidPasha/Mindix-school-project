<script lang="ts">
    import {
        WalletCards,
        ChevronDown,
        IndianRupee,
        CheckCircle2,
        Clock3,
        AlertCircle,
        CalendarDays,
        Receipt,
        CreditCard,
        FileText
    } from '@lucide/svelte';

    let selectedChild = $state('Rahul Kumar');
    let activeFilter = $state('All');

    const children = [
        {
            name: 'Rahul Kumar',
            studentId: 'STU001',
            className: '10th',
            section: 'A'
        },
        {
            name: 'Ayesha Kumar',
            studentId: 'STU002',
            className: '7th',
            section: 'B'
        }
    ];

    const feeItems = [
        {
            name: 'Tuition Fee',
            description: 'Academic tuition fee',
            amount: 45000,
            paid: 45000,
            status: 'Paid',
            dueDate: '10 Jun 2026'
        },
        {
            name: 'Library Fee',
            description: 'Annual library charges',
            amount: 3000,
            paid: 3000,
            status: 'Paid',
            dueDate: '10 Jun 2026'
        },
        {
            name: 'Laboratory Fee',
            description: 'Science and computer laboratory',
            amount: 5000,
            paid: 2500,
            status: 'Pending',
            dueDate: '20 Aug 2026'
        },
        {
            name: 'Transport Fee',
            description: 'School transportation charges',
            amount: 12000,
            paid: 6000,
            status: 'Pending',
            dueDate: '25 Aug 2026'
        },
        {
            name: 'Activity Fee',
            description: 'Sports and extracurricular activities',
            amount: 4000,
            paid: 4000,
            status: 'Paid',
            dueDate: '10 Jun 2026'
        },
        {
            name: 'Examination Fee',
            description: 'Annual examination charges',
            amount: 2500,
            paid: 0,
            status: 'Overdue',
            dueDate: '05 Aug 2026'
        }
    ];

    const paymentHistory = [
        {
            receipt: 'REC-2026-00124',
            date: '10 Jun 2026',
            description: 'Tuition Fee',
            method: 'Online Payment',
            amount: 45000,
            status: 'Paid'
        },
        {
            receipt: 'REC-2026-00125',
            date: '10 Jun 2026',
            description: 'Library Fee',
            method: 'Online Payment',
            amount: 3000,
            status: 'Paid'
        },
        {
            receipt: 'REC-2026-00126',
            date: '10 Jun 2026',
            description: 'Activity Fee',
            method: 'UPI',
            amount: 4000,
            status: 'Paid'
        },
        {
            receipt: 'REC-2026-00201',
            date: '15 Jul 2026',
            description: 'Laboratory Fee - Part Payment',
            method: 'UPI',
            amount: 2500,
            status: 'Paid'
        },
        {
            receipt: 'REC-2026-00215',
            date: '20 Jul 2026',
            description: 'Transport Fee - Part Payment',
            method: 'Online Payment',
            amount: 6000,
            status: 'Paid'
        }
    ];

    function getSelectedChild() {
        return children.find(
            (child) => child.name === selectedChild
        );
    }

    let child = $derived(getSelectedChild());

    let totalFees = $derived(
        feeItems.reduce((sum, item) => sum + item.amount, 0)
    );

    let paidFees = $derived(
        feeItems.reduce((sum, item) => sum + item.paid, 0)
    );

    let pendingFees = $derived(
        totalFees - paidFees
    );

    let paidPercentage = $derived(
        totalFees > 0
            ? Math.round((paidFees / totalFees) * 100)
            : 0
    );

    let pendingCount = $derived(
        feeItems.filter(
            (item) => item.status === 'Pending'
        ).length
    );

    let overdueCount = $derived(
        feeItems.filter(
            (item) => item.status === 'Overdue'
        ).length
    );

    let filteredFees = $derived(
        activeFilter === 'All'
            ? feeItems
            : feeItems.filter(
                  (item) => item.status === activeFilter
              )
    );

    let formatAmount = (amount: number) =>
        new Intl.NumberFormat('en-IN').format(amount);
</script>

<svelte:head>
    <title>Fees & Payments | Parent Dashboard</title>
</svelte:head>

<div class="fees-page">

    <!-- HEADER -->
    <div class="page-header">

        <div class="title-row">

            <div class="title-icon">
                <WalletCards size={24} />
            </div>

            <div>
                <h1>Fees & Payments</h1>

                <p>
                    View fee details, pending payments and payment history.
                </p>
            </div>

        </div>


        <!-- CHILD SELECTOR -->
        <div class="child-selector">

            <label for="child">
                Select Child
            </label>

            <div class="select-wrapper">

                <select
                    id="child"
                    bind:value={selectedChild}
                >
                    {#each children as item}
                        <option value={item.name}>
                            {item.name} · {item.studentId}
                        </option>
                    {/each}
                </select>

                <span class="select-icon">
                    <ChevronDown size={17} />
                </span>

            </div>

        </div>

    </div>


    <!-- CHILD INFO -->
    <section class="child-info-card">

        <div class="child-avatar">
            {child?.name.charAt(0)}
        </div>

        <div class="child-details">

            <h2>{child?.name}</h2>

            <p>
                Student ID:
                <strong>{child?.studentId}</strong>

                <span>•</span>

                Class:
                <strong>{child?.className}</strong>

                <span>•</span>

                Section:
                <strong>{child?.section}</strong>
            </p>

        </div>

        <div class="fee-summary">

            <span>Pending Amount</span>

            <strong>
                ₹{formatAmount(pendingFees)}
            </strong>

            <small>
                Requires attention
            </small>

        </div>

    </section>


    <!-- SUMMARY CARDS -->
    <section class="summary-grid">

        <div class="summary-card">

            <div class="summary-icon blue">
                <WalletCards size={21} />
            </div>

            <div>
                <span>Total Fees</span>

                <strong>
                    ₹{formatAmount(totalFees)}
                </strong>
            </div>

        </div>


        <div class="summary-card">

            <div class="summary-icon green">
                <CheckCircle2 size={21} />
            </div>

            <div>
                <span>Paid</span>

                <strong>
                    ₹{formatAmount(paidFees)}
                </strong>
            </div>

        </div>


        <div class="summary-card">

            <div class="summary-icon orange">
                <Clock3 size={21} />
            </div>

            <div>
                <span>Pending</span>

                <strong>
                    ₹{formatAmount(pendingFees)}
                </strong>
            </div>

        </div>


        <div class="summary-card">

            <div class="summary-icon red">
                <AlertCircle size={21} />
            </div>

            <div>
                <span>Overdue Items</span>

                <strong>{overdueCount}</strong>
            </div>

        </div>

    </section>


    <!-- PAYMENT PROGRESS -->
    <section class="card">

        <div class="card-header">

            <div>
                <h2>Fee Payment Progress</h2>

                <p>
                    Overview of the total academic fee payment.
                </p>
            </div>

            <strong class="percentage-value">
                {paidPercentage}%
            </strong>

        </div>


        <div class="progress-track">

            <div
                class="progress-fill"
                style={`width: ${paidPercentage}%`}
            ></div>

        </div>


        <div class="progress-details">

            <span>
                Paid:
                <strong>₹{formatAmount(paidFees)}</strong>
            </span>

            <span>
                Remaining:
                <strong>₹{formatAmount(pendingFees)}</strong>
            </span>

            <span>
                Total:
                <strong>₹{formatAmount(totalFees)}</strong>
            </span>

        </div>

    </section>


    <!-- FEE BREAKDOWN -->
    <section class="card">

        <div class="filter-header">

            <div>

                <h2>Fee Breakdown</h2>

                <p>
                    View individual fee components and their payment status.
                </p>

            </div>


            <div class="filter-buttons">

                {#each ['All', 'Paid', 'Pending', 'Overdue'] as filter}

                    <button
                        class:active={activeFilter === filter}
                        onclick={() => activeFilter = filter}
                    >
                        {filter}
                    </button>

                {/each}

            </div>

        </div>


        <div class="fee-list">

            {#each filteredFees as fee}

                <div class="fee-item">

                    <div class="fee-icon">

                        {#if fee.status === 'Paid'}

                            <CheckCircle2 size={20} />

                        {:else if fee.status === 'Overdue'}

                            <AlertCircle size={20} />

                        {:else}

                            <Clock3 size={20} />

                        {/if}

                    </div>


                    <div class="fee-content">

                        <div class="fee-title-row">

                            <div>

                                <h3>
                                    {fee.name}
                                </h3>

                                <span>
                                    {fee.description}
                                </span>

                            </div>


                            {#if fee.status === 'Paid'}

                                <span class="status paid">
                                    Paid
                                </span>

                            {:else if fee.status === 'Overdue'}

                                <span class="status overdue">
                                    Overdue
                                </span>

                            {:else}

                                <span class="status pending">
                                    Pending
                                </span>

                            {/if}

                        </div>


                        <div class="fee-details">

                            <div>
                                <span>Fee Amount</span>

                                <strong>
                                    ₹{formatAmount(fee.amount)}
                                </strong>
                            </div>

                            <div>
                                <span>Paid</span>

                                <strong class="paid-text">
                                    ₹{formatAmount(fee.paid)}
                                </strong>
                            </div>

                            <div>
                                <span>Remaining</span>

                                <strong class:remaining-danger={fee.amount - fee.paid > 0}>
                                    ₹{formatAmount(fee.amount - fee.paid)}
                                </strong>
                            </div>

                            <div>
                                <span>Due Date</span>

                                <strong>
                                    {fee.dueDate}
                                </strong>
                            </div>

                        </div>

                    </div>

                </div>

            {:else}

                <div class="empty-state">

                    <div class="empty-icon">
                        <CheckCircle2 size={28} />
                    </div>

                    <h3>
                        No {activeFilter.toLowerCase()} fees
                    </h3>

                    <p>
                        There are no fees in this category.
                    </p>

                </div>

            {/each}

        </div>

    </section>


    <!-- PAYMENT HISTORY -->
    <section class="card">

        <div class="card-header">

            <div>

                <h2>Payment History</h2>

                <p>
                    Previous fee payments and transaction details.
                </p>

            </div>

            <span class="history-count">
                {paymentHistory.length} Transactions
            </span>

        </div>


        <div class="payment-table">

            <div class="table-header">

                <span>Receipt</span>
                <span>Date</span>
                <span>Description</span>
                <span>Payment Method</span>
                <span>Amount</span>
                <span>Status</span>

            </div>


            {#each paymentHistory as payment}

                <div class="table-row">

                    <strong>
                        {payment.receipt}
                    </strong>

                    <span>
                        {payment.date}
                    </span>

                    <span>
                        {payment.description}
                    </span>

                    <span class="payment-method">
                        <CreditCard size={13} />
                        {payment.method}
                    </span>

                    <strong class="payment-amount">
                        ₹{formatAmount(payment.amount)}
                    </strong>

                    <span class="table-status">
                        <CheckCircle2 size={13} />
                        {payment.status}
                    </span>

                </div>

            {/each}

        </div>

    </section>


    <!-- NEXT PAYMENT -->
    <section class="next-payment-card">

        <div class="next-payment-icon">
            <CalendarDays size={22} />
        </div>

        <div class="next-payment-content">

            <span>
                Next Payment Due
            </span>

            <strong>
                20 Aug 2026
            </strong>

            <p>
                Laboratory Fee · ₹2,500 remaining
            </p>

        </div>

        <div class="next-payment-amount">

            <span>Amount Due</span>

            <strong>
                ₹2,500
            </strong>

        </div>

    </section>


    <!-- RECEIPT INFORMATION -->
    <div class="info-note">

        <div class="note-icon">
            <Receipt size={18} />
        </div>

        <div>

            <strong>
                Payment & Receipt Information
            </strong>

            <p>
                Fee amounts, payment history and receipt details
                shown here are currently demo data. During API
                integration, real fee balances, payment status
                and transaction details will be retrieved from
                the school's database.
            </p>

        </div>

    </div>

</div>


<style>
    .fees-page {
        width: 100%;
        min-height: 100vh;
        padding: 36px;
        box-sizing: border-box;
        background: #f8fafc;
    }


    /* HEADER */

    .page-header {
        display: flex;
        align-items: flex-end;
        justify-content: space-between;
        gap: 25px;
        margin-bottom: 25px;
    }

    .title-row {
        display: flex;
        align-items: center;
        gap: 13px;
    }

    .title-icon {
        width: 48px;
        height: 48px;
        display: flex;
        align-items: center;
        justify-content: center;
        flex-shrink: 0;
        background: #eef4ff;
        color: #2563eb;
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


    /* CHILD SELECTOR */

    .child-selector {
        min-width: 245px;
    }

    .child-selector label {
        display: block;
        margin-bottom: 6px;
        color: #475569;
        font-size: 11px;
        font-weight: 700;
    }

    .select-wrapper {
        position: relative;
    }

    .select-wrapper select {
        width: 100%;
        height: 43px;
        appearance: none;
        padding: 0 38px 0 13px;
        border: 1px solid #dbe3ef;
        border-radius: 10px;
        background: white;
        color: #1e293b;
        outline: none;
        font-size: 12px;
        cursor: pointer;
    }

    .select-icon {
        position: absolute;
        top: 13px;
        right: 12px;
        display: flex;
        align-items: center;
        pointer-events: none;
        color: #64748b;
    }


    /* CHILD INFO */

    .child-info-card {
        display: flex;
        align-items: center;
        gap: 15px;
        padding: 20px;
        margin-bottom: 20px;
        border: 1px solid #dbe5f2;
        border-radius: 15px;
        background: white;
        box-shadow: 0 3px 12px rgba(15, 23, 42, 0.03);
    }

    .child-avatar {
        width: 52px;
        height: 52px;
        display: flex;
        align-items: center;
        justify-content: center;
        flex-shrink: 0;
        border-radius: 50%;
        background: #2563eb;
        color: white;
        font-size: 20px;
        font-weight: 700;
    }

    .child-details {
        flex: 1;
    }

    .child-details h2 {
        margin: 0;
        color: #0f172a;
        font-size: 17px;
    }

    .child-details p {
        margin: 5px 0 0;
        color: #64748b;
        font-size: 12px;
    }

    .child-details strong {
        color: #334155;
    }

    .child-details p span {
        margin: 0 7px;
        color: #cbd5e1;
    }

    .fee-summary {
        min-width: 155px;
        padding: 12px 16px;
        border-radius: 11px;
        background: #fff7ed;
        text-align: center;
    }

    .fee-summary span {
        display: block;
        color: #64748b;
        font-size: 10px;
    }

    .fee-summary strong {
        display: block;
        margin: 2px 0;
        color: #ea580c;
        font-size: 23px;
    }

    .fee-summary small {
        color: #c2410c;
        font-size: 10px;
    }


    /* SUMMARY */

    .summary-grid {
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 15px;
        margin-bottom: 20px;
    }

    .summary-card {
        display: flex;
        align-items: center;
        gap: 13px;
        padding: 17px;
        border: 1px solid #e2e8f0;
        border-radius: 13px;
        background: white;
        box-shadow: 0 3px 12px rgba(15, 23, 42, 0.03);
    }

    .summary-icon {
        width: 43px;
        height: 43px;
        display: flex;
        align-items: center;
        justify-content: center;
        flex-shrink: 0;
        border-radius: 11px;
    }

    .summary-icon.blue {
        background: #eef4ff;
        color: #2563eb;
    }

    .summary-icon.green {
        background: #ecfdf5;
        color: #059669;
    }

    .summary-icon.orange {
        background: #fff7ed;
        color: #ea580c;
    }

    .summary-icon.red {
        background: #fef2f2;
        color: #dc2626;
    }

    .summary-card span {
        display: block;
        color: #64748b;
        font-size: 11px;
    }

    .summary-card strong {
        display: block;
        margin-top: 3px;
        color: #0f172a;
        font-size: 19px;
    }


    /* CARD */

    .card {
        margin-bottom: 20px;
        padding: 22px;
        border: 1px solid #e2e8f0;
        border-radius: 15px;
        background: white;
        box-shadow: 0 3px 12px rgba(15, 23, 42, 0.03);
    }

    .card-header,
    .filter-header {
        display: flex;
        align-items: flex-start;
        justify-content: space-between;
        gap: 15px;
        margin-bottom: 20px;
    }

    .card-header h2,
    .filter-header h2 {
        margin: 0;
        color: #0f172a;
        font-size: 17px;
    }

    .card-header p,
    .filter-header p {
        margin: 4px 0 0;
        color: #64748b;
        font-size: 11px;
    }


    /* PAYMENT PROGRESS */

    .percentage-value {
        color: #2563eb;
        font-size: 20px;
    }

    .progress-track {
        width: 100%;
        height: 10px;
        overflow: hidden;
        border-radius: 20px;
        background: #e2e8f0;
    }

    .progress-fill {
        height: 100%;
        border-radius: 20px;
        background: #2563eb;
        transition: width 0.3s ease;
    }

    .progress-details {
        display: flex;
        justify-content: space-between;
        gap: 15px;
        margin-top: 10px;
    }

    .progress-details span {
        color: #64748b;
        font-size: 10px;
    }

    .progress-details strong {
        color: #334155;
    }


    /* FILTERS */

    .filter-header {
        align-items: center;
    }

    .filter-buttons {
        display: flex;
        align-items: center;
        gap: 7px;
        flex-wrap: wrap;
    }

    .filter-buttons button {
        padding: 8px 12px;
        border: 1px solid #dbe3ef;
        border-radius: 8px;
        background: white;
        color: #64748b;
        font-size: 10px;
        font-weight: 600;
        cursor: pointer;
        transition: 0.2s ease;
    }

    .filter-buttons button:hover {
        border-color: #93c5fd;
        color: #2563eb;
    }

    .filter-buttons button.active {
        border-color: #2563eb;
        background: #2563eb;
        color: white;
    }


    /* FEE LIST */

    .fee-list {
        display: flex;
        flex-direction: column;
        gap: 11px;
    }

    .fee-item {
        display: flex;
        align-items: flex-start;
        gap: 14px;
        padding: 16px;
        border: 1px solid #e2e8f0;
        border-radius: 12px;
        background: #f8fafc;
    }

    .fee-icon {
        width: 42px;
        height: 42px;
        display: flex;
        align-items: center;
        justify-content: center;
        flex-shrink: 0;
        border-radius: 10px;
        background: #eef4ff;
        color: #2563eb;
    }

    .fee-item:has(.status.paid) .fee-icon {
        background: #ecfdf5;
        color: #059669;
    }

    .fee-item:has(.status.overdue) .fee-icon {
        background: #fef2f2;
        color: #dc2626;
    }

    .fee-content {
        flex: 1;
        min-width: 0;
    }

    .fee-title-row {
        display: flex;
        align-items: flex-start;
        justify-content: space-between;
        gap: 15px;
    }

    .fee-title-row h3 {
        margin: 0;
        color: #0f172a;
        font-size: 14px;
    }

    .fee-title-row span:not(.status) {
        display: block;
        margin-top: 4px;
        color: #64748b;
        font-size: 10px;
    }

    .status {
        padding: 5px 9px;
        border-radius: 7px;
        font-size: 9px;
        font-weight: 700;
        white-space: nowrap;
    }

    .status.paid {
        background: #ecfdf5;
        color: #059669;
    }

    .status.pending {
        background: #fff7ed;
        color: #ea580c;
    }

    .status.overdue {
        background: #fef2f2;
        color: #dc2626;
    }

    .fee-details {
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 10px;
        margin-top: 13px;
    }

    .fee-details div {
        padding: 9px 10px;
        border-radius: 8px;
        background: white;
    }

    .fee-details span {
        display: block;
        color: #94a3b8;
        font-size: 9px;
    }

    .fee-details strong {
        display: block;
        margin-top: 3px;
        color: #334155;
        font-size: 11px;
    }

    .fee-details .paid-text {
        color: #059669;
    }

    .fee-details .remaining-danger {
        color: #ea580c;
    }


    /* PAYMENT HISTORY */

    .history-count {
        padding: 6px 9px;
        border-radius: 8px;
        background: #eef4ff;
        color: #2563eb;
        font-size: 9px;
        font-weight: 700;
    }

    .payment-table {
        overflow-x: auto;
    }

    .table-header,
    .table-row {
        display: grid;
        grid-template-columns: 1.1fr 0.9fr 1.5fr 1.2fr 0.9fr 0.8fr;
        align-items: center;
        gap: 12px;
        min-width: 850px;
        padding: 13px 12px;
    }

    .table-header {
        border-radius: 9px;
        background: #f8fafc;
        color: #64748b;
        font-size: 10px;
        font-weight: 700;
    }

    .table-row {
        border-bottom: 1px solid #e2e8f0;
        color: #64748b;
        font-size: 10px;
    }

    .table-row strong {
        color: #334155;
    }

    .payment-method {
        display: flex;
        align-items: center;
        gap: 5px;
    }

    .payment-amount {
        color: #059669 !important;
    }

    .table-status {
        display: flex;
        align-items: center;
        gap: 4px;
        color: #059669;
        font-weight: 600;
    }


    /* NEXT PAYMENT */

    .next-payment-card {
        display: flex;
        align-items: center;
        gap: 14px;
        padding: 18px;
        margin-bottom: 12px;
        border: 1px solid #fed7aa;
        border-radius: 13px;
        background: #fffaf5;
    }

    .next-payment-icon {
        width: 45px;
        height: 45px;
        display: flex;
        align-items: center;
        justify-content: center;
        flex-shrink: 0;
        border-radius: 11px;
        background: #ffedd5;
        color: #ea580c;
    }

    .next-payment-content {
        flex: 1;
    }

    .next-payment-content span,
    .next-payment-amount span {
        display: block;
        color: #9a3412;
        font-size: 10px;
    }

    .next-payment-content strong {
        display: block;
        margin-top: 2px;
        color: #7c2d12;
        font-size: 16px;
    }

    .next-payment-content p {
        margin: 3px 0 0;
        color: #9a3412;
        font-size: 10px;
    }

    .next-payment-amount {
        text-align: right;
    }

    .next-payment-amount strong {
        display: block;
        margin-top: 3px;
        color: #ea580c;
        font-size: 21px;
    }


    /* NOTES */

    .info-note {
        display: flex;
        align-items: flex-start;
        gap: 11px;
        padding: 14px;
        border: 1px solid #dbe5f2;
        border-radius: 11px;
        background: #f8fbff;
    }

    .note-icon {
        width: 35px;
        height: 35px;
        display: flex;
        align-items: center;
        justify-content: center;
        flex-shrink: 0;
        border-radius: 9px;
        background: #eef4ff;
        color: #2563eb;
    }

    .info-note strong {
        display: block;
        color: #334155;
        font-size: 11px;
    }

    .info-note p {
        margin: 4px 0 0;
        color: #64748b;
        font-size: 10px;
        line-height: 1.5;
    }


    /* EMPTY STATE */

    .empty-state {
        padding: 45px 20px;
        text-align: center;
    }

    .empty-icon {
        width: 58px;
        height: 58px;
        display: flex;
        align-items: center;
        justify-content: center;
        margin: 0 auto 12px;
        border-radius: 50%;
        background: #ecfdf5;
        color: #059669;
    }

    .empty-state h3 {
        margin: 0;
        color: #334155;
        font-size: 15px;
    }

    .empty-state p {
        margin: 5px 0 0;
        color: #94a3b8;
        font-size: 10px;
    }


    /* RESPONSIVE */

    @media (max-width: 1100px) {

        .fees-page {
            padding: 24px;
        }

        .summary-grid {
            grid-template-columns: repeat(2, 1fr);
        }

        .fee-details {
            grid-template-columns: repeat(2, 1fr);
        }
    }

    @media (max-width: 750px) {

        .fees-page {
            padding: 18px;
        }

        .page-header {
            align-items: flex-start;
            flex-direction: column;
        }

        .child-selector {
            width: 100%;
        }

        .child-info-card {
            align-items: flex-start;
            flex-wrap: wrap;
        }

        .fee-summary {
            width: 100%;
        }

        .summary-grid {
            grid-template-columns: 1fr;
        }

        .filter-header {
            align-items: flex-start;
            flex-direction: column;
        }

        .filter-buttons {
            width: 100%;
        }

        .filter-buttons button {
            flex: 1;
        }

        .fee-title-row {
            align-items: flex-start;
            flex-direction: column;
        }

        .fee-details {
            grid-template-columns: 1fr;
        }

        .next-payment-card {
            align-items: flex-start;
            flex-wrap: wrap;
        }

        .next-payment-amount {
            width: 100%;
            text-align: left;
        }
    }
</style>