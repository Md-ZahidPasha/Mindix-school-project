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
    import {
        getLeaveApplications,
        createLeaveApplication,
        type LeaveApplication
    } from '$lib/services/leave';

    let showForm = $state(false);

    let leaveType = $state('Casual Leave');
    let fromDate = $state('');
    let toDate = $state('');
    let reason = $state('');
    let isLoading = $state(true);
    let error = $state('');
    let success = $state('');

    let leaveRequests = $state<LeaveApplication[]>([]);

    async function loadLeave() {
        isLoading = true;
        error = '';
        try {
            const institutionId = localStorage.getItem('institution_id');
            if (!institutionId) throw new Error('Institution scope is missing. Please sign in again.');
            const employeeId = localStorage.getItem('employee_id') || undefined;
            leaveRequests = await getLeaveApplications(institutionId, employeeId);
        } catch (err) {
            error = err instanceof Error ? err.message : 'Unable to load leave requests.';
        } finally {
            isLoading = false;
        }
    }

    async function submitLeave() {
        if (!fromDate || !toDate || !reason.trim()) {
            alert('Please fill in all leave details.');
            return;
        }

        error = '';
        success = '';
        try {
            const userId = localStorage.getItem('user_id');
            const institutionId = localStorage.getItem('institution_id');
            const employeeId = localStorage.getItem('employee_id') || undefined;
            if (!userId || !institutionId) {
                throw new Error('Account scope is missing. Please sign in again.');
            }
            await createLeaveApplication({
                user_id: userId,
                institution_id: institutionId,
                employee_id: employeeId,
                leave_type: leaveType,
                start_date: fromDate,
                end_date: toDate,
                reason: reason.trim()
            });
            success = 'Leave request submitted successfully.';
            showForm = false;
            fromDate = '';
            toDate = '';
            reason = '';
            await loadLeave();
        } catch (err) {
            error = err instanceof Error ? err.message : 'Unable to submit leave request.';
        }
    }

    const approvedCount = $derived(leaveRequests.filter((r) => (r.status || '').toLowerCase() === 'approved').length);
    const pendingCount = $derived(leaveRequests.filter((r) => (r.status || '').toLowerCase() === 'pending').length);
    const rejectedCount = $derived(leaveRequests.filter((r) => (r.status || '').toLowerCase() === 'rejected').length);

    function fmtDate(value: string): string {
        const d = new Date(value);
        if (isNaN(d.getTime())) return value;
        return d.toLocaleDateString(undefined, { day: 'numeric', month: 'short', year: 'numeric' });
    }

    function daysBetween(start: string, end: string): number {
        const s = new Date(start);
        const e = new Date(end);
        if (isNaN(s.getTime()) || isNaN(e.getTime())) return 1;
        return Math.max(1, Math.round((e.getTime() - s.getTime()) / 86400000) + 1);
    }

    $effect(() => {
        loadLeave();
    });
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
                <h2>Leave Summary</h2>

                <p>
                    Your leave request statistics.
                </p>
            </div>

        </div>


        <div class="balance-grid">

            <div class="balance-card">

                <div class="balance-icon blue">
                    <FileText size={21} />
                </div>

                <div class="balance-content">

                    <span>
                        Total Requests
                    </span>

                    <strong>
                        {leaveRequests.length}
                    </strong>

                    <small>
                        applications
                    </small>

                </div>

            </div>

            <div class="balance-card">

                <div class="balance-icon green">
                    <CheckCircle2 size={21} />
                </div>

                <div class="balance-content">

                    <span>
                        Approved
                    </span>

                    <strong>
                        {approvedCount}
                    </strong>

                    <small>
                        applications
                    </small>

                </div>

            </div>

            <div class="balance-card">

                <div class="balance-icon orange">
                    <Clock3 size={21} />
                </div>

                <div class="balance-content">

                    <span>
                        Pending
                    </span>

                    <strong>
                        {pendingCount}
                    </strong>

                    <small>
                        applications
                    </small>

                </div>

            </div>

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

            {#if isLoading}
                <div class="empty-row">Loading...</div>
            {:else if leaveRequests.length === 0}
                <div class="empty-row">No leave requests yet.</div>
            {:else}
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
                                        {request.leave_type}
                                    </strong>
                                </td>

                                <td>

                                    <div class="date-range">

                                        <CalendarDays size={13} />

                                        <span>
                                            {fmtDate(request.start_date)}
                                            {#if request.start_date !== request.end_date}
                                                - {fmtDate(request.end_date)}
                                            {/if}
                                        </span>

                                    </div>

                                </td>

                                <td>
                                    {daysBetween(request.start_date, request.end_date)}
                                    {daysBetween(request.start_date, request.end_date) === 1 ? ' day' : ' days'}
                                </td>

                                <td>
                                    {request.reason || '—'}
                                </td>

                                <td>
                                    {request.created_at ? fmtDate(request.created_at) : '—'}
                                </td>

                                <td>

                                    {#if (request.status || '').toLowerCase() === 'approved'}

                                        <span class="status approved">
                                            <CheckCircle2 size={12} />
                                            Approved
                                        </span>

                                    {:else if (request.status || '').toLowerCase() === 'pending'}

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
            {/if}

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
                    {approvedCount}
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
                    {pendingCount}
                </strong>
                <small>Awaiting approval</small>
            </div>

        </div>

    </section>


    <!-- INFORMATION -->
    {#if error}
        <section class="information-note error-note">

            <div class="information-icon">
                <Info size={18} />
            </div>

            <div>

                <strong>
                    Unable to load leave data
                </strong>

                <p>
                    {error}
                </p>

            </div>

        </section>
    {/if}

    {#if success}
        <section class="information-note success-note">

            <div class="information-icon">
                <CheckCircle2 size={18} />
            </div>

            <div>

                <strong>
                    {success}
                </strong>

            </div>

        </section>
    {/if}

    <div class="empty-row-hint"></div>

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

    .information-note.error-note {
        border-color: #fecaca;
        background: #fef2f2;
    }

    .information-note.error-note .information-icon {
        background: #fee2e2;
        color: #dc2626;
    }

    .information-note.error-note strong {
        color: #b91c1c;
    }

    .information-note.success-note {
        border-color: #bbf7d0;
        background: #f0fdf4;
    }

    .information-note.success-note .information-icon {
        background: #dcfce7;
        color: #16a34a;
    }

    .information-note.success-note strong {
        color: #15803d;
    }

    .empty-row {
        padding: 30px;
        color: #94a3b8;
        font-size: 11px;
        text-align: center;
    }

    .empty-row-hint {
        height: 1px;
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