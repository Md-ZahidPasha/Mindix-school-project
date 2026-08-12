<script lang="ts">
    import PrincipalSidebar from '$lib/components/principal/PrincipalSidebar.svelte';

    type NotificationType =
        | 'leave'
        | 'notice'
        | 'assignment'
        | 'attendance'
        | 'system';

    type Priority = 'normal' | 'important';

    type Notification = {
        id: number;
        type: NotificationType;
        title: string;
        message: string;
        date: string;
        time: string;
        priority: Priority;
        read: boolean;
    };

    let selectedFilter = $state<'all' | 'unread' | 'important'>('all');

    let searchText = $state('');

    let notifications = $state<Notification[]>([
        {
            id: 1,
            type: 'leave',
            title: 'Teacher Leave Request',
            message:
                'Rahul Sharma (TCH001) submitted a leave request for 18 Aug - 19 Aug.',
            date: '12 Aug 2026',
            time: '10:30 AM',
            priority: 'important',
            read: false
        },
        {
            id: 2,
            type: 'leave',
            title: 'Employee Leave Request',
            message:
                'Ravi Kumar (EMP002) submitted a leave request for 22 Aug.',
            date: '12 Aug 2026',
            time: '09:45 AM',
            priority: 'important',
            read: false
        },
        {
            id: 3,
            type: 'notice',
            title: 'School Notice',
            message:
                'Independence Day celebration arrangements have been updated.',
            date: '11 Aug 2026',
            time: '04:20 PM',
            priority: 'normal',
            read: true
        },
        {
            id: 4,
            type: 'assignment',
            title: 'Assignment Activity',
            message:
                'Students from Class 10-A have submitted new assignments.',
            date: '11 Aug 2026',
            time: '02:15 PM',
            priority: 'normal',
            read: false
        },
        {
            id: 5,
            type: 'attendance',
            title: 'Attendance Update',
            message:
                'Teacher attendance records for yesterday have been updated.',
            date: '11 Aug 2026',
            time: '11:10 AM',
            priority: 'normal',
            read: true
        },
        {
            id: 6,
            type: 'system',
            title: 'System Notification',
            message:
                'The school management system has been successfully updated.',
            date: '10 Aug 2026',
            time: '06:00 PM',
            priority: 'normal',
            read: true
        }
    ]);

    let filteredNotifications = $derived(
        notifications.filter((notification) => {
            const filterMatch =
                selectedFilter === 'all' ||
                (selectedFilter === 'unread' && !notification.read) ||
                (selectedFilter === 'important' &&
                    notification.priority === 'important');

            const query = searchText.trim().toLowerCase();

            const searchMatch =
                !query ||
                notification.title.toLowerCase().includes(query) ||
                notification.message.toLowerCase().includes(query);

            return filterMatch && searchMatch;
        })
    );

    let unreadCount = $derived(
        notifications.filter((notification) => !notification.read).length
    );

    let importantCount = $derived(
        notifications.filter(
            (notification) => notification.priority === 'important'
        ).length
    );

    function markAsRead(id: number) {
        notifications = notifications.map((notification) =>
            notification.id === id
                ? { ...notification, read: true }
                : notification
        );
    }

    function markAllAsRead() {
        notifications = notifications.map((notification) => ({
            ...notification,
            read: true
        }));
    }

    function getIcon(type: NotificationType) {
        if (type === 'leave') return '▢';
        if (type === 'notice') return '♢';
        if (type === 'assignment') return '✓';
        if (type === 'attendance') return '☑';

        return '●';
    }

    function getTypeLabel(type: NotificationType) {
        if (type === 'leave') return 'Leave';
        if (type === 'notice') return 'Notice';
        if (type === 'assignment') return 'Assignment';
        if (type === 'attendance') return 'Attendance';

        return 'System';
    }
</script>


<div class="principal-layout">

    <PrincipalSidebar />

    <main class="main-content">

        <div class="notifications-page">

            <!-- PAGE HEADER -->

            <header class="page-header">

                <div>
                    <h1>Notifications</h1>

                    <p>
                        Stay updated with important activities and notices from your institution.
                    </p>
                </div>

                {#if unreadCount > 0}

                    <button
                        type="button"
                        class="mark-all-button"
                        onclick={markAllAsRead}
                    >
                        Mark All as Read
                    </button>

                {/if}

            </header>


            <!-- SUMMARY -->

            <section class="summary-grid">

                <div class="summary-card">

                    <div class="summary-icon unread">
                        🔔
                    </div>

                    <div>
                        <span>Unread</span>
                        <strong>{unreadCount}</strong>
                    </div>

                </div>


                <div class="summary-card">

                    <div class="summary-icon important">
                        !
                    </div>

                    <div>
                        <span>Important</span>
                        <strong>{importantCount}</strong>
                    </div>

                </div>


                <div class="summary-card">

                    <div class="summary-icon total">
                        ♢
                    </div>

                    <div>
                        <span>Total Notifications</span>
                        <strong>{notifications.length}</strong>
                    </div>

                </div>

            </section>


            <!-- FILTERS -->

            <section class="filter-card">

                <div class="filter-buttons">

                    <button
                        type="button"
                        class:active={selectedFilter === 'all'}
                        onclick={() => (selectedFilter = 'all')}
                    >
                        All
                    </button>

                    <button
                        type="button"
                        class:active={selectedFilter === 'unread'}
                        onclick={() => (selectedFilter = 'unread')}
                    >
                        Unread
                    </button>

                    <button
                        type="button"
                        class:active={selectedFilter === 'important'}
                        onclick={() => (selectedFilter = 'important')}
                    >
                        Important
                    </button>

                </div>


                <div class="search-box">

                    <span>⌕</span>

                    <input
                        type="text"
                        bind:value={searchText}
                        placeholder="Search notifications..."
                    />

                </div>

            </section>


            <!-- NOTIFICATION LIST -->

            <section class="notification-section">

                <div class="section-header">

                    <div>
                        <h2>Recent Notifications</h2>

                        <p>
                            Important updates and activities requiring your attention.
                        </p>
                    </div>

                    <span class="notification-count">
                        {filteredNotifications.length} Notifications
                    </span>

                </div>


                {#if filteredNotifications.length > 0}

                    <div class="notification-list">

                        {#each filteredNotifications as notification}

                            <article
                                class:unread-card={!notification.read}
                                class="notification-card"
                            >

                                <!-- ICON -->

                                <div
                                    class:leave-icon={notification.type === 'leave'}
                                    class:notice-icon={notification.type === 'notice'}
                                    class:assignment-icon={notification.type === 'assignment'}
                                    class:attendance-icon={notification.type === 'attendance'}
                                    class:system-icon={notification.type === 'system'}
                                    class="notification-icon"
                                >
                                    {getIcon(notification.type)}
                                </div>


                                <!-- CONTENT -->

                                <div class="notification-content">

                                    <div class="notification-top">

                                        <div>

                                            <span class="notification-type">
                                                {getTypeLabel(notification.type)}
                                            </span>

                                            <h3>
                                                {notification.title}
                                            </h3>

                                        </div>


                                        <div class="notification-meta">

                                            {#if notification.priority === 'important'}

                                                <span class="important-badge">
                                                    Important
                                                </span>

                                            {/if}

                                            {#if !notification.read}

                                                <span class="unread-badge">
                                                    Unread
                                                </span>

                                            {/if}

                                        </div>

                                    </div>


                                    <p class="notification-message">
                                        {notification.message}
                                    </p>


                                    <div class="notification-bottom">

                                        <span class="date">
                                            {notification.date}
                                            ·
                                            {notification.time}
                                        </span>


                                        {#if !notification.read}

                                            <button
                                                type="button"
                                                class="read-button"
                                                onclick={() =>
                                                    markAsRead(notification.id)
                                                }
                                            >
                                                Mark as Read
                                            </button>

                                        {:else}

                                            <span class="read-label">
                                                Read
                                            </span>

                                        {/if}

                                    </div>

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
                            No notifications found
                        </h3>

                        <p>
                            There are no notifications matching your current filter.
                        </p>

                    </div>

                {/if}

            </section>

        </div>

    </main>

</div>


<style>

    .principal-layout {
        display: flex;
        min-height: 100vh;
        background: #f7f9fc;
    }


    .main-content {
        flex: 1;
        min-width: 0;
    }


    .notifications-page {
        min-height: 100vh;
        padding: 28px 32px;
        box-sizing: border-box;
        background: #f7f9fc;
    }


    /* HEADER */

    .page-header {
        display: flex;
        align-items: center;
        justify-content: space-between;
        gap: 20px;
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


    .mark-all-button {
        height: 40px;
        padding: 0 15px;
        border: 1px solid #dbe3ef;
        border-radius: 9px;
        background: white;
        color: #2563eb;
        font-size: 12px;
        font-weight: 600;
        cursor: pointer;
    }


    .mark-all-button:hover {
        background: #eef4ff;
    }


    /* SUMMARY */

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


    .summary-icon.unread {
        background: #eef4ff;
        color: #2563eb;
    }


    .summary-icon.important {
        background: #fff7ed;
        color: #ea580c;
    }


    .summary-icon.total {
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


    /* FILTER */

    .filter-card {
        display: flex;
        align-items: center;
        justify-content: space-between;
        gap: 18px;
        padding: 18px 20px;
        margin-bottom: 24px;
        background: white;
        border: 1px solid #e5eaf2;
        border-radius: 16px;
        box-shadow:
            0 4px 14px
            rgba(15, 23, 42, 0.03);
    }


    .filter-buttons {
        display: flex;
        gap: 7px;
    }


    .filter-buttons button {
        height: 36px;
        padding: 0 13px;
        border: 1px solid #dbe3ef;
        border-radius: 8px;
        background: white;
        color: #64748b;
        font-size: 11px;
        font-weight: 600;
        cursor: pointer;
    }


    .filter-buttons button:hover {
        background: #f8fafc;
    }


    .filter-buttons button.active {
        border-color: #2563eb;
        background: #2563eb;
        color: white;
    }


    .search-box {
        width: 260px;
        height: 38px;
        display: flex;
        align-items: center;
        gap: 8px;
        padding: 0 11px;
        box-sizing: border-box;
        border: 1px solid #dbe3ef;
        border-radius: 9px;
        background: white;
    }


    .search-box span {
        color: #64748b;
        font-size: 18px;
    }


    .search-box input {
        width: 100%;
        border: none;
        outline: none;
        color: #1e293b;
        font-size: 11px;
    }


    /* SECTION */

    .section-header {
        display: flex;
        align-items: center;
        justify-content: space-between;
        gap: 15px;
        margin-bottom: 14px;
    }


    .section-header h2 {
        margin: 0;
        color: #14213d;
        font-size: 20px;
    }


    .section-header p {
        margin: 5px 0 0;
        color: #64748b;
        font-size: 13px;
    }


    .notification-count {
        padding: 7px 11px;
        border-radius: 8px;
        background: #eef4ff;
        color: #2563eb;
        font-size: 11px;
        font-weight: 700;
    }


    /* NOTIFICATION CARD */

    .notification-list {
        display: flex;
        flex-direction: column;
        gap: 12px;
    }


    .notification-card {
        display: flex;
        gap: 15px;
        padding: 18px;
        background: white;
        border: 1px solid #e5eaf2;
        border-radius: 14px;
        box-shadow:
            0 4px 14px
            rgba(15, 23, 42, 0.03);
    }


    .notification-card.unread-card {
        border-left: 3px solid #2563eb;
        background: #fbfdff;
    }


    .notification-icon {
        width: 44px;
        height: 44px;
        flex-shrink: 0;
        display: flex;
        align-items: center;
        justify-content: center;
        border-radius: 11px;
        font-size: 18px;
        font-weight: 700;
    }


    .leave-icon {
        background: #fff7ed;
        color: #ea580c;
    }


    .notice-icon {
        background: #eef4ff;
        color: #2563eb;
    }


    .assignment-icon {
        background: #f0fdf4;
        color: #16a34a;
    }


    .attendance-icon {
        background: #f5f3ff;
        color: #7c3aed;
    }


    .system-icon {
        background: #f1f5f9;
        color: #475569;
    }


    .notification-content {
        flex: 1;
        min-width: 0;
    }


    .notification-top {
        display: flex;
        align-items: flex-start;
        justify-content: space-between;
        gap: 15px;
    }


    .notification-type {
        display: block;
        margin-bottom: 3px;
        color: #2563eb;
        font-size: 9px;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }


    .notification-content h3 {
        margin: 0;
        color: #14213d;
        font-size: 14px;
    }


    .notification-message {
        max-width: 850px;
        margin: 7px 0 0;
        color: #64748b;
        font-size: 12px;
        line-height: 1.5;
    }


    .notification-meta {
        display: flex;
        align-items: center;
        gap: 6px;
        flex-shrink: 0;
    }


    .important-badge,
    .unread-badge {
        padding: 5px 8px;
        border-radius: 6px;
        font-size: 9px;
        font-weight: 700;
    }


    .important-badge {
        background: #fff7ed;
        color: #ea580c;
    }


    .unread-badge {
        background: #eef4ff;
        color: #2563eb;
    }


    .notification-bottom {
        display: flex;
        align-items: center;
        justify-content: space-between;
        gap: 15px;
        margin-top: 12px;
    }


    .date {
        color: #94a3b8;
        font-size: 10px;
    }


    .read-button {
        padding: 6px 10px;
        border: 1px solid #dbe3ef;
        border-radius: 7px;
        background: white;
        color: #2563eb;
        font-size: 10px;
        font-weight: 600;
        cursor: pointer;
    }


    .read-button:hover {
        background: #eef4ff;
    }


    .read-label {
        color: #94a3b8;
        font-size: 10px;
    }


    /* EMPTY */

    .empty-state {
        padding: 55px 20px;
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


    /* RESPONSIVE */

    @media (max-width: 850px) {

        .notifications-page {
            padding: 22px;
        }


        .summary-grid {
            grid-template-columns: 1fr;
        }


        .filter-card {
            align-items: stretch;
            flex-direction: column;
        }


        .search-box {
            width: 100%;
        }

    }


    @media (max-width: 600px) {

        .notifications-page {
            padding: 18px;
        }


        .page-header {
            align-items: flex-start;
            flex-direction: column;
        }


        .mark-all-button {
            width: 100%;
        }


        .filter-buttons {
            flex-wrap: wrap;
        }


        .notification-card {
            align-items: flex-start;
        }


        .notification-top {
            flex-direction: column;
            gap: 8px;
        }


        .notification-meta {
            flex-wrap: wrap;
        }

    }

</style>