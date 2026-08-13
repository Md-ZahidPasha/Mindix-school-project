<script lang="ts">
    import {
        Bell,
        CalendarDays,
        CheckCheck,
        ChevronDown,
        Clock3,
        FileText,
        GraduationCap,
        Megaphone,
        MessageSquare,
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

    const notifications = [
        {
            id: 1,
            title: 'First Term Examination Schedule Released',
            message:
                'The first term examination timetable has been published. Please check the examination schedule and help your child prepare accordingly.',
            category: 'Examination',
            date: '12 Aug 2026',
            time: '10:30 AM',
            priority: 'Important',
            read: false
        },
        {
            id: 2,
            title: 'New Assignment Added',
            message:
                'A new Mathematics assignment has been added for your child. Please check the Assignments section for details.',
            category: 'Assignment',
            date: '11 Aug 2026',
            time: '04:15 PM',
            priority: 'Normal',
            read: false
        },
        {
            id: 3,
            title: 'Fee Payment Reminder',
            message:
                'There is a pending fee amount for your child. Please complete the payment before the due date.',
            category: 'Fees',
            date: '10 Aug 2026',
            time: '01:20 PM',
            priority: 'Important',
            read: false
        },
        {
            id: 4,
            title: 'Parent-Teacher Meeting',
            message:
                'The next parent-teacher meeting is scheduled for 22 August. Meeting details will be shared through the school portal.',
            category: 'Meeting',
            date: '08 Aug 2026',
            time: '11:45 AM',
            priority: 'Normal',
            read: true
        },
        {
            id: 5,
            title: 'Attendance Update',
            message:
                'Your child has been marked present for today. Attendance information has been updated successfully.',
            category: 'Attendance',
            date: '08 Aug 2026',
            time: '09:10 AM',
            priority: 'Normal',
            read: true
        },
        {
            id: 6,
            title: 'School Holiday Notice',
            message:
                'The school will remain closed on 15 August on account of Independence Day.',
            category: 'School',
            date: '07 Aug 2026',
            time: '02:30 PM',
            priority: 'Normal',
            read: true
        },
        {
            id: 7,
            title: 'Certificate Issued',
            message:
                'A new certificate has been issued to your child. You can view and download it from the Certificates section.',
            category: 'Certificate',
            date: '05 Aug 2026',
            time: '03:40 PM',
            priority: 'Normal',
            read: false
        },
        {
            id: 8,
            title: 'Academic Performance Updated',
            message:
                'Your child’s latest academic performance information has been updated in the Parent Dashboard.',
            category: 'Academic',
            date: '03 Aug 2026',
            time: '12:10 PM',
            priority: 'Normal',
            read: true
        }
    ];

    function getSelectedChild() {
        return children.find(
            (child) => child.name === selectedChild
        );
    }

    let child = $derived(getSelectedChild());

    let unreadCount = $derived(
        notifications.filter(
            (notification) => !notification.read
        ).length
    );

    let importantCount = $derived(
        notifications.filter(
            (notification) =>
                notification.priority === 'Important'
        ).length
    );

    let filteredNotifications = $derived(
        activeFilter === 'All'
            ? notifications
            : activeFilter === 'Unread'
              ? notifications.filter(
                    (notification) => !notification.read
                )
              : activeFilter === 'Important'
                ? notifications.filter(
                      (notification) =>
                          notification.priority === 'Important'
                  )
                : notifications.filter(
                      (notification) =>
                          notification.category === activeFilter
                  )
    );

    function markAsRead(notificationId: number) {
        const notification = notifications.find(
            (item) => item.id === notificationId
        );

        if (notification) {
            notification.read = true;
        }
    }

    function markAllAsRead() {
        notifications.forEach(
            (notification) => {
                notification.read = true;
            }
        );
    }
</script>

<svelte:head>
    <title>Notifications | Parent Dashboard</title>
</svelte:head>

<div class="notifications-page">

    <!-- HEADER -->
    <div class="page-header">

        <div class="title-row">

            <div class="title-icon">
                <Bell size={24} />
            </div>

            <div>
                <h1>Notifications</h1>

                <p>
                    Stay updated with important information about your child.
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

        <div class="notification-summary">

            <span>Unread Notifications</span>

            <strong>{unreadCount}</strong>

            <small>
                Need your attention
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
                <span>Total Notifications</span>
                <strong>{notifications.length}</strong>
            </div>

        </div>


        <div class="summary-card">

            <div class="summary-icon orange">
                <MessageSquare size={21} />
            </div>

            <div>
                <span>Unread</span>
                <strong>{unreadCount}</strong>
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

            <div class="summary-icon green">
                <CheckCheck size={21} />
            </div>

            <div>
                <span>Read</span>

                <strong>
                    {notifications.length - unreadCount}
                </strong>

            </div>

        </div>

    </section>


    <!-- FILTER BAR -->
    <section class="card filter-card">

        <div class="filter-header">

            <div>

                <h2>Notification Center</h2>

                <p>
                    Filter notifications according to their status or category.
                </p>

            </div>


            {#if unreadCount > 0}

                <button
                    class="mark-all-button"
                    onclick={markAllAsRead}
                >
                    <CheckCheck size={14} />
                    Mark all as read
                </button>

            {/if}

        </div>


        <div class="filter-buttons">

            {#each [
                'All',
                'Unread',
                'Important',
                'Examination',
                'Assignment',
                'Fees',
                'Meeting',
                'Attendance',
                'School',
                'Certificate',
                'Academic'
            ] as filter}

                <button
                    class:active={activeFilter === filter}
                    onclick={() => activeFilter = filter}
                >
                    {filter}
                </button>

            {/each}

        </div>

    </section>


    <!-- NOTIFICATION LIST -->
    <section class="card">

        <div class="card-header">

            <div>

                <h2>
                    {activeFilter === 'All'
                        ? 'Latest Notifications'
                        : `${activeFilter} Notifications`}
                </h2>

                <p>
                    {filteredNotifications.length}
                    notification{filteredNotifications.length === 1 ? '' : 's'}
                    found.
                </p>

            </div>

        </div>


        <div class="notification-list">

            {#each filteredNotifications as notification}

                <article
                    class:unread-notification={!notification.read}
                    class:important-notification={
                        notification.priority === 'Important'
                    }
                    class="notification-card"
                >

                    <div class="notification-icon">

                        {#if notification.category === 'Examination'}

                            <FileText size={21} />

                        {:else if notification.category === 'Assignment'}

                            <GraduationCap size={21} />

                        {:else if notification.category === 'Fees'}

                            <ShieldAlert size={21} />

                        {:else if notification.category === 'Meeting'}

                            <MessageSquare size={21} />

                        {:else if notification.category === 'Attendance'}

                            <CheckCheck size={21} />

                        {:else if notification.category === 'Certificate'}

                            <FileText size={21} />

                        {:else if notification.category === 'Academic'}

                            <GraduationCap size={21} />

                        {:else}

                            <Megaphone size={21} />

                        {/if}

                    </div>


                    <div class="notification-content">

                        <div class="notification-title-row">

                            <div class="notification-title-area">

                                <div class="title-line">

                                    <h3>
                                        {notification.title}
                                    </h3>

                                    {#if !notification.read}

                                        <span class="new-badge">
                                            New
                                        </span>

                                    {/if}

                                </div>

                                <span class="notification-category">
                                    {notification.category}
                                </span>

                            </div>


                            {#if notification.priority === 'Important'}

                                <span class="priority important">
                                    Important
                                </span>

                            {:else}

                                <span class="priority normal">
                                    Normal
                                </span>

                            {/if}

                        </div>


                        <p class="notification-message">
                            {notification.message}
                        </p>


                        <div class="notification-footer">

                            <div class="notification-meta">

                                <span>
                                    <CalendarDays size={13} />
                                    {notification.date}
                                </span>

                                <span>
                                    <Clock3 size={13} />
                                    {notification.time}
                                </span>

                            </div>


                            {#if !notification.read}

                                <button
                                    class="read-button"
                                    onclick={() =>
                                        markAsRead(notification.id)
                                    }
                                >
                                    <CheckCheck size={13} />
                                    Mark as read
                                </button>

                            {:else}

                                <span class="read-label">
                                    <CheckCheck size={13} />
                                    Read
                                </span>

                            {/if}

                        </div>

                    </div>

                </article>

            {:else}

                <div class="empty-state">

                    <div class="empty-icon">
                        <Bell size={28} />
                    </div>

                    <h3>
                        No notifications found
                    </h3>

                    <p>
                        There are no notifications in this category.
                    </p>

                </div>

            {/each}

        </div>

    </section>


    <!-- NOTIFICATION INFORMATION -->
    <section class="notification-information">

        <div class="information-icon">
            <Bell size={19} />
        </div>

        <div>

            <strong>
                Never Miss an Important Update
            </strong>

            <p>
                Notifications may include examination updates,
                assignments, fee reminders, attendance information,
                school events and other important messages.
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
                Notification Information
            </strong>

            <p>
                Notifications shown here are currently demo data.
                During API integration, real notifications will
                be retrieved from the backend and displayed for
                the selected child.
            </p>

        </div>

    </div>

</div>


<style>
    .notifications-page {
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

    .notification-summary {
        min-width: 155px;
        padding: 12px 16px;
        border-radius: 11px;
        background: #fff7ed;
        text-align: center;
    }

    .notification-summary span {
        display: block;
        color: #64748b;
        font-size: 10px;
    }

    .notification-summary strong {
        display: block;
        margin: 2px 0;
        color: #ea580c;
        font-size: 24px;
    }

    .notification-summary small {
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

    .summary-icon.orange {
        background: #fff7ed;
        color: #ea580c;
    }

    .summary-icon.red {
        background: #fef2f2;
        color: #dc2626;
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


    /* FILTER CARD */

    .filter-card {
        margin-bottom: 20px;
    }

    .filter-header {
        display: flex;
        align-items: center;
        justify-content: space-between;
        gap: 15px;
        margin-bottom: 15px;
    }

    .filter-header h2 {
        margin: 0;
        color: #0f172a;
        font-size: 17px;
    }

    .filter-header p {
        margin: 4px 0 0;
        color: #64748b;
        font-size: 11px;
    }

    .mark-all-button {
        display: flex;
        align-items: center;
        gap: 6px;
        padding: 8px 11px;
        border: 1px solid #bfdbfe;
        border-radius: 8px;
        background: #eff6ff;
        color: #2563eb;
        font-size: 9px;
        font-weight: 700;
        cursor: pointer;
    }

    .mark-all-button:hover {
        background: #dbeafe;
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


    /* NOTIFICATION LIST */

    .notification-list {
        display: flex;
        flex-direction: column;
        gap: 12px;
    }

    .notification-card {
        display: flex;
        align-items: flex-start;
        gap: 14px;
        padding: 17px;
        border: 1px solid #e2e8f0;
        border-radius: 13px;
        background: #f8fafc;
        transition: 0.2s ease;
    }

    .notification-card:hover {
        border-color: #bfdbfe;
        box-shadow: 0 3px 10px rgba(37, 99, 235, 0.05);
    }

    .notification-card.unread-notification {
        background: #f8fbff;
        border-color: #bfdbfe;
    }

    .notification-card.important-notification {
        border-left: 4px solid #dc2626;
    }

    .notification-icon {
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

    .important-notification .notification-icon {
        background: #fef2f2;
        color: #dc2626;
    }

    .notification-content {
        flex: 1;
        min-width: 0;
    }

    .notification-title-row {
        display: flex;
        align-items: flex-start;
        justify-content: space-between;
        gap: 15px;
    }

    .notification-title-area {
        min-width: 0;
    }

    .title-line {
        display: flex;
        align-items: center;
        gap: 8px;
        flex-wrap: wrap;
    }

    .notification-title-row h3 {
        margin: 0;
        color: #0f172a;
        font-size: 14px;
    }

    .notification-category {
        display: inline-block;
        margin-top: 4px;
        color: #2563eb;
        font-size: 9px;
        font-weight: 700;
    }

    .new-badge {
        padding: 4px 6px;
        border-radius: 6px;
        background: #2563eb;
        color: white;
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

    .notification-message {
        margin: 10px 0 12px;
        color: #64748b;
        font-size: 10px;
        line-height: 1.55;
    }

    .notification-footer {
        display: flex;
        align-items: center;
        justify-content: space-between;
        gap: 15px;
    }

    .notification-meta {
        display: flex;
        align-items: center;
        flex-wrap: wrap;
        gap: 15px;
    }

    .notification-meta span {
        display: flex;
        align-items: center;
        gap: 5px;
        color: #64748b;
        font-size: 9px;
    }

    .read-button {
        display: flex;
        align-items: center;
        gap: 5px;
        padding: 6px 9px;
        border: 1px solid #dbe3ef;
        border-radius: 7px;
        background: white;
        color: #2563eb;
        font-size: 9px;
        font-weight: 600;
        cursor: pointer;
    }

    .read-button:hover {
        border-color: #93c5fd;
        background: #eff6ff;
    }

    .read-label {
        display: flex;
        align-items: center;
        gap: 4px;
        color: #059669;
        font-size: 9px;
        font-weight: 600;
    }


    /* INFORMATION */

    .notification-information {
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

    .notification-information strong {
        display: block;
        color: #1e3a8a;
        font-size: 11px;
    }

    .notification-information p {
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

        .notifications-page {
            padding: 24px;
        }

        .summary-grid {
            grid-template-columns: repeat(2, 1fr);
        }
    }


    @media (max-width: 750px) {

        .notifications-page {
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

        .notification-summary {
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

        .notification-title-row {
            align-items: flex-start;
            flex-direction: column;
        }

        .notification-footer {
            align-items: flex-start;
            flex-direction: column;
        }

        .notification-meta {
            flex-direction: column;
            align-items: flex-start;
            gap: 7px;
        }
    }
</style>