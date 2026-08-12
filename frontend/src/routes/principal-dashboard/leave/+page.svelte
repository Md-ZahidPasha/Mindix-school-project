<script lang="ts">
    import PrincipalSidebar from '$lib/components/principal/PrincipalSidebar.svelte';
    type LeaveType = 'teacher' | 'employee';
    type LeaveStatus = 'pending' | 'approved' | 'rejected';

    type LeaveRequest = {
        id: number;
        personId: string;
        name: string;
        role: LeaveType;
        department: string;
        leaveType: string;
        fromDate: string;
        toDate: string;
        days: number;
        reason: string;
        status: LeaveStatus;
    };

    let selectedType = $state<'all' | LeaveType>('all');
    let selectedStatus = $state<'all' | LeaveStatus>('pending');

    let requests = $state<LeaveRequest[]>([
        {
            id: 1,
            personId: 'TCH001',
            name: 'Rahul Sharma',
            role: 'teacher',
            department: 'Mathematics',
            leaveType: 'Casual Leave',
            fromDate: '18 Aug 2026',
            toDate: '19 Aug 2026',
            days: 2,
            reason: 'Personal work',
            status: 'pending'
        },
        {
            id: 2,
            personId: 'TCH004',
            name: 'Sana Khan',
            role: 'teacher',
            department: 'Biology',
            leaveType: 'Medical Leave',
            fromDate: '20 Aug 2026',
            toDate: '21 Aug 2026',
            days: 2,
            reason: 'Medical appointment',
            status: 'pending'
        },
        {
            id: 3,
            personId: 'EMP002',
            name: 'Ravi Kumar',
            role: 'employee',
            department: 'Driving',
            leaveType: 'Casual Leave',
            fromDate: '22 Aug 2026',
            toDate: '22 Aug 2026',
            days: 1,
            reason: 'Family function',
            status: 'pending'
        },
        {
            id: 4,
            personId: 'EMP004',
            name: 'Lakshmi Devi',
            role: 'employee',
            department: 'Library',
            leaveType: 'Personal Leave',
            fromDate: '15 Aug 2026',
            toDate: '16 Aug 2026',
            days: 2,
            reason: 'Personal reasons',
            status: 'approved'
        }
    ]);

    let filteredRequests = $derived(
        requests.filter((request) => {
            const typeMatch =
                selectedType === 'all' ||
                request.role === selectedType;

            const statusMatch =
                selectedStatus === 'all' ||
                request.status === selectedStatus;

            return typeMatch && statusMatch;
        })
    );

    let pendingCount = $derived(
        requests.filter((request) => request.status === 'pending').length
    );

    let teacherCount = $derived(
        requests.filter(
            (request) =>
                request.role === 'teacher' &&
                request.status === 'pending'
        ).length
    );

    let employeeCount = $derived(
        requests.filter(
            (request) =>
                request.role === 'employee' &&
                request.status === 'pending'
        ).length
    );

    function updateStatus(
        requestId: number,
        status: LeaveStatus
    ) {
        const request = requests.find(
            (item) => item.id === requestId
        );

        if (request) {
            request.status = status;
            requests = [...requests];
        }
    }

    function roleLabel(role: LeaveType) {
        return role === 'teacher'
            ? 'Teacher'
            : 'Employee';
    }
</script>


<div class="principal-layout">
    <PrincipalSidebar />

    <main class="main-content">
        <div class="leave-page">

    <!-- =========================
         PAGE HEADER
         ========================= -->

    <header class="page-header">

        <div>
            <h1>Teacher / Employee Leave</h1>

            <p>
                Review and manage leave requests submitted by teachers and employees.
            </p>
        </div>

    </header>


    <!-- =========================
         SUMMARY CARDS
         ========================= -->

    <section class="summary-grid">

        <div class="summary-card">

            <div class="summary-icon pending">
                ⏳
            </div>

            <div>
                <span>Pending Requests</span>
                <strong>{pendingCount}</strong>
            </div>

        </div>


        <div class="summary-card">

            <div class="summary-icon teacher">
                T
            </div>

            <div>
                <span>Teacher Requests</span>
                <strong>{teacherCount}</strong>
            </div>

        </div>


        <div class="summary-card">

            <div class="summary-icon employee">
                E
            </div>

            <div>
                <span>Employee Requests</span>
                <strong>{employeeCount}</strong>
            </div>

        </div>

    </section>


    <!-- =========================
         FILTERS
         ========================= -->

    <section class="filter-card">

        <div class="filter-field">

            <label for="leave-type">
                Request Type
            </label>

            <select
                id="leave-type"
                bind:value={selectedType}
            >
                <option value="all">
                    All
                </option>

                <option value="teacher">
                    Teachers
                </option>

                <option value="employee">
                    Employees
                </option>
            </select>

        </div>


        <div class="filter-field">

            <label for="leave-status">
                Status
            </label>

            <select
                id="leave-status"
                bind:value={selectedStatus}
            >
                <option value="pending">
                    Pending
                </option>

                <option value="approved">
                    Approved
                </option>

                <option value="rejected">
                    Rejected
                </option>

                <option value="all">
                    All Status
                </option>
            </select>

        </div>

    </section>


    <!-- =========================
         REQUEST LIST
         ========================= -->

    <section class="requests-section">

        <div class="section-title">

            <div>
                <h2>Leave Requests</h2>

                <p>
                    Review requests and approve or reject them.
                </p>
            </div>

            <span class="request-count">
                {filteredRequests.length} requests
            </span>

        </div>


        {#if filteredRequests.length > 0}

            <div class="requests-list">

                {#each filteredRequests as request}

                    <article class="request-card">

                        <!-- PERSON -->

                        <div class="person-section">

                            <div class="avatar">
                                {request.name.charAt(0)}
                            </div>

                            <div class="person-info">

                                <h3>
                                    {request.name}
                                </h3>

                                <p>
                                    {request.personId}
                                    ·
                                    {roleLabel(request.role)}
                                </p>

                                <span class="department">
                                    {request.department}
                                </span>

                            </div>

                        </div>


                        <!-- LEAVE DETAILS -->

                        <div class="leave-details">

                            <div class="detail">

                                <span>Leave Type</span>

                                <strong>
                                    {request.leaveType}
                                </strong>

                            </div>


                            <div class="detail">

                                <span>From</span>

                                <strong>
                                    {request.fromDate}
                                </strong>

                            </div>


                            <div class="detail">

                                <span>To</span>

                                <strong>
                                    {request.toDate}
                                </strong>

                            </div>


                            <div class="detail">

                                <span>Days</span>

                                <strong>
                                    {request.days}
                                </strong>

                            </div>

                        </div>


                        <!-- REASON -->

                        <div class="reason">

                            <span>Reason</span>

                            <p>
                                {request.reason}
                            </p>

                        </div>


                        <!-- STATUS / ACTION -->

                        <div class="request-action">

                            <span
                                class:status-pending={request.status === 'pending'}
                                class:status-approved={request.status === 'approved'}
                                class:status-rejected={request.status === 'rejected'}
                                class="status"
                            >
                                {request.status.charAt(0).toUpperCase() +
                                    request.status.slice(1)}
                            </span>


                            {#if request.status === 'pending'}

                                <div class="action-buttons">

                                    <button
                                        type="button"
                                        class="approve"
                                        onclick={() =>
                                            updateStatus(
                                                request.id,
                                                'approved'
                                            )
                                        }
                                    >
                                        ✓ Approve
                                    </button>


                                    <button
                                        type="button"
                                        class="reject"
                                        onclick={() =>
                                            updateStatus(
                                                request.id,
                                                'rejected'
                                            )
                                        }
                                    >
                                        ✕ Reject
                                    </button>

                                </div>

                            {:else}

                                <span class="processed">
                                    Request processed
                                </span>

                            {/if}

                        </div>

                    </article>

                {/each}

            </div>

        {:else}

            <div class="empty-state">

                <div class="empty-icon">
                    ✓
                </div>

                <h3>
                    No leave requests found
                </h3>

                <p>
                    There are no requests matching the selected filters.
                </p>

            </div>

        {/if}

    </section>

        
  </div>
 </main>
</div>


<style lang="scss">
.principal-layout {
    display: flex;
    min-height: 100vh;
    background: #f7f9fc;
}

.main-content {
    flex: 1;
    min-width: 0;
}

.leave-page {
    min-height: 100vh;

    padding: 28px 32px;

    box-sizing: border-box;

    background: #f7f9fc;
}


/* =========================
   HEADER
   ========================= */

.page-header {
    margin-bottom: 24px;
}

.page-header h1 {
    margin: 0;

    color: #14213d;

    font-size: 30px;
}

.page-header p {
    margin: 7px 0 0;

    color: #64748b;

    font-size: 15px;
}


/* =========================
   SUMMARY
   ========================= */

.summary-grid {
    display: grid;

    grid-template-columns:
        repeat(3, 1fr);

    gap: 16px;

    margin-bottom: 20px;
}

.summary-card {
    display: flex;

    align-items: center;

    gap: 14px;

    padding: 20px;

    background: white;

    border: 1px solid #e5eaf2;

    border-radius: 16px;

    box-shadow:
        0 4px 14px
        rgba(15, 23, 42, 0.03);
}

.summary-icon {
    width: 44px;
    height: 44px;

    display: flex;

    align-items: center;
    justify-content: center;

    border-radius: 12px;

    font-weight: 800;
}

.summary-icon.pending {
    background: #fff7ed;
    color: #ea580c;
}

.summary-icon.teacher {
    background: #eef4ff;
    color: #2563eb;
}

.summary-icon.employee {
    background: #f0fdf4;
    color: #16a34a;
}

.summary-card span {
    display: block;

    margin-bottom: 4px;

    color: #64748b;

    font-size: 12px;
}

.summary-card strong {
    color: #14213d;

    font-size: 23px;
}


/* =========================
   FILTER
   ========================= */

.filter-card {
    display: flex;

    gap: 16px;

    padding: 20px;

    margin-bottom: 24px;

    background: white;

    border: 1px solid #e5eaf2;

    border-radius: 16px;
}

.filter-field {
    width: 230px;
}

.filter-field label {
    display: block;

    margin-bottom: 7px;

    color: #334155;

    font-size: 12px;

    font-weight: 600;
}

select {
    width: 100%;

    height: 42px;

    padding: 0 11px;

    border: 1px solid #dbe3ef;

    border-radius: 9px;

    background: white;

    color: #1e293b;

    font-size: 13px;

    outline: none;
}

select:focus {
    border-color: #2563eb;

    box-shadow:
        0 0 0 3px
        rgba(37, 99, 235, 0.1);
}


/* =========================
   SECTION HEADER
   ========================= */

.section-title {
    display: flex;

    align-items: center;

    justify-content: space-between;

    margin-bottom: 14px;
}

.section-title h2 {
    margin: 0;

    color: #14213d;

    font-size: 20px;
}

.section-title p {
    margin: 5px 0 0;

    color: #64748b;

    font-size: 13px;
}

.request-count {
    padding: 7px 11px;

    border-radius: 8px;

    background: #eef4ff;

    color: #2563eb;

    font-size: 11px;

    font-weight: 700;
}


/* =========================
   REQUEST CARD
   ========================= */

.requests-list {
    display: flex;

    flex-direction: column;

    gap: 14px;
}

.request-card {
    display: grid;

    grid-template-columns:
        1.4fr
        1.8fr
        1.2fr
        1fr;

    gap: 20px;

    align-items: center;

    padding: 20px;

    background: white;

    border: 1px solid #e5eaf2;

    border-radius: 16px;

    box-shadow:
        0 4px 14px
        rgba(15, 23, 42, 0.03);
}


/* =========================
   PERSON
   ========================= */

.person-section {
    display: flex;

    align-items: center;

    gap: 12px;
}

.avatar {
    width: 46px;
    height: 46px;

    flex-shrink: 0;

    display: flex;

    align-items: center;
    justify-content: center;

    border-radius: 50%;

    background: #e8f0ff;

    color: #2563eb;

    font-size: 18px;

    font-weight: 700;
}

.person-info h3 {
    margin: 0;

    color: #14213d;

    font-size: 14px;
}

.person-info p {
    margin: 4px 0;

    color: #64748b;

    font-size: 11px;
}

.department {
    color: #475569;

    font-size: 11px;

    font-weight: 600;
}


/* =========================
   LEAVE DETAILS
   ========================= */

.leave-details {
    display: grid;

    grid-template-columns:
        repeat(2, 1fr);

    gap: 10px;
}

.detail span,
.reason span {
    display: block;

    margin-bottom: 4px;

    color: #94a3b8;

    font-size: 10px;

    font-weight: 600;
}

.detail strong {
    color: #334155;

    font-size: 11px;
}


/* =========================
   REASON
   ========================= */

.reason {
    padding: 12px;

    border-radius: 10px;

    background: #f8fafc;
}

.reason p {
    margin: 0;

    color: #475569;

    font-size: 11px;

    line-height: 1.5;
}


/* =========================
   ACTION
   ========================= */

.request-action {
    display: flex;

    flex-direction: column;

    align-items: flex-end;

    gap: 10px;
}

.status {
    padding: 6px 10px;

    border-radius: 8px;

    font-size: 10px;

    font-weight: 700;
}

.status-pending {
    background: #fff7ed;

    color: #ea580c;
}

.status-approved {
    background: #f0fdf4;

    color: #16a34a;
}

.status-rejected {
    background: #fef2f2;

    color: #dc2626;
}

.action-buttons {
    display: flex;

    gap: 7px;
}

.action-buttons button {
    height: 34px;

    padding: 0 11px;

    border-radius: 8px;

    font-size: 11px;

    font-weight: 600;

    cursor: pointer;
}

.approve {
    border: 1px solid #bbf7d0;

    background: #f0fdf4;

    color: #16a34a;
}

.approve:hover {
    background: #dcfce7;
}

.reject {
    border: 1px solid #fecaca;

    background: #fef2f2;

    color: #dc2626;
}

.reject:hover {
    background: #fee2e2;
}

.processed {
    color: #94a3b8;

    font-size: 10px;
}


/* =========================
   EMPTY STATE
   ========================= */

.empty-state {
    padding: 50px 20px;

    text-align: center;

    background: white;

    border: 1px solid #e5eaf2;

    border-radius: 16px;
}

.empty-icon {
    width: 48px;
    height: 48px;

    margin: 0 auto 12px;

    display: flex;

    align-items: center;
    justify-content: center;

    border-radius: 50%;

    background: #f0fdf4;

    color: #16a34a;

    font-size: 20px;

    font-weight: 700;
}

.empty-state h3 {
    margin: 0;

    color: #14213d;

    font-size: 16px;
}

.empty-state p {
    margin: 6px 0 0;

    color: #64748b;

    font-size: 12px;
}


/* =========================
   RESPONSIVE
   ========================= */

@media (max-width: 1100px) {

    .request-card {
        grid-template-columns:
            1fr
            1fr;
    }

    .request-action {
        align-items: flex-start;
    }

}


@media (max-width: 700px) {

    .leave-page {
        padding: 20px;
    }

    .summary-grid {
        grid-template-columns: 1fr;
    }

    .filter-card {
        flex-direction: column;
    }

    .filter-field {
        width: 100%;
    }

    .request-card {
        grid-template-columns: 1fr;
    }

    .leave-details {
        grid-template-columns:
            repeat(2, 1fr);
    }

}


@media (max-width: 450px) {

    .leave-details {
        grid-template-columns: 1fr;
    }

    .action-buttons {
        flex-direction: column;

        width: 100%;
    }

    .action-buttons button {
        width: 100%;
    }

}

</style>