<script lang="ts">
    import { Users, GraduationCap, TrendingUp, RefreshCw } from '@lucide/svelte';
    import { getMyChildren, type Child } from '$lib/services/parent';

    let selectedChildId = $state<string | null>(null);
    let children = $state<Child[]>([]);
    let isLoading = $state(true);
    let error = $state('');

    async function loadChildren() {
        isLoading = true;
        error = '';
        try {
            children = await getMyChildren();
            if (selectedChildId && !children.some((c) => c.student_id === selectedChildId)) {
                selectedChildId = null;
            }
        } catch (err) {
            error = err instanceof Error ? err.message : 'Unable to load children.';
        } finally {
            isLoading = false;
        }
    }

    function selectChild(childId: string) {
        selectedChildId = childId;
    }

    function clearSelection() {
        selectedChildId = null;
    }

    const selectedChild = $derived(
        selectedChildId ? children.find((c) => c.student_id === selectedChildId) || null : null
    );

    $effect(() => {
        loadChildren();
    });
</script>

<svelte:head>
    <title>My Children | PaperBuddy</title>
</svelte:head>

<section class="children-page">

    <div class="page-header">
        <div>
            <h1>My Children</h1>
            <p>
                View and select a child to access their school information.
            </p>
        </div>

        <button class="refresh-btn" type="button" onclick={loadChildren}>
            <RefreshCw size={15} /> Refresh
        </button>
    </div>

    {#if error}
        <div class="error-box">{error}</div>
    {/if}

    {#if selectedChild}
        <div class="selected-card">
            <div class="selected-head">
                <div>
                    <h2>{selectedChild.full_name || selectedChild.student_id}</h2>
                    <p>
                        Class {selectedChild.class_name || '—'} · Roll {selectedChild.roll_number || '—'}
                    </p>
                </div>
                <button class="clear-btn" type="button" onclick={clearSelection}>
                    Close
                </button>
            </div>

            <div class="child-metrics">
                <div class="metric">
                    <GraduationCap size={20} />
                    <div>
                        <span>Class</span>
                        <strong>{selectedChild.class_name || '—'}</strong>
                    </div>
                </div>
                <div class="metric">
                    <TrendingUp size={20} />
                    <div>
                        <span>Attendance</span>
                        <strong>
                            {selectedChild.attendance_percentage ?? 0}%
                        </strong>
                    </div>
                </div>
                <div class="metric">
                    <Users size={20} />
                    <div>
                        <span>Present Days</span>
                        <strong>
                            {selectedChild.attendance_present ?? 0} / {selectedChild.attendance_total ?? 0}
                        </strong>
                    </div>
                </div>
            </div>
        </div>
    {/if}

    <div class="children-grid">
        {#if isLoading}
            <p class="empty">Loading children...</p>
        {:else if children.length === 0}
            <p class="empty">
                No children are linked to your account yet. Contact the school to link your children.
            </p>
        {:else}
            {#each children as child}
                <div
                    class="child-card"
                    class:selected={selectedChildId === child.student_id}
                    onclick={() => selectChild(child.student_id)}
                >
                    <div class="avatar">
                        {(child.full_name || child.student_id || '?').slice(0, 1).toUpperCase()}
                    </div>
                    <div class="child-info">
                        <strong>{child.full_name || child.student_id}</strong>
                        <span>Student ID: {child.student_id}</span>
                        <span>Class {child.class_name || '—'} · Roll {child.roll_number || '—'}</span>
                    </div>
                    <div class="attendance-badge">
                        <span>Attendance</span>
                        <strong>{child.attendance_percentage ?? 0}%</strong>
                    </div>
                </div>
            {/each}
        {/if}
    </div>

    {#if selectedChild}
        <div class="detail-card">
            <h3>Attendance Details</h3>
            <div class="progress-row">
                <span>Attendance Percentage</span>
                <strong>{selectedChild.attendance_percentage ?? 0}%</strong>
            </div>
            <div class="progress-bar">
                <div class="progress-fill" style="width: {selectedChild.attendance_percentage ?? 0}%;"></div>
            </div>
            <p class="detail-note">
                Present {selectedChild.attendance_present ?? 0} of {selectedChild.attendance_total ?? 0} recorded days.
                More details such as marks and timetable are available from your school.
            </p>
        </div>
    {/if}

</section>

<style>
    .children-page {
        min-height: 100vh;
        padding: 36px;
        box-sizing: border-box;
        background: #f8fafc;
    }

    .page-header {
        display: flex;
        align-items: center;
        justify-content: space-between;
        gap: 20px;
        margin-bottom: 28px;
    }

    .page-header h1 {
        margin: 0;
        color: #0f172a;
        font-size: 30px;
        font-weight: 800;
    }

    .page-header p {
        margin: 7px 0 0;
        color: #64748b;
        font-size: 13px;
    }

    .refresh-btn {
        display: flex;
        align-items: center;
        gap: 6px;
        padding: 10px 16px;
        border: 1px solid #e2e8f0;
        border-radius: 10px;
        background: white;
        color: #334155;
        font-size: 13px;
        font-weight: 600;
        cursor: pointer;
    }

    .error-box {
        padding: 12px 16px;
        margin-bottom: 16px;
        background: #fef2f2;
        border: 1px solid #fecaca;
        border-radius: 10px;
        color: #b91c1c;
        font-size: 13px;
    }

    .empty {
        color: #94a3b8;
        font-size: 13px;
        text-align: center;
        padding: 40px 0;
        grid-column: 1 / -1;
    }

    .children-grid {
        display: grid;
        grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
        gap: 16px;
    }

    .child-card {
        display: flex;
        align-items: center;
        gap: 14px;
        padding: 20px;
        background: white;
        border: 1px solid #e2e8f0;
        border-radius: 15px;
        cursor: pointer;
        transition: all 0.2s ease;
    }

    .child-card:hover {
        border-color: #93c5fd;
        box-shadow: 0 5px 18px rgba(37, 99, 235, 0.08);
    }

    .child-card.selected {
        border-color: #2563eb;
        box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.12);
    }

    .avatar {
        display: flex;
        align-items: center;
        justify-content: center;
        width: 52px;
        height: 52px;
        flex-shrink: 0;
        border-radius: 14px;
        background: linear-gradient(135deg, #2563eb, #7c3aed);
        color: white;
        font-size: 20px;
        font-weight: 700;
    }

    .child-info {
        flex: 1;
        display: flex;
        flex-direction: column;
        gap: 3px;
        min-width: 0;
    }

    .child-info strong {
        color: #0f172a;
        font-size: 15px;
    }

    .child-info span {
        color: #64748b;
        font-size: 12px;
    }

    .attendance-badge {
        display: flex;
        flex-direction: column;
        align-items: flex-end;
        gap: 3px;
        padding-left: 14px;
        border-left: 1px solid #e2e8f0;
    }

    .attendance-badge span {
        color: #94a3b8;
        font-size: 11px;
    }

    .attendance-badge strong {
        color: #16a34a;
        font-size: 17px;
    }

    .selected-card {
        padding: 22px;
        margin-bottom: 20px;
        background: white;
        border: 1px solid #bfdbfe;
        border-radius: 16px;
        background: #f8faff;
    }

    .selected-head {
        display: flex;
        align-items: flex-start;
        justify-content: space-between;
        gap: 15px;
        margin-bottom: 18px;
    }

    .selected-head h2 {
        margin: 0;
        color: #0f172a;
        font-size: 20px;
        font-weight: 800;
    }

    .selected-head p {
        margin: 5px 0 0;
        color: #64748b;
        font-size: 12px;
    }

    .clear-btn {
        padding: 8px 13px;
        border: 1px solid #e2e8f0;
        border-radius: 9px;
        background: white;
        color: #64748b;
        font-size: 12px;
        font-weight: 600;
        cursor: pointer;
    }

    .child-metrics {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 14px;
    }

    .metric {
        display: flex;
        align-items: center;
        gap: 12px;
        padding: 14px;
        background: white;
        border: 1px solid #e2e8f0;
        border-radius: 12px;
        color: #2563eb;
    }

    .metric div {
        display: flex;
        flex-direction: column;
        gap: 2px;
    }

    .metric span {
        color: #64748b;
        font-size: 11px;
    }

    .metric strong {
        color: #0f172a;
        font-size: 16px;
    }

    .detail-card {
        padding: 22px;
        margin-top: 20px;
        background: white;
        border: 1px solid #e2e8f0;
        border-radius: 16px;
    }

    .detail-card h3 {
        margin: 0 0 16px;
        color: #0f172a;
        font-size: 16px;
        font-weight: 700;
    }

    .progress-row {
        display: flex;
        align-items: center;
        justify-content: space-between;
        margin-bottom: 8px;
        color: #64748b;
        font-size: 12px;
    }

    .progress-row strong {
        color: #0f172a;
    }

    .progress-bar {
        width: 100%;
        height: 10px;
        overflow: hidden;
        background: #e2e8f0;
        border-radius: 999px;
    }

    .progress-fill {
        height: 100%;
        background: #2563eb;
        border-radius: 999px;
        transition: width 0.5s ease;
    }

    .detail-note {
        margin: 14px 0 0;
        color: #94a3b8;
        font-size: 12px;
        line-height: 1.6;
    }

    @media (max-width: 700px) {
        .children-page {
            padding: 18px;
        }

        .child-metrics {
            grid-template-columns: 1fr;
        }

        .children-grid {
            grid-template-columns: 1fr;
        }
    }
</style>