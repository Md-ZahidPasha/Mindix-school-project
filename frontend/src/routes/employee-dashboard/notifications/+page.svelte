<script lang="ts">
    import {
        Bell,
        CheckCircle2,
        CalendarDays,
        FileText,
        AlertCircle,
        Info,
        Clock3,
        Check,
        Trash2
    } from '@lucide/svelte';

    let selectedFilter = $state('All');

    const filters = [
        'All',
        'Unread',
        'Attendance',
        'Tasks',
        'Schedule',
        'General'
    ];

    let notifications = $state([
        {
            id: 1,
            title: 'Morning route completed',
            message:
                'Your morning school route has been marked as completed successfully.',
            category: 'Schedule',
            time: '15 minutes ago',
            date: '12 Aug 2026',
            read: false,
            icon: CheckCircle2,
            className: 'green'
        },
        {
            id: 2,
            title: 'New task assigned',
            message:
                'Vehicle Safety Inspection has been assigned to you. Please complete it before 12:30 PM.',
            category: 'Tasks',
            time: '1 hour ago',
            date: '12 Aug 2026',
            read: false,
            icon: AlertCircle,
            className: 'orange'
        },
        {
            id: 3,
            title: 'Attendance marked',
            message:
                'Your attendance for today has been recorded successfully.',
            category: 'Attendance',
            time: '3 hours ago',
            date: '12 Aug 2026',
            read: true,
            icon: Clock3,
            className: 'blue'
        },
        {
            id: 4,
            title: 'Staff transport scheduled',
            message:
                'You have been assigned a staff transport duty at 10:30 AM today.',
            category: 'Schedule',
            time: 'Yesterday',
            date: '11 Aug 2026',
            read: true,
            icon: CalendarDays,
            className: 'purple'
        },
        {
            id: 5,
            title: 'Document updated',
            message:
                'Your vehicle assignment document has been updated in the employee portal.',
            category: 'General',
            time: 'Yesterday',
            date: '11 Aug 2026',
            read: true,
            icon: FileText,
            className: 'blue'
        },
        {
            id: 6,
            title: 'Leave request received',
            message:
                'Your casual leave request for 18 Aug - 19 Aug 2026 is awaiting approval.',
            category: 'General',
            time: '2 days ago',
            date: '10 Aug 2026',
            read: true,
            icon: Info,
            className: 'orange'
        },
        {
            id: 7,
            title: 'Weekly schedule available',
            message:
                'Your schedule for 10 Aug - 16 Aug 2026 is now available to view.',
            category: 'Schedule',
            time: '3 days ago',
            date: '09 Aug 2026',
            read: true,
            icon: CalendarDays,
            className: 'purple'
        }
    ]);

    const filteredNotifications = $derived(
        notifications.filter((notification) => {
            if (selectedFilter === 'Unread') {
                return !notification.read;
            }

            if (selectedFilter === 'All') {
                return true;
            }

            return notification.category === selectedFilter;
        })
    );

    const unreadCount = $derived(
        notifications.filter((notification) => !notification.read).length
    );

    function markAsRead(id: number) {
        const notification = notifications.find(
            (item) => item.id === id
        );

        if (notification) {
            notification.read = true;
            notifications = notifications;
        }
    }

    function markAllAsRead() {
        notifications.forEach((notification) => {
            notification.read = true;
        });

        notifications = notifications;
    }

    function deleteNotification(id: number) {
        notifications = notifications.filter(
            (notification) => notification.id !== id
        );
    }
</script>

<svelte:head>
    <title>Notifications | Employee Dashboard</title>
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
                    Stay updated with your tasks, attendance and schedule.
                </p>
            </div>

        </div>


        <div class="header-actions">

            {#if unreadCount > 0}

                <span class="unread-count">
                    {unreadCount} Unread
                </span>

                <button
                    type="button"
                    class="mark-all"
                    onclick={markAllAsRead}
                >
                    <Check size={15} />
                    Mark all as read
                </button>

            {/if}

        </div>

    </div>


    <!-- SUMMARY -->
    <section class="summary-grid">

        <div class="summary-card">

            <div class="summary-icon blue">
                <Bell size={19} />
            </div>

            <div>
                <span>Total Notifications</span>

                <strong>
                    {notifications.length}
                </strong>

                <small>
                    All notifications
                </small>
            </div>

        </div>


        <div class="summary-card">

            <div class="summary-icon orange">
                <AlertCircle size={19} />
            </div>

            <div>
                <span>Unread</span>

                <strong>
                    {unreadCount}
                </strong>

                <small>
                    Need your attention
                </small>
            </div>

        </div>


        <div class="summary-card">

            <div class="summary-icon green">
                <CheckCircle2 size={19} />
            </div>

            <div>
                <span>Read</span>

                <strong>
                    {notifications.length - unreadCount}
                </strong>

                <small>
                    Already viewed
                </small>
            </div>

        </div>

    </section>


    <!-- FILTERS -->
    <section class="filter-card">

        <div class="filter-title">
            Notification Filter
        </div>

        <div class="filters">

            {#each filters as filter}

                <button
                    type="button"
                    class:active={selectedFilter === filter}
                    onclick={() => selectedFilter = filter}
                >
                    {filter}

                    {#if filter === 'Unread' && unreadCount > 0}
                        <span class="filter-count">
                            {unreadCount}
                        </span>
                    {/if}

                </button>

            {/each}

        </div>

    </section>


    <!-- NOTIFICATIONS -->
    <section class="notification-list">

        {#if filteredNotifications.length > 0}

            {#each filteredNotifications as notification}

                <article
                    class:unread={!notification.read}
                    class="notification-card"
                >

                    <div class={`notification-icon ${notification.className}`}>
                        <notification.icon size={20} />
                    </div>


                    <div class="notification-content">

                        <div class="notification-header">

                            <div>

                                <div class="title-line">

                                    <h2>
                                        {notification.title}
                                    </h2>

                                    {#if !notification.read}
                                        <span class="new-badge">
                                            New
                                        </span>
                                    {/if}

                                </div>

                                <span class="category">
                                    {notification.category}
                                </span>

                            </div>

                            <span class="notification-time">
                                {notification.time}
                            </span>

                        </div>


                        <p>
                            {notification.message}
                        </p>


                        <div class="notification-footer">

                            <span class="notification-date">
                                <CalendarDays size={12} />
                                {notification.date}
                            </span>


                            <div class="notification-actions">

                                {#if !notification.read}

                                    <button
                                        type="button"
                                        onclick={() =>
                                            markAsRead(notification.id)
                                        }
                                    >
                                        <Check size={13} />
                                        Mark as read
                                    </button>

                                {/if}

                                <button
                                    type="button"
                                    class="delete-button"
                                    onclick={() =>
                                        deleteNotification(notification.id)
                                    }
                                >
                                    <Trash2 size={13} />
                                    Delete
                                </button>

                            </div>

                        </div>

                    </div>

                </article>

            {/each}

        {:else}

            <div class="empty-state">

                <div class="empty-icon">
                    <Bell size={27} />
                </div>

                <h2>
                    No Notifications
                </h2>

                <p>
                    There are no notifications matching this filter.
                </p>

            </div>

        {/if}

    </section>


    <!-- INFORMATION -->
    <section class="information-note">

        <div class="information-icon">
            <Info size={18} />
        </div>

        <div>

            <strong>
                Notification Information
            </strong>

            <p>
                Notifications shown here are currently demo data.
                During API integration, real-time notifications from
                attendance, tasks, schedules, leave and administration
                will be loaded from the backend.
            </p>

        </div>

    </section>

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

    .header-actions {
        display: flex;
        align-items: center;
        gap: 9px;
    }

    .unread-count {
        padding: 6px 9px;
        border-radius: 7px;
        background: #fff7ed;
        color: #ea580c;
        font-size: 9px;
        font-weight: 700;
    }

    .mark-all {
        display: flex;
        align-items: center;
        gap: 6px;
        padding: 9px 12px;
        border: 1px solid #dbe3ef;
        border-radius: 8px;
        background: white;
        color: #475569;
        font-size: 9px;
        font-weight: 700;
        cursor: pointer;
    }

    .mark-all:hover {
        background: #f8fafc;
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


    /* FILTER */

    .filter-card {
        display: flex;
        align-items: center;
        gap: 18px;
        padding: 14px 17px;
        margin-bottom: 17px;
        border: 1px solid #e2e8f0;
        border-radius: 13px;
        background: white;
    }

    .filter-title {
        color: #475569;
        font-size: 10px;
        font-weight: 700;
        white-space: nowrap;
    }

    .filters {
        display: flex;
        align-items: center;
        gap: 7px;
        flex-wrap: wrap;
    }

    .filters button {
        display: flex;
        align-items: center;
        gap: 5px;
        padding: 7px 10px;
        border: 1px solid #dbe3ef;
        border-radius: 7px;
        background: white;
        color: #64748b;
        font-size: 8px;
        font-weight: 600;
        cursor: pointer;
    }

    .filters button:hover {
        background: #f8fafc;
    }

    .filters button.active {
        border-color: #2563eb;
        background: #2563eb;
        color: white;
    }

    .filter-count {
        min-width: 15px;
        height: 15px;
        display: inline-flex;
        align-items: center;
        justify-content: center;
        border-radius: 50%;
        background: #fff;
        color: #2563eb;
        font-size: 7px;
        font-weight: 800;
    }


    /* NOTIFICATION LIST */

    .notification-list {
        display: flex;
        flex-direction: column;
        gap: 11px;
        margin-bottom: 20px;
    }

    .notification-card {
        display: flex;
        align-items: flex-start;
        gap: 14px;
        padding: 18px;
        border: 1px solid #e2e8f0;
        border-radius: 14px;
        background: white;
        box-shadow: 0 3px 12px rgba(15, 23, 42, 0.03);
        transition: 0.2s;
    }

    .notification-card:hover {
        border-color: #cbd5e1;
        box-shadow: 0 5px 18px rgba(15, 23, 42, 0.05);
    }

    .notification-card.unread {
        border-left: 3px solid #2563eb;
        background: #fcfdff;
    }

    .notification-icon {
        width: 43px;
        height: 43px;
        display: flex;
        align-items: center;
        justify-content: center;
        flex-shrink: 0;
        border-radius: 11px;
    }

    .notification-icon.blue {
        background: #eef4ff;
        color: #2563eb;
    }

    .notification-icon.green {
        background: #ecfdf5;
        color: #059669;
    }

    .notification-icon.orange {
        background: #fff7ed;
        color: #ea580c;
    }

    .notification-icon.purple {
        background: #f5f3ff;
        color: #7c3aed;
    }

    .notification-content {
        flex: 1;
        min-width: 0;
    }

    .notification-header {
        display: flex;
        align-items: flex-start;
        justify-content: space-between;
        gap: 15px;
    }

    .title-line {
        display: flex;
        align-items: center;
        gap: 7px;
        flex-wrap: wrap;
    }

    .title-line h2 {
        margin: 0;
        color: #0f172a;
        font-size: 14px;
    }

    .new-badge {
        padding: 3px 6px;
        border-radius: 5px;
        background: #eff6ff;
        color: #2563eb;
        font-size: 7px;
        font-weight: 800;
    }

    .category {
        display: block;
        margin-top: 4px;
        color: #94a3b8;
        font-size: 8px;
    }

    .notification-time {
        color: #94a3b8;
        font-size: 8px;
        white-space: nowrap;
    }

    .notification-content > p {
        margin: 9px 0 12px;
        color: #64748b;
        font-size: 10px;
        line-height: 1.5;
    }

    .notification-footer {
        display: flex;
        align-items: center;
        justify-content: space-between;
        gap: 15px;
        padding-top: 10px;
        border-top: 1px solid #f1f5f9;
    }

    .notification-date {
        display: flex;
        align-items: center;
        gap: 5px;
        color: #94a3b8;
        font-size: 8px;
    }

    .notification-actions {
        display: flex;
        align-items: center;
        gap: 8px;
    }

    .notification-actions button {
        display: flex;
        align-items: center;
        gap: 4px;
        padding: 5px 7px;
        border: none;
        border-radius: 6px;
        background: #f1f5f9;
        color: #64748b;
        font-size: 7px;
        font-weight: 700;
        cursor: pointer;
    }

    .notification-actions button:hover {
        background: #e2e8f0;
        color: #334155;
    }

    .notification-actions .delete-button:hover {
        background: #fef2f2;
        color: #dc2626;
    }


    /* EMPTY */

    .empty-state {
        padding: 65px 20px;
        border: 1px solid #e2e8f0;
        border-radius: 14px;
        background: white;
        text-align: center;
    }

    .empty-icon {
        width: 50px;
        height: 50px;
        display: flex;
        align-items: center;
        justify-content: center;
        margin: 0 auto 11px;
        border-radius: 50%;
        background: #f1f5f9;
        color: #94a3b8;
    }

    .empty-state h2 {
        margin: 0;
        color: #334155;
        font-size: 15px;
    }

    .empty-state p {
        margin: 5px 0 0;
        color: #94a3b8;
        font-size: 10px;
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

        .summary-grid {
            grid-template-columns: 1fr;
        }

        .filter-card {
            align-items: flex-start;
            flex-direction: column;
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

        .header-actions {
            width: 100%;
        }

        .mark-all {
            flex: 1;
            justify-content: center;
        }

        .filter-card {
            padding: 13px;
        }

        .notification-card {
            padding: 15px;
        }

        .notification-header {
            align-items: flex-start;
            flex-direction: column;
            gap: 6px;
        }

        .notification-footer {
            align-items: flex-start;
            flex-direction: column;
        }

        .notification-actions {
            width: 100%;
        }
    }
</style>