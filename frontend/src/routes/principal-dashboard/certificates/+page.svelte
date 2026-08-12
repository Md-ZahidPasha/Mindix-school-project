<script lang="ts">
    import PrincipalSidebar from '$lib/components/principal/PrincipalSidebar.svelte';

    type CertificateStatus = 'Issued' | 'Pending';

    type Student = {
        id: string;
        name: string;
        className: string;
        section: string;
        rollNumber: string;
    };

    type CertificateRecord = {
        id: number;
        studentName: string;
        studentId: string;
        certificateType: string;
        issuedDate: string;
        status: CertificateStatus;
    };

    let certificateType = $state('');
    let studentId = $state('');
    let issueDate = $state('2026-08-12');
    let purpose = $state('');

    let selectedStudent = $state<Student | null>(null);
    let message = $state('');
    let messageType = $state<'success' | 'error'>('success');

    const students: Student[] = [
        {
            id: 'STU1001',
            name: 'Rahul Sharma',
            className: '10',
            section: 'A',
            rollNumber: '12'
        },
        {
            id: 'STU1002',
            name: 'Sana Khan',
            className: '10',
            section: 'A',
            rollNumber: '18'
        },
        {
            id: 'STU1003',
            name: 'Arjun Reddy',
            className: '9',
            section: 'B',
            rollNumber: '07'
        },
        {
            id: 'STU1004',
            name: 'Ayesha Begum',
            className: '8',
            section: 'A',
            rollNumber: '21'
        }
    ];

    let certificateRecords = $state<CertificateRecord[]>([
        {
            id: 1,
            studentName: 'Rahul Sharma',
            studentId: 'STU1001',
            certificateType: 'Bonafide Certificate',
            issuedDate: '05 Aug 2026',
            status: 'Issued'
        },
        {
            id: 2,
            studentName: 'Sana Khan',
            studentId: 'STU1002',
            certificateType: 'Character Certificate',
            issuedDate: '03 Aug 2026',
            status: 'Issued'
        },
        {
            id: 3,
            studentName: 'Arjun Reddy',
            studentId: 'STU1003',
            certificateType: 'Study Certificate',
            issuedDate: '01 Aug 2026',
            status: 'Issued'
        },
        {
            id: 4,
            studentName: 'Ayesha Begum',
            studentId: 'STU1004',
            certificateType: 'Transfer Certificate',
            issuedDate: '-',
            status: 'Pending'
        }
    ]);

    let totalIssued = $derived(
        certificateRecords.filter(
            (certificate) => certificate.status === 'Issued'
        ).length
    );

    let pendingCertificates = $derived(
        certificateRecords.filter(
            (certificate) => certificate.status === 'Pending'
        ).length
    );

    let thisYear = $derived(
        certificateRecords.filter(
            (certificate) => certificate.status === 'Issued'
        ).length
    );

    function findStudent() {
        message = '';

        const id = studentId.trim().toUpperCase();

        if (!id) {
            selectedStudent = null;
            message = 'Please enter a Student ID.';
            messageType = 'error';
            return;
        }

        const student = students.find(
            (item) => item.id.toUpperCase() === id
        );

        if (!student) {
            selectedStudent = null;
            message = 'Student not found. Please check the Student ID.';
            messageType = 'error';
            return;
        }

        selectedStudent = student;
        message = '';
    }

    function generateCertificate() {
        message = '';

        if (!selectedStudent) {
            message = 'Please find and verify the student first.';
            messageType = 'error';
            return;
        }

        if (!certificateType) {
            message = 'Please select a certificate type.';
            messageType = 'error';
            return;
        }

        if (!issueDate) {
            message = 'Please select the issue date.';
            messageType = 'error';
            return;
        }

        const formattedDate = new Date(issueDate).toLocaleDateString(
            'en-GB',
            {
                day: '2-digit',
                month: 'short',
                year: 'numeric'
            }
        );

        certificateRecords = [
            {
                id: Date.now(),
                studentName: selectedStudent.name,
                studentId: selectedStudent.id,
                certificateType,
                issuedDate: formattedDate,
                status: 'Issued'
            },
            ...certificateRecords
        ];

        message = `${certificateType} generated successfully for ${selectedStudent.name}.`;
        messageType = 'success';

        certificateType = '';
        purpose = '';
        studentId = '';
        selectedStudent = null;
    }

    function clearStudent() {
        selectedStudent = null;
        studentId = '';
        message = '';
    }

    function viewCertificate(certificate: CertificateRecord) {
        message = `${certificate.certificateType} for ${certificate.studentName} is ready to view.`;
        messageType = 'success';
    }

    function downloadCertificate(certificate: CertificateRecord) {
        message = `Demo download started for ${certificate.certificateType} - ${certificate.studentName}.`;
        messageType = 'success';
    }
</script>


<div class="principal-layout">

    <PrincipalSidebar />

    <main class="main-content">

        <div class="certificates-page">

            <!-- PAGE HEADER -->

            <header class="page-header">

                <div>
                    <h1>Certificates</h1>

                    <p>
                        Generate, issue and manage student certificates.
                    </p>
                </div>

            </header>


            <!-- SUMMARY CARDS -->

            <section class="summary-grid">

                <div class="summary-card">

                    <div class="summary-icon issued">
                        ✓
                    </div>

                    <div>
                        <span>Total Issued</span>
                        <strong>{totalIssued}</strong>
                    </div>

                </div>


                <div class="summary-card">

                    <div class="summary-icon pending">
                        ⏳
                    </div>

                    <div>
                        <span>Pending</span>
                        <strong>{pendingCertificates}</strong>
                    </div>

                </div>


                <div class="summary-card">

                    <div class="summary-icon year">
                        ▣
                    </div>

                    <div>
                        <span>Issued This Year</span>
                        <strong>{thisYear}</strong>
                    </div>

                </div>

            </section>


            <!-- ISSUE CERTIFICATE -->

            <section class="issue-card">

                <div class="section-heading">

                    <div class="heading-icon">
                        ▤
                    </div>

                    <div>
                        <h2>Issue Certificate</h2>

                        <p>
                            Find a student and generate the required certificate.
                        </p>
                    </div>

                </div>


                <!-- FIND STUDENT -->

                <div class="student-search">

                    <div class="field student-id-field">

                        <label for="student-id">
                            Student ID
                        </label>

                        <input
                            id="student-id"
                            type="text"
                            bind:value={studentId}
                            placeholder="Enter Student ID e.g. STU1001"
                            onkeydown={(event) => {
                                if (event.key === 'Enter') {
                                    findStudent();
                                }
                            }}
                        />

                    </div>


                    <button
                        type="button"
                        class="find-button"
                        onclick={findStudent}
                    >
                        Find Student
                    </button>

                </div>


                {#if selectedStudent}

                    <div class="student-details">

                        <div class="student-header">

                            <div class="student-avatar">
                                {selectedStudent.name.charAt(0)}
                            </div>

                            <div>
                                <span>STUDENT FOUND</span>

                                <h3>
                                    {selectedStudent.name}
                                </h3>

                                <p>
                                    {selectedStudent.id}
                                </p>
                            </div>

                            <button
                                type="button"
                                class="clear-button"
                                onclick={clearStudent}
                            >
                                Clear
                            </button>

                        </div>


                        <div class="student-info-grid">

                            <div>
                                <span>Student ID</span>
                                <strong>{selectedStudent.id}</strong>
                            </div>

                            <div>
                                <span>Class</span>
                                <strong>{selectedStudent.className}</strong>
                            </div>

                            <div>
                                <span>Section</span>
                                <strong>{selectedStudent.section}</strong>
                            </div>

                            <div>
                                <span>Roll Number</span>
                                <strong>{selectedStudent.rollNumber}</strong>
                            </div>

                        </div>

                    </div>


                    <!-- CERTIFICATE FORM -->

                    <div class="certificate-form">

                        <div class="field">

                            <label for="certificate-type">
                                Certificate Type
                            </label>

                            <select
                                id="certificate-type"
                                bind:value={certificateType}
                            >
                                <option value="">
                                    Select Certificate
                                </option>

                                <option value="Bonafide Certificate">
                                    Bonafide Certificate
                                </option>

                                <option value="Transfer Certificate">
                                    Transfer Certificate
                                </option>

                                <option value="Character Certificate">
                                    Character Certificate
                                </option>

                                <option value="Study Certificate">
                                    Study Certificate
                                </option>

                                <option value="Course Completion Certificate">
                                    Course Completion Certificate
                                </option>

                                <option value="Participation Certificate">
                                    Participation Certificate
                                </option>

                                <option value="Achievement Certificate">
                                    Achievement Certificate
                                </option>

                                <option value="Attendance Certificate">
                                    Attendance Certificate
                                </option>

                            </select>

                        </div>


                        <div class="field">

                            <label for="issue-date">
                                Issue Date
                            </label>

                            <input
                                id="issue-date"
                                type="date"
                                bind:value={issueDate}
                            />

                        </div>


                        <div class="field purpose-field">

                            <label for="purpose">
                                Purpose
                            </label>

                            <input
                                id="purpose"
                                type="text"
                                bind:value={purpose}
                                placeholder="Enter purpose if required..."
                            />

                        </div>


                        <button
                            type="button"
                            class="generate-button"
                            onclick={generateCertificate}
                        >
                            Generate Certificate
                        </button>

                    </div>

                {:else}

                    <div class="find-student-info">
                        <div class="info-icon">
                            i
                        </div>

                        <p>
                            Enter a Student ID and click
                            <strong>Find Student</strong>
                            to view student details and issue a certificate.
                        </p>
                    </div>

                {/if}


                {#if message}

                    <div
                        class:success-message={messageType === 'success'}
                        class:error-message={messageType === 'error'}
                        class="message"
                    >
                        {message}
                    </div>

                {/if}

            </section>


            <!-- CERTIFICATE HISTORY -->

            <section class="history-section">

                <div class="section-title">

                    <div>
                        <h2>Certificate History</h2>

                        <p>
                            View certificates issued by the institution.
                        </p>
                    </div>

                    <span class="record-count">
                        {certificateRecords.length} Records
                    </span>

                </div>


                <div class="history-card">

                    <div class="table-wrapper">

                        <table>

                            <thead>

                                <tr>
                                    <th>Student</th>
                                    <th>Student ID</th>
                                    <th>Certificate</th>
                                    <th>Issued Date</th>
                                    <th>Status</th>
                                    <th>Action</th>
                                </tr>

                            </thead>


                            <tbody>

                                {#each certificateRecords as certificate}

                                    <tr>

                                        <td>

                                            <div class="student-cell">

                                                <div class="small-avatar">
                                                    {certificate.studentName.charAt(0)}
                                                </div>

                                                <strong>
                                                    {certificate.studentName}
                                                </strong>

                                            </div>

                                        </td>


                                        <td>
                                            {certificate.studentId}
                                        </td>


                                        <td>
                                            {certificate.certificateType}
                                        </td>


                                        <td>
                                            {certificate.issuedDate}
                                        </td>


                                        <td>

                                            {#if certificate.status === 'Issued'}

                                                <span class="status issued-status">
                                                    Issued
                                                </span>

                                            {:else}

                                                <span class="status pending-status">
                                                    Pending
                                                </span>

                                            {/if}

                                        </td>


                                        <td>

                                            <div class="table-actions">

                                                <button
                                                    type="button"
                                                    onclick={() =>
                                                        viewCertificate(certificate)
                                                    }
                                                >
                                                    View
                                                </button>

                                                {#if certificate.status === 'Issued'}

                                                    <button
                                                        type="button"
                                                        onclick={() =>
                                                            downloadCertificate(
                                                                certificate
                                                            )
                                                        }
                                                    >
                                                        Download
                                                    </button>

                                                {/if}

                                            </div>

                                        </td>

                                    </tr>

                                {/each}

                            </tbody>

                        </table>

                    </div>

                </div>

            </section>

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


    .certificates-page {
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


    /* SUMMARY */

    .summary-grid {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 16px;
        margin-bottom: 22px;
    }


    .summary-card {
        display: flex;
        align-items: center;
        gap: 14px;
        padding: 20px;
        background: white;
        border: 1px solid #e5eaf2;
        border-radius: 16px;
        box-shadow:
            0 4px 14px
            rgba(15, 23, 42, 0.03);
    }


    .summary-icon {
        width: 44px;
        height: 44px;
        display: flex;
        align-items: center;
        justify-content: center;
        border-radius: 12px;
        font-weight: 800;
    }


    .summary-icon.issued {
        background: #f0fdf4;
        color: #16a34a;
    }


    .summary-icon.pending {
        background: #fff7ed;
        color: #ea580c;
    }


    .summary-icon.year {
        background: #eef4ff;
        color: #2563eb;
    }


    .summary-card span {
        display: block;
        margin-bottom: 4px;
        color: #64748b;
        font-size: 12px;
    }


    .summary-card strong {
        color: #14213d;
        font-size: 23px;
    }


    /* ISSUE CARD */

    .issue-card {
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


    /* SEARCH */

    .student-search {
        display: flex;
        align-items: flex-end;
        gap: 12px;
    }


    .student-id-field {
        flex: 1;
    }


    .field label {
        display: block;
        margin-bottom: 7px;
        color: #334155;
        font-size: 12px;
        font-weight: 600;
    }


    .field input,
    .field select {
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


    .field input:focus,
    .field select:focus {
        border-color: #2563eb;
        box-shadow:
            0 0 0 3px
            rgba(37, 99, 235, 0.1);
    }


    .find-button {
        height: 42px;
        padding: 0 24px;
        border: none;
        border-radius: 9px;
        background: #2563eb;
        color: white;
        font-size: 13px;
        font-weight: 600;
        cursor: pointer;
    }


    .find-button:hover {
        background: #1d4ed8;
    }


    /* STUDENT DETAILS */

    .student-details {
        margin-top: 20px;
        padding: 18px;
        border: 1px solid #dbe3ef;
        border-radius: 12px;
        background: #f8fafc;
    }


    .student-header {
        display: flex;
        align-items: center;
        gap: 12px;
    }


    .student-avatar {
        width: 46px;
        height: 46px;
        display: flex;
        align-items: center;
        justify-content: center;
        border-radius: 50%;
        background: #e8f0ff;
        color: #2563eb;
        font-size: 18px;
        font-weight: 700;
    }


    .student-header > div:nth-child(2) {
        flex: 1;
    }


    .student-header span {
        display: block;
        margin-bottom: 3px;
        color: #16a34a;
        font-size: 9px;
        font-weight: 700;
        letter-spacing: 0.6px;
    }


    .student-header h3 {
        margin: 0;
        color: #14213d;
        font-size: 15px;
    }


    .student-header p {
        margin: 3px 0 0;
        color: #64748b;
        font-size: 11px;
    }


    .clear-button {
        padding: 7px 11px;
        border: 1px solid #dbe3ef;
        border-radius: 8px;
        background: white;
        color: #64748b;
        font-size: 11px;
        cursor: pointer;
    }


    .clear-button:hover {
        background: #f1f5f9;
    }


    .student-info-grid {
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 10px;
        margin-top: 16px;
    }


    .student-info-grid > div {
        padding: 11px;
        border: 1px solid #e5eaf2;
        border-radius: 9px;
        background: white;
    }


    .student-info-grid span {
        display: block;
        margin-bottom: 5px;
        color: #94a3b8;
        font-size: 10px;
    }


    .student-info-grid strong {
        color: #334155;
        font-size: 12px;
    }


    /* CERTIFICATE FORM */

    .certificate-form {
        display: grid;
        grid-template-columns: 1fr 1fr 1.4fr;
        gap: 14px;
        margin-top: 18px;
        padding-top: 18px;
        border-top: 1px solid #edf1f6;
    }


    .purpose-field {
        min-width: 0;
    }


    .generate-button {
        grid-column: span 3;
        height: 42px;
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


    /* INFO */

    .find-student-info {
        display: flex;
        align-items: center;
        gap: 11px;
        margin-top: 18px;
        padding: 13px;
        border-radius: 10px;
        background: #f8fafc;
        border: 1px solid #e5eaf2;
    }


    .info-icon {
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


    .find-student-info p {
        margin: 0;
        color: #64748b;
        font-size: 11px;
    }


    /* MESSAGE */

    .message {
        margin-top: 14px;
        padding: 11px 13px;
        border-radius: 9px;
        font-size: 11px;
    }


    .success-message {
        background: #f0fdf4;
        border: 1px solid #bbf7d0;
        color: #15803d;
    }


    .error-message {
        background: #fef2f2;
        border: 1px solid #fecaca;
        color: #dc2626;
    }


    /* HISTORY */

    .history-section {
        margin-top: 28px;
    }


    .section-title {
        display: flex;
        align-items: center;
        justify-content: space-between;
        gap: 15px;
        margin-bottom: 14px;
    }


    .section-title h2 {
        margin: 0;
        color: #14213d;
        font-size: 20px;
    }


    .section-title p {
        margin: 5px 0 0;
        color: #64748b;
        font-size: 13px;
    }


    .record-count {
        padding: 7px 11px;
        border-radius: 8px;
        background: #eef4ff;
        color: #2563eb;
        font-size: 11px;
        font-weight: 700;
    }


    .history-card {
        overflow: hidden;
        background: white;
        border: 1px solid #e5eaf2;
        border-radius: 16px;
        box-shadow:
            0 4px 14px
            rgba(15, 23, 42, 0.03);
    }


    .table-wrapper {
        overflow-x: auto;
    }


    table {
        width: 100%;
        min-width: 850px;
        border-collapse: collapse;
    }


    th {
        padding: 15px 18px;
        background: #f8fafc;
        color: #64748b;
        font-size: 11px;
        font-weight: 700;
        text-align: left;
        border-bottom: 1px solid #e5eaf2;
    }


    td {
        padding: 15px 18px;
        color: #64748b;
        font-size: 12px;
        border-bottom: 1px solid #edf1f6;
    }


    tr:last-child td {
        border-bottom: none;
    }


    .student-cell {
        display: flex;
        align-items: center;
        gap: 9px;
    }


    .small-avatar {
        width: 32px;
        height: 32px;
        display: flex;
        align-items: center;
        justify-content: center;
        border-radius: 50%;
        background: #e8f0ff;
        color: #2563eb;
        font-size: 12px;
        font-weight: 700;
    }


    .student-cell strong {
        color: #14213d;
        font-size: 12px;
    }


    .status {
        display: inline-block;
        padding: 6px 9px;
        border-radius: 7px;
        font-size: 10px;
        font-weight: 700;
    }


    .issued-status {
        background: #f0fdf4;
        color: #16a34a;
    }


    .pending-status {
        background: #fff7ed;
        color: #ea580c;
    }


    .table-actions {
        display: flex;
        gap: 7px;
    }


    .table-actions button {
        padding: 6px 9px;
        border: 1px solid #dbe3ef;
        border-radius: 7px;
        background: white;
        color: #2563eb;
        font-size: 10px;
        font-weight: 600;
        cursor: pointer;
    }


    .table-actions button:hover {
        background: #eef4ff;
    }


    /* RESPONSIVE */

    @media (max-width: 950px) {

        .certificates-page {
            padding: 22px;
        }


        .student-info-grid {
            grid-template-columns: repeat(2, 1fr);
        }


        .certificate-form {
            grid-template-columns: 1fr 1fr;
        }


        .generate-button {
            grid-column: span 2;
        }

    }


    @media (max-width: 700px) {

        .summary-grid {
            grid-template-columns: 1fr;
        }


        .student-search {
            flex-direction: column;
            align-items: stretch;
        }


        .find-button {
            width: 100%;
        }


        .certificate-form {
            grid-template-columns: 1fr;
        }


        .generate-button {
            grid-column: span 1;
        }

    }


    @media (max-width: 500px) {

        .certificates-page {
            padding: 18px;
        }


        .student-info-grid {
            grid-template-columns: 1fr;
        }


        .student-header {
            align-items: flex-start;
        }

    }

</style>