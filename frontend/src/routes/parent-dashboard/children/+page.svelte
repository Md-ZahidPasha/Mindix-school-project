<script lang="ts">
    let selectedChildId = $state<string | null>(null);

    const children = [
        {
            id: 'STU001',
            name: 'Rahul Kumar',
            className: '10th',
            section: 'A',
            rollNo: '24',
            attendance: '91%',
            performance: '82%',
            parentId: 'PAR001',
            status: 'Active'
        },
        {
            id: 'STU002',
            name: 'Ayesha Kumar',
            className: '7th',
            section: 'B',
            rollNo: '17',
            attendance: '95%',
            performance: '84%',
            parentId: 'PAR001',
            status: 'Active'
        }
    ];

    function selectChild(childId: string) {
        selectedChildId = childId;
    }

    function clearSelection() {
        selectedChildId = null;
    }
</script>

<svelte:head>
    <title>My Children | PaperBuddy</title>
</svelte:head>

<section class="children-page">

    <!-- PAGE HEADER -->
    <div class="page-header">
        <div>
            <h1>My Children</h1>
            <p>
                View and select a child to access their school information.
            </p>
        </div>

        <div class="parent-badge">
            <span>Parent ID</span>
            <strong>PAR001</strong>
        </div>
    </div>


    <!-- SELECTED CHILD -->
    {#if selectedChildId}
        {@const selectedChild = children.find(
            (child) => child.id === selectedChildId
        )}

        {#if selectedChild}
            <div class="selected-card">

                <div class="selected-header">
                    <div>
                        <span class="selected-label">Selected Child</span>
                        <h2>{selectedChild.name}</h2>
                        <p>
                            {selectedChild.className} Class
                            · Section {selectedChild.section}
                        </p>
                    </div>

                    <button
                        type="button"
                        class="change-button"
                        onclick={clearSelection}
                    >
                        Change Child
                    </button>
                </div>

                <div class="selected-details">

                    <div class="detail-box">
                        <span>Student ID</span>
                        <strong>{selectedChild.id}</strong>
                    </div>

                    <div class="detail-box">
                        <span>Roll Number</span>
                        <strong>{selectedChild.rollNo}</strong>
                    </div>

                    <div class="detail-box">
                        <span>Class</span>
                        <strong>{selectedChild.className}</strong>
                    </div>

                    <div class="detail-box">
                        <span>Section</span>
                        <strong>{selectedChild.section}</strong>
                    </div>

                    <div class="detail-box">
                        <span>Attendance</span>
                        <strong>{selectedChild.attendance}</strong>
                    </div>

                    <div class="detail-box">
                        <span>Performance</span>
                        <strong>{selectedChild.performance}</strong>
                    </div>

                </div>

                <div class="info-message">
                    <span class="info-icon">✓</span>

                    <p>
                        This child is currently selected. Other Parent Dashboard
                        sections will use this child when we connect the API.
                    </p>
                </div>

            </div>
        {/if}
    {/if}


    <!-- CHILDREN LIST -->
    <div class="section-heading">
        <div>
            <h2>Your Children</h2>
            <p>
                {children.length} children are linked to Parent ID
                <strong>PAR001</strong>.
            </p>
        </div>
    </div>


    <div class="children-grid">

        {#each children as child}
            <article
                class:selected={selectedChildId === child.id}
                class="child-card"
            >

                <!-- CARD TOP -->
                <div class="card-top">

                    <div class="avatar">
                        {child.name.charAt(0)}
                    </div>

                    <div class="child-title">
                        <h3>{child.name}</h3>

                        <p>
                            Student ID:
                            <strong>{child.id}</strong>
                        </p>
                    </div>

                    <span class="status">
                        {child.status}
                    </span>

                </div>


                <!-- CLASS -->
                <div class="class-info">

                    <div>
                        <span>Class</span>
                        <strong>{child.className}</strong>
                    </div>

                    <div>
                        <span>Section</span>
                        <strong>{child.section}</strong>
                    </div>

                    <div>
                        <span>Roll No.</span>
                        <strong>{child.rollNo}</strong>
                    </div>

                </div>


                <!-- STATS -->
                <div class="stats">

                    <div class="stat">

                        <div class="stat-heading">
                            <span>Attendance</span>
                            <strong>{child.attendance}</strong>
                        </div>

                        <div class="progress">
                            <div
                                class="progress-fill"
                                style={`width: ${child.attendance}`}
                            ></div>
                        </div>

                    </div>


                    <div class="stat">

                        <div class="stat-heading">
                            <span>Performance</span>
                            <strong>{child.performance}</strong>
                        </div>

                        <div class="progress">
                            <div
                                class="progress-fill performance"
                                style={`width: ${child.performance}`}
                            ></div>
                        </div>

                    </div>

                </div>


                <!-- BUTTON -->
                <button
                    type="button"
                    class="view-button"
                    class:selected-button={selectedChildId === child.id}
                    onclick={() => selectChild(child.id)}
                >
                    {selectedChildId === child.id
                        ? 'Selected Child'
                        : 'View Child'}
                </button>

            </article>
        {/each}

    </div>


    <!-- INFORMATION -->
    <div class="bottom-info">

        <div class="info-icon">i</div>

        <div>
            <strong>About Child Selection</strong>

            <p>
                If you have multiple children studying in the school, select
                the child you want to view. Attendance, performance,
                assignments, exams and other information will be shown for
                the selected child.
            </p>
        </div>

    </div>

</section>


<style>
    .children-page {
        min-height: 100%;
        padding: 28px;
        box-sizing: border-box;
        background: #f7f9fc;
    }

    .page-header {
        display: flex;
        align-items: center;
        justify-content: space-between;
        gap: 20px;
        margin-bottom: 24px;
    }

    .page-header h1 {
        margin: 0;
        color: #14213d;
        font-size: 24px;
        font-weight: 700;
    }

    .page-header p {
        margin: 6px 0 0;
        color: #64748b;
        font-size: 13px;
    }

    .parent-badge {
        display: flex;
        flex-direction: column;
        align-items: flex-end;
        padding: 10px 15px;
        border: 1px solid #dbe3ef;
        border-radius: 10px;
        background: white;
    }

    .parent-badge span {
        color: #64748b;
        font-size: 10px;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }

    .parent-badge strong {
        margin-top: 3px;
        color: #2563eb;
        font-size: 14px;
    }


    /* SELECTED CHILD */

    .selected-card {
        margin-bottom: 28px;
        padding: 22px;
        border: 1px solid #cbdcfb;
        border-radius: 15px;
        background: #f8fbff;
    }

    .selected-header {
        display: flex;
        align-items: center;
        justify-content: space-between;
        gap: 15px;
        margin-bottom: 20px;
    }

    .selected-label {
        color: #2563eb;
        font-size: 11px;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }

    .selected-header h2 {
        margin: 4px 0 0;
        color: #14213d;
        font-size: 19px;
    }

    .selected-header p {
        margin: 4px 0 0;
        color: #64748b;
        font-size: 12px;
    }

    .change-button {
        padding: 9px 14px;
        border: 1px solid #cbd5e1;
        border-radius: 8px;
        background: white;
        color: #334155;
        font-size: 12px;
        font-weight: 600;
        cursor: pointer;
    }

    .change-button:hover {
        background: #f8fafc;
    }

    .selected-details {
        display: grid;
        grid-template-columns: repeat(6, 1fr);
        gap: 10px;
    }

    .detail-box {
        padding: 12px;
        border: 1px solid #e2e8f0;
        border-radius: 9px;
        background: white;
    }

    .detail-box span {
        display: block;
        color: #64748b;
        font-size: 10px;
        font-weight: 600;
    }

    .detail-box strong {
        display: block;
        margin-top: 5px;
        color: #1e293b;
        font-size: 13px;
    }

    .info-message {
        display: flex;
        align-items: center;
        gap: 10px;
        margin-top: 15px;
        padding: 11px 13px;
        border-radius: 9px;
        background: #eff6ff;
    }

    .info-message .info-icon {
        width: 22px;
        height: 22px;
        display: flex;
        align-items: center;
        justify-content: center;
        flex-shrink: 0;
        border-radius: 50%;
        background: #2563eb;
        color: white;
        font-size: 11px;
        font-weight: 700;
    }

    .info-message p {
        margin: 0;
        color: #475569;
        font-size: 11px;
        line-height: 1.5;
    }


    /* SECTION */

    .section-heading {
        margin-bottom: 14px;
    }

    .section-heading h2 {
        margin: 0;
        color: #14213d;
        font-size: 17px;
    }

    .section-heading p {
        margin: 4px 0 0;
        color: #64748b;
        font-size: 12px;
    }

    .section-heading strong {
        color: #334155;
    }


    /* CHILD CARDS */

    .children-grid {
        display: grid;
        grid-template-columns: repeat(2, minmax(0, 1fr));
        gap: 18px;
    }

    .child-card {
        padding: 20px;
        border: 1px solid #e2e8f0;
        border-radius: 15px;
        background: white;
        box-shadow: 0 3px 12px rgba(15, 23, 42, 0.03);
        transition:
            border-color 0.2s ease,
            box-shadow 0.2s ease;
    }

    .child-card:hover {
        border-color: #cbd5e1;
        box-shadow: 0 5px 16px rgba(15, 23, 42, 0.06);
    }

    .child-card.selected {
        border-color: #2563eb;
        box-shadow: 0 0 0 2px rgba(37, 99, 235, 0.08);
    }

    .card-top {
        display: flex;
        align-items: center;
        gap: 12px;
    }

    .avatar {
        width: 48px;
        height: 48px;
        display: flex;
        align-items: center;
        justify-content: center;
        flex-shrink: 0;
        border-radius: 50%;
        background: #eaf1ff;
        color: #2563eb;
        font-size: 18px;
        font-weight: 700;
    }

    .child-title {
        min-width: 0;
        flex: 1;
    }

    .child-title h3 {
        margin: 0;
        color: #14213d;
        font-size: 15px;
    }

    .child-title p {
        margin: 4px 0 0;
        color: #64748b;
        font-size: 11px;
    }

    .child-title strong {
        color: #475569;
    }

    .status {
        padding: 5px 9px;
        border-radius: 20px;
        background: #ecfdf5;
        color: #15803d;
        font-size: 10px;
        font-weight: 700;
    }


    /* CLASS INFO */

    .class-info {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 10px;
        margin-top: 20px;
        padding: 13px;
        border-radius: 10px;
        background: #f8fafc;
    }

    .class-info span {
        display: block;
        color: #64748b;
        font-size: 10px;
    }

    .class-info strong {
        display: block;
        margin-top: 4px;
        color: #1e293b;
        font-size: 13px;
    }


    /* STATS */

    .stats {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 15px;
        margin-top: 18px;
    }

    .stat-heading {
        display: flex;
        align-items: center;
        justify-content: space-between;
        margin-bottom: 7px;
    }

    .stat-heading span {
        color: #64748b;
        font-size: 10px;
        font-weight: 600;
    }

    .stat-heading strong {
        color: #1e293b;
        font-size: 12px;
    }

    .progress {
        height: 6px;
        overflow: hidden;
        border-radius: 10px;
        background: #e2e8f0;
    }

    .progress-fill {
        height: 100%;
        border-radius: 10px;
        background: #2563eb;
    }

    .progress-fill.performance {
        background: #7c3aed;
    }


    /* BUTTON */

    .view-button {
        width: 100%;
        height: 40px;
        margin-top: 20px;
        border: 1px solid #2563eb;
        border-radius: 8px;
        background: white;
        color: #2563eb;
        font-size: 12px;
        font-weight: 600;
        cursor: pointer;
        transition:
            background 0.2s ease,
            color 0.2s ease;
    }

    .view-button:hover {
        background: #eff6ff;
    }

    .view-button.selected-button {
        background: #2563eb;
        color: white;
    }


    /* BOTTOM INFO */

    .bottom-info {
        display: flex;
        align-items: flex-start;
        gap: 11px;
        margin-top: 22px;
        padding: 15px;
        border: 1px solid #e2e8f0;
        border-radius: 11px;
        background: white;
    }

    .bottom-info .info-icon {
        width: 22px;
        height: 22px;
        display: flex;
        align-items: center;
        justify-content: center;
        flex-shrink: 0;
        border-radius: 50%;
        background: #e2e8f0;
        color: #475569;
        font-size: 12px;
        font-weight: 700;
    }

    .bottom-info strong {
        display: block;
        color: #334155;
        font-size: 12px;
    }

    .bottom-info p {
        margin: 4px 0 0;
        color: #64748b;
        font-size: 11px;
        line-height: 1.5;
    }


    /* RESPONSIVE */

    @media (max-width: 1050px) {
        .selected-details {
            grid-template-columns: repeat(3, 1fr);
        }
    }

    @media (max-width: 800px) {
        .children-grid {
            grid-template-columns: 1fr;
        }

        .selected-details {
            grid-template-columns: repeat(2, 1fr);
        }
    }

    @media (max-width: 550px) {
        .children-page {
            padding: 18px;
        }

        .page-header {
            align-items: flex-start;
            flex-direction: column;
        }

        .parent-badge {
            align-items: flex-start;
        }

        .selected-header {
            align-items: flex-start;
            flex-direction: column;
        }

        .selected-details {
            grid-template-columns: 1fr 1fr;
        }

        .stats {
            grid-template-columns: 1fr;
        }
    }
</style>