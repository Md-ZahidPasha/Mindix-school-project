<script lang="ts">
    import {
        Award,
        CalendarDays,
        CheckCircle2,
        ChevronDown,
        Download,
        Eye,
        FileBadge,
        FileText,
        GraduationCap,
        ShieldCheck
    } from '@lucide/svelte';

    let selectedChild = $state('Rahul Kumar');
    let activeFilter = $state('All');

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

    const certificates = [
        {
            id: 'CERT-2026-001',
            title: 'Academic Excellence Certificate',
            category: 'Academic',
            description:
                'Certificate awarded for outstanding academic performance.',
            issuedDate: '05 Aug 2026',
            issuedBy: 'Principal',
            status: 'Issued',
            type: 'Academic Excellence'
        },
        {
            id: 'CERT-2026-002',
            title: 'Science Exhibition Certificate',
            category: 'Achievement',
            description:
                'Certificate for participation and achievement in the Science Exhibition.',
            issuedDate: '28 Jul 2026',
            issuedBy: 'Principal',
            status: 'Issued',
            type: 'Achievement'
        },
        {
            id: 'CERT-2026-003',
            title: 'Inter-School Sports Certificate',
            category: 'Sports',
            description:
                'Certificate awarded for participation in the inter-school sports competition.',
            issuedDate: '15 Jul 2026',
            issuedBy: 'Principal',
            status: 'Issued',
            type: 'Sports'
        },
        {
            id: 'CERT-2026-004',
            title: 'Attendance Excellence Certificate',
            category: 'Attendance',
            description:
                'Certificate awarded for maintaining excellent attendance during the academic year.',
            issuedDate: '30 Jun 2026',
            issuedBy: 'Principal',
            status: 'Issued',
            type: 'Attendance'
        },
        {
            id: 'CERT-2026-005',
            title: 'Cultural Program Certificate',
            category: 'Cultural',
            description:
                'Certificate for participation in the annual cultural program.',
            issuedDate: '18 Jun 2026',
            issuedBy: 'Principal',
            status: 'Issued',
            type: 'Cultural'
        }
    ];

    function getSelectedChild() {
        return children.find(
            (child) => child.name === selectedChild
        );
    }

    let child = $derived(getSelectedChild());

    let filteredCertificates = $derived(
        activeFilter === 'All'
            ? certificates
            : certificates.filter(
                  (certificate) =>
                      certificate.category === activeFilter
              )
    );

    let issuedCount = $derived(
        certificates.filter(
            (certificate) => certificate.status === 'Issued'
        ).length
    );

    function downloadCertificate(certificate: {
        title: string;
        id: string;
    }) {
        alert(
            `Download will be connected to the certificate API for ${certificate.title} (${certificate.id}).`
        );
    }

    function viewCertificate(certificate: {
        title: string;
        id: string;
    }) {
        alert(
            `Certificate preview will be connected to the certificate API for ${certificate.title} (${certificate.id}).`
        );
    }
</script>

<svelte:head>
    <title>Certificates | Parent Dashboard</title>
</svelte:head>

<div class="certificates-page">

    <!-- HEADER -->
    <div class="page-header">

        <div class="title-row">

            <div class="title-icon">
                <Award size={24} />
            </div>

            <div>
                <h1>Certificates</h1>

                <p>
                    View and download certificates issued to your child.
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

        <div class="certificate-summary">

            <span>Certificates Available</span>

            <strong>{issuedCount}</strong>

            <small>
                Ready to view/download
            </small>

        </div>

    </section>


    <!-- SUMMARY -->
    <section class="summary-grid">

        <div class="summary-card">

            <div class="summary-icon blue">
                <Award size={21} />
            </div>

            <div>
                <span>Total Certificates</span>
                <strong>{certificates.length}</strong>
            </div>

        </div>


        <div class="summary-card">

            <div class="summary-icon green">
                <CheckCircle2 size={21} />
            </div>

            <div>
                <span>Issued</span>
                <strong>{issuedCount}</strong>
            </div>

        </div>


        <div class="summary-card">

            <div class="summary-icon purple">
                <GraduationCap size={21} />
            </div>

            <div>
                <span>Academic</span>

                <strong>
                    {certificates.filter(
                        (item) => item.category === 'Academic'
                    ).length}
                </strong>

            </div>

        </div>


        <div class="summary-card">

            <div class="summary-icon orange">
                <ShieldCheck size={21} />
            </div>

            <div>
                <span>Achievements</span>

                <strong>
                    {certificates.filter(
                        (item) => item.category === 'Achievement'
                    ).length}
                </strong>

            </div>

        </div>

    </section>


    <!-- INFORMATION BANNER -->
    <section class="information-banner">

        <div class="banner-icon">
            <ShieldCheck size={21} />
        </div>

        <div>

            <strong>
                Official School Certificates
            </strong>

            <p>
                Certificates shown here are officially issued or
                approved by the school. Parents can view and
                download certificates belonging to the selected child.
            </p>

        </div>

    </section>


    <!-- FILTERS -->
    <section class="card filter-card">

        <div class="filter-header">

            <div>

                <h2>Certificate Collection</h2>

                <p>
                    Browse certificates by category.
                </p>

            </div>


            <div class="filter-buttons">

                {#each [
                    'All',
                    'Academic',
                    'Achievement',
                    'Sports',
                    'Attendance',
                    'Cultural'
                ] as filter}

                    <button
                        class:active={activeFilter === filter}
                        onclick={() => activeFilter = filter}
                    >
                        {filter}
                    </button>

                {/each}

            </div>

        </div>

    </section>


    <!-- CERTIFICATE LIST -->
    <section class="card">

        <div class="card-header">

            <div>

                <h2>
                    {activeFilter === 'All'
                        ? 'All Certificates'
                        : `${activeFilter} Certificates`}
                </h2>

                <p>
                    {filteredCertificates.length}
                    certificate{filteredCertificates.length === 1 ? '' : 's'}
                    available.
                </p>

            </div>

        </div>


        <div class="certificate-list">

            {#each filteredCertificates as certificate}

                <div class="certificate-card">

                    <div class="certificate-left">

                        <div class="certificate-icon">
                            <FileBadge size={25} />
                        </div>

                    </div>


                    <div class="certificate-content">

                        <div class="certificate-title-row">

                            <div>

                                <h3>
                                    {certificate.title}
                                </h3>

                                <span class="certificate-category">
                                    {certificate.category}
                                </span>

                            </div>


                            <span class="issued-badge">
                                <CheckCircle2 size={12} />
                                {certificate.status}
                            </span>

                        </div>


                        <p class="certificate-description">
                            {certificate.description}
                        </p>


                        <div class="certificate-meta">

                            <span>
                                <CalendarDays size={14} />
                                Issued: {certificate.issuedDate}
                            </span>

                            <span>
                                <GraduationCap size={14} />
                                Issued by: {certificate.issuedBy}
                            </span>

                            <span>
                                <FileText size={14} />
                                ID: {certificate.id}
                            </span>

                        </div>


                        <div class="certificate-actions">

                            <button
                                class="view-button"
                                onclick={() =>
                                    viewCertificate(certificate)
                                }
                            >
                                <Eye size={15} />
                                View Certificate
                            </button>


                            <button
                                class="download-button"
                                onclick={() =>
                                    downloadCertificate(certificate)
                                }
                            >
                                <Download size={15} />
                                Download
                            </button>

                        </div>

                    </div>

                </div>

            {:else}

                <div class="empty-state">

                    <div class="empty-icon">
                        <Award size={28} />
                    </div>

                    <h3>
                        No certificates found
                    </h3>

                    <p>
                        There are no certificates available in this category.
                    </p>

                </div>

            {/each}

        </div>

    </section>


    <!-- DOWNLOAD INFORMATION -->
    <section class="download-note">

        <div class="note-icon">
            <Download size={18} />
        </div>

        <div>

            <strong>
                Download Your Child's Certificates
            </strong>

            <p>
                Use the Download button to save an official copy
                of the selected certificate. The actual certificate
                file will be connected through the backend API.
            </p>

        </div>

    </section>


    <!-- API INFORMATION -->
    <div class="info-note">

        <div class="note-icon">
            <FileText size={18} />
        </div>

        <div>

            <strong>
                Certificate Information
            </strong>

            <p>
                Certificate information shown here is currently
                demo data. During API integration, certificates
                issued or approved by the Principal will be loaded
                from the school's database for the selected child.
                The download button will retrieve the actual certificate.
            </p>

        </div>

    </div>

</div>


<style>
    .certificates-page {
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
        color: #0f172a;
        font-size: 28px;
        font-weight: 800;
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
        top: 13px;
        right: 12px;
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

    .certificate-summary {
        min-width: 155px;
        padding: 12px 16px;
        border-radius: 11px;
        background: #ecfdf5;
        text-align: center;
    }

    .certificate-summary span {
        display: block;
        color: #64748b;
        font-size: 10px;
    }

    .certificate-summary strong {
        display: block;
        margin: 2px 0;
        color: #059669;
        font-size: 24px;
    }

    .certificate-summary small {
        color: #047857;
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


    /* INFORMATION BANNER */

    .information-banner {
        display: flex;
        align-items: flex-start;
        gap: 12px;
        padding: 16px;
        margin-bottom: 20px;
        border: 1px solid #bfdbfe;
        border-radius: 13px;
        background: #eff6ff;
    }

    .banner-icon {
        width: 39px;
        height: 39px;
        display: flex;
        align-items: center;
        justify-content: center;
        flex-shrink: 0;
        border-radius: 10px;
        background: #dbeafe;
        color: #2563eb;
    }

    .information-banner strong {
        display: block;
        color: #1e3a8a;
        font-size: 12px;
    }

    .information-banner p {
        margin: 4px 0 0;
        color: #475569;
        font-size: 10px;
        line-height: 1.5;
    }


    /* CARDS */

    .card {
        margin-bottom: 20px;
        padding: 22px;
        border: 1px solid #e2e8f0;
        border-radius: 15px;
        background: white;
        box-shadow: 0 3px 12px rgba(15, 23, 42, 0.03);
    }

    .card-header,
    .filter-header {
        display: flex;
        align-items: flex-start;
        justify-content: space-between;
        gap: 15px;
        margin-bottom: 20px;
    }

    .card-header h2,
    .filter-header h2 {
        margin: 0;
        color: #0f172a;
        font-size: 17px;
    }

    .card-header p,
    .filter-header p {
        margin: 4px 0 0;
        color: #64748b;
        font-size: 11px;
    }


    /* FILTER */

    .filter-header {
        align-items: center;
    }

    .filter-buttons {
        display: flex;
        align-items: center;
        gap: 7px;
        flex-wrap: wrap;
    }

    .filter-buttons button {
        padding: 8px 11px;
        border: 1px solid #dbe3ef;
        border-radius: 8px;
        background: white;
        color: #64748b;
        font-size: 9px;
        font-weight: 600;
        cursor: pointer;
        transition: 0.2s ease;
    }

    .filter-buttons button:hover {
        border-color: #93c5fd;
        color: #2563eb;
    }

    .filter-buttons button.active {
        border-color: #2563eb;
        background: #2563eb;
        color: white;
    }


    /* CERTIFICATE LIST */

    .certificate-list {
        display: flex;
        flex-direction: column;
        gap: 13px;
    }

    .certificate-card {
        display: flex;
        align-items: flex-start;
        gap: 15px;
        padding: 17px;
        border: 1px solid #e2e8f0;
        border-radius: 13px;
        background: #f8fafc;
        transition: 0.2s ease;
    }

    .certificate-card:hover {
        border-color: #bfdbfe;
        box-shadow: 0 3px 10px rgba(37, 99, 235, 0.06);
    }

    .certificate-left {
        flex-shrink: 0;
    }

    .certificate-icon {
        width: 50px;
        height: 50px;
        display: flex;
        align-items: center;
        justify-content: center;
        border-radius: 12px;
        background: #fef3c7;
        color: #d97706;
    }

    .certificate-content {
        flex: 1;
        min-width: 0;
    }

    .certificate-title-row {
        display: flex;
        align-items: flex-start;
        justify-content: space-between;
        gap: 15px;
    }

    .certificate-title-row h3 {
        margin: 0;
        color: #0f172a;
        font-size: 14px;
    }

    .certificate-category {
        display: inline-block;
        margin-top: 4px;
        color: #2563eb;
        font-size: 9px;
        font-weight: 700;
    }

    .issued-badge {
        display: flex;
        align-items: center;
        gap: 4px;
        padding: 5px 8px;
        border-radius: 7px;
        background: #ecfdf5;
        color: #059669;
        font-size: 9px;
        font-weight: 700;
        white-space: nowrap;
    }

    .certificate-description {
        margin: 9px 0 12px;
        color: #64748b;
        font-size: 10px;
        line-height: 1.5;
    }

    .certificate-meta {
        display: flex;
        align-items: center;
        flex-wrap: wrap;
        gap: 15px;
    }

    .certificate-meta span {
        display: flex;
        align-items: center;
        gap: 5px;
        color: #64748b;
        font-size: 9px;
    }

    /* ACTIONS */

    .certificate-actions {
        display: flex;
        align-items: center;
        gap: 8px;
        margin-top: 14px;
    }

    .certificate-actions button {
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 6px;
        padding: 8px 12px;
        border-radius: 8px;
        font-size: 9px;
        font-weight: 700;
        cursor: pointer;
        transition: 0.2s ease;
    }

    .view-button {
        border: 1px solid #dbe3ef;
        background: white;
        color: #475569;
    }

    .view-button:hover {
        border-color: #93c5fd;
        color: #2563eb;
    }

    .download-button {
        border: 1px solid #2563eb;
        background: #2563eb;
        color: white;
    }

    .download-button:hover {
        background: #1d4ed8;
        border-color: #1d4ed8;
    }


    /* DOWNLOAD NOTE */

    .download-note {
        display: flex;
        align-items: flex-start;
        gap: 11px;
        padding: 14px;
        margin-bottom: 12px;
        border: 1px solid #bbf7d0;
        border-radius: 11px;
        background: #f0fdf4;
    }

    .download-note .note-icon {
        background: #dcfce7;
        color: #059669;
    }

    .download-note strong {
        display: block;
        color: #166534;
        font-size: 11px;
    }

    .download-note p {
        margin: 4px 0 0;
        color: #4d7c0f;
        font-size: 10px;
        line-height: 1.5;
    }


    /* INFO NOTE */

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


    /* EMPTY */

    .empty-state {
        padding: 45px 20px;
        text-align: center;
    }

    .empty-icon {
        width: 58px;
        height: 58px;
        display: flex;
        align-items: center;
        justify-content: center;
        margin: 0 auto 12px;
        border-radius: 50%;
        background: #fef3c7;
        color: #d97706;
    }

    .empty-state h3 {
        margin: 0;
        color: #334155;
        font-size: 15px;
    }

    .empty-state p {
        margin: 5px 0 0;
        color: #94a3b8;
        font-size: 10px;
    }


    /* RESPONSIVE */

    @media (max-width: 1100px) {

        .certificates-page {
            padding: 24px;
        }

        .summary-grid {
            grid-template-columns: repeat(2, 1fr);
        }
    }


    @media (max-width: 750px) {

        .certificates-page {
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

        .certificate-summary {
            width: 100%;
        }

        .summary-grid {
            grid-template-columns: 1fr;
        }

        .filter-header {
            align-items: flex-start;
            flex-direction: column;
        }

        .filter-buttons {
            width: 100%;
        }

        .filter-buttons button {
            flex: 1;
        }

        .certificate-title-row {
            align-items: flex-start;
            flex-direction: column;
        }

        .certificate-actions {
            flex-wrap: wrap;
        }

        .certificate-actions button {
            flex: 1;
        }

        .certificate-meta {
            flex-direction: column;
            align-items: flex-start;
            gap: 7px;
        }
    }
</style>