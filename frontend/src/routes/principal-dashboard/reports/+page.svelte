<script lang="ts">
    import PrincipalSidebar from '$lib/components/principal/PrincipalSidebar.svelte';

    type ReportType =
        | 'attendance'
        | 'student-performance'
        | 'teacher-attendance'
        | 'employee-attendance'
        | 'leave'
        | 'assignment'
        | 'library';

    type Period =
        | 'today'
        | 'this-week'
        | 'this-month'
        | 'last-month'
        | 'custom';

    let reportType = $state<ReportType | ''>('');
    let period = $state<Period>('this-month');

    let startDate = $state('');
    let endDate = $state('');

    let showReport = $state(false);
    let generatedReportName = $state('');
    let message = $state('');

    const reportTypes: {
        value: ReportType;
        label: string;
        description: string;
    }[] = [
        {
            value: 'attendance',
            label: 'Attendance Report',
            description: 'Student attendance summary by class and section.'
        },
        {
            value: 'student-performance',
            label: 'Student Performance Report',
            description: 'Student academic performance and subject results.'
        },
        {
            value: 'teacher-attendance',
            label: 'Teacher Attendance Report',
            description: 'Attendance summary of teaching staff.'
        },
        {
            value: 'employee-attendance',
            label: 'Employee Attendance Report',
            description: 'Attendance summary of employees and support staff.'
        },
        {
            value: 'leave',
            label: 'Leave Report',
            description: 'Teacher and employee leave requests and decisions.'
        },
        {
            value: 'assignment',
            label: 'Assignment Report',
            description: 'Assignment submission and evaluation status.'
        },
        {
            value: 'library',
            label: 'Library Report',
            description: 'Books issued, returned and currently borrowed.'
        }
    ];

    function generateReport() {
        message = '';

        if (!reportType) {
            message = 'Please select a report type.';
            showReport = false;
            return;
        }

        if (period === 'custom' && (!startDate || !endDate)) {
            message = 'Please select both start and end dates.';
            showReport = false;
            return;
        }

        const selectedReport = reportTypes.find(
            (report) => report.value === reportType
        );

        generatedReportName = selectedReport?.label ?? 'Report';
        showReport = true;
    }

    function getPeriodLabel() {
        if (period === 'today') return 'Today';
        if (period === 'this-week') return 'This Week';
        if (period === 'this-month') return 'This Month';
        if (period === 'last-month') return 'Last Month';

        if (startDate && endDate) {
            return `${startDate} to ${endDate}`;
        }

        return 'Custom Date Range';
    }

    function viewReport() {
        message = 'Report preview is displayed below using demo data.';
    }

    function downloadReport() {
        message =
            'Demo download requested. Real PDF/Excel generation will be connected through the backend later.';
    }
</script>


<div class="principal-layout">

    <PrincipalSidebar />

    <main class="main-content">

        <div class="reports-page">

            <!-- PAGE HEADER -->

            <header class="page-header">

                <div>
                    <h1>Reports</h1>

                    <p>
                        Generate and monitor important reports for your institution.
                    </p>
                </div>

            </header>


            <!-- REPORT GENERATOR -->

            <section class="generator-card">

                <div class="section-heading">

                    <div class="heading-icon">
                        ▥
                    </div>

                    <div>
                        <h2>Generate Report</h2>

                        <p>
                            Select the report type and time period you want to review.
                        </p>
                    </div>

                </div>


                <div class="form-grid">

                    <!-- REPORT TYPE -->

                    <div class="field">

                        <label for="report-type">
                            Report Type
                        </label>

                        <select
                            id="report-type"
                            bind:value={reportType}
                        >

                            <option value="">
                                Select Report
                            </option>

                            {#each reportTypes as report}

                                <option value={report.value}>
                                    {report.label}
                                </option>

                            {/each}

                        </select>

                    </div>


                    <!-- PERIOD -->

                    <div class="field">

                        <label for="report-period">
                            Period
                        </label>

                        <select
                            id="report-period"
                            bind:value={period}
                        >

                            <option value="today">
                                Today
                            </option>

                            <option value="this-week">
                                This Week
                            </option>

                            <option value="this-month">
                                This Month
                            </option>

                            <option value="last-month">
                                Last Month
                            </option>

                            <option value="custom">
                                Custom Date Range
                            </option>

                        </select>

                    </div>


                    {#if period === 'custom'}

                        <div class="field">

                            <label for="start-date">
                                Start Date
                            </label>

                            <input
                                id="start-date"
                                type="date"
                                bind:value={startDate}
                            />

                        </div>


                        <div class="field">

                            <label for="end-date">
                                End Date
                            </label>

                            <input
                                id="end-date"
                                type="date"
                                bind:value={endDate}
                            />

                        </div>

                    {/if}

                </div>


                {#if reportType}

                    {@const selectedReport = reportTypes.find(
                        (report) => report.value === reportType
                    )}

                    {#if selectedReport}

                        <div class="report-description">

                            <div class="description-icon">
                                i
                            </div>

                            <div>
                                <strong>
                                    {selectedReport.label}
                                </strong>

                                <p>
                                    {selectedReport.description}
                                </p>
                            </div>

                        </div>

                    {/if}

                {/if}


                <button
                    type="button"
                    class="generate-button"
                    onclick={generateReport}
                >
                    Generate Report
                </button>


                {#if message}

                    <div class="message">
                        {message}
                    </div>

                {/if}

            </section>


            <!-- REPORT RESULT -->

            {#if showReport}

                <section class="report-result">

                    <div class="result-header">

                        <div>

                            <span class="result-label">
                                GENERATED REPORT
                            </span>

                            <h2>
                                {generatedReportName}
                            </h2>

                            <p>
                                Period: {getPeriodLabel()}
                            </p>

                        </div>


                        <div class="result-actions">

                            <button
                                type="button"
                                class="secondary-button"
                                onclick={viewReport}
                            >
                                View Report
                            </button>

                            <button
                                type="button"
                                class="download-button"
                                onclick={downloadReport}
                            >
                                Download
                            </button>

                        </div>

                    </div>


                    {#if reportType === 'attendance'}

                        <!-- ATTENDANCE REPORT -->

                        <div class="report-summary-grid">

                            <div class="report-stat">
                                <span>Total Students</span>
                                <strong>450</strong>
                            </div>

                            <div class="report-stat">
                                <span>Present</span>
                                <strong>410</strong>
                            </div>

                            <div class="report-stat">
                                <span>Absent</span>
                                <strong>25</strong>
                            </div>

                            <div class="report-stat">
                                <span>Leave</span>
                                <strong>15</strong>
                            </div>

                        </div>


                        <div class="overall-box">

                            <div>
                                <span>Overall Attendance</span>
                                <strong>91.1%</strong>
                            </div>

                            <div class="progress-track">
                                <div
                                    class="progress-fill"
                                    style="width: 91.1%"
                                ></div>
                            </div>

                        </div>


                        <div class="report-table">

                            <h3>
                                Class-wise Attendance
                            </h3>

                            <table>

                                <thead>

                                    <tr>
                                        <th>Class</th>
                                        <th>Section</th>
                                        <th>Total Students</th>
                                        <th>Attendance</th>
                                    </tr>

                                </thead>

                                <tbody>

                                    <tr>
                                        <td>Class 10</td>
                                        <td>A</td>
                                        <td>42</td>
                                        <td>94%</td>
                                    </tr>

                                    <tr>
                                        <td>Class 10</td>
                                        <td>B</td>
                                        <td>40</td>
                                        <td>91%</td>
                                    </tr>

                                    <tr>
                                        <td>Class 9</td>
                                        <td>A</td>
                                        <td>38</td>
                                        <td>89%</td>
                                    </tr>

                                    <tr>
                                        <td>Class 9</td>
                                        <td>B</td>
                                        <td>41</td>
                                        <td>92%</td>
                                    </tr>

                                </tbody>

                            </table>

                        </div>


                    {:else if reportType === 'student-performance'}

                        <!-- STUDENT PERFORMANCE -->

                        <div class="report-summary-grid">

                            <div class="report-stat">
                                <span>Total Students</span>
                                <strong>450</strong>
                            </div>

                            <div class="report-stat">
                                <span>Excellent</span>
                                <strong>86</strong>
                            </div>

                            <div class="report-stat">
                                <span>Average</span>
                                <strong>291</strong>
                            </div>

                            <div class="report-stat">
                                <span>Needs Attention</span>
                                <strong>73</strong>
                            </div>

                        </div>


                        <div class="report-table">

                            <h3>
                                Class Performance
                            </h3>

                            <table>

                                <thead>

                                    <tr>
                                        <th>Class</th>
                                        <th>Section</th>
                                        <th>Average</th>
                                        <th>Top Performance</th>
                                        <th>Needs Attention</th>
                                    </tr>

                                </thead>

                                <tbody>

                                    <tr>
                                        <td>Class 10</td>
                                        <td>A</td>
                                        <td>82%</td>
                                        <td>94%</td>
                                        <td>4 Students</td>
                                    </tr>

                                    <tr>
                                        <td>Class 10</td>
                                        <td>B</td>
                                        <td>78%</td>
                                        <td>91%</td>
                                        <td>7 Students</td>
                                    </tr>

                                    <tr>
                                        <td>Class 9</td>
                                        <td>A</td>
                                        <td>81%</td>
                                        <td>93%</td>
                                        <td>5 Students</td>
                                    </tr>

                                </tbody>

                            </table>

                        </div>


                    {:else if reportType === 'teacher-attendance'}

                        <!-- TEACHER ATTENDANCE -->

                        <div class="report-summary-grid">

                            <div class="report-stat">
                                <span>Total Teachers</span>
                                <strong>35</strong>
                            </div>

                            <div class="report-stat">
                                <span>Present Days</span>
                                <strong>820</strong>
                            </div>

                            <div class="report-stat">
                                <span>Absent Days</span>
                                <strong>21</strong>
                            </div>

                            <div class="report-stat">
                                <span>Leave Days</span>
                                <strong>34</strong>
                            </div>

                        </div>


                        <div class="overall-box">

                            <div>
                                <span>Overall Teacher Attendance</span>
                                <strong>93.7%</strong>
                            </div>

                            <div class="progress-track">
                                <div
                                    class="progress-fill"
                                    style="width: 93.7%"
                                ></div>
                            </div>

                        </div>


                        <div class="report-table">

                            <h3>
                                Teacher Attendance
                            </h3>

                            <table>

                                <thead>

                                    <tr>
                                        <th>Teacher ID</th>
                                        <th>Teacher</th>
                                        <th>Present</th>
                                        <th>Absent</th>
                                        <th>Attendance</th>
                                    </tr>

                                </thead>

                                <tbody>

                                    <tr>
                                        <td>TCH001</td>
                                        <td>Rahul Sharma</td>
                                        <td>23</td>
                                        <td>1</td>
                                        <td>95.8%</td>
                                    </tr>

                                    <tr>
                                        <td>TCH002</td>
                                        <td>Sana Khan</td>
                                        <td>22</td>
                                        <td>2</td>
                                        <td>91.7%</td>
                                    </tr>

                                    <tr>
                                        <td>TCH003</td>
                                        <td>Arjun Reddy</td>
                                        <td>24</td>
                                        <td>0</td>
                                        <td>100%</td>
                                    </tr>

                                </tbody>

                            </table>

                        </div>


                    {:else if reportType === 'employee-attendance'}

                        <!-- EMPLOYEE ATTENDANCE -->

                        <div class="report-summary-grid">

                            <div class="report-stat">
                                <span>Total Employees</span>
                                <strong>28</strong>
                            </div>

                            <div class="report-stat">
                                <span>Present Days</span>
                                <strong>640</strong>
                            </div>

                            <div class="report-stat">
                                <span>Absent Days</span>
                                <strong>18</strong>
                            </div>

                            <div class="report-stat">
                                <span>Leave Days</span>
                                <strong>27</strong>
                            </div>

                        </div>


                        <div class="report-table">

                            <h3>
                                Employee Attendance
                            </h3>

                            <table>

                                <thead>

                                    <tr>
                                        <th>Employee ID</th>
                                        <th>Employee</th>
                                        <th>Department</th>
                                        <th>Attendance</th>
                                    </tr>

                                </thead>

                                <tbody>

                                    <tr>
                                        <td>EMP001</td>
                                        <td>Ravi Kumar</td>
                                        <td>Library</td>
                                        <td>94%</td>
                                    </tr>

                                    <tr>
                                        <td>EMP002</td>
                                        <td>Mahesh Kumar</td>
                                        <td>Driving</td>
                                        <td>91%</td>
                                    </tr>

                                    <tr>
                                        <td>EMP003</td>
                                        <td>Salman Ahmed</td>
                                        <td>Lab Assistant</td>
                                        <td>96%</td>
                                    </tr>

                                </tbody>

                            </table>

                        </div>


                    {:else if reportType === 'leave'}

                        <!-- LEAVE REPORT -->

                        <div class="report-summary-grid">

                            <div class="report-stat">
                                <span>Total Requests</span>
                                <strong>18</strong>
                            </div>

                            <div class="report-stat">
                                <span>Approved</span>
                                <strong>12</strong>
                            </div>

                            <div class="report-stat">
                                <span>Pending</span>
                                <strong>4</strong>
                            </div>

                            <div class="report-stat">
                                <span>Rejected</span>
                                <strong>2</strong>
                            </div>

                        </div>


                        <div class="report-table">

                            <h3>
                                Leave Requests
                            </h3>

                            <table>

                                <thead>

                                    <tr>
                                        <th>Employee / Teacher</th>
                                        <th>ID</th>
                                        <th>Leave Date</th>
                                        <th>Reason</th>
                                        <th>Status</th>
                                    </tr>

                                </thead>

                                <tbody>

                                    <tr>
                                        <td>Rahul Sharma</td>
                                        <td>TCH001</td>
                                        <td>18 Aug 2026</td>
                                        <td>Personal</td>
                                        <td>
                                            <span class="status approved">
                                                Approved
                                            </span>
                                        </td>
                                    </tr>

                                    <tr>
                                        <td>Ravi Kumar</td>
                                        <td>EMP001</td>
                                        <td>22 Aug 2026</td>
                                        <td>Medical</td>
                                        <td>
                                            <span class="status pending">
                                                Pending
                                            </span>
                                        </td>
                                    </tr>

                                </tbody>

                            </table>

                        </div>


                    {:else if reportType === 'assignment'}

                        <!-- ASSIGNMENT REPORT -->

                        <div class="report-summary-grid">

                            <div class="report-stat">
                                <span>Total Assignments</span>
                                <strong>74</strong>
                            </div>

                            <div class="report-stat">
                                <span>Submitted</span>
                                <strong>61</strong>
                            </div>

                            <div class="report-stat">
                                <span>Pending</span>
                                <strong>13</strong>
                            </div>

                            <div class="report-stat">
                                <span>Evaluated</span>
                                <strong>49</strong>
                            </div>

                        </div>


                        <div class="report-table">

                            <h3>
                                Assignment Summary
                            </h3>

                            <table>

                                <thead>

                                    <tr>
                                        <th>Class</th>
                                        <th>Section</th>
                                        <th>Assignments</th>
                                        <th>Submitted</th>
                                        <th>Pending</th>
                                    </tr>

                                </thead>

                                <tbody>

                                    <tr>
                                        <td>Class 10</td>
                                        <td>A</td>
                                        <td>18</td>
                                        <td>16</td>
                                        <td>2</td>
                                    </tr>

                                    <tr>
                                        <td>Class 10</td>
                                        <td>B</td>
                                        <td>16</td>
                                        <td>13</td>
                                        <td>3</td>
                                    </tr>

                                    <tr>
                                        <td>Class 9</td>
                                        <td>A</td>
                                        <td>14</td>
                                        <td>12</td>
                                        <td>2</td>
                                    </tr>

                                </tbody>

                            </table>

                        </div>


                    {:else if reportType === 'library'}

                        <!-- LIBRARY REPORT -->

                        <div class="report-summary-grid">

                            <div class="report-stat">
                                <span>Total Books</span>
                                <strong>2,450</strong>
                            </div>

                            <div class="report-stat">
                                <span>Issued</span>
                                <strong>183</strong>
                            </div>

                            <div class="report-stat">
                                <span>Returned</span>
                                <strong>142</strong>
                            </div>

                            <div class="report-stat">
                                <span>Currently Borrowed</span>
                                <strong>41</strong>
                            </div>

                        </div>


                        <div class="report-table">

                            <h3>
                                Library Summary
                            </h3>

                            <table>

                                <thead>

                                    <tr>
                                        <th>Category</th>
                                        <th>Total Books</th>
                                        <th>Issued</th>
                                        <th>Available</th>
                                    </tr>

                                </thead>

                                <tbody>

                                    <tr>
                                        <td>Literature</td>
                                        <td>420</td>
                                        <td>31</td>
                                        <td>389</td>
                                    </tr>

                                    <tr>
                                        <td>Science</td>
                                        <td>510</td>
                                        <td>42</td>
                                        <td>468</td>
                                    </tr>

                                    <tr>
                                        <td>Computer Science</td>
                                        <td>380</td>
                                        <td>35</td>
                                        <td>345</td>
                                    </tr>

                                    <tr>
                                        <td>Mathematics</td>
                                        <td>310</td>
                                        <td>27</td>
                                        <td>283</td>
                                    </tr>

                                </tbody>

                            </table>

                        </div>

                    {/if}

                </section>

            {/if}

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


    .reports-page {
        min-height: 100vh;
        padding: 28px 32px;
        box-sizing: border-box;
        background: #f7f9fc;
    }


    /* HEADER */

    .page-header {
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


    /* GENERATOR */

    .generator-card {
        padding: 24px;
        background: white;
        border: 1px solid #e5eaf2;
        border-radius: 16px;
        box-shadow:
            0 4px 14px
            rgba(15, 23, 42, 0.03);
    }


    .section-heading {
        display: flex;
        align-items: center;
        gap: 13px;
        margin-bottom: 22px;
    }


    .heading-icon {
        width: 44px;
        height: 44px;
        display: flex;
        align-items: center;
        justify-content: center;
        border-radius: 12px;
        background: #eef4ff;
        color: #2563eb;
        font-size: 20px;
    }


    .section-heading h2 {
        margin: 0;
        color: #14213d;
        font-size: 19px;
    }


    .section-heading p {
        margin: 4px 0 0;
        color: #64748b;
        font-size: 12px;
    }


    .form-grid {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 15px;
    }


    .field label {
        display: block;
        margin-bottom: 7px;
        color: #334155;
        font-size: 12px;
        font-weight: 600;
    }


    .field select,
    .field input {
        width: 100%;
        height: 42px;
        padding: 0 11px;
        box-sizing: border-box;
        border: 1px solid #dbe3ef;
        border-radius: 9px;
        background: white;
        color: #1e293b;
        font-size: 13px;
        outline: none;
    }


    .field select:focus,
    .field input:focus {
        border-color: #2563eb;
        box-shadow:
            0 0 0 3px
            rgba(37, 99, 235, 0.1);
    }


    /* DESCRIPTION */

    .report-description {
        display: flex;
        align-items: center;
        gap: 11px;
        margin-top: 18px;
        padding: 13px;
        border: 1px solid #e5eaf2;
        border-radius: 10px;
        background: #f8fafc;
    }


    .description-icon {
        width: 30px;
        height: 30px;
        flex-shrink: 0;
        display: flex;
        align-items: center;
        justify-content: center;
        border-radius: 50%;
        background: #eef4ff;
        color: #2563eb;
        font-size: 13px;
        font-weight: 700;
    }


    .report-description strong {
        display: block;
        color: #334155;
        font-size: 12px;
    }


    .report-description p {
        margin: 3px 0 0;
        color: #64748b;
        font-size: 11px;
    }


    /* BUTTON */

    .generate-button {
        width: 100%;
        height: 42px;
        margin-top: 18px;
        border: none;
        border-radius: 9px;
        background: #2563eb;
        color: white;
        font-size: 13px;
        font-weight: 600;
        cursor: pointer;
    }


    .generate-button:hover {
        background: #1d4ed8;
    }


    .message {
        margin-top: 13px;
        padding: 10px 12px;
        border: 1px solid #bfdbfe;
        border-radius: 8px;
        background: #eff6ff;
        color: #2563eb;
        font-size: 11px;
    }


    /* RESULT */

    .report-result {
        margin-top: 24px;
        padding: 24px;
        background: white;
        border: 1px solid #e5eaf2;
        border-radius: 16px;
        box-shadow:
            0 4px 14px
            rgba(15, 23, 42, 0.03);
    }


    .result-header {
        display: flex;
        align-items: center;
        justify-content: space-between;
        gap: 20px;
        padding-bottom: 18px;
        border-bottom: 1px solid #edf1f6;
    }


    .result-label {
        display: block;
        margin-bottom: 5px;
        color: #2563eb;
        font-size: 9px;
        font-weight: 700;
        letter-spacing: 0.7px;
    }


    .result-header h2 {
        margin: 0;
        color: #14213d;
        font-size: 20px;
    }


    .result-header p {
        margin: 5px 0 0;
        color: #64748b;
        font-size: 11px;
    }


    .result-actions {
        display: flex;
        gap: 8px;
    }


    .secondary-button,
    .download-button {
        height: 38px;
        padding: 0 14px;
        border-radius: 8px;
        font-size: 11px;
        font-weight: 600;
        cursor: pointer;
    }


    .secondary-button {
        border: 1px solid #dbe3ef;
        background: white;
        color: #2563eb;
    }


    .download-button {
        border: none;
        background: #2563eb;
        color: white;
    }


    .secondary-button:hover {
        background: #eef4ff;
    }


    .download-button:hover {
        background: #1d4ed8;
    }


    /* SUMMARY */

    .report-summary-grid {
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 12px;
        margin-top: 20px;
    }


    .report-stat {
        padding: 16px;
        border: 1px solid #e5eaf2;
        border-radius: 10px;
        background: #f8fafc;
    }


    .report-stat span {
        display: block;
        margin-bottom: 6px;
        color: #64748b;
        font-size: 10px;
    }


    .report-stat strong {
        color: #14213d;
        font-size: 20px;
    }


    /* OVERALL */

    .overall-box {
        margin-top: 14px;
        padding: 16px;
        border: 1px solid #e5eaf2;
        border-radius: 10px;
        background: #f8fafc;
    }


    .overall-box span {
        display: block;
        margin-bottom: 5px;
        color: #64748b;
        font-size: 10px;
    }


    .overall-box strong {
        display: block;
        margin-bottom: 12px;
        color: #2563eb;
        font-size: 22px;
    }


    .progress-track {
        width: 100%;
        height: 8px;
        overflow: hidden;
        border-radius: 10px;
        background: #e2e8f0;
    }


    .progress-fill {
        height: 100%;
        border-radius: 10px;
        background: #2563eb;
    }


    /* TABLE */

    .report-table {
        margin-top: 22px;
    }


    .report-table h3 {
        margin: 0 0 12px;
        color: #14213d;
        font-size: 15px;
    }


    .report-table {
        overflow-x: auto;
    }


    table {
        width: 100%;
        min-width: 650px;
        border-collapse: collapse;
    }


    th {
        padding: 13px 15px;
        background: #f8fafc;
        color: #64748b;
        font-size: 10px;
        font-weight: 700;
        text-align: left;
        border-bottom: 1px solid #e5eaf2;
    }


    td {
        padding: 14px 15px;
        color: #64748b;
        font-size: 11px;
        border-bottom: 1px solid #edf1f6;
    }


    tr:last-child td {
        border-bottom: none;
    }


    td:first-child {
        color: #14213d;
        font-weight: 600;
    }


    /* STATUS */

    .status {
        display: inline-block;
        padding: 5px 8px;
        border-radius: 6px;
        font-size: 9px;
        font-weight: 700;
    }


    .approved {
        background: #f0fdf4;
        color: #16a34a;
    }


    .pending {
        background: #fff7ed;
        color: #ea580c;
    }


    /* RESPONSIVE */

    @media (max-width: 900px) {

        .reports-page {
            padding: 22px;
        }


        .report-summary-grid {
            grid-template-columns: repeat(2, 1fr);
        }

    }


    @media (max-width: 650px) {

        .reports-page {
            padding: 18px;
        }


        .form-grid {
            grid-template-columns: 1fr;
        }


        .result-header {
            align-items: flex-start;
            flex-direction: column;
        }


        .result-actions {
            width: 100%;
        }


        .secondary-button,
        .download-button {
            flex: 1;
        }

    }


    @media (max-width: 500px) {

        .report-summary-grid {
            grid-template-columns: 1fr;
        }

    }

</style>