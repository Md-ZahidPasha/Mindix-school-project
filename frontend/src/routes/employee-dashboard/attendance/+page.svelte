<script lang="ts">
    import {
        CalendarCheck,
        CheckCircle2,
        XCircle,
        Clock3,
        CalendarDays,
        TrendingUp,
        ClipboardCheck,
        Info
    } from '@lucide/svelte';

    let selectedMonth = $state('August 2026');

    const months = [
        'August 2026',
        'July 2026',
        'June 2026',
        'May 2026'
    ];

    const attendanceRecords = [
        {
            date: '12 Aug 2026',
            day: 'Wednesday',
            checkIn: '08:42 AM',
            checkOut: '05:12 PM',
            status: 'Present',
            hours: '8h 30m'
        },
        {
            date: '11 Aug 2026',
            day: 'Tuesday',
            checkIn: '08:51 AM',
            checkOut: '05:05 PM',
            status: 'Present',
            hours: '8h 14m'
        },
        {
            date: '10 Aug 2026',
            day: 'Monday',
            checkIn: '08:39 AM',
            checkOut: '05:18 PM',
            status: 'Present',
            hours: '8h 39m'
        },
        {
            date: '08 Aug 2026',
            day: 'Saturday',
            checkIn: '08:55 AM',
            checkOut: '01:15 PM',
            status: 'Present',
            hours: '4h 20m'
        },
        {
            date: '07 Aug 2026',
            day: 'Friday',
            checkIn: '08:48 AM',
            checkOut: '05:10 PM',
            status: 'Present',
            hours: '8h 22m'
        },
        {
            date: '06 Aug 2026',
            day: 'Thursday',
            checkIn: '08:57 AM',
            checkOut: '05:02 PM',
            status: 'Late',
            hours: '8h 05m'
        },
        {
            date: '05 Aug 2026',
            day: 'Wednesday',
            checkIn: '08:41 AM',
            checkOut: '05:09 PM',
            status: 'Present',
            hours: '8h 28m'
        },
        {
            date: '04 Aug 2026',
            day: 'Tuesday',
            checkIn: '08:44 AM',
            checkOut: '05:15 PM',
            status: 'Present',
            hours: '8h 31m'
        },
        {
            date: '03 Aug 2026',
            day: 'Monday',
            checkIn: '08:52 AM',
            checkOut: '05:07 PM',
            status: 'Present',
            hours: '8h 15m'
        },
        {
            date: '01 Aug 2026',
            day: 'Saturday',
            checkIn: '09:03 AM',
            checkOut: '01:10 PM',
            status: 'Late',
            hours: '4h 07m'
        }
    ];

    const monthlyStats = {
        workingDays: 12,
        present: 10,
        absent: 0,
        late: 2,
        leave: 0,
        attendancePercentage: 83.3
    };

    const weeklyAttendance = [
        {
            day: 'Mon',
            date: '03',
            status: 'Present'
        },
        {
            day: 'Tue',
            date: '04',
            status: 'Present'
        },
        {
            day: 'Wed',
            date: '05',
            status: 'Present'
        },
        {
            day: 'Thu',
            date: '06',
            status: 'Late'
        },
        {
            day: 'Fri',
            date: '07',
            status: 'Present'
        },
        {
            day: 'Sat',
            date: '08',
            status: 'Present'
        },
        {
            day: 'Sun',
            date: '09',
            status: 'Holiday'
        }
    ];
</script>

<svelte:head>
    <title>Attendance | Employee Dashboard</title>
</svelte:head>

<div class="attendance-page">

    <!-- HEADER -->
    <div class="page-header">

        <div class="title-row">

            <div class="title-icon">
                <CalendarCheck size={24} />
            </div>

            <div>
                <h1>Attendance</h1>

                <p>
                    View your attendance records and working hours.
                </p>
            </div>

        </div>


        <div class="month-selector">

            <label for="month">
                Select Month
            </label>

            <select
                id="month"
                bind:value={selectedMonth}
            >
                {#each months as month}
                    <option value={month}>
                        {month}
                    </option>
                {/each}
            </select>

        </div>

    </div>


    <!-- EMPLOYEE INFO -->
    <section class="employee-info">

        <div class="employee-avatar">
            A
        </div>

        <div class="employee-details">

            <h2>Arjun Kumar</h2>

            <p>
                Employee ID:
                <strong>EMP001</strong>

                <span>•</span>

                Driving Department

                <span>•</span>

                Driver
            </p>

        </div>

        <div class="attendance-status">

            <span>Current Status</span>

            <strong>
                Present
            </strong>

            <small>
                Today
            </small>

        </div>

    </section>


    <!-- STATISTICS -->
    <section class="stats-grid">

        <div class="stat-card">

            <div class="stat-icon blue">
                <CalendarDays size={21} />
            </div>

            <div>
                <span>Working Days</span>
                <strong>{monthlyStats.workingDays}</strong>
            </div>

        </div>


        <div class="stat-card">

            <div class="stat-icon green">
                <CheckCircle2 size={21} />
            </div>

            <div>
                <span>Present</span>
                <strong>{monthlyStats.present}</strong>
            </div>

        </div>


        <div class="stat-card">

            <div class="stat-icon red">
                <XCircle size={21} />
            </div>

            <div>
                <span>Absent</span>
                <strong>{monthlyStats.absent}</strong>
            </div>

        </div>


        <div class="stat-card">

            <div class="stat-icon orange">
                <Clock3 size={21} />
            </div>

            <div>
                <span>Late</span>
                <strong>{monthlyStats.late}</strong>
            </div>

        </div>


        <div class="stat-card">

            <div class="stat-icon purple">
                <TrendingUp size={21} />
            </div>

            <div>
                <span>Attendance</span>
                <strong>{monthlyStats.attendancePercentage}%</strong>
            </div>

        </div>

    </section>


    <!-- WEEKLY OVERVIEW -->
    <section class="card">

        <div class="card-header">

            <div class="header-icon blue">
                <CalendarDays size={19} />
            </div>

            <div>

                <h2>Weekly Overview</h2>

                <p>
                    Your attendance status for the current week.
                </p>

            </div>

        </div>


        <div class="week-grid">

            {#each weeklyAttendance as day}

                <div class="day-card">

                    <span class="day-name">
                        {day.day}
                    </span>

                    <strong class="day-date">
                        {day.date}
                    </strong>


                    {#if day.status === 'Present'}

                        <div class="day-status present">
                            <CheckCircle2 size={18} />
                        </div>

                        <small>Present</small>

                    {:else if day.status === 'Late'}

                        <div class="day-status late">
                            <Clock3 size={18} />
                        </div>

                        <small>Late</small>

                    {:else}

                        <div class="day-status holiday">
                            <CalendarDays size={18} />
                        </div>

                        <small>Holiday</small>

                    {/if}

                </div>

            {/each}

        </div>

    </section>


    <!-- ATTENDANCE RECORDS -->
    <section class="card">

        <div class="card-header">

            <div>

                <div class="header-title">

                    <div class="header-icon green">
                        <ClipboardCheck size={19} />
                    </div>

                    <div>

                        <h2>Attendance Records</h2>

                        <p>
                            Daily check-in and check-out details for {selectedMonth}.
                        </p>

                    </div>

                </div>

            </div>

            <div class="record-count">
                {attendanceRecords.length} Records
            </div>

        </div>


        <div class="table-wrapper">

            <table>

                <thead>

                    <tr>
                        <th>Date</th>
                        <th>Day</th>
                        <th>Check In</th>
                        <th>Check Out</th>
                        <th>Working Hours</th>
                        <th>Status</th>
                    </tr>

                </thead>


                <tbody>

                    {#each attendanceRecords as record}

                        <tr>

                            <td>
                                <strong>
                                    {record.date}
                                </strong>
                            </td>

                            <td>
                                {record.day}
                            </td>

                            <td>
                                <span class="time">
                                    <Clock3 size={13} />
                                    {record.checkIn}
                                </span>
                            </td>

                            <td>
                                <span class="time">
                                    <Clock3 size={13} />
                                    {record.checkOut}
                                </span>
                            </td>

                            <td>
                                {record.hours}
                            </td>

                            <td>

                                {#if record.status === 'Present'}

                                    <span class="status present-status">
                                        <CheckCircle2 size={12} />
                                        Present
                                    </span>

                                {:else}

                                    <span class="status late-status">
                                        <Clock3 size={12} />
                                        Late
                                    </span>

                                {/if}

                            </td>

                        </tr>

                    {/each}

                </tbody>

            </table>

        </div>

    </section>


    <!-- ATTENDANCE SUMMARY -->
    <section class="summary-section">

        <div class="summary-card">

            <div class="summary-progress">

                <div
                    class="progress-circle"
                    style={`--progress: ${monthlyStats.attendancePercentage * 3.6}deg`}
                >
                    <div class="progress-inner">
                        <strong>
                            {monthlyStats.attendancePercentage}%
                        </strong>

                        <span>
                            Attendance
                        </span>
                    </div>
                </div>

            </div>


            <div class="summary-content">

                <h3>
                    Attendance Performance
                </h3>

                <p>
                    Your attendance for {selectedMonth}
                    is currently
                    <strong>
                        {monthlyStats.attendancePercentage}%
                    </strong>.
                </p>

                <div class="summary-points">

                    <span>
                        <CheckCircle2 size={14} />
                        {monthlyStats.present} days present
                    </span>

                    <span>
                        <Clock3 size={14} />
                        {monthlyStats.late} late arrivals
                    </span>

                    <span>
                        <XCircle size={14} />
                        {monthlyStats.absent} absent days
                    </span>

                </div>

            </div>

        </div>

    </section>


    <!-- INFORMATION -->
    <section class="information-note">

        <div class="information-icon">
            <Info size={18} />
        </div>

        <div>

            <strong>
                Attendance Information
            </strong>

            <p>
                Attendance records shown here are currently demo
                data. During API integration, real attendance,
                check-in, check-out and leave information will be
                retrieved from the backend.
            </p>

        </div>

    </section>

</div>


<style>
    .attendance-page {
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


    /* MONTH */

    .month-selector {
        min-width: 180px;
    }

    .month-selector label {
        display: block;
        margin-bottom: 6px;
        color: #475569;
        font-size: 10px;
        font-weight: 700;
    }

    .month-selector select {
        width: 100%;
        height: 42px;
        padding: 0 12px;
        border: 1px solid #dbe3ef;
        border-radius: 9px;
        outline: none;
        background: white;
        color: #334155;
        font-size: 11px;
        cursor: pointer;
    }

    .month-selector select:focus {
        border-color: #93c5fd;
        box-shadow: 0 0 0 3px #eff6ff;
    }


    /* EMPLOYEE INFO */

    .employee-info {
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

    .employee-avatar {
        width: 54px;
        height: 54px;
        display: flex;
        align-items: center;
        justify-content: center;
        flex-shrink: 0;
        border-radius: 50%;
        background: #2563eb;
        color: white;
        font-size: 20px;
        font-weight: 800;
    }

    .employee-details {
        flex: 1;
    }

    .employee-details h2 {
        margin: 0;
        color: #0f172a;
        font-size: 17px;
    }

    .employee-details p {
        margin: 5px 0 0;
        color: #64748b;
        font-size: 11px;
    }

    .employee-details strong {
        color: #334155;
    }

    .employee-details p span {
        margin: 0 7px;
        color: #cbd5e1;
    }

    .attendance-status {
        min-width: 135px;
        padding: 11px 15px;
        border-radius: 10px;
        background: #ecfdf5;
        text-align: center;
    }

    .attendance-status span {
        display: block;
        color: #64748b;
        font-size: 9px;
    }

    .attendance-status strong {
        display: block;
        margin: 2px 0;
        color: #059669;
        font-size: 15px;
    }

    .attendance-status small {
        color: #047857;
        font-size: 9px;
    }


    /* STATS */

    .stats-grid {
        display: grid;
        grid-template-columns: repeat(5, 1fr);
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

    .stat-icon.red {
        background: #fef2f2;
        color: #dc2626;
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


    /* CARD */

    .card {
        padding: 22px;
        margin-bottom: 20px;
        border: 1px solid #e2e8f0;
        border-radius: 15px;
        background: white;
        box-shadow: 0 3px 12px rgba(15, 23, 42, 0.03);
    }

    .card-header {
        display: flex;
        align-items: center;
        justify-content: space-between;
        gap: 15px;
        margin-bottom: 20px;
    }

    .header-title {
        display: flex;
        align-items: center;
        gap: 11px;
    }

    .header-icon {
        width: 39px;
        height: 39px;
        display: flex;
        align-items: center;
        justify-content: center;
        flex-shrink: 0;
        border-radius: 10px;
    }

    .header-icon.blue {
        background: #eef4ff;
        color: #2563eb;
    }

    .header-icon.green {
        background: #ecfdf5;
        color: #059669;
    }

    .card-header h2 {
        margin: 0;
        color: #0f172a;
        font-size: 16px;
    }

    .card-header p {
        margin: 3px 0 0;
        color: #64748b;
        font-size: 10px;
    }

    .record-count {
        padding: 6px 9px;
        border-radius: 7px;
        background: #f1f5f9;
        color: #64748b;
        font-size: 9px;
        font-weight: 700;
        white-space: nowrap;
    }


    /* WEEK */

    .week-grid {
        display: grid;
        grid-template-columns: repeat(7, 1fr);
        gap: 10px;
    }

    .day-card {
        padding: 13px 8px;
        border: 1px solid #e2e8f0;
        border-radius: 10px;
        text-align: center;
        background: #f8fafc;
    }

    .day-name {
        display: block;
        color: #64748b;
        font-size: 9px;
        font-weight: 600;
    }

    .day-date {
        display: block;
        margin: 3px 0 9px;
        color: #0f172a;
        font-size: 15px;
    }

    .day-status {
        width: 31px;
        height: 31px;
        display: flex;
        align-items: center;
        justify-content: center;
        margin: 0 auto 5px;
        border-radius: 50%;
    }

    .day-status.present {
        background: #dcfce7;
        color: #16a34a;
    }

    .day-status.late {
        background: #ffedd5;
        color: #ea580c;
    }

    .day-status.holiday {
        background: #f1f5f9;
        color: #64748b;
    }

    .day-card small {
        color: #64748b;
        font-size: 8px;
    }


    /* TABLE */

    .table-wrapper {
        width: 100%;
        overflow-x: auto;
    }

    table {
        width: 100%;
        border-collapse: collapse;
        min-width: 700px;
    }

    th {
        padding: 11px 12px;
        border-bottom: 1px solid #e2e8f0;
        background: #f8fafc;
        color: #64748b;
        font-size: 9px;
        font-weight: 700;
        text-align: left;
    }

    td {
        padding: 13px 12px;
        border-bottom: 1px solid #f1f5f9;
        color: #64748b;
        font-size: 10px;
    }

    tbody tr:last-child td {
        border-bottom: none;
    }

    tbody tr:hover {
        background: #f8fafc;
    }

    td strong {
        color: #334155;
    }

    .time {
        display: inline-flex;
        align-items: center;
        gap: 5px;
    }

    .status {
        display: inline-flex;
        align-items: center;
        gap: 4px;
        padding: 5px 8px;
        border-radius: 7px;
        font-size: 8px;
        font-weight: 700;
    }

    .present-status {
        background: #ecfdf5;
        color: #059669;
    }

    .late-status {
        background: #fff7ed;
        color: #ea580c;
    }


    /* SUMMARY */

    .summary-section {
        margin-bottom: 20px;
    }

    .summary-card {
        display: flex;
        align-items: center;
        gap: 25px;
        padding: 22px;
        border: 1px solid #dbe5f2;
        border-radius: 15px;
        background: white;
        box-shadow: 0 3px 12px rgba(15, 23, 42, 0.03);
    }

    .summary-progress {
        flex-shrink: 0;
    }

    .progress-circle {
        width: 105px;
        height: 105px;
        display: flex;
        align-items: center;
        justify-content: center;
        border-radius: 50%;
        background: conic-gradient(
            #2563eb var(--progress),
            #e2e8f0 var(--progress)
        );
        position: relative;
    }

    .progress-inner {
        width: 80px;
        height: 80px;
        display: flex;
        align-items: center;
        justify-content: center;
        flex-direction: column;
        border-radius: 50%;
        background: white;
    }

    .progress-inner strong {
        color: #0f172a;
        font-size: 17px;
    }

    .progress-inner span {
        margin-top: 2px;
        color: #94a3b8;
        font-size: 8px;
    }

    .summary-content {
        flex: 1;
    }

    .summary-content h3 {
        margin: 0;
        color: #0f172a;
        font-size: 15px;
    }

    .summary-content > p {
        margin: 5px 0 12px;
        color: #64748b;
        font-size: 10px;
        line-height: 1.5;
    }

    .summary-content > p strong {
        color: #2563eb;
    }

    .summary-points {
        display: flex;
        align-items: center;
        flex-wrap: wrap;
        gap: 12px;
    }

    .summary-points span {
        display: flex;
        align-items: center;
        gap: 5px;
        color: #64748b;
        font-size: 9px;
    }

    .summary-points span:nth-child(1) {
        color: #059669;
    }

    .summary-points span:nth-child(2) {
        color: #ea580c;
    }

    .summary-points span:nth-child(3) {
        color: #dc2626;
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

        .week-grid {
            grid-template-columns: repeat(4, 1fr);
        }
    }


    @media (max-width: 700px) {

        .attendance-page {
            padding: 18px;
        }

        .page-header {
            align-items: flex-start;
            flex-direction: column;
        }

        .month-selector {
            width: 100%;
        }

        .employee-info {
            align-items: flex-start;
            flex-wrap: wrap;
        }

        .attendance-status {
            width: 100%;
        }

        .stats-grid {
            grid-template-columns: 1fr;
        }

        .week-grid {
            grid-template-columns: repeat(2, 1fr);
        }

        .card {
            padding: 16px;
        }

        .summary-card {
            align-items: flex-start;
            flex-direction: column;
        }

        .summary-points {
            flex-direction: column;
            align-items: flex-start;
        }
    }
</style>