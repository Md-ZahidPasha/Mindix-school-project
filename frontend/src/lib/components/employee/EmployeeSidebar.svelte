<script lang="ts">
    import {
        LayoutDashboard,
        UserCircle,
        CalendarCheck,
        CalendarDays,
        CheckSquare,
        FileText,
        Bell,
        Bot,
        BarChart3,
        Settings,
        Briefcase,
        LogOut
    } from '@lucide/svelte';

    const menuItems = [
        {
            icon: LayoutDashboard,
            label: 'Dashboard',
            href: '/employee-dashboard'
        },
        {
            icon: UserCircle,
            label: 'My Profile',
            href: '/employee-dashboard/profile'
        },
        {
            icon: CalendarCheck,
            label: 'Attendance',
            href: '/employee-dashboard/attendance'
        },
        {
            icon: CalendarDays,
            label: 'My Schedule',
            href: '/employee-dashboard/schedule'
        },
        {
            icon: CheckSquare,
            label: 'Tasks',
            href: '/employee-dashboard/tasks'
        },
        {
            icon: CalendarDays,
            label: 'Leave',
            href: '/employee-dashboard/leave'
        },
        {
            icon: FileText,
            label: 'Documents',
            href: '/employee-dashboard/documents'
        },
        {
            icon: Bell,
            label: 'Notifications',
            href: '/employee-dashboard/notifications'
        },
        {
            icon: Bot,
            label: 'AI Assistant',
            href: '/employee-dashboard/ai-assistant'
        },
        {
            icon: BarChart3,
            label: 'Reports',
            href: '/employee-dashboard/reports'
        },
        {
            icon: Settings,
            label: 'Settings',
            href: '/employee-dashboard/settings'
        }
    ];

    function handleLogout() {
        window.location.href = '/login';
    }
</script>

<aside class="sidebar">

    <!-- BRAND -->
    <div class="brand">

        <div class="brand-icon">
            <Briefcase size={28} />
        </div>

        <div>
            <h2>PaperBuddy</h2>
            <span>Employee Portal</span>
        </div>

    </div>


    <!-- NAVIGATION -->
    <nav class="navigation">

        {#each menuItems as item}

            <a
                href={item.href}
                class="nav-item"
            >
                <item.icon size={21} />
                <span>{item.label}</span>
            </a>

        {/each}

    </nav>


    <!-- EMPLOYEE PROFILE -->
    <div class="profile-card">

        <div class="avatar">
            👨‍💼
        </div>

        <div>
            <strong>Arjun Kumar</strong>
            <span>Driving Department</span>
        </div>

    </div>


    <!-- LOGOUT -->
    <button
        class="logout"
        type="button"
        onclick={handleLogout}
    >
        <LogOut size={20} />
        <span>Logout</span>
    </button>

</aside>


<style>
    .sidebar {
        width: 280px;
        height: 100vh;
        position: fixed;
        left: 0;
        top: 0;
        background: #15315B;
        display: flex;
        flex-direction: column;
        padding: 28px 20px;
        box-sizing: border-box;
        z-index: 10;
        overflow: hidden;
    }


    /* BRAND */

    .brand {
        display: flex;
        align-items: center;
        gap: 14px;
        margin-bottom: 36px;
    }

    .brand-icon {
        width: 52px;
        height: 52px;
        display: flex;
        align-items: center;
        justify-content: center;
        background: #2563EB;
        color: white;
        border-radius: 14px;
    }

    .brand h2 {
        margin: 0;
        font-size: 24px;
        font-weight: 800;
        color: white;
    }

    .brand span {
        display: block;
        margin-top: 3px;
        font-size: 12px;
        color: rgba(255, 255, 255, 0.75);
    }


    /* NAVIGATION */

    .navigation {
        flex: 1;
        display: flex;
        flex-direction: column;
        gap: 6px;
        overflow-y: auto;
        padding-right: 6px;
        scrollbar-width: none;
    }

    .navigation::-webkit-scrollbar {
        display: none;
    }

    .nav-item {
        width: 100%;
        box-sizing: border-box;
        display: flex;
        align-items: center;
        gap: 14px;
        padding: 13px 14px;
        border-radius: 13px;
        text-decoration: none;
        color: white;
        font-size: 15px;
        font-weight: 600;
        transition: 0.25s;
    }

  

    .nav-item:hover {
        background: rgba(255, 255, 255, 0.08);
        color: white;
    }

   

    /* PROFILE */

    .profile-card {
        display: flex;
        align-items: center;
        gap: 12px;
        padding: 14px;
        margin-top: 14px;
        background: rgba(255, 255, 255, 0.08);
        border: 1px solid rgba(255, 255, 255, 0.12);
        border-radius: 15px;
        color: white;
    }

    .avatar {
        width: 44px;
        height: 44px;
        display: flex;
        align-items: center;
        justify-content: center;
        border-radius: 50%;
        background: #2563EB;
        font-size: 20px;
    }

    .profile-card strong {
        display: block;
        font-size: 14px;
    }

    .profile-card span {
        display: block;
        margin-top: 3px;
        font-size: 12px;
        color: rgba(255, 255, 255, 0.7);
    }


    /* LOGOUT */

    .logout {
        width: 100%;
        display: flex;
        align-items: center;
        gap: 14px;
        padding: 14px 18px;
        margin-top: 14px;
        border: none;
        border-radius: 14px;
        background: white;
        color: #DC2626;
        font-size: 15px;
        font-weight: 600;
        cursor: pointer;
    }

    .logout:hover {
        background: #fef2f2;
    }


    /* RESPONSIVE */

    @media (max-width: 1100px) {

        .sidebar {
            width: 250px;
        }
    }


    @media (max-width: 800px) {

        .sidebar {
            position: relative;
            width: 100%;
            height: auto;
        }
    }
</style>