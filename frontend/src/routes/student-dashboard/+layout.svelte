<script lang="ts">
    import {
        LayoutDashboard,
        UserCircle,
        BookOpen,
        CalendarCheck,
        CalendarDays,
        ClipboardCheck,
        FileText,
        IndianRupee,
        Award,
        Bell,
        LogOut
    } from '@lucide/svelte';
    import { Bot } from '@lucide/svelte';

    let { children } = $props();

    const menuItems = [
        {
            icon: LayoutDashboard,
            label: 'Dashboard',
            href: '/student-dashboard'
        },
        {
            icon: UserCircle,
            label: 'My Profile',
            href: '/student-dashboard/profile'
        },
        {
            icon: CalendarCheck,
            label: 'Attendance',
            href: '/student-dashboard/attendance'
        },
        {
            icon: CalendarDays,
            label: 'My Timetable',
            href: '/student-dashboard/timetable'
        },
        {
            icon: ClipboardCheck,
            label: 'Assignments',
            href: '/student-dashboard/assignments'
        },
        {
            icon: FileText,
            label: 'Exams & Results',
            href: '/student-dashboard/exams'
        },
        {
            icon: IndianRupee,
            label: 'Fees & Payments',
            href: '/student-dashboard/fees'
        },
        {
            icon: Award,
            label: 'Certificates',
            href: '/student-dashboard/certificates'
        },
        {
            icon: BookOpen,
            label: 'Library',
            href: '/student-dashboard/library'
        },
        {
            icon: Bell,
            label: 'Notifications',
            href: '/student-dashboard/notifications'
        },
        {
            icon: Bot,
            label: 'AI Assistant',
            href: '/student-dashboard/ai-assistant'
        }
    ];
</script>

<div class="student-layout">
    <aside class="sidebar">
        <div class="brand">
            <div class="brand-icon">
                <BookOpen size={28} />
            </div>

            <div>
                <h2>PaperBuddy</h2>
                <span>Student Portal</span>
            </div>
        </div>

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

        <a href="/student-dashboard/profile" class="profile-card">
            <div class="avatar">👨‍🎓</div>

            <div class="profile-info">
                <strong>Student</strong>
                <span>Student Portal</span>
            </div>
        </a>

       <a href="/login" class="logout">
             <LogOut size={20} />
             <span>Logout</span>
       </a>
    </aside>

    <main class="student-content">
        {@render children()}
    </main>
</div>

<style>
    .student-layout {
        min-height: 100vh;
        background: #f8fafc;
        margin: 0;
        padding: 0;
    }

    .student-content {
        min-height: 100vh;
        margin-left: 280px;
        width: calc(100%-280px);
        box-sizing: border-box;
    }

    /* =========================
       SIDEBAR
       ========================= */

    .sidebar {
        position: fixed;
        top: 0;
        left: 0;
        z-index: 100;
        width: 280px;
        height: 100vh;
        padding: 28px 20px;
        box-sizing: border-box;
        background: #173764;
        color: white;
        display: flex;
        flex-direction: column;
    }

    .brand {
        display: flex;
        align-items: center;
        gap: 12px;
        margin-bottom: 30px;
    }

    .brand-icon {
        display: flex;
        align-items: center;
        justify-content: center;
        width: 48px;
        height: 48px;
        color: white;
        background: #2563eb;
        border-radius: 12px;
    }

    .brand h2 {
        margin: 0;
        color: white;
        font-size: 18px;
        font-weight: 800;
    }

    .brand span {
        display: block;
        margin-top: 3px;
        color: #cbd5e1;
        font-size: 11px;
    }

    /* =========================
       NAVIGATION
       ========================= */

    .navigation {
        display: flex;
        flex-direction: column;
        gap: 6px;

        flex: 1;
        min-height: 0;

        overflow-y: auto;
        overflow-x: hidden;
        padding-right: 4px;
    }
    
    /* =========================
   SIDEBAR SCROLLBAR
   ========================= */

.navigation::-webkit-scrollbar {
    width: 5px;
}

.navigation::-webkit-scrollbar-track {
    background: transparent;
}

.navigation::-webkit-scrollbar-thumb {
    background: rgba(255, 255, 255, 0.3);
    border-radius: 10px;
}

.navigation::-webkit-scrollbar-thumb:hover {
    background: rgba(255, 255, 255, 0.5);
}

    .nav-item {
        display: flex;
        align-items: center;
        gap: 12px;
        padding: 12px 14px;
        color: white;
        text-decoration: none;
        border-radius: 10px;
        font-size: 13px;
        font-weight: 600;
        transition:
            background 0.2s ease,
            color 0.2s ease;
    }

    .nav-item:hover {
        color: white;
        background: rgba(255, 255, 255, 0.1);
    }

    /* =========================
   PROFILE CARD
   ========================= */

.profile-card {
    display: flex;
    align-items: center;
    gap: 10px;

    margin-top: auto;
    padding: 14px;

    color: inherit;
    text-decoration: none;

    background: rgba(255, 255, 255, 0.08);
    border: 1px solid rgba(255, 255, 255, 0.12);
    border-radius: 12px;

    cursor: pointer;

    transition:
        background 0.2s ease,
        border-color 0.2s ease,
        transform 0.2s ease;
}

.profile-card:hover {
    background: rgba(255, 255, 255, 0.14);
    border-color: rgba(255, 255, 255, 0.2);
    transform: translateY(-1px);
}

.avatar {
    display: flex;
    align-items: center;
    justify-content: center;

    width: 38px;
    height: 38px;

    flex-shrink: 0;

    background: #2563eb;
    border-radius: 50%;

    font-size: 18px;
}

.profile-info {
    min-width: 0;
}

.profile-card strong {
    display: block;

    color: white;
    font-size: 12px;
    font-weight: 700;
}

.profile-card span {
    display: block;

    margin-top: 3px;

    color: #cbd5e1;
    font-size: 10px;
}

.logout {
    display: flex;
    align-items: center;
    gap: 10px;

    width: 100%;
    margin-top: 10px;
    padding: 11px 14px;

    box-sizing: border-box;

    color: #dc2626;
    background: transparent;

    border: none;
    border-radius: 10px;

    font-size: 13px;
    font-weight: 600;

    cursor: pointer;
    text-align: left;
    text-decoration: none;
}

.logout:hover {
    background: #fef2f2;
}

    /* =========================
       RESPONSIVE
       ========================= */

    @media (max-width: 1100px) {
        .student-content {
            margin-left: 250px;
        }

        .sidebar {
            width: 250px;
        }
    }

    @media (max-width: 800px) {
        .student-content {
            margin-left: 0;
        }

        .sidebar {
            display: none;
        }
    }
</style>
