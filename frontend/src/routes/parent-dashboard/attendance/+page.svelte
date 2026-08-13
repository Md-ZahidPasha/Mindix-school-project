<script lang="ts">
    import {
        CalendarCheck,
        CheckCircle2,
        XCircle,
        Clock3,
        ChevronDown,
        TrendingUp
    } from '@lucide/svelte';

    let selectedChild = $state('Rahul Kumar');

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

    const attendanceData = {
        'Rahul Kumar': {
            percentage: 93,
            total: 93,
            present: 86,
            absent: 5,
            late: 2,
            workingDays: 93
        },
        'Ayesha Kumar': {
            percentage: 95,
            total: 95,
            present: 90,
            absent: 3,
            late: 2,
            workingDays: 95
        }
    };

    const monthlyAttendance = [
        { month: 'January', present: 19, absent: 1, percentage: 95 },
        { month: 'February', present: 18, absent: 2, percentage: 90 },
        { month: 'March', present: 21, absent: 1, percentage: 95 },
        { month: 'April', present: 20, absent: 2, percentage: 91 },
        { month: 'May', present: 18, absent: 1, percentage: 95 },
        { month: 'June', present: 17, absent: 2, percentage: 89 },
        { month: 'July', present: 20, absent: 1, percentage: 95 },
        { month: 'August', present: 13, absent: 0, percentage: 100 }
    ];

    const subjectAttendance = [
        {
            subject: 'Mathematics',
            present: 24,
            total: 25,
            percentage: 96
        },
        {
            subject: 'Science',
            present: 23,
            total: 25,
            percentage: 92
        },
        {
            subject: 'English',
            present: 24,
            total: 26,
            percentage: 92
        },
        {
            subject: 'Social Studies',
            present: 22,
            total: 24,
            percentage: 92
        },
        {
            subject: 'Computer Science',
            present: 21,
            total: 23,
            percentage: 91
        },
        {
            subject: 'Hindi',
            present: 20,
            total: 22,
            percentage: 91
        }
    ];

    const recentAttendance = [
        {
            date: '11 Aug 2026',
            day: 'Tuesday',
            status: 'Present'
        },
        {
            date: '10 Aug 2026',
            day: 'Monday',
            status: 'Present'
        },
        {
            date: '08 Aug 2026',
            day: 'Saturday',
            status: 'Present'
        },
        {
            date: '07 Aug 2026',
            day: 'Friday',
            status: 'Absent'
        },
        {
            date: '06 Aug 2026',
            day: 'Thursday',
            status: 'Present'
        }
    ];

    function getAttendance() {
        return attendanceData[
            selectedChild as keyof typeof attendanceData
        ];
    }

    function getSelectedChild() {
        return children.find(
            (child) => child.name === selectedChild
        );
    }
    let child = $derived(getSelectedChild());

    let attendance = $derived(getAttendance());
</script>

<svelte:head>
    <title>Attendance | Parent Dashboard</title>
</svelte:head>

<div class="attendance-page">

    <!-- HEADER -->
    <div class="page-header">

        <div>
            <div class="title-row">
                <div class="title-icon">
                    <CalendarCheck size={24} />
                </div>

                <div>
                    <h1>Attendance</h1>
                    <p>
                        Monitor your child's attendance and
                        daily presence.
                    </p>
                </div>
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
        {#each children as child}
            <option value={child.name}>
                {child.name} · {child.studentId}
            </option>
        {/each}
    </select>

    <span class="select-icon">
        <ChevronDown size={17} />
    </span>

</div>     

        </div>

    </div>


    <!-- CHILD INFORMATION -->

    <section class="child-info-card">

        <div class="child-avatar">
            {child?.name.charAt(0)}
        </div>

        <div class="child-details">

            <h2>{child?.name}</h2>

            <p>
                Student ID: <strong>{child?.studentId}</strong>
                <span>•</span>
                Class: <strong>{child?.className}</strong>
                <span>•</span>
                Section: <strong>{child?.section}</strong>
            </p>

        </div>

        <div class="attendance-status">

            <span>Current Attendance</span>

            <strong>{attendance.percentage}%</strong>

            <small>
                {attendance.percentage >= 75
                    ? 'Good Attendance'
                    : 'Attendance Needs Attention'}
            </small>

        </div>

    </section>


    <!-- SUMMARY CARDS -->
    <section class="summary-grid">

        <div class="summary-card">

            <div class="summary-icon blue">
                <CalendarCheck size={21} />
            </div>

            <div>
                <span>Total Classes</span>
                <strong>{attendance.total}</strong>
            </div>

        </div>


        <div class="summary-card">

            <div class="summary-icon green">
                <CheckCircle2 size={21} />
            </div>

            <div>
                <span>Present</span>
                <strong>{attendance.present}</strong>
            </div>

        </div>


        <div class="summary-card">

            <div class="summary-icon red">
                <XCircle size={21} />
            </div>

            <div>
                <span>Absent</span>
                <strong>{attendance.absent}</strong>
            </div>

        </div>


        <div class="summary-card">

            <div class="summary-icon orange">
                <Clock3 size={21} />
            </div>

            <div>
                <span>Late</span>
                <strong>{attendance.late}</strong>
            </div>

        </div>

    </section>


    <!-- ATTENDANCE OVERVIEW -->
    <div class="content-grid">

        <section class="card">

            <div class="card-header">

                <div>
                    <h2>Attendance Overview</h2>
                    <p>Current academic year attendance</p>
                </div>

                <span class="trend-icon">
                     <TrendingUp size={20} />
                </span>                

            </div>


            <div class="percentage-area">

                <div class="percentage-circle">

                    <div>
                        <strong>{attendance.percentage}%</strong>
                        <span>Attendance</span>
                    </div>

                </div>


                <div class="percentage-info">

                    <div class="legend-item">
                        <span class="dot present"></span>
                        <div>
                            <strong>{attendance.present}</strong>
                            <small>Present</small>
                        </div>
                    </div>

                    <div class="legend-item">
                        <span class="dot absent"></span>
                        <div>
                            <strong>{attendance.absent}</strong>
                            <small>Absent</small>
                        </div>
                    </div>

                    <div class="legend-item">
                        <span class="dot late"></span>
                        <div>
                            <strong>{attendance.late}</strong>
                            <small>Late</small>
                        </div>
                    </div>

                </div>

            </div>


            <div class="attendance-progress">

                <div class="progress-header">
                    <span>Attendance Percentage</span>
                    <strong>{attendance.percentage}%</strong>
                </div>

                <div class="progress-track">
                    <div
                        class="progress-fill"
                        style={`width: ${attendance.percentage}%`}
                    ></div>
                </div>

                <p>
                    Minimum required attendance: 75%
                </p>

            </div>

        </section>


        <!-- ATTENDANCE STATUS -->
        <section class="card status-card">

            <div class="card-header">
                <div>
                    <h2>Attendance Status</h2>
                    <p>Current attendance standing</p>
                </div>
            </div>


            <div class="status-main">

                <div class="status-circle">
                    <CheckCircle2 size={32} />
                </div>

                <h3>
                    Good Attendance
                </h3>

                <p>
                    {child?.name} has maintained attendance
                    above the required 75% threshold.
                </p>

            </div>


            <div class="status-details">

                <div>
                    <span>Required</span>
                    <strong>75%</strong>
                </div>

                <div>
                    <span>Current</span>
                    <strong>{attendance.percentage}%</strong>
                </div>

                <div>
                    <span>Difference</span>
                    <strong>
                        +{attendance.percentage - 75}%
                    </strong>
                </div>

            </div>

        </section>

    </div>


    <!-- MONTHLY ATTENDANCE -->
    <section class="card">

        <div class="card-header">

            <div>
                <h2>Monthly Attendance</h2>
                <p>
                    Month-wise attendance for the academic year.
                </p>
            </div>

        </div>


        <div class="monthly-list">

            {#each monthlyAttendance as month}

                <div class="monthly-row">

                    <div class="month-name">
                        <strong>{month.month}</strong>

                        <span>
                            {month.present} present
                            · {month.absent} absent
                        </span>
                    </div>


                    <div class="monthly-progress">

                        <div class="monthly-track">
                            <div
                                class="monthly-fill"
                                style={`width: ${month.percentage}%`}
                            ></div>
                        </div>

                    </div>


                    <strong class="monthly-percentage">
                        {month.percentage}%
                    </strong>

                </div>

            {/each}

        </div>

    </section>


    <!-- SUBJECT ATTENDANCE -->
    <section class="card">

        <div class="card-header">

            <div>
                <h2>Subject-wise Attendance</h2>
                <p>
                    Attendance breakdown by subject.
                </p>
            </div>

        </div>


        <div class="subject-grid">

            {#each subjectAttendance as subject}

                <div class="subject-card">

                    <div class="subject-header">

                        <strong>
                            {subject.subject}
                        </strong>

                        <span>
                            {subject.percentage}%
                        </span>

                    </div>

                    <div class="subject-progress">

                        <div
                            class="subject-fill"
                            style={`width: ${subject.percentage}%`}
                        ></div>

                    </div>

                    <div class="subject-footer">

                        <span>
                            {subject.present} / {subject.total}
                            classes
                        </span>

                        {#if subject.percentage >= 90}

                            <small class="good">
                                Good
                            </small>

                        {:else}

                            <small class="watch">
                                Monitor
                            </small>

                        {/if}

                    </div>

                </div>

            {/each}

        </div>

    </section>


    <!-- RECENT ATTENDANCE -->
    <section class="card">

        <div class="card-header">

            <div>
                <h2>Recent Attendance</h2>
                <p>
                    Latest attendance records.
                </p>
            </div>

        </div>


        <div class="recent-list">

            {#each recentAttendance as record}

                <div class="recent-row">

                    <div class="date-icon">
                        <CalendarCheck size={18} />
                    </div>

                    <div class="date-details">

                        <strong>{record.date}</strong>

                        <span>{record.day}</span>

                    </div>


                    {#if record.status === 'Present'}

                        <span class="record-status present-status">
                            <CheckCircle2 size={14} />
                            Present
                        </span>

                    {:else}

                        <span class="record-status absent-status">
                            <XCircle size={14} />
                            Absent
                        </span>

                    {/if}

                </div>

            {/each}

        </div>

    </section>


    <!-- NOTE -->
    <div class="info-note">

        <div class="note-icon">
            <CalendarCheck size={18} />
        </div>

        <div>
            <strong>Attendance Information</strong>

            <p>
                Attendance data shown here is for the selected
                child. The final attendance records will be
                retrieved from the school database when API
                integration is completed.
            </p>
        </div>

    </div>

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
        font-size: 28px;
        font-weight: 800;
        color: #0f172a;
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
    right: 12px;
    top: 13px;
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

    .attendance-status {
        min-width: 150px;
        padding: 12px 16px;
        border-radius: 11px;
        background: #ecfdf5;
        text-align: center;
    }

    .attendance-status span {
        display: block;
        color: #64748b;
        font-size: 10px;
    }

    .attendance-status strong {
        display: block;
        margin: 2px 0;
        color: #059669;
        font-size: 23px;
    }

    .attendance-status small {
        color: #047857;
        font-size: 10px;
        font-weight: 600;
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

    .summary-icon.green {
        background: #ecfdf5;
        color: #059669;
    }

    .summary-icon.red {
        background: #fef2f2;
        color: #dc2626;
    }

    .summary-icon.orange {
        background: #fff7ed;
        color: #ea580c;
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
        font-size: 22px;
    }


    /* CONTENT GRID */

    .content-grid {
        display: grid;
        grid-template-columns: 1.4fr 1fr;
        gap: 20px;
        margin-bottom: 20px;
    }

    .card {
        margin-bottom: 20px;
        padding: 22px;
        border: 1px solid #e2e8f0;
        border-radius: 15px;
        background: white;
        box-shadow: 0 3px 12px rgba(15, 23, 42, 0.03);
    }

    .content-grid .card {
        margin-bottom: 0;
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

    .trend-icon {
    display: flex;
    align-items: center;
    color: #059669;
    }

    /* PERCENTAGE */

    .percentage-area {
        display: flex;
        align-items: center;
        gap: 35px;
    }

    .percentage-circle {
        width: 150px;
        height: 150px;
        display: flex;
        align-items: center;
        justify-content: center;
        flex-shrink: 0;
        border-radius: 50%;
        background: conic-gradient(
            #2563eb 0% 93%,
            #e2e8f0 93% 100%
        );
    }

    .percentage-circle > div {
        width: 118px;
        height: 118px;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        border-radius: 50%;
        background: white;
    }

    .percentage-circle strong {
        color: #0f172a;
        font-size: 28px;
    }

    .percentage-circle span {
        margin-top: 2px;
        color: #64748b;
        font-size: 10px;
    }

    .percentage-info {
        display: flex;
        flex-direction: column;
        gap: 14px;
    }

    .legend-item {
        display: flex;
        align-items: center;
        gap: 9px;
    }

    .dot {
        width: 10px;
        height: 10px;
        border-radius: 50%;
    }

    .dot.present {
        background: #2563eb;
    }

    .dot.absent {
        background: #dc2626;
    }

    .dot.late {
        background: #ea580c;
    }

    .legend-item strong {
        display: block;
        color: #0f172a;
        font-size: 13px;
    }

    .legend-item small {
        display: block;
        color: #64748b;
        font-size: 10px;
    }


    /* PROGRESS */

    .attendance-progress {
        margin-top: 25px;
    }

    .progress-header {
        display: flex;
        align-items: center;
        justify-content: space-between;
        margin-bottom: 7px;
    }

    .progress-header span {
        color: #475569;
        font-size: 11px;
        font-weight: 600;
    }

    .progress-header strong {
        color: #2563eb;
        font-size: 12px;
    }

    .progress-track {
        height: 8px;
        overflow: hidden;
        border-radius: 20px;
        background: #e2e8f0;
    }

    .progress-fill {
        height: 100%;
        border-radius: 20px;
        background: #2563eb;
    }

    .attendance-progress p {
        margin: 7px 0 0;
        color: #94a3b8;
        font-size: 10px;
    }


    /* STATUS */

    .status-main {
        padding: 15px 5px;
        text-align: center;
    }

    .status-circle {
        width: 62px;
        height: 62px;
        display: flex;
        align-items: center;
        justify-content: center;
        margin: 0 auto 12px;
        border-radius: 50%;
        background: #ecfdf5;
        color: #059669;
    }

    .status-main h3 {
        margin: 0;
        color: #047857;
        font-size: 16px;
    }

    .status-main p {
        max-width: 300px;
        margin: 7px auto 0;
        color: #64748b;
        font-size: 11px;
        line-height: 1.5;
    }

    .status-details {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 8px;
        margin-top: 10px;
    }

    .status-details div {
        padding: 10px;
        border-radius: 9px;
        background: #f8fafc;
        text-align: center;
    }

    .status-details span {
        display: block;
        color: #64748b;
        font-size: 9px;
    }

    .status-details strong {
        display: block;
        margin-top: 3px;
        color: #0f172a;
        font-size: 14px;
    }


    /* MONTHLY */

    .monthly-list {
        display: flex;
        flex-direction: column;
        gap: 14px;
    }

    .monthly-row {
        display: grid;
        grid-template-columns: 145px 1fr 55px;
        align-items: center;
        gap: 15px;
    }

    .month-name strong {
        display: block;
        color: #334155;
        font-size: 12px;
    }

    .month-name span {
        display: block;
        margin-top: 3px;
        color: #94a3b8;
        font-size: 9px;
    }

    .monthly-track {
        height: 7px;
        overflow: hidden;
        border-radius: 20px;
        background: #e2e8f0;
    }

    .monthly-fill {
        height: 100%;
        border-radius: 20px;
        background: #2563eb;
    }

    .monthly-percentage {
        color: #334155;
        font-size: 11px;
        text-align: right;
    }


    /* SUBJECT */

    .subject-grid {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 13px;
    }

    .subject-card {
        padding: 15px;
        border: 1px solid #e2e8f0;
        border-radius: 11px;
        background: #f8fafc;
    }

    .subject-header {
        display: flex;
        align-items: center;
        justify-content: space-between;
        gap: 10px;
        margin-bottom: 11px;
    }

    .subject-header strong {
        color: #334155;
        font-size: 12px;
    }

    .subject-header span {
        color: #2563eb;
        font-size: 12px;
        font-weight: 700;
    }

    .subject-progress {
        height: 6px;
        overflow: hidden;
        border-radius: 20px;
        background: #e2e8f0;
    }

    .subject-fill {
        height: 100%;
        border-radius: 20px;
        background: #2563eb;
    }

    .subject-footer {
        display: flex;
        align-items: center;
        justify-content: space-between;
        margin-top: 8px;
    }

    .subject-footer span {
        color: #94a3b8;
        font-size: 9px;
    }

    .subject-footer small {
        font-size: 9px;
        font-weight: 700;
    }

    .subject-footer .good {
        color: #059669;
    }

    .subject-footer .watch {
        color: #ea580c;
    }


    /* RECENT */

    .recent-list {
        display: flex;
        flex-direction: column;
    }

    .recent-row {
        display: flex;
        align-items: center;
        gap: 12px;
        padding: 13px 0;
        border-bottom: 1px solid #e2e8f0;
    }

    .recent-row:last-child {
        border-bottom: none;
    }

    .date-icon {
        width: 38px;
        height: 38px;
        display: flex;
        align-items: center;
        justify-content: center;
        flex-shrink: 0;
        border-radius: 10px;
        background: #eef4ff;
        color: #2563eb;
    }

    .date-details {
        flex: 1;
    }

    .date-details strong {
        display: block;
        color: #334155;
        font-size: 12px;
    }

    .date-details span {
        display: block;
        margin-top: 3px;
        color: #94a3b8;
        font-size: 10px;
    }

    .record-status {
        display: flex;
        align-items: center;
        gap: 5px;
        padding: 6px 9px;
        border-radius: 8px;
        font-size: 10px;
        font-weight: 700;
    }

    .present-status {
        background: #ecfdf5;
        color: #059669;
    }

    .absent-status {
        background: #fef2f2;
        color: #dc2626;
    }


    /* INFO */

    .info-note {
        display: flex;
        align-items: flex-start;
        gap: 11px;
        margin-top: 2px;
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


    /* RESPONSIVE */

    @media (max-width: 1100px) {
        .attendance-page {
            padding: 24px;
        }

        .summary-grid {
            grid-template-columns: repeat(2, 1fr);
        }

        .content-grid {
            grid-template-columns: 1fr;
        }

        .subject-grid {
            grid-template-columns: repeat(2, 1fr);
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

        .child-selector {
            width: 100%;
        }

        .child-info-card {
            align-items: flex-start;
            flex-wrap: wrap;
        }

        .attendance-status {
            width: 100%;
        }

        .summary-grid {
            grid-template-columns: 1fr;
        }

        .percentage-area {
            flex-direction: column;
            gap: 25px;
        }

        .subject-grid {
            grid-template-columns: 1fr;
        }

        .monthly-row {
            grid-template-columns: 100px 1fr 45px;
            gap: 9px;
        }
    }
</style>