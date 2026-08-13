<script lang="ts">
    const menuItems = [
        { label: 'Dashboard', icon: '⌂' },
        { label: 'My Children', icon: '♧' },
        { label: 'Attendance', icon: '☑' },
        { label: 'Academic Performance', icon: '▤' },
        { label: 'Exams & Results', icon: '▣' },
        { label: 'Assignments', icon: '✓' },
        { label: 'Fees & Payments', icon: '₹' },
        { label: 'Certificates', icon: '▤' },
        { label: 'Notices', icon: '♢' },
        { label: 'Notifications', icon: '◈' },
        { label: 'AI Assistant', icon: '✦' }
    ];

    function getHref(label: string) {
        switch (label) {
            case 'Dashboard':
                return '/parent-dashboard';

            case 'My Children':
                return '/parent-dashboard/children';

            case 'Attendance':
                return '/parent-dashboard/attendance';

            case 'Academic Performance':
                return '/parent-dashboard/performance';

            case 'Exams & Results':
                return '/parent-dashboard/exams';

            case 'Assignments':
                return '/parent-dashboard/assignments';

            case 'Fees & Payments':
                return '/parent-dashboard/fees';

            case 'Certificates':
                return '/parent-dashboard/certificates';

            case 'Notices':
                return '/parent-dashboard/notices';

            case 'Notifications':
                return '/parent-dashboard/notifications';

            case 'AI Assistant':
                return '/parent-dashboard/ai-assistant';

            default:
                return '/parent-dashboard';
        }
    }
    function handleLogout() {
    // API/session logout will be connected tomorrow.
    window.location.href = '/login';
}
</script>

<aside class="sidebar">

    <!-- BRAND -->
    <div class="brand">
        <div class="brand-icon">📖</div>

        <div class="brand-text">
            <h2>PaperBuddy</h2>
            <p>School Management System</p>
        </div>
    </div>


    <!-- NAVIGATION -->
    <nav class="navigation" aria-label="Parent navigation">

        {#each menuItems as item}

            <a
                href={getHref(item.label)}
                class="nav-item"
            >
                <span class="nav-icon">{item.icon}</span>

                <span>{item.label}</span>
            </a>

        {/each}

    </nav>


    <!-- BOTTOM -->
    <div class="sidebar-bottom">

        <a
            href="/parent-dashboard/profile"
            class="profile-link"
        >
            <span class="bottom-icon">◎</span>
            <span>Profile</span>
        </a>

        <button
            class="logout"
            type="button"
            onclick={handleLogout}
        >
            <span class="logout-icon">↪</span>
            <span>Logout</span>
        </button>

    </div>

</aside>


<style>
    .sidebar {
        width: 250px;
        min-height: 100vh;

        display: flex;
        flex-direction: column;

        background: #102a56;
        color: white;

        padding: 22px 14px;

        box-sizing: border-box;

        flex-shrink: 0;
    }


    /* BRAND */

    .brand {
        display: flex;
        align-items: center;

        gap: 10px;

        padding: 4px 8px 24px;
    }

    .brand-icon {
        width: 42px;
        height: 42px;

        display: flex;
        align-items: center;
        justify-content: center;

        background: #1f5fe5;

        border-radius: 10px;

        font-size: 22px;

        flex-shrink: 0;
    }

    .brand-text {
        min-width: 0;
    }

    .brand h2 {
        margin: 0;

        font-size: 21px;
        font-weight: 700;
    }

    .brand p {
        margin: 3px 0 0;

        font-size: 10px;

        color: #d7e2f4;
    }


    /* NAVIGATION */

    .navigation {
        display: flex;
        flex-direction: column;

        gap: 5px;

        overflow-y: auto;

        scrollbar-width: none;
    }

    .navigation::-webkit-scrollbar {
        display: none;
    }

    .nav-item {
        display: flex;
        align-items: center;

        gap: 13px;

        min-height: 44px;

        padding: 0 14px;

        border-radius: 10px;

        color: #e8eef8;

        text-decoration: none;

        font-size: 14px;
        font-weight: 500;

        transition:
            background 0.2s ease,
            color 0.2s ease;
    }

    .nav-item:hover {
        background: rgba(255, 255, 255, 0.1);

        color: white;
    }

    .nav-item:active {
        background: rgba(255, 255, 255, 0.14);
    }


    /* ICONS */

    .nav-icon,
    .bottom-icon,
    .logout-icon {
        width: 22px;

        display: inline-flex;
        align-items: center;
        justify-content: center;

        text-align: center;

        font-size: 18px;

        flex-shrink: 0;
    }


    /* BOTTOM */

    .sidebar-bottom {
        margin-top: auto;

        padding-top: 20px;

        border-top: 1px solid rgba(255, 255, 255, 0.14);
    }

    .profile-link {
        display: flex;
        align-items: center;

        gap: 13px;

        min-height: 44px;

        padding: 0 14px;

        margin-bottom: 8px;

        border-radius: 10px;

        color: #e8eef8;

        text-decoration: none;

        font-size: 14px;
        font-weight: 500;

        transition:
            background 0.2s ease,
            color 0.2s ease;
    }

    .profile-link:hover {
        background: rgba(255, 255, 255, 0.1);

        color: white;
    }


    /* LOGOUT */

    .logout {
        width: 100%;

        display: flex;
        align-items: center;

        gap: 13px;

        min-height: 44px;

        padding: 0 14px;

        border: none;

        border-radius: 10px;

        background: transparent;

        color: #ff7777;

        font: inherit;

        font-size: 14px;
        font-weight: 500;

        cursor: pointer;

        text-align: left;

        transition:
            background 0.2s ease,
            color 0.2s ease;
    }

    .logout:hover {
        background: rgba(255, 255, 255, 0.08);

        color: #ff8b8b;
    }


    /* RESPONSIVE */

    @media (max-width: 900px) {
        .sidebar {
            width: 220px;
        }

        .nav-item,
        .profile-link,
        .logout {
            font-size: 13px;
        }
    }
</style>