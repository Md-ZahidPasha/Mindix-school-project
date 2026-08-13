<script lang="ts">
    import {
        FileText,
        Download,
        Eye,
        Search,
        FileCheck,
        FileSpreadsheet,
        FileImage,
        FileArchive,
        CalendarDays,
        User,
        Info
    } from '@lucide/svelte';

    let searchQuery = $state('');
    let selectedCategory = $state('All');

    const categories = [
        'All',
        'Personal',
        'Employment',
        'Transport',
        'Certificates'
    ];

    const documents = [
        {
            id: 1,
            name: 'Employee ID Card',
            description: 'Official employee identification document',
            category: 'Personal',
            type: 'PDF',
            size: '245 KB',
            date: '01 Aug 2026',
            icon: FileText,
            className: 'blue'
        },
        {
            id: 2,
            name: 'Employment Agreement',
            description: 'Signed employment agreement and terms',
            category: 'Employment',
            type: 'PDF',
            size: '1.2 MB',
            date: '15 Jul 2026',
            icon: FileCheck,
            className: 'green'
        },
        {
            id: 3,
            name: 'Driving License',
            description: 'Valid driving license document',
            category: 'Transport',
            type: 'PDF',
            size: '580 KB',
            date: '10 Jul 2026',
            icon: FileText,
            className: 'orange'
        },
        {
            id: 4,
            name: 'Vehicle Assignment Letter',
            description: 'Current vehicle assignment document',
            category: 'Transport',
            type: 'PDF',
            size: '420 KB',
            date: '05 Aug 2026',
            icon: FileCheck,
            className: 'purple'
        },
        {
            id: 5,
            name: 'Employee Joining Form',
            description: 'Employee joining and onboarding form',
            category: 'Employment',
            type: 'DOCX',
            size: '315 KB',
            date: '01 Jul 2026',
            icon: FileSpreadsheet,
            className: 'blue'
        },
        {
            id: 6,
            name: 'Medical Fitness Certificate',
            description: 'Latest employee fitness certificate',
            category: 'Certificates',
            type: 'PDF',
            size: '680 KB',
            date: '28 Jun 2026',
            icon: FileCheck,
            className: 'green'
        },
        {
            id: 7,
            name: 'Safety Training Certificate',
            description: 'Completed workplace safety training certificate',
            category: 'Certificates',
            type: 'PDF',
            size: '510 KB',
            date: '20 Jun 2026',
            icon: FileCheck,
            className: 'orange'
        },
        {
            id: 8,
            name: 'Profile Photograph',
            description: 'Official employee profile photograph',
            category: 'Personal',
            type: 'JPG',
            size: '1.8 MB',
            date: '01 Jun 2026',
            icon: FileImage,
            className: 'pink'
        }
    ];

    const filteredDocuments = $derived(
        documents.filter((document) => {
            const matchesCategory =
                selectedCategory === 'All' ||
                document.category === selectedCategory;

            const query = searchQuery.toLowerCase().trim();

            const matchesSearch =
                !query ||
                document.name.toLowerCase().includes(query) ||
                document.description.toLowerCase().includes(query) ||
                document.category.toLowerCase().includes(query);

            return matchesCategory && matchesSearch;
        })
    );

    function downloadDocument(name: string) {
        alert(`Download for "${name}" will be connected to the backend/API later.`);
    }

    function viewDocument(name: string) {
        alert(`Preview for "${name}" will be connected to the document service later.`);
    }
</script>

<svelte:head>
    <title>Documents | Employee Dashboard</title>
</svelte:head>

<div class="documents-page">

    <!-- HEADER -->
    <div class="page-header">

        <div class="title-row">

            <div class="title-icon">
                <FileText size={24} />
            </div>

            <div>
                <h1>Documents</h1>

                <p>
                    Access your personal, employment and official documents.
                </p>
            </div>

        </div>

        <div class="employee-label">
            <User size={15} />
            Arjun Kumar
        </div>

    </div>


    <!-- SEARCH -->
    <section class="search-card">

        <div class="search-wrapper">

            <Search size={18} />

            <input
                type="text"
                placeholder="Search documents..."
                bind:value={searchQuery}
            />

        </div>

        <span class="document-count">
            {filteredDocuments.length} Documents
        </span>

    </section>


    <!-- CATEGORIES -->
    <section class="category-bar">

        <div class="category-label">
            Category
        </div>

        <div class="categories">

            {#each categories as category}

                <button
                    type="button"
                    class:active={selectedCategory === category}
                    onclick={() => selectedCategory = category}
                >
                    {category}
                </button>

            {/each}

        </div>

    </section>


    <!-- DOCUMENT GRID -->
    {#if filteredDocuments.length > 0}

        <section class="documents-grid">

            {#each filteredDocuments as document}

                <article class="document-card">

                    <div class="document-top">

                        <div class={`document-icon ${document.className}`}>
                            <document.icon size={23} />
                        </div>

                        <span class="file-type">
                            {document.type}
                        </span>

                    </div>


                    <div class="document-content">

                        <h2>
                            {document.name}
                        </h2>

                        <p>
                            {document.description}
                        </p>

                    </div>


                    <div class="document-meta">

                        <div>
                            <CalendarDays size={13} />
                            <span>{document.date}</span>
                        </div>

                        <span>
                            {document.size}
                        </span>

                    </div>


                    <div class="document-actions">

                        <button
                            type="button"
                            onclick={() => viewDocument(document.name)}
                        >
                            <Eye size={15} />
                            View
                        </button>

                        <button
                            class="download-button"
                            type="button"
                            onclick={() => downloadDocument(document.name)}
                        >
                            <Download size={15} />
                            Download
                        </button>

                    </div>

                </article>

            {/each}

        </section>

    {:else}

        <section class="empty-state">

            <div class="empty-icon">
                <FileText size={26} />
            </div>

            <h2>
                No Documents Found
            </h2>

            <p>
                Try changing your search or selecting another category.
            </p>

        </section>

    {/if}


    <!-- DOCUMENT SUMMARY -->
    <section class="summary-grid">

        <div class="summary-card">

            <div class="summary-icon blue">
                <FileText size={19} />
            </div>

            <div>
                <span>Total Documents</span>
                <strong>{documents.length}</strong>
                <small>Available documents</small>
            </div>

        </div>


        <div class="summary-card">

            <div class="summary-icon green">
                <FileCheck size={19} />
            </div>

            <div>
                <span>Certificates</span>

                <strong>
                    {documents.filter(
                        (document) => document.category === 'Certificates'
                    ).length}
                </strong>

                <small>Official certificates</small>
            </div>

        </div>


        <div class="summary-card">

            <div class="summary-icon orange">
                <Download size={19} />
            </div>

            <div>
                <span>Download Access</span>
                <strong>Active</strong>
                <small>Documents available to you</small>
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
                Document Information
            </strong>

            <p>
                Documents shown here are currently demo data.
                During API integration, your actual documents will
                be loaded securely from the backend and the View and
                Download buttons will connect to the document service.
            </p>

        </div>

    </section>

</div>


<style>
    .documents-page {
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

    .employee-label {
        display: flex;
        align-items: center;
        gap: 7px;
        padding: 9px 12px;
        border: 1px solid #dbe3ef;
        border-radius: 9px;
        background: white;
        color: #475569;
        font-size: 10px;
        font-weight: 700;
    }


    /* SEARCH */

    .search-card {
        display: flex;
        align-items: center;
        justify-content: space-between;
        gap: 15px;
        padding: 13px;
        margin-bottom: 13px;
        border: 1px solid #e2e8f0;
        border-radius: 13px;
        background: white;
    }

    .search-wrapper {
        flex: 1;
        max-width: 500px;
        display: flex;
        align-items: center;
        gap: 9px;
        padding: 0 11px;
        border: 1px solid #dbe3ef;
        border-radius: 8px;
        color: #94a3b8;
    }

    .search-wrapper input {
        width: 100%;
        height: 38px;
        border: none;
        outline: none;
        color: #334155;
        font-family: inherit;
        font-size: 10px;
    }

    .search-wrapper input::placeholder {
        color: #94a3b8;
    }

    .document-count {
        padding: 6px 9px;
        border-radius: 7px;
        background: #f1f5f9;
        color: #64748b;
        font-size: 9px;
        font-weight: 700;
        white-space: nowrap;
    }


    /* CATEGORY */

    .category-bar {
        display: flex;
        align-items: center;
        gap: 15px;
        padding: 12px 15px;
        margin-bottom: 18px;
        border: 1px solid #e2e8f0;
        border-radius: 12px;
        background: white;
    }

    .category-label {
        color: #475569;
        font-size: 10px;
        font-weight: 700;
    }

    .categories {
        display: flex;
        align-items: center;
        flex-wrap: wrap;
        gap: 7px;
    }

    .categories button {
        padding: 7px 11px;
        border: 1px solid #dbe3ef;
        border-radius: 7px;
        background: white;
        color: #64748b;
        font-size: 9px;
        font-weight: 600;
        cursor: pointer;
    }

    .categories button:hover {
        background: #f8fafc;
    }

    .categories button.active {
        border-color: #2563eb;
        background: #2563eb;
        color: white;
    }


    /* DOCUMENT GRID */

    .documents-grid {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 15px;
        margin-bottom: 20px;
    }

    .document-card {
        padding: 18px;
        border: 1px solid #e2e8f0;
        border-radius: 14px;
        background: white;
        box-shadow: 0 3px 12px rgba(15, 23, 42, 0.03);
        transition: 0.2s;
    }

    .document-card:hover {
        border-color: #cbd5e1;
        box-shadow: 0 6px 18px rgba(15, 23, 42, 0.05);
        transform: translateY(-1px);
    }

    .document-top {
        display: flex;
        align-items: center;
        justify-content: space-between;
    }

    .document-icon {
        width: 46px;
        height: 46px;
        display: flex;
        align-items: center;
        justify-content: center;
        border-radius: 11px;
    }

    .document-icon.blue {
        background: #eef4ff;
        color: #2563eb;
    }

    .document-icon.green {
        background: #ecfdf5;
        color: #059669;
    }

    .document-icon.orange {
        background: #fff7ed;
        color: #ea580c;
    }

    .document-icon.purple {
        background: #f5f3ff;
        color: #7c3aed;
    }

    .document-icon.pink {
        background: #fdf2f8;
        color: #db2777;
    }

    .file-type {
        padding: 5px 7px;
        border-radius: 6px;
        background: #f1f5f9;
        color: #64748b;
        font-size: 7px;
        font-weight: 700;
    }

    .document-content {
        min-height: 82px;
        margin-top: 15px;
    }

    .document-content h2 {
        margin: 0;
        color: #0f172a;
        font-size: 14px;
    }

    .document-content p {
        margin: 5px 0 0;
        color: #64748b;
        font-size: 9px;
        line-height: 1.5;
    }

    .document-meta {
        display: flex;
        align-items: center;
        justify-content: space-between;
        gap: 10px;
        padding: 11px 0;
        border-top: 1px solid #f1f5f9;
        border-bottom: 1px solid #f1f5f9;
    }

    .document-meta div {
        display: flex;
        align-items: center;
        gap: 5px;
        color: #64748b;
        font-size: 8px;
    }

    .document-meta > span {
        color: #94a3b8;
        font-size: 8px;
    }

    .document-actions {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 7px;
        margin-top: 12px;
    }

    .document-actions button {
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 5px;
        padding: 8px;
        border: 1px solid #dbe3ef;
        border-radius: 7px;
        background: white;
        color: #475569;
        font-size: 8px;
        font-weight: 700;
        cursor: pointer;
    }

    .document-actions button:hover {
        background: #f8fafc;
    }

    .document-actions .download-button {
        border-color: #2563eb;
        background: #2563eb;
        color: white;
    }

    .document-actions .download-button:hover {
        background: #1d4ed8;
    }


    /* EMPTY */

    .empty-state {
        padding: 65px 20px;
        margin-bottom: 20px;
        border: 1px solid #e2e8f0;
        border-radius: 14px;
        background: white;
        text-align: center;
    }

    .empty-icon {
        width: 50px;
        height: 50px;
        display: flex;
        align-items: center;
        justify-content: center;
        margin: 0 auto 11px;
        border-radius: 50%;
        background: #f1f5f9;
        color: #94a3b8;
    }

    .empty-state h2 {
        margin: 0;
        color: #334155;
        font-size: 15px;
    }

    .empty-state p {
        margin: 5px 0 0;
        color: #94a3b8;
        font-size: 10px;
    }


    /* SUMMARY */

    .summary-grid {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 14px;
        margin-bottom: 20px;
    }

    .summary-card {
        display: flex;
        align-items: center;
        gap: 12px;
        padding: 17px;
        border: 1px solid #e2e8f0;
        border-radius: 13px;
        background: white;
        box-shadow: 0 3px 12px rgba(15, 23, 42, 0.03);
    }

    .summary-icon {
        width: 42px;
        height: 42px;
        display: flex;
        align-items: center;
        justify-content: center;
        flex-shrink: 0;
        border-radius: 10px;
    }

    .summary-icon.blue {
        background: #eef4ff;
        color: #2563eb;
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
        font-size: 9px;
    }

    .summary-card strong {
        display: block;
        margin-top: 2px;
        color: #0f172a;
        font-size: 18px;
    }

    .summary-card small {
        display: block;
        margin-top: 2px;
        color: #94a3b8;
        font-size: 8px;
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

    @media (max-width: 1000px) {

        .documents-grid {
            grid-template-columns: repeat(2, 1fr);
        }

        .summary-grid {
            grid-template-columns: 1fr;
        }
    }


    @media (max-width: 700px) {

        .documents-page {
            padding: 18px;
        }

        .page-header {
            align-items: flex-start;
            flex-direction: column;
        }

        .employee-label {
            width: 100%;
            box-sizing: border-box;
        }

        .search-card {
            align-items: stretch;
            flex-direction: column;
        }

        .search-wrapper {
            max-width: none;
        }

        .category-bar {
            align-items: flex-start;
            flex-direction: column;
        }

        .documents-grid {
            grid-template-columns: 1fr;
        }

        .summary-grid {
            grid-template-columns: 1fr;
        }
    }
</style>