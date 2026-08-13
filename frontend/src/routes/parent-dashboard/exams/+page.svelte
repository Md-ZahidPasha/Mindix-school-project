<script lang="ts">
    import {
        GraduationCap,
        ChevronDown,
        CalendarDays,
        Clock3,
        BookOpen,
        Award,
        TrendingUp,
        CheckCircle2,
        FileText
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

    const upcomingExams = [
        {
            name: 'First Term Examination',
            subject: 'Mathematics',
            date: '20 Aug 2026',
            day: 'Thursday',
            time: '10:00 AM - 12:30 PM',
            syllabus: 'Algebra & Geometry',
            daysLeft: 9
        },
        {
            name: 'First Term Examination',
            subject: 'Science',
            date: '23 Aug 2026',
            day: 'Sunday',
            time: '10:00 AM - 12:30 PM',
            syllabus: 'Light & Human Eye',
            daysLeft: 12
        },
        {
            name: 'First Term Examination',
            subject: 'English',
            date: '26 Aug 2026',
            day: 'Wednesday',
            time: '10:00 AM - 12:00 PM',
            syllabus: 'Grammar & Literature',
            daysLeft: 15
        },
        {
            name: 'First Term Examination',
            subject: 'Social Studies',
            date: '28 Aug 2026',
            day: 'Friday',
            time: '10:00 AM - 12:30 PM',
            syllabus: 'History & Geography',
            daysLeft: 17
        }
    ];

    const results = [
        {
            exam: 'Mid Term Examination',
            date: '02 Aug 2026',
            total: 500,
            marks: 405,
            percentage: 81,
            grade: 'A',
            rank: 8
        },
        {
            exam: 'Unit Test - 2',
            date: '18 Jul 2026',
            total: 300,
            marks: 234,
            percentage: 78,
            grade: 'A',
            rank: 11
        },
        {
            exam: 'Unit Test - 1',
            date: '15 Jun 2026',
            total: 300,
            marks: 222,
            percentage: 74,
            grade: 'B+',
            rank: 14
        }
    ];

    const subjectResults = [
        {
            subject: 'Mathematics',
            marks: 78,
            total: 100,
            percentage: 78,
            grade: 'A'
        },
        {
            subject: 'Science',
            marks: 74,
            total: 100,
            percentage: 74,
            grade: 'A'
        },
        {
            subject: 'English',
            marks: 81,
            total: 100,
            percentage: 81,
            grade: 'A+'
        },
        {
            subject: 'Social Studies',
            marks: 75,
            total: 100,
            percentage: 75,
            grade: 'A'
        },
        {
            subject: 'Computer Science',
            marks: 88,
            total: 100,
            percentage: 88,
            grade: 'A+'
        }
    ];

    function getSelectedChild() {
        return children.find(
            (child) => child.name === selectedChild
        );
    }

    let child = $derived(getSelectedChild());

    const latestResult = results[0];

    let averagePercentage = $derived(
        Math.round(
            subjectResults.reduce(
                (sum, item) => sum + item.percentage,
                0
            ) / subjectResults.length
        )
    );
</script>

<svelte:head>
    <title>Exams & Results | Parent Dashboard</title>
</svelte:head>

<div class="exams-page">

    <!-- HEADER -->
    <div class="page-header">

        <div class="title-row">

            <div class="title-icon">
                <GraduationCap size={24} />
            </div>

            <div>
                <h1>Exams & Results</h1>

                <p>
                    View upcoming examinations and your child's
                    academic results.
                </p>
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
                    {#each children as item}
                        <option value={item.name}>
                            {item.name} · {item.studentId}
                        </option>
                    {/each}
                </select>

                <span class="select-icon">
                    <ChevronDown size={17} />
                </span>

            </div>

        </div>

    </div>


    <!-- CHILD INFO -->
    <section class="child-info-card">

        <div class="child-avatar">
            {child?.name.charAt(0)}
        </div>

        <div class="child-details">

            <h2>{child?.name}</h2>

            <p>
                Student ID:
                <strong>{child?.studentId}</strong>

                <span>•</span>

                Class:
                <strong>{child?.className}</strong>

                <span>•</span>

                Section:
                <strong>{child?.section}</strong>
            </p>

        </div>

        <div class="result-summary">

            <span>Latest Result</span>

            <strong>{latestResult.percentage}%</strong>

            <small>
                Grade {latestResult.grade}
            </small>

        </div>

    </section>


    <!-- SUMMARY CARDS -->
    <section class="summary-grid">

        <div class="summary-card">

            <div class="summary-icon blue">
                <CalendarDays size={21} />
            </div>

            <div>
                <span>Upcoming Exams</span>
                <strong>{upcomingExams.length}</strong>
            </div>

        </div>


        <div class="summary-card">

            <div class="summary-icon purple">
                <FileText size={21} />
            </div>

            <div>
                <span>Exams Completed</span>
                <strong>{results.length}</strong>
            </div>

        </div>


        <div class="summary-card">

            <div class="summary-icon green">
                <Award size={21} />
            </div>

            <div>
                <span>Latest Grade</span>
                <strong>{latestResult.grade}</strong>
            </div>

        </div>


        <div class="summary-card">

            <div class="summary-icon orange">
                <TrendingUp size={21} />
            </div>

            <div>
                <span>Average Score</span>
                <strong>{averagePercentage}%</strong>
            </div>

        </div>

    </section>


    <!-- UPCOMING EXAMS -->
    <section class="card">

        <div class="card-header">

            <div>
                <h2>Upcoming Examinations</h2>

                <p>
                    Keep track of the upcoming examination
                    schedule.
                </p>
            </div>

            <span class="count-badge">
                {upcomingExams.length} Upcoming
            </span>

        </div>


        <div class="exam-list">

            {#each upcomingExams as exam}

                <div class="exam-card">

                    <div class="exam-date">

                        <CalendarDays size={20} />

                        <strong>
                            {exam.date}
                        </strong>

                        <span>
                            {exam.day}
                        </span>

                    </div>


                    <div class="exam-details">

                        <div class="exam-title-row">

                            <div>
                                <h3>
                                    {exam.subject}
                                </h3>

                                <span>
                                    {exam.name}
                                </span>
                            </div>

                            <span class="days-badge">
                                {exam.daysLeft} days left
                            </span>

                        </div>


                        <div class="exam-meta">

                            <span>
                                <Clock3 size={14} />
                                {exam.time}
                            </span>

                            <span>
                                <BookOpen size={14} />
                                {exam.syllabus}
                            </span>

                        </div>

                    </div>

                </div>

            {/each}

        </div>

    </section>


    <!-- LATEST RESULT -->
    <section class="card">

        <div class="card-header">

            <div>
                <h2>Latest Result</h2>

                <p>
                    Performance in the most recent examination.
                </p>
            </div>

            <span class="result-badge">
                <CheckCircle2 size={14} />
                Published
            </span>

        </div>


        <div class="latest-result">

            <div class="latest-score">

                <span>Overall Score</span>

                <strong>
                    {latestResult.percentage}%
                </strong>

                <small>
                    {latestResult.marks} / {latestResult.total}
                    marks
                </small>

            </div>


            <div class="result-details">

                <div>
                    <span>Examination</span>
                    <strong>{latestResult.exam}</strong>
                </div>

                <div>
                    <span>Grade</span>
                    <strong>{latestResult.grade}</strong>
                </div>

                <div>
                    <span>Class Rank</span>
                    <strong>#{latestResult.rank}</strong>
                </div>

                <div>
                    <span>Date</span>
                    <strong>{latestResult.date}</strong>
                </div>

            </div>

        </div>

    </section>


    <!-- SUBJECT RESULTS -->
    <section class="card">

        <div class="card-header">

            <div>
                <h2>Subject-wise Results</h2>

                <p>
                    Marks and grades from the latest examination.
                </p>
            </div>

        </div>


        <div class="subject-grid">

            {#each subjectResults as result}

                <div class="subject-card">

                    <div class="subject-top">

                        <div class="subject-icon">
                            <BookOpen size={18} />
                        </div>

                        <div class="subject-name">

                            <strong>
                                {result.subject}
                            </strong>

                            <span>
                                {result.marks}/{result.total}
                            </span>

                        </div>

                        <div class="grade">
                            {result.grade}
                        </div>

                    </div>


                    <div class="subject-progress">

                        <div
                            class="subject-fill"
                            style={`width: ${result.percentage}%`}
                        ></div>

                    </div>


                    <div class="subject-footer">

                        <span>
                            {result.percentage}%
                        </span>

                        <small>
                            {result.marks} marks
                        </small>

                    </div>

                </div>

            {/each}

        </div>

    </section>


    <!-- RESULT HISTORY -->
    <section class="card">

        <div class="card-header">

            <div>
                <h2>Result History</h2>

                <p>
                    Previous examination results.
                </p>
            </div>

        </div>


        <div class="results-table">

            <div class="table-header">

                <span>Examination</span>
                <span>Date</span>
                <span>Marks</span>
                <span>Percentage</span>
                <span>Grade</span>
                <span>Rank</span>

            </div>


            {#each results as result}

                <div class="table-row">

                    <strong>
                        {result.exam}
                    </strong>

                    <span>
                        {result.date}
                    </span>

                    <span>
                        {result.marks}/{result.total}
                    </span>

                    <span class="percentage">
                        {result.percentage}%
                    </span>

                    <span class="table-grade">
                        {result.grade}
                    </span>

                    <span>
                        #{result.rank}
                    </span>

                </div>

            {/each}

        </div>

    </section>


    <!-- PERFORMANCE TREND -->
    <section class="card">

        <div class="card-header">

            <div>
                <h2>Result Progress</h2>

                <p>
                    Improvement across recent examinations.
                </p>
            </div>

            <span class="trend-icon">
               <TrendingUp size={20} />
            </span>

        </div>


        <div class="progress-chart">

            {#each results.slice().reverse() as result}

                <div class="progress-column">

                    <div class="bar-wrapper">

                        <div
                            class="result-bar"
                            style={`height: ${result.percentage}%`}
                        ></div>

                        <span>
                            {result.percentage}%
                        </span>

                    </div>

                    <small>
                        {result.exam.replace(
                            ' Examination',
                            ''
                        )}
                    </small>

                </div>

            {/each}

        </div>

    </section>


    <!-- INFORMATION -->
    <div class="info-note">

        <div class="note-icon">
            <GraduationCap size={18} />
        </div>

        <div>

            <strong>
                Exams & Results Information
            </strong>

            <p>
                Examination schedules and results shown here
                are currently demo data. During API integration,
                exam schedules, marks, grades and results will
                be retrieved from the school's database for
                the selected child.
            </p>

        </div>

    </div>

</div>


<style>
    .exams-page {
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


    /* SELECTOR */

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

    .result-summary {
        min-width: 135px;
        padding: 12px 16px;
        border-radius: 11px;
        background: #eef4ff;
        text-align: center;
    }

    .result-summary span {
        display: block;
        color: #64748b;
        font-size: 10px;
    }

    .result-summary strong {
        display: block;
        margin: 2px 0;
        color: #2563eb;
        font-size: 24px;
    }

    .result-summary small {
        color: #475569;
        font-size: 10px;
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

    .summary-icon.purple {
        background: #f5f3ff;
        color: #7c3aed;
    }

    .summary-icon.green {
        background: #ecfdf5;
        color: #059669;
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
        font-size: 21px;
    }


    /* CARD */

    .card {
        margin-bottom: 20px;
        padding: 22px;
        border: 1px solid #e2e8f0;
        border-radius: 15px;
        background: white;
        box-shadow: 0 3px 12px rgba(15, 23, 42, 0.03);
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

    .count-badge,
    .result-badge {
        display: flex;
        align-items: center;
        gap: 5px;
        padding: 6px 9px;
        border-radius: 8px;
        font-size: 10px;
        font-weight: 700;
    }

    .count-badge {
        background: #eef4ff;
        color: #2563eb;
    }

    .result-badge {
        background: #ecfdf5;
        color: #059669;
    }


    /* UPCOMING EXAMS */

    .exam-list {
        display: flex;
        flex-direction: column;
        gap: 12px;
    }

    .exam-card {
        display: flex;
        align-items: stretch;
        gap: 15px;
        padding: 15px;
        border: 1px solid #e2e8f0;
        border-radius: 12px;
        background: #f8fafc;
    }

    .exam-date {
        width: 130px;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        flex-shrink: 0;
        padding: 10px;
        border-radius: 10px;
        background: #eef4ff;
        color: #2563eb;
        text-align: center;
    }

    .exam-date strong {
        margin-top: 6px;
        font-size: 12px;
    }

    .exam-date span {
        margin-top: 3px;
        color: #64748b;
        font-size: 9px;
    }

    .exam-details {
        flex: 1;
    }

    .exam-title-row {
        display: flex;
        align-items: center;
        justify-content: space-between;
        gap: 15px;
    }

    .exam-title-row h3 {
        margin: 0;
        color: #0f172a;
        font-size: 14px;
    }

    .exam-title-row span {
        display: block;
        margin-top: 3px;
        color: #64748b;
        font-size: 10px;
    }

    .days-badge {
        padding: 6px 9px;
        border-radius: 8px;
        background: #fff7ed;
        color: #ea580c;
        font-size: 9px !important;
        font-weight: 700;
        white-space: nowrap;
    }

    .exam-meta {
        display: flex;
        align-items: center;
        flex-wrap: wrap;
        gap: 18px;
        margin-top: 14px;
    }

    .exam-meta span {
        display: flex;
        align-items: center;
        gap: 5px;
        color: #64748b;
        font-size: 10px;
    }


    /* LATEST RESULT */

    .latest-result {
        display: grid;
        grid-template-columns: 200px 1fr;
        gap: 25px;
        align-items: center;
    }

    .latest-score {
        padding: 20px;
        border-radius: 12px;
        background: #eef4ff;
        text-align: center;
    }

    .latest-score span {
        display: block;
        color: #64748b;
        font-size: 10px;
    }

    .latest-score strong {
        display: block;
        margin: 5px 0;
        color: #2563eb;
        font-size: 38px;
    }

    .latest-score small {
        color: #64748b;
        font-size: 10px;
    }

    .result-details {
        display: grid;
        grid-template-columns: repeat(2, 1fr);
        gap: 12px;
    }

    .result-details div {
        padding: 13px;
        border-radius: 10px;
        background: #f8fafc;
    }

    .result-details span {
        display: block;
        color: #64748b;
        font-size: 9px;
    }

    .result-details strong {
        display: block;
        margin-top: 4px;
        color: #0f172a;
        font-size: 13px;
    }


    /* SUBJECT RESULTS */

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

    .subject-top {
        display: flex;
        align-items: center;
        gap: 9px;
        margin-bottom: 12px;
    }

    .subject-icon {
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

    .subject-name {
        flex: 1;
        min-width: 0;
    }

    .subject-name strong {
        display: block;
        color: #334155;
        font-size: 11px;
    }

    .subject-name span {
        display: block;
        margin-top: 3px;
        color: #94a3b8;
        font-size: 9px;
    }

    .grade,
    .table-grade {
        padding: 5px 7px;
        border-radius: 7px;
        background: #ecfdf5;
        color: #059669;
        font-size: 10px;
        font-weight: 800;
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

    .subject-footer span,
    .subject-footer small {
        color: #64748b;
        font-size: 9px;
    }


    /* RESULT TABLE */

    .results-table {
        overflow-x: auto;
    }

    .table-header,
    .table-row {
        display: grid;
        grid-template-columns: 1.5fr 1fr 1fr 0.9fr 0.7fr 0.7fr;
        align-items: center;
        gap: 12px;
        min-width: 700px;
        padding: 13px 12px;
    }

    .table-header {
        border-radius: 9px;
        background: #f8fafc;
        color: #64748b;
        font-size: 10px;
        font-weight: 700;
    }

    .table-row {
        border-bottom: 1px solid #e2e8f0;
        color: #64748b;
        font-size: 10px;
    }

    .table-row strong {
        color: #334155;
    }

    .percentage {
        color: #2563eb;
        font-weight: 700;
    }


    /* TREND */

    .trend-icon {
        color: #059669;
    }

    .progress-chart {
        height: 250px;
        display: flex;
        align-items: flex-end;
        justify-content: space-around;
        gap: 40px;
        padding: 20px 50px 0;
        border-bottom: 1px solid #e2e8f0;
    }

    .progress-column {
        height: 100%;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: flex-end;
        gap: 9px;
        flex: 1;
    }

    .bar-wrapper {
        height: 210px;
        display: flex;
        align-items: flex-end;
        position: relative;
    }

    .result-bar {
        width: 55px;
        min-height: 20px;
        border-radius: 8px 8px 0 0;
        background: #2563eb;
    }

    .bar-wrapper span {
        position: absolute;
        top: -20px;
        left: 50%;
        transform: translateX(-50%);
        color: #334155;
        font-size: 10px;
        font-weight: 700;
    }

    .progress-column small {
        color: #64748b;
        font-size: 9px;
        text-align: center;
    }


    /* INFO */

    .info-note {
        display: flex;
        align-items: flex-start;
        gap: 11px;
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
        .exams-page {
            padding: 24px;
        }

        .summary-grid {
            grid-template-columns: repeat(2, 1fr);
        }

        .subject-grid {
            grid-template-columns: repeat(2, 1fr);
        }

        .latest-result {
            grid-template-columns: 1fr;
        }
    }

    @media (max-width: 700px) {
        .exams-page {
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

        .result-summary {
            width: 100%;
        }

        .summary-grid {
            grid-template-columns: 1fr;
        }

        .exam-card {
            flex-direction: column;
        }

        .exam-date {
            width: auto;
        }

        .exam-title-row {
            align-items: flex-start;
            flex-direction: column;
            gap: 8px;
        }

        .subject-grid {
            grid-template-columns: 1fr;
        }

        .result-details {
            grid-template-columns: 1fr;
        }

        .progress-chart {
            gap: 15px;
            padding-left: 15px;
            padding-right: 15px;
        }

        .result-bar {
            width: 40px;
        }
    }
</style>