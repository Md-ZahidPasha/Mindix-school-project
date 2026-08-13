<script lang="ts">
    import {
        BookOpen,
        CalendarDays,
        CheckCircle2,
        ChevronDown,
        Clock3,
        FileText,
        GraduationCap,
        AlertCircle
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

    const assignments = [
        {
            title: 'Quadratic Equations Worksheet',
            subject: 'Mathematics',
            teacher: 'Mr. Rajesh Kumar',
            assignedDate: '08 Aug 2026',
            dueDate: '15 Aug 2026',
            status: 'Pending',
            priority: 'High',
            description: 'Complete the given problems on quadratic equations.'
        },
        {
            title: 'Light and Reflection Notes',
            subject: 'Science',
            teacher: 'Mrs. Priya Sharma',
            assignedDate: '07 Aug 2026',
            dueDate: '17 Aug 2026',
            status: 'Pending',
            priority: 'Medium',
            description: 'Prepare notes covering reflection and refraction of light.'
        },
        {
            title: 'English Grammar Exercise',
            subject: 'English',
            teacher: 'Ms. Anjali Reddy',
            assignedDate: '05 Aug 2026',
            dueDate: '14 Aug 2026',
            status: 'Pending',
            priority: 'Medium',
            description: 'Complete the grammar exercises from Chapter 6.'
        },
        {
            title: 'Indian Constitution Project',
            subject: 'Social Studies',
            teacher: 'Mr. Arun Singh',
            assignedDate: '01 Aug 2026',
            dueDate: '12 Aug 2026',
            status: 'Submitted',
            priority: 'High',
            description: 'Prepare and submit the assigned constitution project.'
        },
        {
            title: 'Python Programming Basics',
            subject: 'Computer Science',
            teacher: 'Mr. Mohammed Ali',
            assignedDate: '30 Jul 2026',
            dueDate: '08 Aug 2026',
            status: 'Completed',
            priority: 'Low',
            description: 'Write and execute the given Python programming exercises.'
        },
        {
            title: 'Hindi Essay Writing',
            subject: 'Hindi',
            teacher: 'Mrs. Kavitha Rao',
            assignedDate: '28 Jul 2026',
            dueDate: '05 Aug 2026',
            status: 'Completed',
            priority: 'Low',
            description: 'Write an essay on the given topic and submit it.'
        }
    ];

    function getSelectedChild() {
        return children.find(
            (child) => child.name === selectedChild
        );
    }

    let child = $derived(getSelectedChild());

    let filteredAssignments = $derived(
        activeFilter === 'All'
            ? assignments
            : assignments.filter(
                  (assignment) => assignment.status === activeFilter
              )
    );

    let pendingCount = $derived(
        assignments.filter(
            (assignment) => assignment.status === 'Pending'
        ).length
    );

    let submittedCount = $derived(
        assignments.filter(
            (assignment) => assignment.status === 'Submitted'
        ).length
    );

    let completedCount = $derived(
        assignments.filter(
            (assignment) => assignment.status === 'Completed'
        ).length
    );
</script>

<svelte:head>
    <title>Assignments | Parent Dashboard</title>
</svelte:head>

<div class="assignments-page">

    <!-- HEADER -->
    <div class="page-header">

        <div class="title-row">

            <div class="title-icon">
                <FileText size={24} />
            </div>

            <div>
                <h1>Assignments</h1>

                <p>
                    Track your child's assignments,
                    submissions and deadlines.
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

        <div class="assignment-summary">

            <span>Pending Assignments</span>

            <strong>{pendingCount}</strong>

            <small>
                Need attention
            </small>

        </div>

    </section>


    <!-- SUMMARY CARDS -->
    <section class="summary-grid">

        <div class="summary-card">

            <div class="summary-icon orange">
                <Clock3 size={21} />
            </div>

            <div>
                <span>Pending</span>
                <strong>{pendingCount}</strong>
            </div>

        </div>


        <div class="summary-card">

            <div class="summary-icon blue">
                <FileText size={21} />
            </div>

            <div>
                <span>Submitted</span>
                <strong>{submittedCount}</strong>
            </div>

        </div>


        <div class="summary-card">

            <div class="summary-icon green">
                <CheckCircle2 size={21} />
            </div>

            <div>
                <span>Completed</span>
                <strong>{completedCount}</strong>
            </div>

        </div>


        <div class="summary-card">

            <div class="summary-icon purple">
                <BookOpen size={21} />
            </div>

            <div>
                <span>Total</span>
                <strong>{assignments.length}</strong>
            </div>

        </div>

    </section>


    <!-- FILTERS -->
    <section class="card filter-card">

        <div class="filter-header">

            <div>
                <h2>All Assignments</h2>

                <p>
                    View and track assignments by their current status.
                </p>
            </div>

            <div class="filter-buttons">

                {#each ['All', 'Pending', 'Submitted', 'Completed'] as filter}

                    <button
                        class:active={activeFilter === filter}
                        onclick={() => activeFilter = filter}
                    >
                        {filter}
                    </button>

                {/each}

            </div>

        </div>

    </section>


    <!-- ASSIGNMENT LIST -->
    <section class="card">

        <div class="card-header">

            <div>
                <h2>
                    {activeFilter === 'All'
                        ? 'All Assignments'
                        : `${activeFilter} Assignments`}
                </h2>

                <p>
                    {filteredAssignments.length}
                    assignment{filteredAssignments.length === 1 ? '' : 's'}
                    found.
                </p>
            </div>

        </div>


        <div class="assignment-list">

            {#each filteredAssignments as assignment}

                <div class="assignment-card">

                    <div class="assignment-icon">
                        <BookOpen size={20} />
                    </div>


                    <div class="assignment-content">

                        <div class="assignment-top">

                            <div>

                                <h3>
                                    {assignment.title}
                                </h3>

                                <span class="subject">
                                    {assignment.subject}
                                </span>

                            </div>


                            <div class="badges">

                                {#if assignment.priority === 'High'}

                                    <span class="priority high">
                                        <AlertCircle size={12} />
                                        High
                                    </span>

                                {:else if assignment.priority === 'Medium'}

                                    <span class="priority medium">
                                        Medium
                                    </span>

                                {:else}

                                    <span class="priority low">
                                        Low
                                    </span>

                                {/if}


                                {#if assignment.status === 'Pending'}

                                    <span class="status pending">
                                        Pending
                                    </span>

                                {:else if assignment.status === 'Submitted'}

                                    <span class="status submitted">
                                        Submitted
                                    </span>

                                {:else}

                                    <span class="status completed">
                                        Completed
                                    </span>

                                {/if}

                            </div>

                        </div>


                        <p class="description">
                            {assignment.description}
                        </p>


                        <div class="assignment-meta">

                            <span>
                                <GraduationCap size={14} />
                                {assignment.teacher}
                            </span>

                            <span>
                                <CalendarDays size={14} />
                                Assigned: {assignment.assignedDate}
                            </span>

                            <span class:deadline-warning={assignment.status === 'Pending'}>
                                <Clock3 size={14} />
                                Due: {assignment.dueDate}
                            </span>

                        </div>

                    </div>

                </div>

            {:else}

                <div class="empty-state">

                    <div class="empty-icon">
                        <CheckCircle2 size={28} />
                    </div>

                    <h3>
                        No {activeFilter.toLowerCase()} assignments
                    </h3>

                    <p>
                        There are no assignments in this category.
                    </p>

                </div>

            {/each}

        </div>

    </section>


    <!-- DEADLINE REMINDER -->
    <div class="deadline-note">

        <div class="note-icon">
            <Clock3 size={18} />
        </div>

        <div>

            <strong>
                Assignment Reminder
            </strong>

            <p>
                Keep track of upcoming deadlines and make sure
                pending assignments are completed before their
                due dates.
            </p>

        </div>

    </div>


    <!-- INFORMATION -->
    <div class="info-note">

        <div class="note-icon">
            <FileText size={18} />
        </div>

        <div>

            <strong>
                Assignment Information
            </strong>

            <p>
                Assignment information shown here is currently
                demo data. During API integration, assignments,
                teachers, deadlines and submission status will
                be retrieved from the school's database for the
                selected child.
            </p>

        </div>

    </div>

</div>


<style>
    .assignments-page {
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

    .assignment-summary {
        min-width: 150px;
        padding: 12px 16px;
        border-radius: 11px;
        background: #fff7ed;
        text-align: center;
    }

    .assignment-summary span {
        display: block;
        color: #64748b;
        font-size: 10px;
    }

    .assignment-summary strong {
        display: block;
        margin: 2px 0;
        color: #ea580c;
        font-size: 24px;
    }

    .assignment-summary small {
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

    .summary-icon.orange {
        background: #fff7ed;
        color: #ea580c;
    }

    .summary-icon.blue {
        background: #eef4ff;
        color: #2563eb;
    }

    .summary-icon.green {
        background: #ecfdf5;
        color: #059669;
    }

    .summary-icon.purple {
        background: #f5f3ff;
        color: #7c3aed;
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
        font-size: 21px;
    }


    /* CARDS */

    .card {
        margin-bottom: 20px;
        padding: 22px;
        border: 1px solid #e2e8f0;
        border-radius: 15px;
        background: white;
        box-shadow: 0 3px 12px rgba(15, 23, 42, 0.03);
    }

    .card-header {
        display: flex;
        align-items: flex-start;
        justify-content: space-between;
        gap: 15px;
        margin-bottom: 20px;
    }

    .card-header h2 {
        margin: 0;
        color: #0f172a;
        font-size: 17px;
    }

    .card-header p {
        margin: 4px 0 0;
        color: #64748b;
        font-size: 11px;
    }


    /* FILTERS */

    .filter-card {
        padding: 18px 22px;
    }

    .filter-header {
        display: flex;
        align-items: center;
        justify-content: space-between;
        gap: 20px;
    }

    .filter-header h2 {
        margin: 0;
        color: #0f172a;
        font-size: 16px;
    }

    .filter-header p {
        margin: 4px 0 0;
        color: #64748b;
        font-size: 10px;
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


    /* ASSIGNMENTS */

    .assignment-list {
        display: flex;
        flex-direction: column;
        gap: 12px;
    }

    .assignment-card {
        display: flex;
        align-items: flex-start;
        gap: 14px;
        padding: 17px;
        border: 1px solid #e2e8f0;
        border-radius: 12px;
        background: #f8fafc;
    }

    .assignment-icon {
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

    .assignment-content {
        flex: 1;
        min-width: 0;
    }

    .assignment-top {
        display: flex;
        align-items: flex-start;
        justify-content: space-between;
        gap: 15px;
    }

    .assignment-top h3 {
        margin: 0;
        color: #0f172a;
        font-size: 14px;
    }

    .subject {
        display: block;
        margin-top: 4px;
        color: #2563eb;
        font-size: 10px;
        font-weight: 600;
    }

    .badges {
        display: flex;
        align-items: center;
        gap: 6px;
        flex-wrap: wrap;
        justify-content: flex-end;
    }

    .priority,
    .status {
        display: flex;
        align-items: center;
        gap: 4px;
        padding: 5px 8px;
        border-radius: 7px;
        font-size: 9px;
        font-weight: 700;
        white-space: nowrap;
    }

    .priority.high {
        background: #fef2f2;
        color: #dc2626;
    }

    .priority.medium {
        background: #fff7ed;
        color: #ea580c;
    }

    .priority.low {
        background: #f1f5f9;
        color: #64748b;
    }

    .status.pending {
        background: #fff7ed;
        color: #ea580c;
    }

    .status.submitted {
        background: #eef4ff;
        color: #2563eb;
    }

    .status.completed {
        background: #ecfdf5;
        color: #059669;
    }

    .description {
        margin: 10px 0 12px;
        color: #64748b;
        font-size: 10px;
        line-height: 1.5;
    }

    .assignment-meta {
        display: flex;
        align-items: center;
        flex-wrap: wrap;
        gap: 16px;
    }

    .assignment-meta span {
        display: flex;
        align-items: center;
        gap: 5px;
        color: #64748b;
        font-size: 9px;
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


    /* NOTES */

    .deadline-note,
    .info-note {
        display: flex;
        align-items: flex-start;
        gap: 11px;
        padding: 14px;
        margin-bottom: 12px;
        border: 1px solid #dbe5f2;
        border-radius: 11px;
        background: #f8fbff;
    }

    .deadline-note {
        border-color: #fed7aa;
        background: #fffaf5;
    }

    .deadline-note .note-icon {
        background: #ffedd5;
        color: #ea580c;
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

    .deadline-note strong,
    .info-note strong {
        display: block;
        color: #334155;
        font-size: 11px;
    }

    .deadline-note p,
    .info-note p {
        margin: 4px 0 0;
        color: #64748b;
        font-size: 10px;
        line-height: 1.5;
    }


    /* RESPONSIVE */

    @media (max-width: 1100px) {
        .assignments-page {
            padding: 24px;
        }

        .summary-grid {
            grid-template-columns: repeat(2, 1fr);
        }
    }

    @media (max-width: 750px) {
        .assignments-page {
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

        .assignment-summary {
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

        .assignment-top {
            align-items: flex-start;
            flex-direction: column;
        }

        .badges {
            justify-content: flex-start;
        }

        .assignment-meta {
            flex-direction: column;
            align-items: flex-start;
            gap: 7px;
        }
    }
</style>