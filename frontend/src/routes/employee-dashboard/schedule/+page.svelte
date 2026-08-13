<script lang="ts">
    import {
        CalendarDays,
        Clock3,
        MapPin,
        User,
        Car,
        ChevronLeft,
        ChevronRight,
        CalendarCheck,
        Info
    } from '@lucide/svelte';

    let selectedDate = $state('12');

    const weekDays = [
        {
            day: 'Mon',
            date: '10',
            month: 'Aug',
            fullDate: '10 Aug 2026'
        },
        {
            day: 'Tue',
            date: '11',
            month: 'Aug',
            fullDate: '11 Aug 2026'
        },
        {
            day: 'Wed',
            date: '12',
            month: 'Aug',
            fullDate: '12 Aug 2026'
        },
        {
            day: 'Thu',
            date: '13',
            month: 'Aug',
            fullDate: '13 Aug 2026'
        },
        {
            day: 'Fri',
            date: '14',
            month: 'Aug',
            fullDate: '14 Aug 2026'
        },
        {
            day: 'Sat',
            date: '15',
            month: 'Aug',
            fullDate: '15 Aug 2026'
        },
        {
            day: 'Sun',
            date: '16',
            month: 'Aug',
            fullDate: '16 Aug 2026'
        }
    ];

    const schedules = [
        {
            date: '10',
            day: 'Monday',
            dateLabel: '10 Aug 2026',
            title: 'Morning School Route',
            time: '07:30 AM - 09:15 AM',
            location: 'Main Campus',
            route: 'Route A - North Zone',
            passengers: '32 Students',
            type: 'School Route',
            status: 'Completed'
        },
        {
            date: '10',
            day: 'Monday',
            dateLabel: '10 Aug 2026',
            title: 'Afternoon School Route',
            time: '03:30 PM - 05:15 PM',
            location: 'Main Campus',
            route: 'Route A - North Zone',
            passengers: '32 Students',
            type: 'School Route',
            status: 'Completed'
        },
        {
            date: '11',
            day: 'Tuesday',
            dateLabel: '11 Aug 2026',
            title: 'Morning School Route',
            time: '07:30 AM - 09:15 AM',
            location: 'Main Campus',
            route: 'Route A - North Zone',
            passengers: '32 Students',
            type: 'School Route',
            status: 'Completed'
        },
        {
            date: '11',
            day: 'Tuesday',
            dateLabel: '11 Aug 2026',
            title: 'Vehicle Maintenance',
            time: '11:00 AM - 12:30 PM',
            location: 'School Garage',
            route: 'Vehicle Inspection',
            passengers: '—',
            type: 'Maintenance',
            status: 'Completed'
        },
        {
            date: '11',
            day: 'Tuesday',
            dateLabel: '11 Aug 2026',
            title: 'Afternoon School Route',
            time: '03:30 PM - 05:15 PM',
            location: 'Main Campus',
            route: 'Route A - North Zone',
            passengers: '32 Students',
            type: 'School Route',
            status: 'Completed'
        },
        {
            date: '12',
            day: 'Wednesday',
            dateLabel: '12 Aug 2026',
            title: 'Morning School Route',
            time: '07:30 AM - 09:15 AM',
            location: 'Main Campus',
            route: 'Route A - North Zone',
            passengers: '32 Students',
            type: 'School Route',
            status: 'Current'
        },
        {
            date: '12',
            day: 'Wednesday',
            dateLabel: '12 Aug 2026',
            title: 'Staff Transport',
            time: '10:30 AM - 11:30 AM',
            location: 'Admin Block',
            route: 'Staff Transport Route',
            passengers: '12 Staff',
            type: 'Staff Transport',
            status: 'Upcoming'
        },
        {
            date: '12',
            day: 'Wednesday',
            dateLabel: '12 Aug 2026',
            title: 'Afternoon School Route',
            time: '03:30 PM - 05:15 PM',
            location: 'Main Campus',
            route: 'Route A - North Zone',
            passengers: '32 Students',
            type: 'School Route',
            status: 'Upcoming'
        },
        {
            date: '13',
            day: 'Thursday',
            dateLabel: '13 Aug 2026',
            title: 'Morning School Route',
            time: '07:30 AM - 09:15 AM',
            location: 'Main Campus',
            route: 'Route A - North Zone',
            passengers: '32 Students',
            type: 'School Route',
            status: 'Upcoming'
        },
        {
            date: '13',
            day: 'Thursday',
            dateLabel: '13 Aug 2026',
            title: 'Afternoon School Route',
            time: '03:30 PM - 05:15 PM',
            location: 'Main Campus',
            route: 'Route A - North Zone',
            passengers: '32 Students',
            type: 'School Route',
            status: 'Upcoming'
        },
        {
            date: '14',
            day: 'Friday',
            dateLabel: '14 Aug 2026',
            title: 'Morning School Route',
            time: '07:30 AM - 09:15 AM',
            location: 'Main Campus',
            route: 'Route A - North Zone',
            passengers: '32 Students',
            type: 'School Route',
            status: 'Upcoming'
        },
        {
            date: '14',
            day: 'Friday',
            dateLabel: '14 Aug 2026',
            title: 'Afternoon School Route',
            time: '03:30 PM - 05:15 PM',
            location: 'Main Campus',
            route: 'Route A - North Zone',
            passengers: '32 Students',
            type: 'School Route',
            status: 'Upcoming'
        }
    ];

    const todaySchedules = schedules.filter(
        (schedule) => schedule.date === selectedDate
    );

    function previousWeek() {
        alert('Previous week will be connected to the calendar API later.');
    }

    function nextWeek() {
        alert('Next week will be connected to the calendar API later.');
    }
</script>

<svelte:head>
    <title>My Schedule | Employee Dashboard</title>
</svelte:head>

<div class="schedule-page">

    <!-- HEADER -->
    <div class="page-header">

        <div class="title-row">

            <div class="title-icon">
                <CalendarDays size={24} />
            </div>

            <div>
                <h1>My Schedule</h1>

                <p>
                    View your daily routes, duties and scheduled activities.
                </p>
            </div>

        </div>

        <div class="week-navigation">

            <button
                type="button"
                onclick={previousWeek}
                aria-label="Previous week"
            >
                <ChevronLeft size={17} />
            </button>

            <strong>
                10 - 16 August 2026
            </strong>

            <button
                type="button"
                onclick={nextWeek}
                aria-label="Next week"
            >
                <ChevronRight size={17} />
            </button>

        </div>

    </div>


    <!-- EMPLOYEE INFO -->
    <section class="employee-info">

        <div class="employee-avatar">
            A
        </div>

        <div class="employee-details">

            <h2>Arjun Kumar</h2>

            <p>
                Employee ID:
                <strong>EMP001</strong>

                <span>•</span>

                Driving Department

                <span>•</span>

                Driver
            </p>

        </div>

        <div class="today-card">

            <span>Today's Duties</span>

            <strong>
                {todaySchedules.length}
            </strong>

        </div>

    </section>


    <!-- WEEK SELECTOR -->
    <section class="week-selector">

        {#each weekDays as day}

            <button
                type="button"
                class:active={selectedDate === day.date}
                class="day-selector"
                onclick={() => selectedDate = day.date}
            >

                <span>
                    {day.day}
                </span>

                <strong>
                    {day.date}
                </strong>

                <small>
                    {day.month}
                </small>

            </button>

        {/each}

    </section>


    <!-- SELECTED DAY -->
    <section class="selected-day-header">

        <div>

            <h2>
                Schedule for
                {weekDays.find((day) => day.date === selectedDate)?.fullDate}
            </h2>

            <p>
                Your assigned duties and activities for the selected day.
            </p>

        </div>

        <span class="duty-count">
            {todaySchedules.length} Activities
        </span>

    </section>


    <!-- SCHEDULE CARDS -->
    <section class="schedule-list">

        {#if todaySchedules.length > 0}

            {#each todaySchedules as schedule}

                <article class="schedule-card">

                    <div class="time-column">

                        <strong>
                            {schedule.time.split(' - ')[0]}
                        </strong>

                        <span>
                            {schedule.time.split(' - ')[1]}
                        </span>

                    </div>


                    <div class="timeline-line">

                        <div
                            class:current-dot={schedule.status === 'Current'}
                            class="timeline-dot"
                        ></div>

                    </div>


                    <div class="schedule-content">

                        <div class="schedule-top">

                            <div>

                                <div class="schedule-title-row">

                                    {#if schedule.type === 'School Route'}

                                        <div class="schedule-icon blue">
                                            <Car size={18} />
                                        </div>

                                    {:else if schedule.type === 'Maintenance'}

                                        <div class="schedule-icon orange">
                                            <CalendarCheck size={18} />
                                        </div>

                                    {:else}

                                        <div class="schedule-icon purple">
                                            <User size={18} />
                                        </div>

                                    {/if}

                                    <div>

                                        <h3>
                                            {schedule.title}
                                        </h3>

                                        <span class="type-label">
                                            {schedule.type}
                                        </span>

                                    </div>

                                </div>

                            </div>


                            {#if schedule.status === 'Completed'}

                                <span class="status completed">
                                    Completed
                                </span>

                            {:else if schedule.status === 'Current'}

                                <span class="status current">
                                    Current
                                </span>

                            {:else}

                                <span class="status upcoming">
                                    Upcoming
                                </span>

                            {/if}

                        </div>


                        <div class="schedule-details">

                            <div>
                                <Clock3 size={14} />
                                <span>{schedule.time}</span>
                            </div>

                            <div>
                                <MapPin size={14} />
                                <span>{schedule.location}</span>
                            </div>

                            <div>
                                <Car size={14} />
                                <span>{schedule.route}</span>
                            </div>

                            {#if schedule.passengers !== '—'}

                                <div>
                                    <User size={14} />
                                    <span>{schedule.passengers}</span>
                                </div>

                            {/if}

                        </div>

                    </div>

                </article>

            {/each}

        {:else}

            <div class="empty-state">

                <div class="empty-icon">
                    <CalendarDays size={25} />
                </div>

                <h3>
                    No Schedule
                </h3>

                <p>
                    There are no scheduled activities for this day.
                </p>

            </div>

        {/if}

    </section>


    <!-- WEEK SUMMARY -->
    <section class="summary-grid">

        <div class="summary-card">

            <div class="summary-icon blue">
                <CalendarDays size={20} />
            </div>

            <div>

                <span>Total Activities</span>

                <strong>
                    {schedules.length}
                </strong>

                <small>
                    This week
                </small>

            </div>

        </div>


        <div class="summary-card">

            <div class="summary-icon green">
                <CalendarCheck size={20} />
            </div>

            <div>

                <span>Completed</span>

                <strong>
                    {schedules.filter((schedule) =>
                        schedule.status === 'Completed'
                    ).length}
                </strong>

                <small>
                    Activities completed
                </small>

            </div>

        </div>


        <div class="summary-card">

            <div class="summary-icon orange">
                <Clock3 size={20} />
            </div>

            <div>

                <span>Upcoming</span>

                <strong>
                    {schedules.filter((schedule) =>
                        schedule.status === 'Upcoming'
                    ).length}
                </strong>

                <small>
                    Remaining activities
                </small>

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
                Schedule Information
            </strong>

            <p>
                Schedule information shown here is currently demo data.
                During API integration, your assigned routes, duties,
                timings, locations and activities will be loaded from
                the backend.
            </p>

        </div>

    </section>

</div>


<style>
    .schedule-page {
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


    /* WEEK NAVIGATION */

    .week-navigation {
        display: flex;
        align-items: center;
        gap: 12px;
        padding: 7px;
        border: 1px solid #dbe3ef;
        border-radius: 10px;
        background: white;
    }

    .week-navigation strong {
        min-width: 145px;
        color: #334155;
        font-size: 10px;
        text-align: center;
    }

    .week-navigation button {
        width: 30px;
        height: 30px;
        display: flex;
        align-items: center;
        justify-content: center;
        border: 1px solid #e2e8f0;
        border-radius: 7px;
        background: white;
        color: #64748b;
        cursor: pointer;
    }

    .week-navigation button:hover {
        background: #eff6ff;
        border-color: #bfdbfe;
        color: #2563eb;
    }


    /* EMPLOYEE INFO */

    .employee-info {
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

    .employee-avatar {
        width: 54px;
        height: 54px;
        display: flex;
        align-items: center;
        justify-content: center;
        flex-shrink: 0;
        border-radius: 50%;
        background: #2563eb;
        color: white;
        font-size: 20px;
        font-weight: 800;
    }

    .employee-details {
        flex: 1;
    }

    .employee-details h2 {
        margin: 0;
        color: #0f172a;
        font-size: 17px;
    }

    .employee-details p {
        margin: 5px 0 0;
        color: #64748b;
        font-size: 11px;
    }

    .employee-details strong {
        color: #334155;
    }

    .employee-details p span {
        margin: 0 7px;
        color: #cbd5e1;
    }

    .today-card {
        min-width: 110px;
        padding: 11px 15px;
        border-radius: 10px;
        background: #eef4ff;
        text-align: center;
    }

    .today-card span {
        display: block;
        color: #64748b;
        font-size: 9px;
    }

    .today-card strong {
        display: block;
        margin-top: 2px;
        color: #2563eb;
        font-size: 19px;
    }


    /* WEEK SELECTOR */

    .week-selector {
        display: grid;
        grid-template-columns: repeat(7, 1fr);
        gap: 9px;
        padding: 10px;
        margin-bottom: 25px;
        border: 1px solid #e2e8f0;
        border-radius: 14px;
        background: white;
        box-shadow: 0 3px 12px rgba(15, 23, 42, 0.03);
    }

    .day-selector {
        min-height: 76px;
        display: flex;
        align-items: center;
        justify-content: center;
        flex-direction: column;
        gap: 3px;
        border: 1px solid transparent;
        border-radius: 10px;
        background: transparent;
        color: #64748b;
        cursor: pointer;
    }

    .day-selector:hover {
        background: #f8fafc;
    }

    .day-selector span {
        font-size: 9px;
        font-weight: 600;
    }

    .day-selector strong {
        color: #0f172a;
        font-size: 20px;
    }

    .day-selector small {
        font-size: 8px;
        color: #94a3b8;
    }

    .day-selector.active {
        background: #2563eb;
        color: white;
        border-color: #2563eb;
        box-shadow: 0 7px 18px rgba(37, 99, 235, 0.18);
    }

    .day-selector.active strong,
    .day-selector.active small {
        color: white;
    }


    /* SELECTED DAY */

    .selected-day-header {
        display: flex;
        align-items: center;
        justify-content: space-between;
        gap: 15px;
        margin-bottom: 15px;
    }

    .selected-day-header h2 {
        margin: 0;
        color: #0f172a;
        font-size: 18px;
    }

    .selected-day-header p {
        margin: 4px 0 0;
        color: #64748b;
        font-size: 10px;
    }

    .duty-count {
        padding: 6px 9px;
        border-radius: 7px;
        background: #eef4ff;
        color: #2563eb;
        font-size: 9px;
        font-weight: 700;
        white-space: nowrap;
    }


    /* SCHEDULE */

    .schedule-list {
        display: flex;
        flex-direction: column;
        gap: 12px;
        margin-bottom: 20px;
    }

    .schedule-card {
        display: grid;
        grid-template-columns: 115px 25px 1fr;
        padding: 18px 20px;
        border: 1px solid #e2e8f0;
        border-radius: 14px;
        background: white;
        box-shadow: 0 3px 12px rgba(15, 23, 42, 0.03);
    }

    .time-column {
        padding-top: 2px;
    }

    .time-column strong {
        display: block;
        color: #334155;
        font-size: 12px;
    }

    .time-column span {
        display: block;
        margin-top: 3px;
        color: #94a3b8;
        font-size: 9px;
    }

    .timeline-line {
        position: relative;
        display: flex;
        justify-content: center;
    }

    .timeline-line::after {
        content: '';
        position: absolute;
        top: 8px;
        bottom: -18px;
        width: 1px;
        background: #e2e8f0;
    }

    .schedule-card:last-child .timeline-line::after {
        display: none;
    }

    .timeline-dot {
        width: 9px;
        height: 9px;
        margin-top: 5px;
        z-index: 1;
        border: 3px solid #dbeafe;
        border-radius: 50%;
        background: #2563eb;
        box-sizing: content-box;
    }

    .timeline-dot.current-dot {
        border-color: #bfdbfe;
        background: #2563eb;
        box-shadow: 0 0 0 4px #eff6ff;
    }

    .schedule-content {
        min-width: 0;
        padding-left: 5px;
    }

    .schedule-top {
        display: flex;
        align-items: flex-start;
        justify-content: space-between;
        gap: 15px;
    }

    .schedule-title-row {
        display: flex;
        align-items: center;
        gap: 10px;
    }

    .schedule-icon {
        width: 38px;
        height: 38px;
        display: flex;
        align-items: center;
        justify-content: center;
        flex-shrink: 0;
        border-radius: 9px;
    }

    .schedule-icon.blue {
        background: #eef4ff;
        color: #2563eb;
    }

    .schedule-icon.orange {
        background: #fff7ed;
        color: #ea580c;
    }

    .schedule-icon.purple {
        background: #f5f3ff;
        color: #7c3aed;
    }

    .schedule-title-row h3 {
        margin: 0;
        color: #0f172a;
        font-size: 14px;
    }

    .type-label {
        display: block;
        margin-top: 3px;
        color: #94a3b8;
        font-size: 8px;
    }

    .status {
        padding: 5px 8px;
        border-radius: 7px;
        font-size: 8px;
        font-weight: 700;
        white-space: nowrap;
    }

    .status.completed {
        background: #ecfdf5;
        color: #059669;
    }

    .status.current {
        background: #eff6ff;
        color: #2563eb;
    }

    .status.upcoming {
        background: #f1f5f9;
        color: #64748b;
    }

    .schedule-details {
        display: flex;
        align-items: center;
        flex-wrap: wrap;
        gap: 14px;
        margin-top: 14px;
        padding-top: 12px;
        border-top: 1px solid #f1f5f9;
    }

    .schedule-details div {
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
        font-size: 19px;
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

        .week-selector {
            grid-template-columns: repeat(4, 1fr);
        }

        .summary-grid {
            grid-template-columns: 1fr;
        }
    }


    @media (max-width: 700px) {

        .schedule-page {
            padding: 18px;
        }

        .page-header {
            align-items: flex-start;
            flex-direction: column;
        }

        .week-navigation {
            width: 100%;
            box-sizing: border-box;
            justify-content: space-between;
        }

        .employee-info {
            align-items: flex-start;
            flex-wrap: wrap;
        }

        .today-card {
            width: 100%;
        }

        .week-selector {
            grid-template-columns: repeat(2, 1fr);
        }

        .selected-day-header {
            align-items: flex-start;
            flex-direction: column;
        }

        .schedule-card {
            grid-template-columns: 85px 18px 1fr;
            padding: 15px;
        }

        .schedule-top {
            align-items: flex-start;
            flex-direction: column;
        }

        .schedule-details {
            align-items: flex-start;
            flex-direction: column;
            gap: 8px;
        }
    }
</style>