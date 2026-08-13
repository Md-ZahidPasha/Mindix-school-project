<script lang="ts">
    import {
        Bell,
        CalendarDays,
        ChevronDown,
        Clock3,
        FileText,
        Megaphone,
        Pin,
        School,
        ShieldAlert
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

    const notices = [
        {
            title: 'First Term Examination Schedule Released',
            category: 'Examination',
            date: '12 Aug 2026',
            time: '10:30 AM',
            priority: 'Important',
            pinned: true,
            description:
                'The first term examination timetable has been published. Parents are requested to check the examination schedule and help students prepare accordingly.'
        },
        {
            title: 'Independence Day Celebration',
            category: 'Event',
            date: '10 Aug 2026',
            time: '09:15 AM',
            priority: 'Normal',
            pinned: false,
            description:
                'The school will conduct Independence Day celebrations on 15 August. Students participating in the programme should report to school at the instructed time.'
        },
        {
            title: 'Fee Payment Reminder',
            category: 'Fees',
            date: '08 Aug 2026',
            time: '02:20 PM',
            priority: 'Important',
            pinned: true,
            description:
                'Parents are requested to clear the pending fee amount before the due date to avoid late payment charges.'
        },
        {
            title: 'Parent-Teacher Meeting',
            category: 'Meeting',
            date: '05 Aug 2026',
            time: '11:45 AM',
            priority: 'Normal',
            pinned: false,
            description:
                'The next parent-teacher meeting will be conducted on 22 August. Details regarding the time slots will be shared shortly.'
        },
        {
            title: 'School Transport Timing Update',
            category: 'Transport',
            date: '03 Aug 2026',
            time: '04:10 PM',
            priority: 'Normal',
            pinned: false,
            description:
                'There has been a minor change in school bus timings for selected routes. Parents are requested to check the updated timings.'
        },
        {
            title: 'Annual Sports Day Registration',
            category: 'Sports',
            date: '01 Aug 2026',
            time: '01:00 PM',
            priority: 'Normal',
            pinned: false,
            description:
                'Students interested in participating in Annual Sports Day events can register through their respective class teachers.'
        }
    ];

    function getSelectedChild() {
        return children.find(
            (child) => child.name === selectedChild
        );
    }

    let child = $derived(getSelectedChild());

    let filteredNotices = $derived(
        activeFilter === 'All'
            ? notices
            : notices.filter(
                  (notice) => notice.category === activeFilter
              )
    );

    let importantCount = $derived(
        notices.filter(
            (notice) => notice.priority === 'Important'
        ).length
    );

    let pinnedCount = $derived(
        notices.filter(
            (notice) => notice.pinned
        ).length
    );
</script>

<svelte:head>
    <title>Notices | Parent Dashboard</title>
</svelte:head>

<div class="notices-page">

    <!-- HEADER -->
    <div class="page-header">

        <div class="title-row">

            <div class="title-icon">
                <Bell size={24} />
            </div>

            <div>
                <h1>Notices</h1>

                <p>
                    Stay updated with important school announcements and notices.
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

        <div class="notice-summary">

            <span>Important Notices</span>

            <strong>{importantCount}</strong>

            <small>
                Require attention
            </small>

        </div>

    </section>


    <!-- SUMMARY -->
    <section class="summary-grid">

        <div class="summary-card">

            <div class="summary-icon blue">
                <Bell size={21} />
            </div>

            <div>
                <span>Total Notices</span>
                <strong>{notices.length}</strong>
            </div>

        </div>


        <div class="summary-card">

            <div class="summary-icon red">
                <ShieldAlert size={21} />
            </div>

            <div>
                <span>Important</span>
                <strong>{importantCount}</strong>
            </div>

        </div>


        <div class="summary-card">

            <div class="summary-icon orange">
                <Pin size={21} />
            </div>

            <div>
                <span>Pinned</span>
                <strong>{pinnedCount}</strong>
            </div>

        </div>


        <div class="summary-card">

            <div class="summary-icon green">
                <School size={21} />
            </div>

            <div>
                <span>School Updates</span>

                <strong>
                    {notices.filter(
                        (notice) => notice.category === 'Event'
                    ).length}
                </strong>

            </div>

        </div>

    </section>


    <!-- FILTERS -->
    <section class="card filter-card">

        <div class="filter-header">

            <div>

                <h2>Notice Board</h2>

                <p>
                    Browse announcements by category.
                </p>

            </div>


            <div class="filter-buttons">

                {#each [
                    'All',
                    'Examination',
                    'Event',
                    'Fees',
                    'Meeting',
                    'Transport',
                    'Sports'
                ] as filter}

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


    <!-- NOTICE LIST -->
    <section class="card">

        <div class="card-header">

            <div>

                <h2>
                    {activeFilter === 'All'
                        ? 'Latest Notices'
                        : `${activeFilter} Notices`}
                </h2>

                <p>
                    {filteredNotices.length}
                    notice{filteredNotices.length === 1 ? '' : 's'}
                    available.
                </p>

            </div>

        </div>


        <div class="notice-list">

            {#each filteredNotices as notice}

                <article
                    class:important-notice={notice.priority === 'Important'}
                    class="notice-card"
                >

                    <div class="notice-icon">

                        {#if notice.category === 'Examination'}

                            <FileText size={21} />

                        {:else if notice.category === 'Event'}

                            <Megaphone size={21} />

                        {:else if notice.category === 'Fees'}

                            <ShieldAlert size={21} />

                        {:else if notice.category === 'Meeting'}

                            <School size={21} />

                        {:else if notice.category === 'Transport'}

                            <Clock3 size={21} />

                        {:else}

                            <Bell size={21} />

                        {/if}

                    </div>


                    <div class="notice-content">

                        <div class="notice-title-row">

                            <div>

                                <div class="title-with-pin">

                                    <h3>
                                        {notice.title}
                                    </h3>

                                    {#if notice.pinned}

                                        <span class="pin-badge">
                                            <Pin size={11} />
                                            Pinned
                                        </span>

                                    {/if}

                                </div>

                                <span class="notice-category">
                                    {notice.category}
                                </span>

                            </div>


                            {#if notice.priority === 'Important'}

                                <span class="priority important">
                                    Important
                                </span>

                            {:else}

                                <span class="priority normal">
                                    Normal
                                </span>

                            {/if}

                        </div>


                        <p class="notice-description">
                            {notice.description}
                        </p>


                        <div class="notice-meta">

                            <span>
                                <CalendarDays size={14} />
                                {notice.date}
                            </span>

                            <span>
                                <Clock3 size={14} />
                                {notice.time}
                            </span>

                        </div>

                    </div>

                </article>

            {:else}

                <div class="empty-state">

                    <div class="empty-icon">
                        <Bell size={28} />
                    </div>

                    <h3>
                        No notices found
                    </h3>

                    <p>
                        There are no notices in this category.
                    </p>

                </div>

            {/each}

        </div>

    </section>


    <!-- NOTICE INFORMATION -->
    <section class="notice-information">

        <div class="information-icon">
            <Megaphone size={19} />
        </div>

        <div>

            <strong>
                Stay Updated
            </strong>

            <p>
                Please check the notice board regularly for
                examination schedules, school events, fee reminders,
                meetings and other important announcements.
            </p>

        </div>

    </section>


    <!-- API NOTE -->
    <div class="info-note">

        <div class="note-icon">
            <FileText size={18} />
        </div>

        <div>

            <strong>
                Notice Information
            </strong>

            <p>
                Notices shown here are currently demo data.
                During API integration, announcements published
                by the school will be retrieved from the backend
                and displayed here for the parent.
            </p>

        </div>

    </div>

</div>


<style>
    .notices-page {
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

    .notice-summary {
        min-width: 150px;
        padding: 12px 16px;
        border-radius: 11px;
        background: #fef2f2;
        text-align: center;
    }

    .notice-summary span {
        display: block;
        color: #64748b;
        font-size: 10px;
    }

    .notice-summary strong {
        display: block;
        margin: 2px 0;
        color: #dc2626;
        font-size: 24px;
    }

    .notice-summary small {
        color: #b91c1c;
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

    .summary-icon.red {
        background: #fef2f2;
        color: #dc2626;
    }

    .summary-icon.orange {
        background: #fff7ed;
        color: #ea580c;
    }

    .summary-icon.green {
        background: #ecfdf5;
        color: #059669;
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
        padding: 8px 11px;
        border: 1px solid #dbe3ef;
        border-radius: 8px;
        background: white;
        color: #64748b;
        font-size: 9px;
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


    /* NOTICE LIST */

    .notice-list {
        display: flex;
        flex-direction: column;
        gap: 13px;
    }

    .notice-card {
        display: flex;
        align-items: flex-start;
        gap: 14px;
        padding: 17px;
        border: 1px solid #e2e8f0;
        border-radius: 13px;
        background: #f8fafc;
        transition: 0.2s ease;
    }

    .notice-card:hover {
        border-color: #bfdbfe;
        box-shadow: 0 3px 10px rgba(37, 99, 235, 0.05);
    }

    .notice-card.important-notice {
        border-left: 4px solid #dc2626;
    }

    .notice-icon {
        width: 43px;
        height: 43px;
        display: flex;
        align-items: center;
        justify-content: center;
        flex-shrink: 0;
        border-radius: 10px;
        background: #eef4ff;
        color: #2563eb;
    }

    .important-notice .notice-icon {
        background: #fef2f2;
        color: #dc2626;
    }

    .notice-content {
        flex: 1;
        min-width: 0;
    }

    .notice-title-row {
        display: flex;
        align-items: flex-start;
        justify-content: space-between;
        gap: 15px;
    }

    .title-with-pin {
        display: flex;
        align-items: center;
        gap: 8px;
        flex-wrap: wrap;
    }

    .notice-title-row h3 {
        margin: 0;
        color: #0f172a;
        font-size: 14px;
    }

    .notice-category {
        display: inline-block;
        margin-top: 4px;
        color: #2563eb;
        font-size: 9px;
        font-weight: 700;
    }

    .pin-badge {
        display: flex;
        align-items: center;
        gap: 3px;
        padding: 4px 6px;
        border-radius: 6px;
        background: #fff7ed;
        color: #ea580c;
        font-size: 8px;
        font-weight: 700;
    }

    .priority {
        padding: 5px 8px;
        border-radius: 7px;
        font-size: 9px;
        font-weight: 700;
        white-space: nowrap;
    }

    .priority.important {
        background: #fef2f2;
        color: #dc2626;
    }

    .priority.normal {
        background: #f1f5f9;
        color: #64748b;
    }

    .notice-description {
        margin: 10px 0 12px;
        color: #64748b;
        font-size: 10px;
        line-height: 1.55;
    }

    .notice-meta {
        display: flex;
        align-items: center;
        flex-wrap: wrap;
        gap: 16px;
    }

    .notice-meta span {
        display: flex;
        align-items: center;
        gap: 5px;
        color: #64748b;
        font-size: 9px;
    }

    


    /* INFORMATION */

    .notice-information {
        display: flex;
        align-items: flex-start;
        gap: 11px;
        padding: 15px;
        margin-bottom: 12px;
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

    .notice-information strong {
        display: block;
        color: #1e3a8a;
        font-size: 11px;
    }

    .notice-information p {
        margin: 4px 0 0;
        color: #475569;
        font-size: 10px;
        line-height: 1.5;
    }


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


    /* EMPTY */

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
        background: #eef4ff;
        color: #2563eb;
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

        .notices-page {
            padding: 24px;
        }

        .summary-grid {
            grid-template-columns: repeat(2, 1fr);
        }
    }


    @media (max-width: 750px) {

        .notices-page {
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

        .notice-summary {
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

        .notice-title-row {
            align-items: flex-start;
            flex-direction: column;
        }

        .notice-meta {
            flex-direction: column;
            align-items: flex-start;
            gap: 7px;
        }
    }
</style>