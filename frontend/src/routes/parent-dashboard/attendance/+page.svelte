<script lang="ts">
    import {
        CalendarCheck,
        CheckCircle2,
        XCircle,
        Clock3,
        TrendingUp
    } from '@lucide/svelte';
    import { getMyChildren, type Child } from '$lib/services/parent';

    let selectedChild = $state<Child | null>(null);
    let children = $state<Child[]>([]);
    let isLoading = $state(true);
    let error = $state('');

    async function loadChildren() {
        isLoading = true;
        error = '';
        try {
            children = await getMyChildren();
            if (!selectedChild && children.length > 0) {
                selectedChild = children[0];
            }
        } catch (err) {
            error = err instanceof Error ? err.message : 'Unable to load attendance.';
        } finally {
            isLoading = false;
        }
    }

    $effect(() => {
        loadChildren();
    });
</script>

<svelte:head>
    <title>Attendance | PaperBuddy</title>
</svelte:head>

<div class="attendance-page">
    <div class="page-header">
        <div>
            <h1>Attendance</h1>
            <p>Track your children's attendance.</p>
        </div>

        {#if children.length > 1}
            <select class="child-select" bind:value={selectedChild}>
                {#each children as child}
                    <option value={child}>{child.full_name || child.student_id}</option>
                {/each}
            </select>
        {/if}
    </div>

    {#if error}
        <div class="error-box">{error}</div>
    {/if}

    {#if isLoading}
        <p class="empty">Loading...</p>
    {:else if children.length === 0}
        <p class="empty">No children are linked to your account yet.</p>
    {:else}
        {@const percentage = selectedChild?.attendance_percentage ?? 0}
        {@const present = selectedChild?.attendance_present ?? 0}
        {@const total = selectedChild?.attendance_total ?? 0}

        <div class="summary-grid">
            <div class="summary-card">
                <div class="summary-icon">
                    <TrendingUp size={21} />
                </div>
                <div>
                    <span>Overall Attendance</span>
                    <strong>{percentage}%</strong>
                </div>
            </div>

            <div class="summary-card">
                <div class="summary-icon present-icon">
                    <CheckCircle2 size={21} />
                </div>
                <div>
                    <span>Present Days</span>
                    <strong>{present}</strong>
                </div>
            </div>

            <div class="summary-card">
                <div class="summary-icon absent-icon">
                    <XCircle size={21} />
                </div>
                <div>
                    <span>Absent Days</span>
                    <strong>{Math.max(0, total - present)}</strong>
                </div>
            </div>

            <div class="summary-card">
                <div class="summary-icon late-icon">
                    <Clock3 size={21} />
                </div>
                <div>
                    <span>Recorded Days</span>
                    <strong>{total}</strong>
                </div>
            </div>
        </div>

        <section class="attendance-card">
            <div class="card-header">
                <div>
                    <h2>Attendance Overview</h2>
                    <p>{selectedChild?.full_name || 'Your child'}'s attendance performance</p>
                </div>
                <div class="percentage-badge">
                    {percentage}%
                </div>
            </div>

            <div class="progress-section">
                <div class="progress-label">
                    <span>Attendance Percentage</span>
                    <strong>{percentage}%</strong>
                </div>
                <div class="progress-bar">
                    <div class="progress-fill" style="width: {percentage}%;"></div>
                </div>
                <div class="attendance-note">
                    <CalendarCheck size={16} />
                    <span>
                        {percentage >= 75
                            ? 'Attendance is healthy.'
                            : 'Attendance is below 75%. Please ensure regular attendance.'}
                    </span>
                </div>
            </div>
        </section>

        <section class="attendance-card">
            <div class="card-header">
                <div>
                    <h2>Summary</h2>
                    <p>Attendance summary for {selectedChild?.full_name || 'your child'}</p>
                </div>
            </div>

            <table class="history-table">
                <tbody>
                    <tr>
                        <td>Student</td>
                        <td><strong>{selectedChild?.full_name || '—'}</strong></td>
                    </tr>
                    <tr>
                        <td>Student ID</td>
                        <td>{selectedChild?.student_id || '—'}</td>
                    </tr>
                    <tr>
                        <td>Class</td>
                        <td>{selectedChild?.class_name || '—'}</td>
                    </tr>
                    <tr>
                        <td>Roll Number</td>
                        <td>{selectedChild?.roll_number || '—'}</td>
                    </tr>
                    <tr>
                        <td>Present Days</td>
                        <td>{present}</td>
                    </tr>
                    <tr>
                        <td>Absent Days</td>
                        <td>{Math.max(0, total - present)}</td>
                    </tr>
                    <tr>
                        <td>Attendance Percentage</td>
                        <td><strong>{percentage}%</strong></td>
                    </tr>
                </tbody>
            </table>
        </section>
    {/if}
</div>

<style>
    .attendance-page {
        min-height: 100vh;
        padding: 36px;
        background: #f8fafc;
        box-sizing: border-box;
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

    .child-select {
        padding: 10px 14px;
        border: 1px solid #e2e8f0;
        border-radius: 10px;
        background: white;
        color: #334155;
        font-size: 12px;
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
    }

    .summary-grid {
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 16px;
        margin-bottom: 20px;
    }

    .summary-card {
        display: flex;
        align-items: center;
        gap: 14px;
        padding: 20px;
        background: white;
        border: 1px solid #e2e8f0;
        border-radius: 15px;
        box-shadow: 0 5px 18px rgba(15, 23, 42, 0.04);
    }

    .summary-icon {
        display: flex;
        align-items: center;
        justify-content: center;
        width: 44px;
        height: 44px;
        flex-shrink: 0;
        color: #2563eb;
        background: #eff6ff;
        border-radius: 11px;
    }

    .present-icon {
        color: #16a34a;
        background: #f0fdf4;
    }

    .absent-icon {
        color: #dc2626;
        background: #fef2f2;
    }

    .late-icon {
        color: #d97706;
        background: #fffbeb;
    }

    .summary-card span {
        display: block;
        margin-bottom: 5px;
        color: #64748b;
        font-size: 11px;
    }

    .summary-card strong {
        color: #0f172a;
        font-size: 22px;
        font-weight: 800;
    }

    .attendance-card {
        margin-bottom: 20px;
        padding: 24px;
        background: white;
        border: 1px solid #e2e8f0;
        border-radius: 16px;
        box-shadow: 0 5px 18px rgba(15, 23, 42, 0.04);
    }

    .card-header {
        display: flex;
        align-items: center;
        justify-content: space-between;
        gap: 15px;
        margin-bottom: 24px;
    }

    .card-header h2 {
        margin: 0;
        color: #0f172a;
        font-size: 17px;
        font-weight: 800;
    }

    .card-header p {
        margin: 5px 0 0;
        color: #64748b;
        font-size: 11px;
    }

    .percentage-badge {
        padding: 8px 12px;
        color: #64748b;
        background: #f8fafc;
        border: 1px solid #e2e8f0;
        border-radius: 9px;
        font-size: 13px;
        font-weight: 800;
    }

    .progress-section {
        padding: 4px 0;
    }

    .progress-label {
        display: flex;
        align-items: center;
        justify-content: space-between;
        margin-bottom: 9px;
        color: #64748b;
        font-size: 12px;
    }

    .progress-label strong {
        color: #0f172a;
        font-size: 13px;
    }

    .progress-bar {
        width: 100%;
        height: 10px;
        overflow: hidden;
        background: #e2e8f0;
        border-radius: 999px;
    }

    .progress-fill {
        width: 0;
        height: 100%;
        background: #2563eb;
        border-radius: 999px;
        transition: width 0.5s ease;
    }

    .attendance-note {
        display: flex;
        align-items: center;
        gap: 7px;
        margin-top: 13px;
        color: #64748b;
        font-size: 11px;
    }

    .history-table {
        width: 100%;
        border-collapse: collapse;
        font-size: 13px;
    }

    .history-table td {
        padding: 12px 14px;
        border-bottom: 1px solid #e2e8f0;
        color: #64748b;
    }

    .history-table tr:last-child td {
        border-bottom: none;
    }

    .history-table td:first-child {
        width: 40%;
        color: #94a3b8;
    }

    .history-table td strong {
        color: #0f172a;
    }

    @media (max-width: 1100px) {
        .attendance-page {
            padding: 24px;
        }

        .summary-grid {
            grid-template-columns: repeat(2, 1fr);
        }
    }

    @media (max-width: 700px) {
        .attendance-page {
            padding: 18px;
        }

        .page-header {
            align-items: flex-start;
            flex-direction: column;
        }

        .summary-grid {
            grid-template-columns: 1fr;
        }
    }
</style>