<script lang="ts">
    import ParentSidebar from '$lib/components/parent/ParentSidebar.svelte';

    let { children } = $props();
</script>

<div class="parent-layout">
    <ParentSidebar />

    <main class="main-content">
        {@render children()}
    </main>
</div>

<style>
    .parent-layout {
        display: flex;
        min-height: 100vh;
        width: 100%;
        background: #f7f9fc;
    }

    .main-content {
        flex: 1;
        min-width: 0;
        min-height: 100vh;
        overflow-x: hidden;
    }
</style>