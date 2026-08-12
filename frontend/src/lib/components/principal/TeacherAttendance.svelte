<script lang="ts">
    let selectedPeriod = $state('today');
    let teacherId = $state('');
    let searchedTeacher = $state('');
    let fromDate = $state('');
    let toDate = $state('');

    const teachers = [
        {
            id: 'TCH001',
            name: 'Ravi Kumar',
            department: 'Mathematics',
            totalDays: 24,
            present: 22,
            absent: 1,
            late: 1,
            percentage: 92
        },
        {
            id: 'TCH002',
            name: 'Anjali Sharma',
            department: 'Biology',
            totalDays: 24,
            present: 23,
            absent: 0,
            late: 1,
            percentage: 96
        },
        {
            id: 'TCH003',
            name: 'Mohammed Sameer',
            department: 'English',
            totalDays: 24,
            present: 21,
            absent: 2,
            late: 1,
            percentage: 88
        },
        {
            id: 'TCH004',
            name: 'Priya Reddy',
            department: 'Social Studies',
            totalDays: 24,
            present: 24,
            absent: 0,
            late: 0,
            percentage: 100
        }
    ];

    let selectedTeacher = $derived(
        teachers.find(
            (teacher) =>
                teacher.id.toLowerCase() ===
                searchedTeacher.toLowerCase()
        )
    );

    function searchTeacher() {
        searchedTeacher = teacherId.trim();
    }

    function clearSearch() {
        teacherId = '';
        searchedTeacher = '';
    }

    function periodLabel() {
        if (selectedPeriod === 'today') return "Today's Attendance";
        if (selectedPeriod === 'yesterday') return 'Yesterday';
        if (selectedPeriod === 'last-week') return 'Last Week';
        if (selectedPeriod === 'last-month') return 'Last Month';

        if (selectedPeriod === 'custom') {
            if (fromDate && toDate) {
                return `${fromDate} to ${toDate}`;
            }

            return 'Custom Date Range';
        }

        return "Today's Attendance";
    }
</script>


<section class="teacher-attendance">

    <!-- HEADER -->

    <div class="section-header">
        <div>
            <h2>Teacher Attendance</h2>

            <p>
                View attendance of all teachers or search for a particular teacher.
            </p>
        </div>
    </div>


    <!-- ATTENDANCE PERIOD -->

    <div class="filter-card">

        <div class="field">

            <label for="period">
                Attendance Period
            </label>

            <select
                id="period"
                bind:value={selectedPeriod}
            >
                <option value="today">
                    Today's Attendance
                </option>

                <option value="yesterday">
                    Yesterday
                </option>

                <option value="last-week">
                    Last Week
                </option>

                <option value="last-month">
                    Last Month
                </option>

                <option value="custom">
                    Custom Date Range
                </option>
            </select>

        </div>


        {#if selectedPeriod === 'custom'}

            <div class="field">

                <label for="from-date">
                    From Date
                </label>

                <input
                    id="from-date"
                    type="date"
                    bind:value={fromDate}
                />

            </div>


            <div class="field">

                <label for="to-date">
                    To Date
                </label>

                <input
                    id="to-date"
                    type="date"
                    bind:value={toDate}
                />

            </div>

        {/if}

    </div>


    <!-- ALL TEACHERS -->

    <div class="result-header">

        <div>
            <h3>{periodLabel()}</h3>

            <p>
                Attendance of all teachers for the selected period.
            </p>
        </div>

    </div>


    <div class="table-card">

        <div class="table">

            <div class="table-header">

                <span>Teacher</span>
                <span>Teacher ID</span>
                <span>Department</span>
                <span>Total Days</span>
                <span>Present</span>
                <span>Absent</span>
                <span>Late</span>
                <span>Attendance</span>

            </div>


            {#each teachers as teacher}

                <div class="table-row">

                    <strong>
                        {teacher.name}
                    </strong>

                    <span>
                        {teacher.id}
                    </span>

                    <span>
                        {teacher.department}
                    </span>

                    <span>
                        {teacher.totalDays}
                    </span>

                    <span class="present">
                        {teacher.present}
                    </span>

                    <span class="absent">
                        {teacher.absent}
                    </span>

                    <span class="late">
                        {teacher.late}
                    </span>

                    <span class="percentage">
                        {teacher.percentage}%
                    </span>

                </div>

            {/each}

        </div>

    </div>


    <!-- PARTICULAR TEACHER -->

    <div class="search-card">

        <div class="search-header">

            <div>
                <h3>Find Particular Teacher</h3>

                <p>
                    Enter Teacher ID to view individual attendance.
                </p>
            </div>

        </div>


        <div class="search-row">

            <div class="field">

                <label for="teacher-id">
                    Teacher ID
                </label>

                <input
                    id="teacher-id"
                    type="text"
                    placeholder="Enter Teacher ID e.g. TCH001"
                    bind:value={teacherId}
                />

            </div>


            <button
                type="button"
                onclick={searchTeacher}
            >
                View Attendance
            </button>


            {#if searchedTeacher}

                <button
                    type="button"
                    class="clear"
                    onclick={clearSearch}
                >
                    Clear
                </button>

            {/if}

        </div>


        {#if searchedTeacher && selectedTeacher}

            <div class="teacher-details">

                <div class="teacher-info">

                    <span>Teacher</span>

                    <strong>
                        {selectedTeacher.name}
                    </strong>

                    <small>
                        {selectedTeacher.id}
                        ·
                        {selectedTeacher.department}
                    </small>

                </div>


                <div class="detail-card">

                    <span>Total Days</span>

                    <strong>
                        {selectedTeacher.totalDays}
                    </strong>

                </div>


                <div class="detail-card">

                    <span>Present</span>

                    <strong class="green">
                        {selectedTeacher.present}
                    </strong>

                </div>


                <div class="detail-card">

                    <span>Absent</span>

                    <strong class="red">
                        {selectedTeacher.absent}
                    </strong>

                </div>


                <div class="detail-card">

                    <span>Late</span>

                    <strong class="orange">
                        {selectedTeacher.late}
                    </strong>

                </div>


                <div class="detail-card attendance">

                    <span>Attendance</span>

                    <strong>
                        {selectedTeacher.percentage}%
                    </strong>

                </div>

            </div>

        {:else if searchedTeacher}

            <div class="not-found">
                No teacher found with ID
                <strong>{searchedTeacher}</strong>.
            </div>

        {/if}

    </div>

</section>


<style lang="scss">

.teacher-attendance {
    margin-top: 24px;
}


/* HEADER */

.section-header {
    margin-bottom: 16px;
}

.section-header h2 {
    margin: 0;

    color: #14213d;

    font-size: 20px;
}

.section-header p {
    margin: 5px 0 0;

    color: #64748b;

    font-size: 13px;
}


/* FILTER */

.filter-card {
    display: flex;

    gap: 16px;

    padding: 20px;

    background: white;

    border: 1px solid #e5eaf2;

    border-radius: 16px;

    box-shadow:
        0 4px 14px
        rgba(15, 23, 42, 0.03);
}

.field {
    flex: 1;
}

.field label {
    display: block;

    margin-bottom: 7px;

    color: #334155;

    font-size: 12px;

    font-weight: 600;
}

select,
input {
    width: 100%;

    height: 42px;

    padding: 0 12px;

    box-sizing: border-box;

    border: 1px solid #dbe3ef;

    border-radius: 9px;

    background: white;

    color: #1e293b;

    font-size: 13px;

    outline: none;
}

select:focus,
input:focus {
    border-color: #2563eb;

    box-shadow:
        0 0 0 3px
        rgba(37, 99, 235, 0.1);
}


/* RESULT HEADER */

.result-header {
    display: flex;

    align-items: center;

    margin-top: 20px;

    padding: 18px 20px;

    background: #f8fafc;

    border: 1px solid #e5eaf2;

    border-radius: 14px;
}

.result-header h3 {
    margin: 0;

    color: #14213d;

    font-size: 17px;
}

.result-header p {
    margin: 5px 0 0;

    color: #64748b;

    font-size: 12px;
}


/* TABLE */

.table-card {
    margin-top: 14px;

    overflow-x: auto;

    background: white;

    border: 1px solid #e5eaf2;

    border-radius: 16px;

    box-shadow:
        0 4px 14px
        rgba(15, 23, 42, 0.03);
}

.table {
    min-width: 900px;
}

.table-header,
.table-row {
    display: grid;

    grid-template-columns:
        1.5fr
        1fr
        1.3fr
        0.9fr
        0.8fr
        0.8fr
        0.7fr
        0.9fr;

    gap: 12px;

    align-items: center;

    padding: 15px 20px;
}

.table-header {
    background: #f8fafc;

    color: #64748b;

    font-size: 11px;

    font-weight: 700;
}

.table-row {
    border-top: 1px solid #edf1f6;

    color: #64748b;

    font-size: 12px;
}

.table-row strong {
    color: #14213d;

    font-size: 13px;
}

.present {
    color: #16a34a;

    font-weight: 700;
}

.absent {
    color: #dc2626;

    font-weight: 700;
}

.late {
    color: #ea580c;

    font-weight: 700;
}

.percentage {
    width: fit-content;

    padding: 6px 9px;

    border-radius: 8px;

    background: #eef4ff;

    color: #2563eb;

    font-weight: 700;
}


/* SEARCH */

.search-card {
    margin-top: 22px;

    padding: 22px;

    background: white;

    border: 1px solid #e5eaf2;

    border-radius: 16px;

    box-shadow:
        0 4px 14px
        rgba(15, 23, 42, 0.03);
}

.search-header h3 {
    margin: 0;

    color: #14213d;

    font-size: 17px;
}

.search-header p {
    margin: 5px 0 18px;

    color: #64748b;

    font-size: 12px;
}

.search-row {
    display: flex;

    align-items: flex-end;

    gap: 12px;
}

.search-row .field {
    flex: 1;
}

.search-row button {
    height: 42px;

    padding: 0 20px;

    border: none;

    border-radius: 9px;

    background: #2563eb;

    color: white;

    font-size: 13px;

    font-weight: 600;

    cursor: pointer;
}

.search-row button:hover {
    background: #1d4ed8;
}

.search-row button.clear {
    border: 1px solid #dbe3ef;

    background: white;

    color: #475569;
}

.search-row button.clear:hover {
    background: #f8fafc;
}


/* TEACHER DETAILS */

.teacher-details {
    display: grid;

    grid-template-columns:
        1.5fr
        repeat(5, 1fr);

    gap: 12px;

    margin-top: 18px;
}

.teacher-info,
.detail-card {
    padding: 16px;

    border: 1px solid #e5eaf2;

    border-radius: 12px;

    background: #f8fafc;
}

.teacher-info span,
.detail-card span {
    display: block;

    margin-bottom: 6px;

    color: #64748b;

    font-size: 11px;
}

.teacher-info strong {
    display: block;

    color: #14213d;

    font-size: 14px;
}

.teacher-info small {
    display: block;

    margin-top: 4px;

    color: #64748b;

    font-size: 11px;
}

.detail-card strong {
    color: #14213d;

    font-size: 20px;
}

.detail-card .green,
.green {
    color: #16a34a;
}

.detail-card .red,
.red {
    color: #dc2626;
}

.detail-card .orange,
.orange {
    color: #ea580c;
}

.detail-card.attendance {
    background: #eef4ff;

    border-color: #d5e2ff;
}

.detail-card.attendance strong {
    color: #2563eb;
}


/* NOT FOUND */

.not-found {
    margin-top: 16px;

    padding: 12px 14px;

    border: 1px solid #fecaca;

    border-radius: 9px;

    background: #fef2f2;

    color: #dc2626;

    font-size: 12px;
}


/* RESPONSIVE */

@media (max-width: 1000px) {

    .teacher-details {
        grid-template-columns:
            repeat(3, 1fr);
    }

}


@media (max-width: 700px) {

    .filter-card,
    .search-row {
        flex-direction: column;

        align-items: stretch;
    }

    .search-row button {
        width: 100%;
    }

    .teacher-details {
        grid-template-columns:
            repeat(2, 1fr);
    }

}


@media (max-width: 500px) {

    .teacher-details {
        grid-template-columns: 1fr;
    }

}

</style>