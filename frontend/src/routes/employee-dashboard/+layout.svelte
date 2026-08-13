<script lang="ts">
    import EmployeeSidebar from '$lib/components/employee/EmployeeSidebar.svelte';

    let { children } = $props();
</script>

<div class="employee-layout">

    <EmployeeSidebar />

    <main class="employee-content">
        {@render children()}
    </main>

</div>

<style>
    .employee-layout {
        min-height: 100vh;
        background: #f8fafc;
    }

    .employee-content {
        min-height: 100vh;
        margin-left: 280px;
    }

    @media (max-width: 1100px) {
        .employee-content {
            margin-left: 250px;
        }
    }

    @media (max-width: 800px) {
        .employee-content {
            margin-left: 0;
        }
    }
</style>