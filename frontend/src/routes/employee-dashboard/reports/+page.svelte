<script lang="ts">
    import {
        BarChart3,
        CalendarDays,
        CheckCircle2,
        Clock3,
        TrendingUp,
        FileText,
        Download,
        Info,
        Car,
        UserCheck,
        AlertCircle
    } from '@lucide/svelte';

    let selectedPeriod = $state('This Month');

    const periods = [
        'This Week',
        'This Month',
        'Last 3 Months'
    ];

    const attendanceData = [
        { day: 'Mon', present: 8, absent: 0 },
        { day: 'Tue', present: 8, absent: 0 },
        { day: 'Wed', present: 7, absent: 1 },
        { day: 'Thu', present: 8, absent: 0 },
        { day: 'Fri', present: 8, absent: 0 },
        { day: 'Sat', present: 4, absent: 0 }
    ];

    const monthlyReports = [
        {
            title: 'Attendance Report',
            description:
                'Monthly attendance summary including working days and attendance percentage.',
            date: 'August 2026',
            type: 'Attendance',
            icon: UserCheck,
            className: 'blue'
        },
        {
            title: 'Task Completion Report',
            description:
                'Summary of assigned, completed and pending tasks for the selected period.',
            date: 'August 2026',
            type: 'Tasks',
            icon: CheckCircle2,
            className: 'green'
        },
        {
            title: 'Schedule Report',
            description:
                'Overview of scheduled routes, duties and completed activities.',
            date: 'August 2026',
            type: 'Schedule',
            icon: CalendarDays,
            className: 'purple'
        },
        {
            title: 'Working Hours Report',
            description:
                'Summary of total working hours, scheduled hours and average daily hours.',
            date: 'August 2026',
            type: 'Working Hours',
            icon: Clock3,
            className: 'orange'
        }
    ];

    const totalPresent = attendanceData.reduce(
        (sum, item) => sum + item.present,
        0
    );

    const totalAbsent = attendanceData.reduce(
        (sum, item) => sum + item.absent,
        0
    );

    const totalWorkingDays = totalPresent + totalAbsent;

    const attendancePercentage =
        totalWorkingDays > 0
            ? Math.round((totalPresent / totalWorkingDays) * 100)
            : 0;

    function downloadReport(title: string) {
        alert(`Download for "${title}" will be connected to the backend/API later.`);
    }
</script>

<svelte:head>
    <title>Reports | Employee Dashboard</title>
</svelte:head>

<div class="reports-page">

    <!-- HEADER -->
    <div class="page-header">

        <div class="title-row">

            <div class="title-icon">
                <BarChart3 size={24} />
            </div>

            <div>
                <h1>Reports</h1>

                <p>
                    View your attendance, tasks, schedule and work performance reports.
                </p>
            </div>

        </div>


        <div class="period-selector">

            <CalendarDays size={15} />

            <select bind:value={selectedPeriod}>
                {#each periods as period}
                    <option value={period}>
                        {period}
                    </option>
                {/each}
            </select>

        </div>

    </div>


    <!-- PERFORMANCE SUMMARY -->
    <section class="stats-grid">

        <div class="stat-card">

            <div class="stat-icon blue">
                <UserCheck size={21} />
            </div>

            <div>
                <span>Attendance</span>

                <strong>
                    {attendancePercentage}%
                </strong>

                <small>
                    Overall attendance
                </small>
            </div>

        </div>


        <div class="stat-card">

            <div class="stat-icon green">
                <CheckCircle2 size={21} />
            </div>

            <div>
                <span>Tasks Completed</span>

                <strong>
                    86%
                </strong>

                <small>
                    Completion rate
                </small>
            </div>

        </div>


        <div class="stat-card">

            <div class="stat-icon orange">
                <Clock3 size={21} />
            </div>

            <div>
                <span>Working Hours</span>

                <strong>
                    42h
                </strong>

                <small>
                    This week
                </small>
            </div>

        </div>


        <div class="stat-card">

            <div class="stat-icon purple">
                <TrendingUp size={21} />
            </div>

            <div>
                <span>Performance</span>

                <strong>
                    Good
                </strong>

                <small>
                    Current performance
                </small>
            </div>

        </div>

    </section>


    <!-- ATTENDANCE REPORT -->
    <section class="report-card">

        <div class="card-header">

            <div>

                <h2>Attendance Overview</h2>

                <p>
                    Attendance activity for the selected period.
                </p>

            </div>

            <span class="period-badge">
                {selectedPeriod}
            </span>

        </div>


        <div class="attendance-content">

            <div class="attendance-chart">

                <div class="chart-y-axis">
                    <span>8</span>
                    <span>6</span>
                    <span>4</span>
                    <span>2</span>
                    <span>0</span>
                </div>

                <div class="chart-area">

                    <div class="grid-line line-1"></div>
                    <div class="grid-line line-2"></div>
                    <div class="grid-line line-3"></div>
                    <div class="grid-line line-4"></div>
                    <div class="grid-line line-5"></div>

                    <div class="bars">

                        {#each attendanceData as item}

                            <div class="bar-group">

                                <div class="bar-wrapper">

                                    <div
                                        class="bar present"
                                        style={`height: ${(item.present / 8) * 100}%`}
                                        title={`${item.present} hours present`}
                                    ></div>

                                    {#if item.absent > 0}

                                        <div
                                            class="bar absent"
                                            style={`height: ${(item.absent / 8) * 100}%`}
                                            title={`${item.absent} hours absent`}
                                        ></div>

                                    {/if}

                                </div>

                                <span>
                                    {item.day}
                                </span>

                            </div>

                        {/each}

                    </div>

                </div>

            </div>


            <div class="attendance-summary">

                <div class="attendance-percentage">

                    <div class="percentage-circle">
                        <strong>
                            {attendancePercentage}%
                        </strong>

                        <span>
                            Attendance
                        </span>
                    </div>

                </div>


                <div class="attendance-items">

                    <div>
                        <span class="dot present-dot"></span>

                        <span>
                            Present
                        </span>

                        <strong>
                            {totalPresent}
                        </strong>
                    </div>

                    <div>
                        <span class="dot absent-dot"></span>

                        <span>
                            Absent
                        </span>

                        <strong>
                            {totalAbsent}
                        </strong>
                    </div>

                    <div>
                        <span class="dot working-dot"></span>

                        <span>
                            Working Days
                        </span>

                        <strong>
                            {totalWorkingDays}
                        </strong>
                    </div>

                </div>

            </div>

        </div>

    </section>


    <!-- PERFORMANCE -->
    <section class="two-column">

        <div class="performance-card">

            <div class="card-header">

                <div>

                    <h2>Task Performance</h2>

                    <p>
                        Current task completion statistics.
                    </p>

                </div>

                <CheckCircle2 size={20} />

            </div>


            <div class="progress-section">

                <div class="progress-label">

                    <span>
                        Completed Tasks
                    </span>

                    <strong>
                        86%
                    </strong>

                </div>

                <div class="progress-bar">
                    <div
                        class="progress-fill green-progress"
                        style="width: 86%"
                    ></div>
                </div>

            </div>


            <div class="progress-section">

                <div class="progress-label">

                    <span>
                        On-Time Completion
                    </span>

                    <strong>
                        92%
                    </strong>

                </div>

                <div class="progress-bar">
                    <div
                        class="progress-fill blue-progress"
                        style="width: 92%"
                    ></div>
                </div>

            </div>


            <div class="progress-section">

                <div class="progress-label">

                    <span>
                        Pending Tasks
                    </span>

                    <strong>
                        14%
                    </strong>

                </div>

                <div class="progress-bar">
                    <div
                        class="progress-fill orange-progress"
                        style="width: 14%"
                    ></div>
                </div>

            </div>

        </div>


        <div class="performance-card">

            <div class="card-header">

                <div>

                    <h2>Work Summary</h2>

                    <p>
                        Your current work statistics.
                    </p>

                </div>

                <Car size={20} />

            </div>


            <div class="summary-list">

                <div class="summary-row">

                    <div class="summary-row-icon blue">
                        <Car size={15} />
                    </div>

                    <span>
                        Routes Completed
                    </span>

                    <strong>
                        24
                    </strong>

                </div>


                <div class="summary-row">

                    <div class="summary-row-icon green">
                        <CheckCircle2 size={15} />
                    </div>

                    <span>
                        Duties Completed
                    </span>

                    <strong>
                        18
                    </strong>

                </div>


                <div class="summary-row">

                    <div class="summary-row-icon orange">
                        <Clock3 size={15} />
                    </div>

                    <span>
                        Average Hours / Day
                    </span>

                    <strong>
                        7.2h
                    </strong>

                </div>


                <div class="summary-row">

                    <div class="summary-row-icon purple">
                        <TrendingUp size={15} />
                    </div>

                    <span>
                        Performance Score
                    </span>

                    <strong>
                        92
                    </strong>

                </div>

            </div>

        </div>

    </section>


    <!-- AVAILABLE REPORTS -->
    <section class="reports-section">

        <div class="section-heading">

            <div>

                <h2>Available Reports</h2>

                <p>
                    Download detailed reports for your records.
                </p>

            </div>

            <span>
                {monthlyReports.length} Reports
            </span>

        </div>


        <div class="reports-grid">

            {#each monthlyReports as report}

                <article class="available-report">

                    <div class={`report-icon ${report.className}`}>
                        <report.icon size={21} />
                    </div>


                    <div class="report-content">

                        <h3>
                            {report.title}
                        </h3>

                        <p>
                            {report.description}
                        </p>

                        <div class="report-meta">

                            <span>
                                <CalendarDays size={12} />
                                {report.date}
                            </span>

                            <span>
                                {report.type}
                            </span>

                        </div>

                    </div>


                    <button
                        type="button"
                        onclick={() => downloadReport(report.title)}
                    >
                        <Download size={15} />
                        Download
                    </button>

                </article>

            {/each}

        </div>

    </section>


    <!-- INFORMATION -->
    <section class="information-note">

        <div class="information-icon">
            <Info size={18} />
        </div>

        <div>

            <strong>
                Report Information
            </strong>

            <p>
                Report information shown here is currently demo data.
                During API integration, attendance, task, schedule and
                performance statistics will be retrieved from the backend
                and downloadable reports will be generated automatically.
            </p>

        </div>

    </section>

</div>


<style>
    .reports-page {
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

    .period-selector {
        display: flex;
        align-items: center;
        gap: 7px;
        padding: 8px 10px;
        border: 1px solid #dbe3ef;
        border-radius: 9px;
        background: white;
        color: #64748b;
    }

    .period-selector select {
        border: none;
        outline: none;
        background: white;
        color: #475569;
        font-family: inherit;
        font-size: 9px;
        font-weight: 700;
        cursor: pointer;
    }


    /* STATS */

    .stats-grid {
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 14px;
        margin-bottom: 20px;
    }

    .stat-card {
        display: flex;
        align-items: center;
        gap: 11px;
        padding: 16px;
        border: 1px solid #e2e8f0;
        border-radius: 13px;
        background: white;
        box-shadow: 0 3px 12px rgba(15, 23, 42, 0.03);
    }

    .stat-icon {
        width: 40px;
        height: 40px;
        display: flex;
        align-items: center;
        justify-content: center;
        flex-shrink: 0;
        border-radius: 10px;
    }

    .stat-icon.blue {
        background: #eef4ff;
        color: #2563eb;
    }

    .stat-icon.green {
        background: #ecfdf5;
        color: #059669;
    }

    .stat-icon.orange {
        background: #fff7ed;
        color: #ea580c;
    }

    .stat-icon.purple {
        background: #f5f3ff;
        color: #7c3aed;
    }

    .stat-card span {
        display: block;
        color: #64748b;
        font-size: 9px;
    }

    .stat-card strong {
        display: block;
        margin-top: 2px;
        color: #0f172a;
        font-size: 19px;
    }

    .stat-card small {
        display: block;
        margin-top: 2px;
        color: #94a3b8;
        font-size: 8px;
    }


    /* COMMON CARD */

    .report-card,
    .performance-card {
        padding: 20px;
        border: 1px solid #e2e8f0;
        border-radius: 14px;
        background: white;
        box-shadow: 0 3px 12px rgba(15, 23, 42, 0.03);
    }

    .report-card {
        margin-bottom: 18px;
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
        font-size: 15px;
    }

    .card-header p {
        margin: 4px 0 0;
        color: #64748b;
        font-size: 9px;
    }

    .period-badge {
        padding: 5px 8px;
        border-radius: 6px;
        background: #eef4ff;
        color: #2563eb;
        font-size: 8px;
        font-weight: 700;
    }


    /* ATTENDANCE */

    .attendance-content {
        display: grid;
        grid-template-columns: 1fr 250px;
        gap: 25px;
    }

    .attendance-chart {
        display: flex;
        height: 230px;
        padding-top: 5px;
    }

    .chart-y-axis {
        width: 25px;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        padding: 3px 0 20px;
    }

    .chart-y-axis span {
        color: #94a3b8;
        font-size: 8px;
    }

    .chart-area {
        position: relative;
        flex: 1;
        height: 100%;
    }

    .grid-line {
        position: absolute;
        left: 0;
        right: 0;
        border-top: 1px dashed #e2e8f0;
    }

    .line-1 {
        top: 2%;
    }

    .line-2 {
        top: 25%;
    }

    .line-3 {
        top: 50%;
    }

    .line-4 {
        top: 75%;
    }

    .line-5 {
        top: 98%;
    }

    .bars {
        position: absolute;
        inset: 0;
        display: flex;
        align-items: flex-end;
        justify-content: space-around;
        gap: 15px;
        padding: 0 10px 20px;
    }

    .bar-group {
        height: 100%;
        flex: 1;
        display: flex;
        align-items: center;
        justify-content: flex-end;
        flex-direction: column;
        gap: 7px;
    }

    .bar-wrapper {
        width: 100%;
        max-width: 45px;
        height: calc(100% - 20px);
        display: flex;
        align-items: flex-end;
        justify-content: center;
        gap: 3px;
    }

    .bar {
        width: 45%;
        min-height: 3px;
        border-radius: 5px 5px 0 0;
    }

    .bar.present {
        background: #2563eb;
    }

    .bar.absent {
        background: #f97316;
    }

    .bar-group > span {
        color: #64748b;
        font-size: 8px;
    }


    /* ATTENDANCE SUMMARY */

    .attendance-summary {
        display: flex;
        align-items: center;
        gap: 25px;
        padding: 20px;
        border-radius: 12px;
        background: #f8fafc;
    }

    .attendance-percentage {
        flex-shrink: 0;
    }

    .percentage-circle {
        width: 105px;
        height: 105px;
        display: flex;
        align-items: center;
        justify-content: center;
        flex-direction: column;
        border: 9px solid #dbeafe;
        border-right-color: #2563eb;
        border-radius: 50%;
    }

    .percentage-circle strong {
        color: #0f172a;
        font-size: 21px;
    }

    .percentage-circle span {
        margin-top: 2px;
        color: #94a3b8;
        font-size: 7px;
    }

    .attendance-items {
        flex: 1;
        display: flex;
        flex-direction: column;
        gap: 13px;
    }

    .attendance-items div {
        display: grid;
        grid-template-columns: 8px 1fr auto;
        align-items: center;
        gap: 7px;
        color: #64748b;
        font-size: 8px;
    }

    .attendance-items strong {
        color: #334155;
    }

    .dot {
        width: 7px;
        height: 7px;
        border-radius: 50%;
    }

    .present-dot {
        background: #2563eb;
    }

    .absent-dot {
        background: #f97316;
    }

    .working-dot {
        background: #94a3b8;
    }


    /* TWO COLUMN */

    .two-column {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 18px;
        margin-bottom: 25px;
    }

    .progress-section {
        margin-bottom: 18px;
    }

    .progress-section:last-child {
        margin-bottom: 0;
    }

    .progress-label {
        display: flex;
        align-items: center;
        justify-content: space-between;
        margin-bottom: 7px;
    }

    .progress-label span {
        color: #64748b;
        font-size: 9px;
    }

    .progress-label strong {
        color: #334155;
        font-size: 9px;
    }

    .progress-bar {
        width: 100%;
        height: 7px;
        overflow: hidden;
        border-radius: 10px;
        background: #f1f5f9;
    }

    .progress-fill {
        height: 100%;
        border-radius: inherit;
    }

    .green-progress {
        background: #10b981;
    }

    .blue-progress {
        background: #2563eb;
    }

    .orange-progress {
        background: #f97316;
    }


    /* WORK SUMMARY */

    .summary-list {
        display: flex;
        flex-direction: column;
        gap: 11px;
    }

    .summary-row {
        display: flex;
        align-items: center;
        gap: 9px;
        padding: 8px 0;
        border-bottom: 1px solid #f1f5f9;
    }

    .summary-row:last-child {
        border-bottom: none;
    }

    .summary-row > span {
        flex: 1;
        color: #64748b;
        font-size: 9px;
    }

    .summary-row > strong {
        color: #334155;
        font-size: 10px;
    }

    .summary-row-icon {
        width: 30px;
        height: 30px;
        display: flex;
        align-items: center;
        justify-content: center;
        border-radius: 8px;
    }

    .summary-row-icon.blue {
        background: #eef4ff;
        color: #2563eb;
    }

    .summary-row-icon.green {
        background: #ecfdf5;
        color: #059669;
    }

    .summary-row-icon.orange {
        background: #fff7ed;
        color: #ea580c;
    }

    .summary-row-icon.purple {
        background: #f5f3ff;
        color: #7c3aed;
    }


    /* AVAILABLE REPORTS */

    .reports-section {
        margin-bottom: 20px;
    }

    .section-heading {
        display: flex;
        align-items: center;
        justify-content: space-between;
        gap: 15px;
        margin-bottom: 13px;
    }

    .section-heading h2 {
        margin: 0;
        color: #0f172a;
        font-size: 17px;
    }

    .section-heading p {
        margin: 4px 0 0;
        color: #64748b;
        font-size: 10px;
    }

    .section-heading > span {
        padding: 6px 9px;
        border-radius: 7px;
        background: #f1f5f9;
        color: #64748b;
        font-size: 8px;
        font-weight: 700;
    }

    .reports-grid {
        display: grid;
        grid-template-columns: repeat(2, 1fr);
        gap: 13px;
    }

    .available-report {
        display: flex;
        align-items: flex-start;
        gap: 12px;
        padding: 16px;
        border: 1px solid #e2e8f0;
        border-radius: 13px;
        background: white;
    }

    .report-icon {
        width: 42px;
        height: 42px;
        display: flex;
        align-items: center;
        justify-content: center;
        flex-shrink: 0;
        border-radius: 10px;
    }

    .report-icon.blue {
        background: #eef4ff;
        color: #2563eb;
    }

    .report-icon.green {
        background: #ecfdf5;
        color: #059669;
    }

    .report-icon.orange {
        background: #fff7ed;
        color: #ea580c;
    }

    .report-icon.purple {
        background: #f5f3ff;
        color: #7c3aed;
    }

    .report-content {
        flex: 1;
        min-width: 0;
    }

    .report-content h3 {
        margin: 0;
        color: #0f172a;
        font-size: 12px;
    }

    .report-content p {
        margin: 5px 0 8px;
        color: #64748b;
        font-size: 8px;
        line-height: 1.5;
    }

    .report-meta {
        display: flex;
        align-items: center;
        gap: 10px;
    }

    .report-meta span {
        display: flex;
        align-items: center;
        gap: 4px;
        color: #94a3b8;
        font-size: 7px;
    }

    .available-report > button {
        display: flex;
        align-items: center;
        gap: 5px;
        padding: 7px 9px;
        border: 1px solid #dbe3ef;
        border-radius: 7px;
        background: white;
        color: #475569;
        font-size: 8px;
        font-weight: 700;
        cursor: pointer;
    }

    .available-report > button:hover {
        border-color: #2563eb;
        color: #2563eb;
        background: #eff6ff;
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

    @media (max-width: 1100px) {

        .stats-grid {
            grid-template-columns: repeat(2, 1fr);
        }

        .attendance-content {
            grid-template-columns: 1fr;
        }

        .two-column {
            grid-template-columns: 1fr;
        }
    }


    @media (max-width: 800px) {

        .reports-page {
            padding: 24px;
        }

        .reports-grid {
            grid-template-columns: 1fr;
        }
    }


    @media (max-width: 600px) {

        .reports-page {
            padding: 18px;
        }

        .page-header {
            align-items: flex-start;
            flex-direction: column;
        }

        .period-selector {
            width: 100%;
            box-sizing: border-box;
        }

        .period-selector select {
            flex: 1;
        }

        .stats-grid {
            grid-template-columns: 1fr;
        }

        .attendance-summary {
            align-items: flex-start;
            flex-direction: column;
        }

        .section-heading {
            align-items: flex-start;
            flex-direction: column;
        }

        .available-report {
            flex-wrap: wrap;
        }

        .available-report > button {
            width: 100%;
            justify-content: center;
        }
    }
</style>