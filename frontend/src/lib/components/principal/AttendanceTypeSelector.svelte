<script lang="ts">
    import {
        Users,
        GraduationCap,
        BriefcaseBusiness,
        QrCode,
        Check
    } from '@lucide/svelte';

    type AttendanceType = 'students' | 'teachers' | 'employees' | 'qr';

    let {
        selectedType = $bindable<AttendanceType>()
    } = $props<{
        selectedType: AttendanceType;
    }>();
</script>


<div class="selector">

    <!-- STUDENTS -->

    <button
        type="button"
        class:active={selectedType === 'students'}
        class="type-card"
        onclick={() => selectedType = 'students'}
    >

        <div class="icon-box">
            <Users size={20} />
        </div>

        <span>Students</span>

        {#if selectedType === 'students'}
            <div class="check">
                <Check size={15} />
            </div>
        {/if}

    </button>


    <!-- TEACHERS -->

    <button
        type="button"
        class:active={selectedType === 'teachers'}
        class="type-card"
        onclick={() => selectedType = 'teachers'}
    >

        <div class="icon-box">
            <GraduationCap size={20} />
        </div>

        <span>Teachers</span>

        {#if selectedType === 'teachers'}
            <div class="check">
                <Check size={15} />
            </div>
        {/if}

    </button>


    <!-- EMPLOYEES -->

    <button
        type="button"
        class:active={selectedType === 'employees'}
        class="type-card"
        onclick={() => selectedType = 'employees'}
    >

        <div class="icon-box">
            <BriefcaseBusiness size={20} />
        </div>

        <span>Employees / Staff</span>

        {#if selectedType === 'employees'}
            <div class="check">
                <Check size={15} />
            </div>
        {/if}

    </button>


    <!-- QR / STUDENT ID -->

    <button
        type="button"
        class:active={selectedType === 'qr'}
        class="type-card"
        onclick={() => selectedType = 'qr'}
    >

        <div class="icon-box">
            <QrCode size={20} />
        </div>

        <span>QR / Student-ID</span>

        {#if selectedType === 'qr'}
            <div class="check">
                <Check size={15} />
            </div>
        {/if}

    </button>

</div>


<style lang="scss">

.selector {
    display: grid;

    grid-template-columns:
        repeat(4, 1fr);

    gap: 16px;

    margin-bottom: 28px;
}


.type-card {
    position: relative;

    display: flex;

    align-items: center;

    gap: 14px;

    width: 100%;

    min-height: 82px;

    padding: 18px;

    box-sizing: border-box;

    border: 1px solid #e5eaf2;

    border-radius: 16px;

    background: white;

    color: #14213d;

    font-size: 15px;

    font-weight: 600;

    text-align: left;

    cursor: pointer;

    transition:
        border-color 0.2s,
        box-shadow 0.2s,
        background 0.2s;
}


.type-card:hover {
    border-color: #b9cdf7;

    box-shadow:
        0 4px 14px
        rgba(37, 99, 235, 0.08);
}


.type-card.active {
    border-color: #2563eb;

    box-shadow:
        0 0 0 1px #2563eb,
        0 6px 18px
        rgba(37, 99, 235, 0.08);

    background: #ffffff;
}


.icon-box {
    width: 48px;

    height: 48px;

    display: flex;

    align-items: center;

    justify-content: center;

    flex-shrink: 0;

    border-radius: 12px;

    background: #eef4ff;

    color: #2563eb;
}


.type-card span {
    color: #14213d;
}


.check {
    position: absolute;

    top: 14px;

    right: 14px;

    width: 22px;

    height: 22px;

    display: flex;

    align-items: center;

    justify-content: center;

    border-radius: 50%;

    background: #2563eb;

    color: white;
}


@media (max-width: 800px) {

    .selector {
        grid-template-columns: 1fr;
    }

}
</style>