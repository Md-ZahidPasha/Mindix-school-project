<script lang="ts">
    import {
        CheckSquare,
        Clock3,
        CalendarDays,
        MapPin,
        User,
        AlertCircle,
        CheckCircle2,
        Circle,
        ListTodo,
        Info
    } from '@lucide/svelte';

    let selectedFilter = $state('All');

    const filters = [
        'All',
        'Pending',
        'In Progress',
        'Completed'
    ];

    const tasks = [
        {
            id: 1,
            title: 'Complete Morning School Route',
            description:
                'Pick up assigned students from Route A and safely reach the main campus.',
            category: 'Transport',
            priority: 'High',
            status: 'Completed',
            dueDate: '12 Aug 2026',
            dueTime: '09:15 AM',
            location: 'Route A - North Zone',
            assignedBy: 'Transport Manager'
        },
        {
            id: 2,
            title: 'Vehicle Safety Inspection',
            description:
                'Check tyres, brakes, lights, fuel level and emergency equipment before the next route.',
            category: 'Maintenance',
            priority: 'High',
            status: 'In Progress',
            dueDate: '12 Aug 2026',
            dueTime: '12:30 PM',
            location: 'School Garage',
            assignedBy: 'Transport Manager'
        },
        {
            id: 3,
            title: 'Staff Transport Duty',
            description:
                'Complete the assigned staff transportation duty according to the scheduled route.',
            category: 'Transport',
            priority: 'Medium',
            status: 'Pending',
            dueDate: '12 Aug 2026',
            dueTime: '11:30 AM',
            location: 'Admin Block',
            assignedBy: 'HR Department'
        },
        {
            id: 4,
            title: 'Afternoon School Route',
            description:
                'Drop assigned students safely at their designated locations after school hours.',
            category: 'Transport',
            priority: 'High',
            status: 'Pending',
            dueDate: '12 Aug 2026',
            dueTime: '05:15 PM',
            location: 'Route A - North Zone',
            assignedBy: 'Transport Manager'
        },
        {
            id: 5,
            title: 'Daily Vehicle Log Update',
            description:
                'Update the vehicle log with mileage, fuel usage and any issues noticed during the day.',
            category: 'Documentation',
            priority: 'Low',
            status: 'Pending',
            dueDate: '12 Aug 2026',
            dueTime: '05:30 PM',
            location: 'Transport Office',
            assignedBy: 'Transport Manager'
        },
        {
            id: 6,
            title: 'Weekly Vehicle Cleaning',
            description:
                'Complete the interior and exterior cleaning of the assigned school vehicle.',
            category: 'Maintenance',
            priority: 'Medium',
            status: 'Completed',
            dueDate: '11 Aug 2026',
            dueTime: '04:30 PM',
            location: 'School Garage',
            assignedBy: 'Transport Manager'
        },
        {
            id: 7,
            title: 'Emergency Contact List Verification',
            description:
                'Verify the emergency contact list for all students assigned to the transport route.',
            category: 'Documentation',
            priority: 'Medium',
            status: 'Completed',
            dueDate: '08 Aug 2026',
            dueTime: '02:00 PM',
            location: 'Transport Office',
            assignedBy: 'School Administration'
        }
    ];

    const filteredTasks = $derived(
        selectedFilter === 'All'
            ? tasks
            : tasks.filter((task) => task.status === selectedFilter)
    );

    const totalTasks = tasks.length;

    const completedTasks = tasks.filter(
        (task) => task.status === 'Completed'
    ).length;

    const pendingTasks = tasks.filter(
        (task) => task.status === 'Pending'
    ).length;

    const inProgressTasks = tasks.filter(
        (task) => task.status === 'In Progress'
    ).length;

    function getStatusClass(status: string) {
        if (status === 'Completed') return 'completed';
        if (status === 'In Progress') return 'progress';
        return 'pending';
    }

    function getPriorityClass(priority: string) {
        if (priority === 'High') return 'high';
        if (priority === 'Medium') return 'medium';
        return 'low';
    }
</script>

<svelte:head>
    <title>Tasks | Employee Dashboard</title>
</svelte:head>

<div class="tasks-page">

    <!-- HEADER -->
    <div class="page-header">

        <div class="title-row">

            <div class="title-icon">
                <CheckSquare size={24} />
            </div>

            <div>
                <h1>My Tasks</h1>

                <p>
                    View and manage your assigned tasks and duties.
                </p>
            </div>

        </div>

        <div class="employee-label">
            <User size={15} />
            Arjun Kumar
        </div>

    </div>


    <!-- SUMMARY -->
    <section class="stats-grid">

        <div class="stat-card">

            <div class="stat-icon blue">
                <ListTodo size={21} />
            </div>

            <div>
                <span>Total Tasks</span>
                <strong>{totalTasks}</strong>
            </div>

        </div>


        <div class="stat-card">

            <div class="stat-icon orange">
                <Clock3 size={21} />
            </div>

            <div>
                <span>Pending</span>
                <strong>{pendingTasks}</strong>
            </div>

        </div>


        <div class="stat-card">

            <div class="stat-icon purple">
                <AlertCircle size={21} />
            </div>

            <div>
                <span>In Progress</span>
                <strong>{inProgressTasks}</strong>
            </div>

        </div>


        <div class="stat-card">

            <div class="stat-icon green">
                <CheckCircle2 size={21} />
            </div>

            <div>
                <span>Completed</span>
                <strong>{completedTasks}</strong>
            </div>

        </div>

    </section>


    <!-- FILTERS -->
    <section class="filter-card">

        <div class="filter-title">

            <span>
                Filter Tasks
            </span>

            <small>
                {filteredTasks.length} tasks
            </small>

        </div>


        <div class="filters">

            {#each filters as filter}

                <button
                    type="button"
                    class:active={selectedFilter === filter}
                    onclick={() => selectedFilter = filter}
                >
                    {filter}
                </button>

            {/each}

        </div>

    </section>


    <!-- TASK LIST -->
    <section class="tasks-list">

        {#if filteredTasks.length > 0}

            {#each filteredTasks as task}

                <article class="task-card">

                    <!-- TASK STATUS ICON -->
                    <div class="task-check">

                        {#if task.status === 'Completed'}

                            <div class="check completed-check">
                                <CheckCircle2 size={20} />
                            </div>

                        {:else if task.status === 'In Progress'}

                            <div class="check progress-check">
                                <Clock3 size={20} />
                            </div>

                        {:else}

                            <div class="check pending-check">
                                <Circle size={20} />
                            </div>

                        {/if}

                    </div>


                    <!-- TASK CONTENT -->
                    <div class="task-content">

                        <div class="task-header">

                            <div>

                                <div class="task-title-row">

                                    <h2>
                                        {task.title}
                                    </h2>

                                    <span
                                        class={`priority ${getPriorityClass(task.priority)}`}
                                    >
                                        {task.priority}
                                    </span>

                                </div>

                                <span class="category">
                                    {task.category}
                                </span>

                            </div>


                            <span
                                class={`status ${getStatusClass(task.status)}`}
                            >
                                {#if task.status === 'Completed'}
                                    <CheckCircle2 size={12} />
                                {:else if task.status === 'In Progress'}
                                    <Clock3 size={12} />
                                {:else}
                                    <Circle size={12} />
                                {/if}

                                {task.status}
                            </span>

                        </div>


                        <p class="description">
                            {task.description}
                        </p>


                        <!-- TASK DETAILS -->
                        <div class="task-details">

                            <div>
                                <CalendarDays size={14} />
                                <span>
                                    {task.dueDate}
                                </span>
                            </div>

                            <div>
                                <Clock3 size={14} />
                                <span>
                                    {task.dueTime}
                                </span>
                            </div>

                            <div>
                                <MapPin size={14} />
                                <span>
                                    {task.location}
                                </span>
                            </div>

                            <div>
                                <User size={14} />
                                <span>
                                    {task.assignedBy}
                                </span>
                            </div>

                        </div>

                    </div>

                </article>

            {/each}

        {:else}

            <div class="empty-state">

                <div class="empty-icon">
                    <CheckSquare size={25} />
                </div>

                <h3>
                    No {selectedFilter} Tasks
                </h3>

                <p>
                    There are no tasks matching this filter.
                </p>

            </div>

        {/if}

    </section>


    <!-- INFORMATION -->
    <section class="information-note">

        <div class="information-icon">
            <Info size={18} />
        </div>

        <div>

            <strong>
                Task Information
            </strong>

            <p>
                Task information shown here is currently demo data.
                During API integration, assigned tasks, priorities,
                deadlines and completion status will be retrieved
                from the backend.
            </p>

        </div>

    </section>

</div>


<style>
    .tasks-page {
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


    /* STATS */

    .stats-grid {
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 14px;
        margin-bottom: 20px;
    }

    .stat-card {
        display: flex;
        align-items: center;
        gap: 11px;
        padding: 16px;
        border: 1px solid #e2e8f0;
        border-radius: 13px;
        background: white;
        box-shadow: 0 3px 12px rgba(15, 23, 42, 0.03);
    }

    .stat-icon {
        width: 40px;
        height: 40px;
        display: flex;
        align-items: center;
        justify-content: center;
        flex-shrink: 0;
        border-radius: 10px;
    }

    .stat-icon.blue {
        background: #eef4ff;
        color: #2563eb;
    }

    .stat-icon.orange {
        background: #fff7ed;
        color: #ea580c;
    }

    .stat-icon.purple {
        background: #f5f3ff;
        color: #7c3aed;
    }

    .stat-icon.green {
        background: #ecfdf5;
        color: #059669;
    }

    .stat-card span {
        display: block;
        color: #64748b;
        font-size: 9px;
    }

    .stat-card strong {
        display: block;
        margin-top: 2px;
        color: #0f172a;
        font-size: 19px;
    }


    /* FILTER */

    .filter-card {
        display: flex;
        align-items: center;
        justify-content: space-between;
        gap: 15px;
        padding: 15px 18px;
        margin-bottom: 18px;
        border: 1px solid #e2e8f0;
        border-radius: 13px;
        background: white;
    }

    .filter-title span {
        display: block;
        color: #334155;
        font-size: 11px;
        font-weight: 700;
    }

    .filter-title small {
        display: block;
        margin-top: 3px;
        color: #94a3b8;
        font-size: 8px;
    }

    .filters {
        display: flex;
        align-items: center;
        gap: 7px;
        flex-wrap: wrap;
    }

    .filters button {
        padding: 7px 11px;
        border: 1px solid #dbe3ef;
        border-radius: 7px;
        background: white;
        color: #64748b;
        font-size: 9px;
        font-weight: 600;
        cursor: pointer;
    }

    .filters button:hover {
        background: #f8fafc;
    }

    .filters button.active {
        border-color: #2563eb;
        background: #2563eb;
        color: white;
    }


    /* TASK LIST */

    .tasks-list {
        display: flex;
        flex-direction: column;
        gap: 12px;
        margin-bottom: 20px;
    }

    .task-card {
        display: flex;
        align-items: flex-start;
        gap: 15px;
        padding: 20px;
        border: 1px solid #e2e8f0;
        border-radius: 14px;
        background: white;
        box-shadow: 0 3px 12px rgba(15, 23, 42, 0.03);
        transition: 0.2s;
    }

    .task-card:hover {
        border-color: #cbd5e1;
        box-shadow: 0 5px 18px rgba(15, 23, 42, 0.05);
    }

    .task-check {
        flex-shrink: 0;
        padding-top: 2px;
    }

    .check {
        width: 38px;
        height: 38px;
        display: flex;
        align-items: center;
        justify-content: center;
        border-radius: 10px;
    }

    .completed-check {
        background: #ecfdf5;
        color: #059669;
    }

    .progress-check {
        background: #eff6ff;
        color: #2563eb;
    }

    .pending-check {
        background: #f8fafc;
        color: #94a3b8;
    }

    .task-content {
        flex: 1;
        min-width: 0;
    }

    .task-header {
        display: flex;
        align-items: flex-start;
        justify-content: space-between;
        gap: 15px;
    }

    .task-title-row {
        display: flex;
        align-items: center;
        gap: 8px;
        flex-wrap: wrap;
    }

    .task-title-row h2 {
        margin: 0;
        color: #0f172a;
        font-size: 14px;
    }

    .category {
        display: block;
        margin-top: 4px;
        color: #94a3b8;
        font-size: 8px;
    }

    .priority,
    .status {
        display: inline-flex;
        align-items: center;
        gap: 4px;
        padding: 4px 7px;
        border-radius: 6px;
        font-size: 7px;
        font-weight: 700;
        white-space: nowrap;
    }

    .priority.high {
        background: #fef2f2;
        color: #dc2626;
    }

    .priority.medium {
        background: #fff7ed;
        color: #ea580c;
    }

    .priority.low {
        background: #f1f5f9;
        color: #64748b;
    }

    .status.completed {
        background: #ecfdf5;
        color: #059669;
    }

    .status.progress {
        background: #eff6ff;
        color: #2563eb;
    }

    .status.pending {
        background: #f1f5f9;
        color: #64748b;
    }

    .description {
        margin: 10px 0 13px;
        color: #64748b;
        font-size: 10px;
        line-height: 1.5;
    }

    .task-details {
        display: flex;
        align-items: center;
        flex-wrap: wrap;
        gap: 14px;
        padding-top: 11px;
        border-top: 1px solid #f1f5f9;
    }

    .task-details div {
        display: flex;
        align-items: center;
        gap: 5px;
        color: #64748b;
        font-size: 9px;
    }


    /* EMPTY */

    .empty-state {
        padding: 55px 20px;
        border: 1px solid #e2e8f0;
        border-radius: 14px;
        background: white;
        text-align: center;
    }

    .empty-icon {
        width: 48px;
        height: 48px;
        display: flex;
        align-items: center;
        justify-content: center;
        margin: 0 auto 10px;
        border-radius: 50%;
        background: #f1f5f9;
        color: #94a3b8;
    }

    .empty-state h3 {
        margin: 0;
        color: #334155;
        font-size: 14px;
    }

    .empty-state p {
        margin: 5px 0 0;
        color: #94a3b8;
        font-size: 10px;
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

        .stats-grid {
            grid-template-columns: repeat(2, 1fr);
        }

        .filter-card {
            align-items: flex-start;
            flex-direction: column;
        }
    }


    @media (max-width: 700px) {

        .tasks-page {
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

        .stats-grid {
            grid-template-columns: 1fr;
        }

        .task-card {
            gap: 10px;
            padding: 15px;
        }

        .task-header {
            align-items: flex-start;
            flex-direction: column;
        }

        .task-details {
            align-items: flex-start;
            flex-direction: column;
            gap: 8px;
        }
    }
</style>