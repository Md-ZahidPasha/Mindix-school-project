<script lang="ts">
    import {
        CalendarDays,
        CheckCircle2,
        Clock3,
        XCircle,
        Plus,
        FileText,
        Info,
        Briefcase,
        Heart,
        Coffee
    } from '@lucide/svelte';

    let showForm = $state(false);

    let leaveType = $state('Casual Leave');
    let fromDate = $state('');
    let toDate = $state('');
    let reason = $state('');

    const leaveBalance = [
        {
            type: 'Casual Leave',
            total: 12,
            used: 4,
            remaining: 8,
            icon: Coffee,
            className: 'blue'
        },
        {
            type: 'Sick Leave',
            total: 10,
            used: 2,
            remaining: 8,
            icon: Heart,
            className: 'red'
        },
        {
            type: 'Earned Leave',
            total: 15,
            used: 3,
            remaining: 12,
            icon: Briefcase,
            className: 'green'
        }
    ];

    const leaveRequests = [
        {
            type: 'Casual Leave',
            from: '18 Aug 2026',
            to: '19 Aug 2026',
            days: 2,
            reason: 'Personal work',
            appliedOn: '10 Aug 2026',
            status: 'Pending'
        },
        {
            type: 'Sick Leave',
            from: '28 Jul 2026',
            to: '29 Jul 2026',
            days: 2,
            reason: 'Not feeling well',
            appliedOn: '27 Jul 2026',
            status: 'Approved'
        },
        {
            type: 'Casual Leave',
            from: '15 Jul 2026',
            to: '15 Jul 2026',
            days: 1,
            reason: 'Family function',
            appliedOn: '10 Jul 2026',
            status: 'Approved'
        },
        {
            type: 'Earned Leave',
            from: '22 Jun 2026',
            to: '24 Jun 2026',
            days: 3,
            reason: 'Personal work',
            appliedOn: '15 Jun 2026',
            status: 'Rejected'
        }
    ];

    function submitLeave() {
        if (!fromDate || !toDate || !reason.trim()) {
            alert('Please fill in all leave details.');
            return;
        }

        alert('Leave request submitted successfully.');
        showForm = false;
        fromDate = '';
        toDate = '';
        reason = '';
    }
</script>

<svelte:head>
    <title>Leave | Employee Dashboard</title>
</svelte:head>

<div class="leave-page">

    <!-- HEADER -->
    <div class="page-header">

        <div class="title-row">

            <div class="title-icon">
                <CalendarDays size={24} />
            </div>

            <div>
                <h1>Leave</h1>

                <p>
                    Manage your leave balance and leave requests.
                </p>
            </div>

        </div>

        <button
            class="apply-button"
            type="button"
            onclick={() => showForm = !showForm}
        >
            <Plus size={17} />
            Apply for Leave
        </button>

    </div>


    <!-- LEAVE APPLICATION FORM -->
    {#if showForm}

        <section class="application-card">

            <div class="application-header">

                <div>
                    <h2>Apply for Leave</h2>

                    <p>
                        Submit a new leave request for approval.
                    </p>
                </div>

                <button
                    class="close-button"
                    type="button"
                    onclick={() => showForm = false}
                >
                    ×
                </button>

            </div>


            <div class="form-grid">

                <div class="form-group">

                    <label for="leaveType">
                        Leave Type
                    </label>

                    <select
                        id="leaveType"
                        bind:value={leaveType}
                    >
                        <option>Casual Leave</option>
                        <option>Sick Leave</option>
                        <option>Earned Leave</option>
                    </select>

                </div>


                <div class="form-group">

                    <label for="fromDate">
                        From Date
                    </label>

                    <input
                        id="fromDate"
                        type="date"
                        bind:value={fromDate}
                    />

                </div>


                <div class="form-group">

                    <label for="toDate">
                        To Date
                    </label>

                    <input
                        id="toDate"
                        type="date"
                        bind:value={toDate}
                    />

                </div>


                <div class="form-group full-width">

                    <label for="reason">
                        Reason
                    </label>

                    <textarea
                        id="reason"
                        rows="3"
                        placeholder="Enter the reason for your leave..."
                        bind:value={reason}
                    ></textarea>

                </div>

            </div>


            <div class="form-actions">

                <button
                    class="cancel-button"
                    type="button"
                    onclick={() => showForm = false}
                >
                    Cancel
                </button>

                <button
                    class="submit-button"
                    type="button"
                    onclick={submitLeave}
                >
                    Submit Request
                </button>

            </div>

        </section>

    {/if}


    <!-- LEAVE BALANCE -->
    <section>

        <div class="section-heading">

            <div>
                <h2>Leave Balance</h2>

                <p>
                    Your available leave for the current year.
                </p>
            </div>

        </div>


        <div class="balance-grid">

            {#each leaveBalance as leave}

                <div class="balance-card">

                    <div class={`balance-icon ${leave.className}`}>
                        <leave.icon size={21} />
                    </div>

                    <div class="balance-content">

                        <span>
                            {leave.type}
                        </span>

                        <strong>
                            {leave.remaining}
                        </strong>

                        <small>
                            days remaining
                        </small>

                    </div>

                    <div class="balance-details">

                        <span>
                            Total
                            <strong>{leave.total}</strong>
                        </span>

                        <span>
                            Used
                            <strong>{leave.used}</strong>
                        </span>

                    </div>

                </div>

            {/each}

        </div>

    </section>


    <!-- LEAVE REQUESTS -->
    <section class="requests-section">

        <div class="section-heading">

            <div>

                <h2>Leave Requests</h2>

                <p>
                    Track your submitted leave applications.
                </p>

            </div>

            <span class="request-count">
                {leaveRequests.length} Requests
            </span>

        </div>


        <div class="requests-card">

            <div class="table-wrapper">

                <table>

                    <thead>

                        <tr>
                            <th>Leave Type</th>
                            <th>Duration</th>
                            <th>Days</th>
                            <th>Reason</th>
                            <th>Applied On</th>
                            <th>Status</th>
                        </tr>

                    </thead>

                    <tbody>

                        {#each leaveRequests as request}

                            <tr>

                                <td>
                                    <strong>
                                        {request.type}
                                    </strong>
                                </td>

                                <td>

                                    <div class="date-range">

                                        <CalendarDays size={13} />

                                        <span>
                                            {request.from}
                                            {#if request.from !== request.to}
                                                - {request.to}
                                            {/if}
                                        </span>

                                    </div>

                                </td>

                                <td>
                                    {request.days}
                                    {request.days === 1 ? ' day' : ' days'}
                                </td>

                                <td>
                                    {request.reason}
                                </td>

                                <td>
                                    {request.appliedOn}
                                </td>

                                <td>

                                    {#if request.status === 'Approved'}

                                        <span class="status approved">
                                            <CheckCircle2 size={12} />
                                            Approved
                                        </span>

                                    {:else if request.status === 'Pending'}

                                        <span class="status pending">
                                            <Clock3 size={12} />
                                            Pending
                                        </span>

                                    {:else}

                                        <span class="status rejected">
                                            <XCircle size={12} />
                                            Rejected
                                        </span>

                                    {/if}

                                </td>

                            </tr>

                        {/each}

                    </tbody>

                </table>

            </div>

        </div>

    </section>


    <!-- SUMMARY -->
    <section class="summary-grid">

        <div class="summary-card">

            <div class="summary-icon blue">
                <FileText size={19} />
            </div>

            <div>
                <span>Total Requests</span>
                <strong>{leaveRequests.length}</strong>
                <small>This year</small>
            </div>

        </div>


        <div class="summary-card">

            <div class="summary-icon green">
                <CheckCircle2 size={19} />
            </div>

            <div>
                <span>Approved</span>
                <strong>
                    {leaveRequests.filter(
                        (request) => request.status === 'Approved'
                    ).length}
                </strong>
                <small>Approved requests</small>
            </div>

        </div>


        <div class="summary-card">

            <div class="summary-icon orange">
                <Clock3 size={19} />
            </div>

            <div>
                <span>Pending</span>
                <strong>
                    {leaveRequests.filter(
                        (request) => request.status === 'Pending'
                    ).length}
                </strong>
                <small>Awaiting approval</small>
            </div>

        </div>

    </section>


    <!-- INFORMATION -->
    <section class="information-note">

        <div class="information-icon">
            <Info size={18} />
        </div>

        <div>

            <strong>
                Leave Information
            </strong>

            <p>
                Leave balance and request information shown here is
                currently demo data. During API integration, balances,
                requests and approval status will be retrieved from
                the backend.
            </p>

        </div>

    </section>

</div>


<style>
    .leave-page {
        width: 100%;
        min-height: 100vh;
        padding: 36px;
        box-sizing: border-box;
        background: #f8fafc;
    }


    /* HEADER */

    .page-header {
        display: flex;
        align-items: center;
        justify-content: space-between;
        gap: 20px;
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
        border-radius: 13px;
        background: #eef4ff;
        color: #2563eb;
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

    .apply-button {
        display: flex;
        align-items: center;
        gap: 7px;
        padding: 11px 15px;
        border: none;
        border-radius: 9px;
        background: #2563eb;
        color: white;
        font-size: 10px;
        font-weight: 700;
        cursor: pointer;
    }

    .apply-button:hover {
        background: #1d4ed8;
    }


    /* APPLICATION */

    .application-card {
        padding: 22px;
        margin-bottom: 25px;
        border: 1px solid #bfdbfe;
        border-radius: 15px;
        background: white;
        box-shadow: 0 3px 12px rgba(15, 23, 42, 0.03);
    }

    .application-header {
        display: flex;
        align-items: flex-start;
        justify-content: space-between;
        gap: 15px;
        margin-bottom: 20px;
    }

    .application-header h2 {
        margin: 0;
        color: #0f172a;
        font-size: 16px;
    }

    .application-header p {
        margin: 4px 0 0;
        color: #64748b;
        font-size: 10px;
    }

    .close-button {
        width: 30px;
        height: 30px;
        border: 1px solid #e2e8f0;
        border-radius: 7px;
        background: white;
        color: #64748b;
        font-size: 20px;
        line-height: 1;
        cursor: pointer;
    }

    .close-button:hover {
        background: #f8fafc;
    }

    .form-grid {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 15px;
    }

    .form-group {
        display: flex;
        flex-direction: column;
        gap: 6px;
    }

    .form-group.full-width {
        grid-column: 1 / -1;
    }

    .form-group label {
        color: #475569;
        font-size: 10px;
        font-weight: 700;
    }

    .form-group input,
    .form-group select,
    .form-group textarea {
        width: 100%;
        box-sizing: border-box;
        padding: 10px 11px;
        border: 1px solid #dbe3ef;
        border-radius: 8px;
        outline: none;
        background: white;
        color: #334155;
        font-family: inherit;
        font-size: 10px;
    }

    .form-group textarea {
        resize: vertical;
    }

    .form-group input:focus,
    .form-group select:focus,
    .form-group textarea:focus {
        border-color: #93c5fd;
        box-shadow: 0 0 0 3px #eff6ff;
    }

    .form-actions {
        display: flex;
        justify-content: flex-end;
        gap: 8px;
        margin-top: 18px;
    }

    .cancel-button,
    .submit-button {
        padding: 9px 14px;
        border-radius: 8px;
        font-size: 9px;
        font-weight: 700;
        cursor: pointer;
    }

    .cancel-button {
        border: 1px solid #dbe3ef;
        background: white;
        color: #64748b;
    }

    .submit-button {
        border: none;
        background: #2563eb;
        color: white;
    }


    /* SECTION */

    .section-heading {
        display: flex;
        align-items: center;
        justify-content: space-between;
        gap: 15px;
        margin-bottom: 13px;
    }

    .section-heading h2 {
        margin: 0;
        color: #0f172a;
        font-size: 17px;
    }

    .section-heading p {
        margin: 4px 0 0;
        color: #64748b;
        font-size: 10px;
    }

    .request-count {
        padding: 6px 9px;
        border-radius: 7px;
        background: #f1f5f9;
        color: #64748b;
        font-size: 9px;
        font-weight: 700;
    }


    /* BALANCE */

    .balance-grid {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 14px;
        margin-bottom: 25px;
    }

    .balance-card {
        display: flex;
        align-items: center;
        gap: 12px;
        padding: 18px;
        border: 1px solid #e2e8f0;
        border-radius: 14px;
        background: white;
        box-shadow: 0 3px 12px rgba(15, 23, 42, 0.03);
    }

    .balance-icon {
        width: 43px;
        height: 43px;
        display: flex;
        align-items: center;
        justify-content: center;
        flex-shrink: 0;
        border-radius: 10px;
    }

    .balance-icon.blue {
        background: #eef4ff;
        color: #2563eb;
    }

    .balance-icon.red {
        background: #fef2f2;
        color: #dc2626;
    }

    .balance-icon.green {
        background: #ecfdf5;
        color: #059669;
    }

    .balance-content {
        flex: 1;
    }

    .balance-content span {
        display: block;
        color: #64748b;
        font-size: 9px;
    }

    .balance-content strong {
        display: inline-block;
        margin-top: 2px;
        color: #0f172a;
        font-size: 21px;
    }

    .balance-content small {
        margin-left: 4px;
        color: #94a3b8;
        font-size: 8px;
    }

    .balance-details {
        display: flex;
        flex-direction: column;
        gap: 4px;
        padding-left: 12px;
        border-left: 1px solid #e2e8f0;
    }

    .balance-details span {
        color: #94a3b8;
        font-size: 8px;
    }

    .balance-details strong {
        margin-left: 4px;
        color: #475569;
    }


    /* REQUESTS */

    .requests-section {
        margin-bottom: 25px;
    }

    .requests-card {
        overflow: hidden;
        border: 1px solid #e2e8f0;
        border-radius: 14px;
        background: white;
        box-shadow: 0 3px 12px rgba(15, 23, 42, 0.03);
    }

    .table-wrapper {
        width: 100%;
        overflow-x: auto;
    }

    table {
        width: 100%;
        min-width: 800px;
        border-collapse: collapse;
    }

    th {
        padding: 11px 13px;
        border-bottom: 1px solid #e2e8f0;
        background: #f8fafc;
        color: #64748b;
        font-size: 9px;
        font-weight: 700;
        text-align: left;
    }

    td {
        padding: 13px;
        border-bottom: 1px solid #f1f5f9;
        color: #64748b;
        font-size: 9px;
    }

    tbody tr:last-child td {
        border-bottom: none;
    }

    tbody tr:hover {
        background: #f8fafc;
    }

    td strong {
        color: #334155;
    }

    .date-range {
        display: flex;
        align-items: center;
        gap: 5px;
    }

    .status {
        display: inline-flex;
        align-items: center;
        gap: 4px;
        padding: 5px 8px;
        border-radius: 7px;
        font-size: 8px;
        font-weight: 700;
    }

    .status.approved {
        background: #ecfdf5;
        color: #059669;
    }

    .status.pending {
        background: #fff7ed;
        color: #ea580c;
    }

    .status.rejected {
        background: #fef2f2;
        color: #dc2626;
    }


    /* SUMMARY */

    .summary-grid {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 14px;
        margin-bottom: 20px;
    }

    .summary-card {
        display: flex;
        align-items: center;
        gap: 12px;
        padding: 17px;
        border: 1px solid #e2e8f0;
        border-radius: 13px;
        background: white;
        box-shadow: 0 3px 12px rgba(15, 23, 42, 0.03);
    }

    .summary-icon {
        width: 42px;
        height: 42px;
        display: flex;
        align-items: center;
        justify-content: center;
        flex-shrink: 0;
        border-radius: 10px;
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

    .summary-card span {
        display: block;
        color: #64748b;
        font-size: 9px;
    }

    .summary-card strong {
        display: block;
        margin-top: 2px;
        color: #0f172a;
        font-size: 19px;
    }

    .summary-card small {
        display: block;
        margin-top: 2px;
        color: #94a3b8;
        font-size: 8px;
    }


    /* INFORMATION */

    .information-note {
        display: flex;
        align-items: flex-start;
        gap: 11px;
        padding: 15px;
        border: 1px solid #bfdbfe;
        border-radius: 11px;
        background: #eff6ff;
    }

    .information-icon {
        width: 36px;
        height: 36px;
        display: flex;
        align-items: center;
        justify-content: center;
        flex-shrink: 0;
        border-radius: 9px;
        background: #dbeafe;
        color: #2563eb;
    }

    .information-note strong {
        display: block;
        color: #1e3a8a;
        font-size: 11px;
    }

    .information-note p {
        margin: 4px 0 0;
        color: #475569;
        font-size: 10px;
        line-height: 1.5;
    }


    /* RESPONSIVE */

    @media (max-width: 1000px) {

        .balance-grid,
        .summary-grid {
            grid-template-columns: 1fr;
        }

        .form-grid {
            grid-template-columns: repeat(2, 1fr);
        }
    }


    @media (max-width: 700px) {

        .leave-page {
            padding: 18px;
        }

        .page-header {
            align-items: flex-start;
            flex-direction: column;
        }

        .apply-button {
            width: 100%;
            justify-content: center;
        }

        .form-grid {
            grid-template-columns: 1fr;
        }

        .form-group.full-width {
            grid-column: auto;
        }

        .balance-grid,
        .summary-grid {
            grid-template-columns: 1fr;
        }

        .section-heading {
            align-items: flex-start;
            flex-direction: column;
        }
    }
</style>