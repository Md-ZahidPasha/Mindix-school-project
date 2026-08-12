<script lang="ts">
    let selectedDepartment = $state('all');
    let selectedPeriod = $state('today');

    let employeeId = $state('');
    let searchedEmployee = $state('');

    let fromDate = $state('');
    let toDate = $state('');

    const employees = [
        {
            id: 'EMP001',
            name: 'Ramesh Kumar',
            department: 'Driving',
            totalDays: 24,
            present: 23,
            absent: 0,
            late: 1,
            percentage: 96
        },
        {
            id: 'EMP002',
            name: 'Suresh Ahmed',
            department: 'Driving',
            totalDays: 24,
            present: 22,
            absent: 1,
            late: 1,
            percentage: 92
        },
        {
            id: 'EMP003',
            name: 'Lakshmi Devi',
            department: 'Lab Assistant',
            totalDays: 24,
            present: 21,
            absent: 2,
            late: 1,
            percentage: 88
        },
        {
            id: 'EMP004',
            name: 'Ravi Prakash',
            department: 'Library',
            totalDays: 24,
            present: 24,
            absent: 0,
            late: 0,
            percentage: 100
        }
    ];

    let filteredEmployees = $derived(
        selectedDepartment === 'all'
            ? employees
            : employees.filter(
                (employee) =>
                    employee.department.toLowerCase() ===
                    selectedDepartment
            )
    );

    let selectedEmployee = $derived(
        employees.find(
            (employee) =>
                employee.id.toLowerCase() ===
                searchedEmployee.toLowerCase()
        )
    );

    function searchEmployee() {
        searchedEmployee = employeeId.trim();
    }

    function clearSearch() {
        employeeId = '';
        searchedEmployee = '';
    }

    function periodLabel() {
        if (selectedPeriod === 'today') {
            return "Today's Attendance";
        }

        if (selectedPeriod === 'yesterday') {
            return 'Yesterday';
        }

        if (selectedPeriod === 'last-week') {
            return 'Last Week';
        }

        if (selectedPeriod === 'last-month') {
            return 'Last Month';
        }

        if (selectedPeriod === 'custom') {
            if (fromDate && toDate) {
                return `${fromDate} to ${toDate}`;
            }

            return 'Custom Date Range';
        }

        return "Today's Attendance";
    }

    function departmentLabel() {
        if (selectedDepartment === 'all') {
            return 'All Departments';
        }

        if (selectedDepartment === 'driving') {
            return 'Driving Department';
        }

        if (selectedDepartment === 'lab-assistant') {
            return 'Lab Assistant Department';
        }

        if (selectedDepartment === 'library') {
            return 'Library Department';
        }

        return 'All Departments';
    }
</script>


<section class="employee-attendance">

    <!-- =========================
         HEADER
         ========================= -->

    <div class="section-header">

        <div>

            <h2>Employee / Staff Attendance</h2>

            <p>
                View attendance of employees and staff by department or employee ID.
            </p>

        </div>

    </div>


    <!-- =========================
         FILTERS
         ========================= -->

    <div class="selection-card">

        <!-- DEPARTMENT -->

        <div class="field">

            <label for="employee-department">
                Department
            </label>

            <select
                id="employee-department"
                bind:value={selectedDepartment}
            >

                <option value="all">
                    All Departments
                </option>

                <option value="driving">
                    Driving
                </option>

                <option value="lab-assistant">
                    Lab Assistant
                </option>

                <option value="library">
                    Library
                </option>

            </select>

        </div>


        <!-- ATTENDANCE PERIOD -->

        <div class="field">

            <label for="employee-period">
                Attendance Period
            </label>

            <select
                id="employee-period"
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


        <!-- CUSTOM FROM DATE -->

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


            <!-- CUSTOM TO DATE -->

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


    <!-- =========================
         RESULT HEADING
         ========================= -->

    <div class="result-heading">

        <div>

            <h3>
                {departmentLabel()}
            </h3>

            <p>
                {periodLabel()} · All employees in the selected department
            </p>

        </div>

    </div>


    <!-- =========================
         EMPLOYEE TABLE
         ========================= -->

    <div class="table-card">

        <div class="table">

            <!-- TABLE HEADER -->

            <div class="table-header">

                <span>Employee</span>

                <span>Employee ID</span>

                <span>Department</span>

                <span>Total Days</span>

                <span>Present</span>

                <span>Absent</span>

                <span>Late</span>

                <span>Attendance</span>

            </div>


            <!-- TABLE DATA -->

            {#each filteredEmployees as employee}

                <div class="table-row">

                    <strong>
                        {employee.name}
                    </strong>

                    <span>
                        {employee.id}
                    </span>

                    <span>
                        {employee.department}
                    </span>

                    <span>
                        {employee.totalDays}
                    </span>

                    <span class="present">
                        {employee.present}
                    </span>

                    <span class="absent">
                        {employee.absent}
                    </span>

                    <span class="late">
                        {employee.late}
                    </span>

                    <span class="percentage">
                        {employee.percentage}%
                    </span>

                </div>

            {:else}

                <div class="empty-row">
                    No employees found in this department.
                </div>

            {/each}

        </div>

    </div>


    <!-- =========================
         PARTICULAR EMPLOYEE
         ========================= -->

    <div class="search-card">

        <div class="search-header">

            <div>

                <h3>Find Particular Employee</h3>

                <p>
                    Enter Employee ID to view individual attendance.
                </p>

            </div>

        </div>


        <div class="search-row">

            <div class="field">

                <label for="employee-id">
                    Employee ID
                </label>

                <input
                    id="employee-id"
                    type="text"
                    placeholder="Enter Employee ID e.g. EMP001"
                    bind:value={employeeId}
                    onkeydown={(event) => {
                        if (event.key === 'Enter') {
                            searchEmployee();
                        }
                    }}
                />

            </div>


            <button
                type="button"
                onclick={searchEmployee}
            >
                View Attendance
            </button>


            {#if searchedEmployee}

                <button
                    type="button"
                    class="clear"
                    onclick={clearSearch}
                >
                    Clear
                </button>

            {/if}

        </div>


        <!-- =========================
             EMPLOYEE DETAILS
             ========================= -->

        {#if searchedEmployee && selectedEmployee}

            <div class="employee-details">

                <div class="employee-info">

                    <span>Employee</span>

                    <strong>
                        {selectedEmployee.name}
                    </strong>

                    <small>
                        {selectedEmployee.id}
                        ·
                        {selectedEmployee.department}
                    </small>

                </div>


                <div class="detail-card">

                    <span>Total Days</span>

                    <strong>
                        {selectedEmployee.totalDays}
                    </strong>

                </div>


                <div class="detail-card">

                    <span>Present</span>

                    <strong class="green">
                        {selectedEmployee.present}
                    </strong>

                </div>


                <div class="detail-card">

                    <span>Absent</span>

                    <strong class="red">
                        {selectedEmployee.absent}
                    </strong>

                </div>


                <div class="detail-card">

                    <span>Late</span>

                    <strong class="orange">
                        {selectedEmployee.late}
                    </strong>

                </div>


                <div class="detail-card attendance">

                    <span>Attendance</span>

                    <strong>
                        {selectedEmployee.percentage}%
                    </strong>

                </div>

            </div>


        {:else if searchedEmployee}

            <div class="not-found">

                No employee found with ID
                <strong>{searchedEmployee}</strong>.

            </div>

        {/if}

    </div>

</section>


<style lang="scss">

.employee-attendance {
    margin-top: 24px;
}


/* =========================
   HEADER
   ========================= */

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


/* =========================
   SELECTION CARD
   ========================= */

.selection-card {
    display: grid;

    grid-template-columns:
        repeat(2, 1fr);

    gap: 16px;

    padding: 22px;

    background: white;

    border: 1px solid #e5eaf2;

    border-radius: 16px;

    box-shadow:
        0 4px 14px
        rgba(15, 23, 42, 0.03);
}

.field {
    min-width: 0;
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

    padding: 0 11px;

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


/* =========================
   RESULT HEADING
   ========================= */

.result-heading {
    display: flex;

    align-items: center;

    justify-content: space-between;

    margin-top: 20px;

    padding: 18px 20px;

    background: #f8fafc;

    border: 1px solid #e5eaf2;

    border-radius: 13px;
}

.result-heading h3 {
    margin: 0;

    color: #14213d;

    font-size: 16px;
}

.result-heading p {
    margin: 5px 0 0;

    color: #64748b;

    font-size: 12px;
}


/* =========================
   TABLE
   ========================= */

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

.empty-row {
    padding: 25px;

    text-align: center;

    color: #64748b;

    font-size: 13px;
}


/* =========================
   SEARCH CARD
   ========================= */

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


/* =========================
   EMPLOYEE DETAILS
   ========================= */

.employee-details {
    display: grid;

    grid-template-columns:
        1.5fr
        repeat(5, 1fr);

    gap: 12px;

    margin-top: 18px;
}

.employee-info,
.detail-card {
    padding: 16px;

    border: 1px solid #e5eaf2;

    border-radius: 12px;

    background: #f8fafc;
}

.employee-info span,
.detail-card span {
    display: block;

    margin-bottom: 6px;

    color: #64748b;

    font-size: 11px;
}

.employee-info strong {
    display: block;

    color: #14213d;

    font-size: 14px;
}

.employee-info small {
    display: block;

    margin-top: 4px;

    color: #64748b;

    font-size: 11px;
}

.detail-card strong {
    color: #14213d;

    font-size: 20px;
}

.green {
    color: #16a34a !important;
}

.red {
    color: #dc2626 !important;
}

.orange {
    color: #ea580c !important;
}

.detail-card.attendance {
    background: #eef4ff;

    border-color: #d5e2ff;
}

.detail-card.attendance strong {
    color: #2563eb;
}


/* =========================
   NOT FOUND
   ========================= */

.not-found {
    margin-top: 16px;

    padding: 12px 14px;

    border: 1px solid #fecaca;

    border-radius: 9px;

    background: #fef2f2;

    color: #dc2626;

    font-size: 12px;
}


/* =========================
   RESPONSIVE
   ========================= */

@media (max-width: 700px) {

    .selection-card {
        grid-template-columns: 1fr;
    }

    .search-row {
        flex-direction: column;

        align-items: stretch;
    }

    .search-row button {
        width: 100%;
    }

    .employee-details {
        grid-template-columns:
            repeat(2, 1fr);
    }

}


@media (max-width: 500px) {

    .employee-details {
        grid-template-columns: 1fr;
    }

}

</style>