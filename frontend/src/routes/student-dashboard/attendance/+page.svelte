<script lang="ts">
    import {
        CalendarCheck,
        CheckCircle2,
        XCircle,
        Clock3,
        TrendingUp
    } from '@lucide/svelte';
    import { API } from '$lib/config/api';

    let isLoading = $state(true);
    let error = $state('');
    let attendance = $state({ percentage: 0, present: 0, absent: 0, late: 0 });
    let recentRecords = $state<{ date: string; status: string }[]>([]);

    async function loadAttendance() {
        isLoading = true;
        error = '';
        try {
            const token = localStorage.getItem('access_token');
            const response = await fetch(`${API.baseUrl}/api/students/dashboard`, {
                headers: { Authorization: `Bearer ${token}` }
            });
            const result = await response.json();
            if (!response.ok) {
                throw new Error(result.detail || 'Unable to load attendance.');
            }
            attendance = result.attendance || { percentage: 0, present: 0, absent: 0, late: 0 };
            recentRecords = (result.recent_attendance || []).slice(0, 20);
        } catch (err) {
            error = err instanceof Error ? err.message : 'Unable to load attendance.';
        } finally {
            isLoading = false;
        }
    }

    $effect(() => {
        loadAttendance();
    });
</script>

<svelte:head>
    <title>Attendance | PaperBuddy</title>
</svelte:head>

<div class="attendance-page">
    <div class="page-header">
        <div>
            <h1>Attendance</h1>
            <p>Track your attendance and attendance history.</p>
        </div>
    </div>

    {#if error}
        <div class="error-box">{error}</div>
    {/if}

    <div class="summary-grid">
        <div class="summary-card">
            <div class="summary-icon">
                <TrendingUp size={21} />
            </div>
            <div>
                <span>Overall Attendance</span>
                <strong>{isLoading ? '…' : `${attendance.percentage}%`}</strong>
            </div>
        </div>

        <div class="summary-card">
            <div class="summary-icon present-icon">
                <CheckCircle2 size={21} />
            </div>
            <div>
                <span>Present Days</span>
                <strong>{isLoading ? '…' : attendance.present}</strong>
            </div>
        </div>

        <div class="summary-card">
            <div class="summary-icon absent-icon">
                <XCircle size={21} />
            </div>
            <div>
                <span>Absent Days</span>
                <strong>{isLoading ? '…' : attendance.absent}</strong>
            </div>
        </div>

        <div class="summary-card">
            <div class="summary-icon late-icon">
                <Clock3 size={21} />
            </div>
            <div>
                <span>Late Days</span>
                <strong>{isLoading ? '…' : attendance.late}</strong>
            </div>
        </div>
    </div>

    <section class="attendance-card">
        <div class="card-header">
            <div>
                <h2>Attendance Overview</h2>
                <p>Your current attendance performance</p>
            </div>
            <div class="percentage-badge">
                {isLoading ? '…' : `${attendance.percentage}%`}
            </div>
        </div>

        <div class="progress-section">
            <div class="progress-label">
                <span>Attendance Percentage</span>
                <strong>{isLoading ? '…' : `${attendance.percentage}%`}</strong>
            </div>
            <div class="progress-bar">
                <div class="progress-fill" style="width: {attendance.percentage}%;"></div>
            </div>
            <div class="attendance-note">
                <CalendarCheck size={16} />
                <span>
                    {attendance.percentage >= 75
                        ? 'Attendance is healthy.'
                        : 'Attendance is below 75%. Please attend classes regularly.'}
                </span>
            </div>
        </div>
    </section>

    <section class="attendance-card">
        <div class="card-header">
            <div>
                <h2>Attendance History</h2>
                <p>Recent date-wise attendance</p>
            </div>
        </div>

        {#if isLoading}
            <p class="empty-muted">Loading...</p>
        {:else if recentRecords.length === 0}
            <div class="empty-message">
                <CalendarCheck size={24} />
                <p>No attendance records available yet.</p>
                <span>Your date-wise attendance history will appear here.</span>
            </div>
        {:else}
            <table class="history-table">
                <thead>
                    <tr>
                        <th>Date</th>
                        <th>Status</th>
                    </tr>
                </thead>
                <tbody>
                    {#each recentRecords as record}
                        <tr>
                            <td>{record.date}</td>
                            <td>
                                <span class="status-pill status-{record.status.toLowerCase()}">
                                    {record.status.toUpperCase()}
                                </span>
                            </td>
                        </tr>
                    {/each}
                </tbody>
            </table>
        {/if}
    </section>
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

    .error-box {
        padding: 12px 16px;
        margin-bottom: 16px;
        background: #fef2f2;
        border: 1px solid #fecaca;
        border-radius: 10px;
        color: #b91c1c;
        font-size: 13px;
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

    .empty-muted {
        color: #94a3b8;
        font-size: 13px;
        text-align: center;
        padding: 20px 0;
    }

    .empty-message {
        display: flex;
        align-items: center;
        flex-direction: column;
        justify-content: center;
        min-height: 130px;
        padding: 25px 20px;
        color: #94a3b8;
        text-align: center;
    }

    .empty-message p {
        margin: 10px 0 4px;
        color: #64748b;
        font-size: 12px;
        font-weight: 600;
    }

    .empty-message span {
        max-width: 450px;
        color: #94a3b8;
        font-size: 11px;
        line-height: 1.5;
    }

    .history-table {
        width: 100%;
        border-collapse: collapse;
        font-size: 12px;
    }

    .history-table th,
    .history-table td {
        padding: 11px 12px;
        text-align: left;
        border-bottom: 1px solid #e2e8f0;
    }

    .history-table th {
        color: #64748b;
        font-size: 11px;
        text-transform: uppercase;
        letter-spacing: 0.4px;
    }

    .history-table td {
        color: #334155;
    }

    .status-pill {
        padding: 4px 10px;
        border-radius: 20px;
        font-size: 11px;
        font-weight: 700;
    }

    .status-present {
        background: #dcfce7;
        color: #15803d;
    }

    .status-absent,
    .status-leave {
        background: #fee2e2;
        color: #b91c1c;
    }

    .status-late {
        background: #fef3c7;
        color: #b45309;
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