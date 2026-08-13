<script lang="ts">
    import {
        BarChart3,
        ChevronDown,
        TrendingUp,
        Award,
        BookOpen,
        CheckCircle2,
        ArrowUp,
        ArrowDown
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

    const performanceData = {
        'Rahul Kumar': {
            percentage: 81,
            grade: 'A',
            rank: 8,
            totalStudents: 42,
            previousPercentage: 77,
            highest: 94,
            lowest: 62
        },
        'Ayesha Kumar': {
            percentage: 84,
            grade: 'A',
            rank: 5,
            totalStudents: 38,
            previousPercentage: 81,
            highest: 96,
            lowest: 68
        }
    };

    const subjects = [
        {
            subject: 'Mathematics',
            marks: 78,
            total: 100,
            grade: 'A',
            percentage: 78,
            performance: 'Good'
        },
        {
            subject: 'Science',
            marks: 74,
            total: 100,
            grade: 'A',
            percentage: 74,
            performance: 'Good'
        },
        {
            subject: 'English',
            marks: 81,
            total: 100,
            grade: 'A+',
            percentage: 81,
            performance: 'Excellent'
        },
        {
            subject: 'Social Studies',
            marks: 75,
            total: 100,
            grade: 'A',
            percentage: 75,
            performance: 'Good'
        },
        {
            subject: 'Computer Science',
            marks: 88,
            total: 100,
            grade: 'A+',
            percentage: 88,
            performance: 'Excellent'
        },
        {
            subject: 'Hindi',
            marks: 80,
            total: 100,
            grade: 'A',
            percentage: 80,
            performance: 'Good'
        }
    ];

    const examResults = [
        {
            exam: 'Unit Test - 1',
            date: '15 Jun 2026',
            percentage: 74,
            grade: 'B+'
        },
        {
            exam: 'Unit Test - 2',
            date: '18 Jul 2026',
            percentage: 78,
            grade: 'A'
        },
        {
            exam: 'Mid Term Examination',
            date: '02 Aug 2026',
            percentage: 81,
            grade: 'A'
        }
    ];

    const monthlyProgress = [
        { month: 'Apr', percentage: 72 },
        { month: 'May', percentage: 75 },
        { month: 'Jun', percentage: 77 },
        { month: 'Jul', percentage: 79 },
        { month: 'Aug', percentage: 81 }
    ];

    function getPerformance() {
        return performanceData[
            selectedChild as keyof typeof performanceData
        ];
    }

    function getSelectedChild() {
        return children.find(
            (child) => child.name === selectedChild
        );
    }

    let performance = $derived(getPerformance());
    let child = $derived(getSelectedChild());

    let improvement = $derived(
        performance.percentage - performance.previousPercentage
    );
</script>

<svelte:head>
    <title>Academic Performance | Parent Dashboard</title>
</svelte:head>

<div class="performance-page">

    <!-- HEADER -->
    <div class="page-header">

        <div class="title-row">

            <div class="title-icon">
                <BarChart3 size={24} />
            </div>

            <div>
                <h1>Academic Performance</h1>

                <p>
                    Monitor your child's academic progress,
                    marks and grades.
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


    <!-- CHILD INFORMATION -->
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

        <div class="current-grade">

            <span>Overall Grade</span>

            <strong>{performance.grade}</strong>

            <small>
                {performance.percentage}% overall
            </small>

        </div>

    </section>


    <!-- SUMMARY -->
    <section class="summary-grid">

        <div class="summary-card">

            <div class="summary-icon blue">
                <BarChart3 size={21} />
            </div>

            <div>
                <span>Overall Percentage</span>
                <strong>{performance.percentage}%</strong>
            </div>

        </div>


        <div class="summary-card">

            <div class="summary-icon green">
                <Award size={21} />
            </div>

            <div>
                <span>Overall Grade</span>
                <strong>{performance.grade}</strong>
            </div>

        </div>


        <div class="summary-card">

            <div class="summary-icon purple">
                <TrendingUp size={21} />
            </div>

            <div>
                <span>Class Rank</span>
                <strong>
                    {performance.rank}/{performance.totalStudents}
                </strong>
            </div>

        </div>


        <div class="summary-card">

            <div class="summary-icon orange">
                <BookOpen size={21} />
            </div>

            <div>
                <span>Subjects</span>
                <strong>{subjects.length}</strong>
            </div>

        </div>

    </section>


    <!-- PERFORMANCE OVERVIEW -->
    <div class="content-grid">

        <section class="card">

            <div class="card-header">

                <div>
                    <h2>Performance Overview</h2>

                    <p>
                        Current academic performance.
                    </p>
                </div>

                <span class="trend-badge">
                    <TrendingUp size={14} />
                    Improving
                </span>

            </div>


            <div class="performance-overview">

                <div class="big-score">

                    <strong>{performance.percentage}%</strong>

                    <span>Overall Score</span>

                </div>


                <div class="score-details">

                    <div>
                        <span>Previous</span>
                        <strong>
                            {performance.previousPercentage}%
                        </strong>
                    </div>

                    <div>
                        <span>Highest</span>
                        <strong>
                            {performance.highest}%
                        </strong>
                    </div>

                    <div>
                        <span>Lowest</span>
                        <strong>
                            {performance.lowest}%
                        </strong>
                    </div>

                </div>

            </div>


            <div class="progress-section">

                <div class="progress-header">
                    <span>Overall Progress</span>

                    <strong>
                        {performance.percentage}%
                    </strong>
                </div>

                <div class="progress-track">
                    <div
                        class="progress-fill"
                        style={`width: ${performance.percentage}%`}
                    ></div>
                </div>

            </div>


            <div class="improvement">

                {#if improvement >= 0}

                    <ArrowUp size={16} />

                    <span>
                        Improved by
                        <strong>{improvement}%</strong>
                        compared with the previous assessment.
                    </span>

                {:else}

                    <ArrowDown size={16} />

                    <span>
                        Decreased by
                        <strong>{Math.abs(improvement)}%</strong>
                        compared with the previous assessment.
                    </span>

                {/if}

            </div>

        </section>


        <!-- CLASS RANK -->
        <section class="card rank-card">

            <div class="card-header">

                <div>
                    <h2>Class Performance</h2>

                    <p>
                        Current position in the class.
                    </p>
                </div>

            </div>


            <div class="rank-circle">

                <div>
                    <span>Rank</span>

                    <strong>
                        #{performance.rank}
                    </strong>

                    <small>
                        out of {performance.totalStudents}
                    </small>
                </div>

            </div>


            <div class="rank-message">

                <CheckCircle2 size={18} />

                <span>
                    Your child is performing well compared
                    with the class average.
                </span>

            </div>

        </section>

    </div>


    <!-- SUBJECT PERFORMANCE -->
    <section class="card">

        <div class="card-header">

            <div>
                <h2>Subject-wise Performance</h2>

                <p>
                    Marks and grades for each subject.
                </p>
            </div>

        </div>


        <div class="subject-grid">

            {#each subjects as subject}

                <div class="subject-card">

                    <div class="subject-header">

                        <div class="subject-icon">
                            <BookOpen size={18} />
                        </div>

                        <div>
                            <strong>
                                {subject.subject}
                            </strong>

                            <span>
                                {subject.marks}/{subject.total}
                            </span>
                        </div>

                        <div class="grade">
                            {subject.grade}
                        </div>

                    </div>


                    <div class="subject-progress">

                        <div
                            class="subject-fill"
                            style={`width: ${subject.percentage}%`}
                        ></div>

                    </div>


                    <div class="subject-footer">

                        <span>
                            {subject.percentage}%
                        </span>

                        {#if subject.performance === 'Excellent'}

                            <small class="excellent">
                                Excellent
                            </small>

                        {:else}

                            <small class="good">
                                Good
                            </small>

                        {/if}

                    </div>

                </div>

            {/each}

        </div>

    </section>


    <!-- PROGRESS TREND -->
    <section class="card">

        <div class="card-header">

            <div>
                <h2>Academic Progress</h2>

                <p>
                    Performance trend across recent assessments.
                </p>
            </div>

           <span class="trend-icon">
              <TrendingUp size={20} />
           </span>

        </div>


        <div class="trend-chart">

            {#each monthlyProgress as item}

                <div class="trend-column">

                    <div class="bar-container">

                        <div
                            class="trend-bar"
                            style={`height: ${item.percentage}%`}
                        ></div>

                        <span>
                            {item.percentage}%
                        </span>

                    </div>

                    <small>
                        {item.month}
                    </small>

                </div>

            {/each}

        </div>

    </section>


    <!-- EXAM RESULTS -->
    <section class="card">

        <div class="card-header">

            <div>
                <h2>Recent Examination Results</h2>

                <p>
                    Latest exam and assessment results.
                </p>
            </div>

            <a
                href="/parent-dashboard/exams"
                class="view-link"
            >
                View Exams
            </a>

        </div>


        <div class="exam-table">

            <div class="exam-table-header">

                <span>Examination</span>
                <span>Date</span>
                <span>Percentage</span>
                <span>Grade</span>

            </div>


            {#each examResults as result}

                <div class="exam-row">

                    <strong>
                        {result.exam}
                    </strong>

                    <span>
                        {result.date}
                    </span>

                    <span>
                        {result.percentage}%
                    </span>

                    <span class="exam-grade">
                        {result.grade}
                    </span>

                </div>

            {/each}

        </div>

    </section>


    <!-- STRENGTHS + IMPROVEMENT -->
    <div class="content-grid">

        <section class="card insight-card">

            <div class="insight-heading">

                <div class="insight-icon green">
                    <CheckCircle2 size={20} />
                </div>

                <div>
                    <h2>Strengths</h2>

                    <p>
                        Subjects where your child is doing well.
                    </p>
                </div>

            </div>


            <ul>

                <li>
                    Computer Science — 88%
                </li>

                <li>
                    English — 81%
                </li>

                <li>
                    Hindi — 80%
                </li>

            </ul>

        </section>


        <section class="card insight-card">

            <div class="insight-heading">

                <div class="insight-icon orange">
                    <TrendingUp size={20} />
                </div>

                <div>
                    <h2>Areas to Improve</h2>

                    <p>
                        Subjects that need additional attention.
                    </p>
                </div>

            </div>


            <ul>

                <li>
                    Science — Focus on conceptual understanding
                </li>

                <li>
                    Social Studies — Improve answer writing
                </li>

                <li>
                    Mathematics — Practice more problem solving
                </li>

            </ul>

        </section>

    </div>


    <!-- INFORMATION NOTE -->
    <div class="info-note">

        <div class="note-icon">
            <BarChart3 size={18} />
        </div>

        <div>

            <strong>
                Academic Performance Information
            </strong>

            <p>
                The academic information displayed here is
                currently demo data. During API integration,
                marks, grades, rankings and subject performance
                will be retrieved from the school's database for
                the selected child.
            </p>

        </div>

    </div>

</div>


<style>
    .performance-page {
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

    .current-grade {
        min-width: 135px;
        padding: 12px 16px;
        border-radius: 11px;
        background: #eef4ff;
        text-align: center;
    }

    .current-grade span {
        display: block;
        color: #64748b;
        font-size: 10px;
    }

    .current-grade strong {
        display: block;
        margin: 2px 0;
        color: #2563eb;
        font-size: 24px;
    }

    .current-grade small {
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

    .summary-icon.green {
        background: #ecfdf5;
        color: #059669;
    }

    .summary-icon.purple {
        background: #f5f3ff;
        color: #7c3aed;
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


    /* CARDS */

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

    .trend-badge {
        display: flex;
        align-items: center;
        gap: 5px;
        padding: 6px 9px;
        border-radius: 8px;
        background: #ecfdf5;
        color: #059669;
        font-size: 10px;
        font-weight: 700;
    }

    .trend-icon {
        color: #059669;
    }


    /* PERFORMANCE OVERVIEW */

    .performance-overview {
        display: flex;
        align-items: center;
        gap: 35px;
    }

    .big-score strong {
        display: block;
        color: #2563eb;
        font-size: 48px;
        line-height: 1;
    }

    .big-score span {
        display: block;
        margin-top: 7px;
        color: #64748b;
        font-size: 11px;
    }

    .score-details {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        flex: 1;
        gap: 10px;
    }

    .score-details div {
        padding: 12px;
        background: #f8fafc;
        border-radius: 10px;
        text-align: center;
    }

    .score-details span {
        display: block;
        color: #64748b;
        font-size: 9px;
    }

    .score-details strong {
        display: block;
        margin-top: 4px;
        color: #0f172a;
        font-size: 15px;
    }

    .progress-section {
        margin-top: 24px;
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

    .improvement {
        display: flex;
        align-items: center;
        gap: 7px;
        margin-top: 15px;
        padding: 11px;
        border-radius: 9px;
        background: #ecfdf5;
        color: #059669;
        font-size: 10px;
    }


    /* RANK */

    .rank-card {
        text-align: center;
    }

    .rank-circle {
        width: 145px;
        height: 145px;
        display: flex;
        align-items: center;
        justify-content: center;
        margin: 10px auto 15px;
        border-radius: 50%;
        background: conic-gradient(
            #7c3aed 0% 82%,
            #ede9fe 82% 100%
        );
    }

    .rank-circle > div {
        width: 112px;
        height: 112px;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        border-radius: 50%;
        background: white;
    }

    .rank-circle span {
        color: #64748b;
        font-size: 10px;
    }

    .rank-circle strong {
        margin: 3px 0;
        color: #7c3aed;
        font-size: 28px;
    }

    .rank-circle small {
        color: #94a3b8;
        font-size: 9px;
    }

    .rank-message {
        display: flex;
        align-items: flex-start;
        gap: 7px;
        padding: 11px;
        border-radius: 9px;
        background: #f5f3ff;
        color: #7c3aed;
        font-size: 10px;
        text-align: left;
    }


    /* SUBJECTS */

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

    .subject-header > div:nth-child(2) {
        flex: 1;
        min-width: 0;
    }

    .subject-header strong {
        display: block;
        color: #334155;
        font-size: 11px;
    }

    .subject-header span {
        display: block;
        margin-top: 3px;
        color: #94a3b8;
        font-size: 9px;
    }

    .grade {
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

    .subject-footer > span {
        color: #64748b;
        font-size: 10px;
    }

    .subject-footer small {
        font-size: 9px;
        font-weight: 700;
    }

    .excellent {
        color: #059669;
    }

    .good {
        color: #2563eb;
    }


    /* TREND */

    .trend-chart {
        height: 250px;
        display: flex;
        align-items: flex-end;
        justify-content: space-around;
        gap: 25px;
        padding: 20px 30px 0;
        border-bottom: 1px solid #e2e8f0;
    }

    .trend-column {
        height: 100%;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: flex-end;
        gap: 8px;
        flex: 1;
    }

    .bar-container {
        height: 210px;
        display: flex;
        align-items: flex-end;
        position: relative;
    }

    .trend-bar {
        width: 48px;
        min-height: 20px;
        border-radius: 8px 8px 0 0;
        background: #2563eb;
    }

    .bar-container span {
        position: absolute;
        top: -20px;
        left: 50%;
        transform: translateX(-50%);
        color: #334155;
        font-size: 10px;
        font-weight: 700;
        white-space: nowrap;
    }

    .trend-column small {
        color: #64748b;
        font-size: 10px;
    }


    /* EXAM TABLE */

    .view-link {
        color: #2563eb;
        font-size: 11px;
        font-weight: 700;
        text-decoration: none;
    }

    .exam-table {
        overflow-x: auto;
    }

    .exam-table-header,
    .exam-row {
        display: grid;
        grid-template-columns: 1.6fr 1fr 1fr 0.7fr;
        align-items: center;
        gap: 15px;
        min-width: 600px;
        padding: 13px 12px;
    }

    .exam-table-header {
        border-radius: 9px;
        background: #f8fafc;
        color: #64748b;
        font-size: 10px;
        font-weight: 700;
    }

    .exam-row {
        border-bottom: 1px solid #e2e8f0;
        color: #64748b;
        font-size: 11px;
    }

    .exam-row strong {
        color: #334155;
    }

    .exam-grade {
        width: fit-content;
        padding: 5px 8px;
        border-radius: 7px;
        background: #ecfdf5;
        color: #059669;
        font-weight: 700;
    }


    /* INSIGHTS */

    .insight-heading {
        display: flex;
        align-items: center;
        gap: 11px;
        margin-bottom: 15px;
    }

    .insight-icon {
        width: 40px;
        height: 40px;
        display: flex;
        align-items: center;
        justify-content: center;
        flex-shrink: 0;
        border-radius: 10px;
    }

    .insight-icon.green {
        background: #ecfdf5;
        color: #059669;
    }

    .insight-icon.orange {
        background: #fff7ed;
        color: #ea580c;
    }

    .insight-heading h2 {
        margin: 0;
        color: #0f172a;
        font-size: 16px;
    }

    .insight-heading p {
        margin: 3px 0 0;
        color: #64748b;
        font-size: 10px;
    }

    .insight-card ul {
        margin: 0;
        padding-left: 18px;
    }

    .insight-card li {
        margin-bottom: 9px;
        color: #475569;
        font-size: 11px;
        line-height: 1.4;
    }

    .insight-card li:last-child {
        margin-bottom: 0;
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
        .performance-page {
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
        .performance-page {
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

        .current-grade {
            width: 100%;
        }

        .summary-grid {
            grid-template-columns: 1fr;
        }

        .performance-overview {
            flex-direction: column;
            align-items: flex-start;
        }

        .score-details {
            width: 100%;
        }

        .subject-grid {
            grid-template-columns: 1fr;
        }

        .trend-chart {
            gap: 10px;
            padding-left: 10px;
            padding-right: 10px;
        }

        .trend-bar {
            width: 32px;
        }
    }
</style>