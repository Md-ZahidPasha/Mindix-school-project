<script lang="ts">
    import {
        Users,
        CalendarCheck,
        BarChart3,
        GraduationCap,
        ClipboardCheck,
        IndianRupee,
        Award,
        Bell,
        Bot,
        UserCircle,
        Search,
        ArrowRight,
        CheckCircle2,
        FileText
    } from '@lucide/svelte';

    const children = [
        {
            name: 'Rahul Kumar',
            className: '10th',
            section: 'A',
            attendance: '92%',
            grade: '77%'
        },
        {
            name: 'Ayesha Kumar',
            className: '7th',
            section: 'B',
            attendance: '95%',
            grade: '84%'
        }
    ];

    const performance = [
        { subject: 'Mathematics', marks: '78 / 100', grade: 'A' },
        { subject: 'Science', marks: '74 / 100', grade: 'A' },
        { subject: 'English', marks: '81 / 100', grade: 'A+' },
        { subject: 'Social Studies', marks: '75 / 100', grade: 'A' }
    ];

    const exams = [
        {
            subject: 'Mathematics',
            date: '20 Aug',
            time: '10:00 AM',
            syllabus: 'Algebra & Geometry'
        },
        {
            subject: 'Science',
            date: '23 Aug',
            time: '10:00 AM',
            syllabus: 'Light & Human Eye'
        },
        {
            subject: 'English',
            date: '26 Aug',
            time: '10:00 AM',
            syllabus: 'Grammar & Literature'
        }
    ];

    const assignments = [
        {
            name: 'Quadratic Equations',
            subject: 'Mathematics',
            due: 'Today',
            status: 'Pending'
        },
        {
            name: 'Cellular Structure',
            subject: 'Biology',
            due: 'Tomorrow',
            status: 'Submitted'
        },
        {
            name: 'Grammar Practice',
            subject: 'English',
            due: '18 Aug',
            status: 'Pending'
        }
    ];
</script>

<svelte:head>
    <title>Parent Dashboard | PaperBuddy</title>
</svelte:head>

<div class="dashboard-page">

    <!-- MAIN CONTENT -->
    <main class="main-content">

        <!-- HEADER -->
        <header class="header">
            <div class="welcome">
                <h1>Welcome, Parent 👋</h1>

                <p>
                    Stay connected with your child's academic journey.
                </p>

                <span>Tuesday, August 11, 2026</span>
            </div>

            <div class="header-actions">

                <div class="search-box">
                    <Search size={18} />

                    <input
                        type="text"
                        placeholder="Search..."
                    />
                </div>

                <button class="icon-button" type="button">
                    <Bell size={20} />
                </button>

                <div class="profile">
                    <UserCircle size={36} />

                    <div>
                        <strong>Mr. Kumar</strong>
                        <span>Parent</span>
                    </div>
                </div>

            </div>
        </header>


        <!-- KPI CARDS -->
        <section class="stats-grid">

            <div class="stat-card">
                <div class="stat-icon">
                    <Users size={23} />
                </div>

                <div>
                    <span>Children</span>
                    <strong>2</strong>
                </div>
            </div>

            <div class="stat-card">
                <div class="stat-icon">
                    <CalendarCheck size={23} />
                </div>

                <div>
                    <span>Attendance</span>
                    <strong>93%</strong>
                </div>
            </div>

            <div class="stat-card">
                <div class="stat-icon">
                    <BarChart3 size={23} />
                </div>

                <div>
                    <span>Average Grade</span>
                    <strong>81%</strong>
                </div>
            </div>

            <div class="stat-card">
                <div class="stat-icon">
                    <ClipboardCheck size={23} />
                </div>

                <div>
                    <span>Pending Assignments</span>
                    <strong>3</strong>
                </div>
            </div>

            <div class="stat-card">
                <div class="stat-icon">
                    <GraduationCap size={23} />
                </div>

                <div>
                    <span>Upcoming Exams</span>
                    <strong>4</strong>
                </div>
            </div>

            <div class="stat-card">
                <div class="stat-icon">
                    <IndianRupee size={23} />
                </div>

                <div>
                    <span>Pending Fees</span>
                    <strong>₹6,500</strong>
                </div>
            </div>

            <div class="stat-card">
                <div class="stat-icon">
                    <Award size={23} />
                </div>

                <div>
                    <span>Certificates</span>
                    <strong>7</strong>
                </div>
            </div>

            <div class="stat-card">
                <div class="stat-icon">
                    <Bell size={23} />
                </div>

                <div>
                    <span>Notifications</span>
                    <strong>5</strong>
                </div>
            </div>

        </section>


        <!-- CHILDREN OVERVIEW -->
        <section class="large-card">

            <div class="section-header">
                <div>
                    <h2>Children Overview</h2>
                    <p>Monitor your children's academic progress.</p>
                </div>

                <a
                    href="/parent-dashboard/children"
                    class="action-link"
                >
                    View All
                    <ArrowRight size={17} />
                </a>
            </div>

            <div class="children-grid">

                {#each children as child}

                    <div class="child-card">

                        <div class="child-top">

                            <div class="child-avatar">
                                {child.name.charAt(0)}
                            </div>

                            <div>
                                <strong>{child.name}</strong>

                                <span>
                                    {child.className} - {child.section}
                                </span>
                            </div>

                        </div>

                        <div class="child-stats">

                            <div>
                                <span>Attendance</span>
                                <strong>{child.attendance}</strong>
                            </div>

                            <div>
                                <span>Average Grade</span>
                                <strong>{child.grade}</strong>
                            </div>

                        </div>

                        <a
                            href="/parent-dashboard/children"
                            class="view-profile"
                        >
                            View Profile
                            <ArrowRight size={15} />
                        </a>

                    </div>

                {/each}

            </div>

        </section>


        <!-- ATTENDANCE + PERFORMANCE -->
        <div class="content-grid">

            <section class="large-card">

                <div class="section-header">
                    <div>
                        <h2>Attendance</h2>
                        <p>Monthly attendance overview</p>
                    </div>

                    <a
                        href="/parent-dashboard/attendance"
                        class="action-link"
                    >
                        View Details
                        <ArrowRight size={17} />
                    </a>
                </div>

                <div class="attendance-value">
                    <strong>93%</strong>
                    <span>Overall Attendance</span>
                </div>

                <div class="attendance-bar">
                    <div style="width: 93%;"></div>
                </div>

                <div class="attendance-stats">

                    <div>
                        <strong>86</strong>
                        <span>Present</span>
                    </div>

                    <div>
                        <strong>5</strong>
                        <span>Absent</span>
                    </div>

                    <div>
                        <strong>2</strong>
                        <span>Late</span>
                    </div>

                </div>

                <div class="attendance-note">
                    <CheckCircle2 size={17} />
                    <span>
                        Attendance is above the required threshold.
                    </span>
                </div>

            </section>


            <section class="large-card">

                <div class="section-header">
                    <div>
                        <h2>Academic Performance</h2>
                        <p>Recent subject performance</p>
                    </div>

                    <a
                        href="/parent-dashboard/performance"
                        class="action-link"
                    >
                        View Details
                        <ArrowRight size={17} />
                    </a>
                </div>

                <div class="performance-list">

                    {#each performance as item}

                        <div class="performance-row">

                            <div>
                                <strong>{item.subject}</strong>
                                <span>{item.marks}</span>
                            </div>

                            <div class="grade">
                                {item.grade}
                            </div>

                        </div>

                    {/each}

                </div>

            </section>

        </div>


        <!-- UPCOMING EXAMS -->
        <section class="large-card">

            <div class="section-header">
                <div>
                    <h2>Upcoming Exams</h2>
                    <p>
                        Keep track of your child's examination schedule.
                    </p>
                </div>

                <a
                    href="/parent-dashboard/exams"
                    class="action-link"
                >
                    View All
                    <ArrowRight size={17} />
                </a>
            </div>

            <div class="exam-list">

                {#each exams as exam}

                    <div class="exam-item">

                        <div class="exam-icon">
                            <GraduationCap size={21} />
                        </div>

                        <div class="exam-info">
                            <strong>{exam.subject}</strong>

                            <span>
                                {exam.date} • {exam.time}
                            </span>
                        </div>

                        <div class="syllabus">
                            {exam.syllabus}
                        </div>

                    </div>

                {/each}

            </div>

        </section>


        <!-- ASSIGNMENTS -->
        <section class="large-card">

            <div class="section-header">
                <div>
                    <h2>Assignments</h2>
                    <p>Monitor your child's assignments.</p>
                </div>

                <a
                    href="/parent-dashboard/assignments"
                    class="action-link"
                >
                    View All
                    <ArrowRight size={17} />
                </a>
            </div>

            <div class="table">

                <div class="table-header">
                    <span>Assignment</span>
                    <span>Subject</span>
                    <span>Due Date</span>
                    <span>Status</span>
                </div>

                {#each assignments as assignment}

                    <div class="table-row">

                        <strong>{assignment.name}</strong>

                        <span>{assignment.subject}</span>

                        <span>{assignment.due}</span>

                        <span
                            class:pending={
                                assignment.status === 'Pending'
                            }
                            class:submitted={
                                assignment.status === 'Submitted'
                            }
                        >
                            {assignment.status}
                        </span>

                    </div>

                {/each}

            </div>

        </section>


        <!-- FEES -->
        <section class="large-card">

            <div class="section-header">
                <div>
                    <h2>Fees</h2>
                    <p>Track school fees and payments.</p>
                </div>

                <a
                    href="/parent-dashboard/fees"
                    class="action-link"
                >
                    View Details
                    <ArrowRight size={17} />
                </a>
            </div>

            <div class="fees-grid">

                <div>
                    <span>Total Fees</span>
                    <strong>₹45,000</strong>
                </div>

                <div>
                    <span>Paid</span>
                    <strong>₹38,500</strong>
                </div>

                <div>
                    <span>Pending</span>
                    <strong class="pending-fee">₹6,500</strong>
                </div>

                <div>
                    <span>Due Date</span>
                    <strong>30 Aug</strong>
                </div>

            </div>

        </section>


        <!-- NOTIFICATIONS -->
        <section class="large-card">

            <div class="section-header">
                <div>
                    <h2>Notifications</h2>
                    <p>Important school updates.</p>
                </div>

                <a
                    href="/parent-dashboard/notifications"
                    class="action-link"
                >
                    View All
                    <ArrowRight size={17} />
                </a>
            </div>

            <div class="notifications-list">

                <div class="notification-item">

                    <div class="notification-icon">
                        <Bell size={18} />
                    </div>

                    <div>
                        <strong>School Annual Day</strong>
                        <span>
                            Annual Day will be held on 28 August.
                        </span>
                    </div>

                </div>

                <div class="notification-item">

                    <div class="notification-icon">
                        <FileText size={18} />
                    </div>

                    <div>
                        <strong>Exam Schedule Published</strong>
                        <span>
                            The upcoming examination schedule is now
                            available.
                        </span>
                    </div>

                </div>

                <div class="notification-item">

                    <div class="notification-icon">
                        <IndianRupee size={18} />
                    </div>

                    <div>
                        <strong>Fee Reminder</strong>
                        <span>
                            ₹6,500 fee payment is pending.
                        </span>
                    </div>

                </div>

            </div>

        </section>


        <!-- AI ASSISTANT -->
        <section class="large-card ai-card">

            <div class="ai-heading">

                <div class="ai-icon">
                    <Bot size={24} />
                </div>

                <div>
                    <h2>AI Assistant</h2>
                    <p>
                        Ask PaperBuddy about your child's academics.
                    </p>
                </div>

            </div>

            <div class="prompt-list">

                <button class="prompt" type="button">
                    <span>
                        How is my child's attendance?
                    </span>

                    <ArrowRight size={16} />
                </button>

                <button class="prompt" type="button">
                    <span>
                        How is my child's academic performance?
                    </span>

                    <ArrowRight size={16} />
                </button>

                <button class="prompt" type="button">
                    <span>
                        What exams are coming?
                    </span>

                    <ArrowRight size={16} />
                </button>

                <button class="prompt" type="button">
                    <span>
                        Does my child have pending assignments?
                    </span>

                    <ArrowRight size={16} />
                </button>

            </div>

        </section>

    </main>

</div>


<style>
    .dashboard-page {
        width: 100%;
        min-height: 100vh;
        background: #f8fafc;
    }

    .main-content {
        width: 100%;
        min-width: 0;
        padding: 36px;
        box-sizing: border-box;
    }


    /* HEADER */

    .header {
        display: flex;
        align-items: center;
        justify-content: space-between;
        gap: 30px;
        margin-bottom: 32px;
    }

    .welcome h1 {
        margin: 0 0 8px;
        font-size: 34px;
        font-weight: 800;
        color: #0f172a;
    }

    .welcome p {
        margin: 0 0 6px;
        font-size: 16px;
        color: #64748b;
    }

    .welcome span {
        font-size: 14px;
        color: #94a3b8;
    }

    .header-actions {
        display: flex;
        align-items: center;
        gap: 14px;
    }

    .search-box {
        width: 280px;
        height: 46px;
		color: #64748b;
        display: flex;
        align-items: center;
        gap: 10px;
        padding: 0 14px;
        background: white;
        border: 1px solid #e2e8f0;
        border-radius: 12px;
        box-sizing: border-box;
    }


    .search-box input {
        width: 100%;
        border: none;
        outline: none;
        background: transparent;
        font-size: 14px;
    }

    .icon-button {
        width: 46px;
        height: 46px;
        display: flex;
        align-items: center;
        justify-content: center;
        background: white;
        border: 1px solid #e2e8f0;
        border-radius: 12px;
        color: #475569;
        cursor: pointer;
    }

    .profile {
        display: flex;
        align-items: center;
		color: #2563eb;
        gap: 10px;
        padding: 7px 12px;
        background: white;
        border: 1px solid #e2e8f0;
        border-radius: 14px;
    }

    

    .profile strong {
        display: block;
        font-size: 14px;
        color: #0f172a;
    }

    .profile span {
        display: block;
        margin-top: 2px;
        font-size: 12px;
        color: #64748b;
    }


    /* KPI */

    .stats-grid {
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 18px;
        margin-bottom: 28px;
    }

    .stat-card {
        display: flex;
        align-items: center;
        gap: 15px;
        padding: 20px;
        background: white;
        border: 1px solid #e2e8f0;
        border-radius: 18px;
        box-shadow: 0 4px 15px rgba(15, 23, 42, 0.04);
    }

    .stat-icon {
        width: 46px;
        height: 46px;
        flex-shrink: 0;
        display: flex;
        align-items: center;
        justify-content: center;
        background: #eef4ff;
        color: #2563eb;
        border-radius: 13px;
    }

    .stat-card span {
        display: block;
        margin-bottom: 5px;
        font-size: 13px;
        color: #64748b;
    }

    .stat-card strong {
        display: block;
        font-size: 24px;
        font-weight: 800;
        color: #0f172a;
    }


    /* CARDS */

    .content-grid {
        display: grid;
        grid-template-columns: 1.6fr 1.4fr;
        gap: 28px;
        margin-bottom: 28px;
    }

    .large-card {
        background: white;
        border: 1px solid #e2e8f0;
        border-radius: 18px;
        padding: 24px;
        box-shadow: 0 4px 15px rgba(15, 23, 42, 0.04);
        margin-bottom: 28px;
    }

    .section-header {
        display: flex;
        align-items: center;
        justify-content: space-between;
        gap: 20px;
        margin-bottom: 20px;
    }

    .section-header h2 {
        margin: 0 0 5px;
        font-size: 21px;
        font-weight: 800;
        color: #0f172a;
    }

    .section-header p {
        margin: 0;
        font-size: 14px;
        color: #64748b;
    }

    .action-link {
        display: flex;
        align-items: center;
        gap: 7px;
        border: none;
        background: transparent;
        color: #2563eb;
        font-size: 13px;
        font-weight: 700;
        text-decoration: none;
        cursor: pointer;
    }

    .action-link:hover {
        color: #1d4ed8;
    }


    /* CHILDREN */

    .children-grid {
        display: grid;
        grid-template-columns: repeat(2, 1fr);
        gap: 18px;
    }

    .child-card {
        padding: 20px;
        background: #f8fafc;
        border: 1px solid #e2e8f0;
        border-radius: 15px;
    }

    .child-top {
        display: flex;
        align-items: center;
        gap: 13px;
        margin-bottom: 20px;
    }

    .child-avatar {
        width: 46px;
        height: 46px;
        display: flex;
        align-items: center;
        justify-content: center;
        background: #2563eb;
        color: white;
        border-radius: 50%;
        font-size: 18px;
        font-weight: 700;
    }

    .child-top strong {
        display: block;
        font-size: 16px;
        color: #0f172a;
    }

    .child-top span {
        display: block;
        margin-top: 4px;
        font-size: 13px;
        color: #64748b;
    }

    .child-stats {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 12px;
        margin-bottom: 18px;
    }

    .child-stats div {
        padding: 12px;
        background: white;
        border-radius: 11px;
    }

    .child-stats span {
        display: block;
        font-size: 12px;
        color: #64748b;
    }

    .child-stats strong {
        display: block;
        margin-top: 5px;
        font-size: 19px;
        color: #0f172a;
    }

    .view-profile {
        display: flex;
        align-items: center;
        gap: 7px;
        border: none;
        background: transparent;
        color: #2563eb;
        font-size: 13px;
        font-weight: 700;
        text-decoration: none;
        cursor: pointer;
    }


    /* ATTENDANCE */

    .attendance-value strong {
        display: block;
        font-size: 38px;
        color: #2563eb;
    }

    .attendance-value span {
        font-size: 13px;
        color: #64748b;
    }

    .attendance-bar {
        height: 9px;
        margin: 15px 0 20px;
        background: #e2e8f0;
        border-radius: 20px;
        overflow: hidden;
    }

    .attendance-bar div {
        height: 100%;
        background: #2563eb;
        border-radius: 20px;
    }

    .attendance-stats {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 10px;
    }

    .attendance-stats div {
        padding: 13px;
        text-align: center;
        background: #f8fafc;
        border-radius: 12px;
    }

    .attendance-stats strong {
        display: block;
        font-size: 18px;
        color: #0f172a;
    }

    .attendance-stats span {
        font-size: 12px;
        color: #64748b;
    }

    .attendance-note {
        display: flex;
        align-items: center;
        gap: 8px;
        margin-top: 16px;
        padding: 11px;
        background: #ecfdf5;
        color: #059669;
        border-radius: 10px;
        font-size: 12px;
    }


    /* PERFORMANCE */

    .performance-list {
        display: flex;
        flex-direction: column;
    }

    .performance-row {
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 14px 0;
        border-bottom: 1px solid #e2e8f0;
    }

    .performance-row:last-child {
        border-bottom: none;
    }

    .performance-row strong {
        display: block;
        font-size: 14px;
        color: #0f172a;
    }

    .performance-row span {
        display: block;
        margin-top: 4px;
        font-size: 12px;
        color: #64748b;
    }

    .grade {
        padding: 7px 11px;
        background: #ecfdf5;
        color: #059669;
        border-radius: 9px;
        font-size: 12px;
        font-weight: 800;
    }


    /* EXAMS */

    .exam-list {
        display: flex;
        flex-direction: column;
        gap: 12px;
    }

    .exam-item {
        display: flex;
        align-items: center;
        gap: 14px;
        padding: 15px;
        background: #f8fafc;
        border: 1px solid #e2e8f0;
        border-radius: 13px;
    }

    .exam-icon {
        width: 43px;
        height: 43px;
        display: flex;
        align-items: center;
        justify-content: center;
        background: #eef4ff;
        color: #2563eb;
        border-radius: 12px;
        flex-shrink: 0;
    }

    .exam-info {
        flex: 1;
    }

    .exam-info strong {
        display: block;
        font-size: 14px;
        color: #0f172a;
    }

    .exam-info span {
        display: block;
        margin-top: 4px;
        font-size: 12px;
        color: #64748b;
    }

    .syllabus {
        font-size: 12px;
        color: #64748b;
        text-align: right;
    }


    /* ASSIGNMENTS */

    .table {
        width: 100%;
        overflow-x: auto;
    }

    .table-header,
    .table-row {
        display: grid;
        grid-template-columns: 1.5fr 1fr 0.8fr 0.8fr;
        align-items: center;
        gap: 15px;
        padding: 14px 12px;
        min-width: 650px;
    }

    .table-header {
        background: #f8fafc;
        border-radius: 10px;
        font-size: 12px;
        font-weight: 700;
        color: #64748b;
    }

    .table-row {
        border-bottom: 1px solid #e2e8f0;
        font-size: 13px;
        color: #64748b;
    }

    .table-row strong {
        color: #0f172a;
    }

    .table-row > span:last-child {
        width: fit-content;
        padding: 6px 10px;
        border-radius: 8px;
        background: #eef4ff;
        color: #2563eb;
        font-size: 11px;
        font-weight: 700;
    }

    .table-row > span.pending {
        background: #fff7ed;
        color: #ea580c;
    }

    .table-row > span.submitted {
        background: #ecfdf5;
        color: #059669;
    }


    /* FEES */

    .fees-grid {
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 16px;
    }

    .fees-grid > div {
        padding: 18px;
        background: #f8fafc;
        border-radius: 14px;
    }

    .fees-grid span {
        display: block;
        margin-bottom: 7px;
        font-size: 13px;
        color: #64748b;
    }

    .fees-grid strong {
        font-size: 22px;
        color: #0f172a;
    }

    .fees-grid .pending-fee {
        color: #ea580c;
    }


    /* NOTIFICATIONS */

    .notifications-list {
        display: flex;
        flex-direction: column;
    }

    .notification-item {
        display: flex;
        align-items: center;
        gap: 14px;
        padding: 15px 0;
        border-bottom: 1px solid #e2e8f0;
    }

    .notification-item:last-child {
        border-bottom: none;
    }

    .notification-icon {
        width: 42px;
        height: 42px;
        display: flex;
        align-items: center;
        justify-content: center;
        flex-shrink: 0;
        background: #eef4ff;
        color: #2563eb;
        border-radius: 11px;
    }

    .notification-item strong {
        display: block;
        font-size: 14px;
        color: #0f172a;
    }

    .notification-item span {
        display: block;
        margin-top: 4px;
        font-size: 12px;
        color: #64748b;
    }


    /* AI */

    .ai-card {
        background: linear-gradient(
            135deg,
            #eef4ff,
            white
        );

        border-color: #d8e5ff;
    }

    .ai-heading {
        display: flex;
        align-items: center;
        gap: 14px;
        margin-bottom: 20px;
    }

    .ai-icon {
        width: 48px;
        height: 48px;
        display: flex;
        align-items: center;
        justify-content: center;
        background: #2563eb;
        color: white;
        border-radius: 13px;
    }

    .ai-heading h2 {
        margin: 0 0 4px;
        font-size: 21px;
        color: #0f172a;
    }

    .ai-heading p {
        margin: 0;
        font-size: 13px;
        color: #64748b;
    }

    .prompt-list {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 10px;
    }

    .prompt {
        display: flex;
        align-items: center;
        justify-content: space-between;
        gap: 10px;
        padding: 13px 14px;
        background: white;
        border: 1px solid #d8e5ff;
        border-radius: 10px;
        color: #2563eb;
        font-size: 12px;
        text-align: left;
        cursor: pointer;
    }

    .prompt:hover {
        background: #2563eb;
        color: white;
    }


    /* RESPONSIVE */

    @media (max-width: 1350px) {
        .stats-grid {
            grid-template-columns: repeat(2, 1fr);
        }

        .fees-grid {
            grid-template-columns: repeat(2, 1fr);
        }
    }

    @media (max-width: 1100px) {
        .main-content {
            padding: 24px;
        }

        .content-grid {
            grid-template-columns: 1fr;
        }

        .children-grid {
            grid-template-columns: 1fr;
        }
    }

    @media (max-width: 800px) {
        .main-content {
            padding: 20px;
        }

        .header {
            flex-direction: column;
            align-items: flex-start;
        }

        .header-actions {
            width: 100%;
        }

        .search-box {
            flex: 1;
            width: auto;
        }

        .stats-grid {
            grid-template-columns: 1fr;
        }

        .children-grid {
            grid-template-columns: 1fr;
        }

        .attendance-stats {
            grid-template-columns: 1fr;
        }

        .fees-grid {
            grid-template-columns: 1fr;
        }

        .prompt-list {
            grid-template-columns: 1fr;
        }
    }
</style>