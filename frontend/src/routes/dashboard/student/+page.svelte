<script lang="ts">
    import StudentForm from './components/StudentForm.svelte';
    import AIDocumentReader from '$lib/components/AIDocumentReader.svelte';
</script>

<div class="student-page">

    <div class="page-header">
        <h1>Add Student</h1>
        <p>Create a student account.</p>
    </div>

    <div class="page-grid">
       <div class="student-form-section">
    <StudentForm />
</div>
        

        <div class="ai-reader-section">
            <AIDocumentReader />
        </div>

    </div>

</div>

<style>
    .student-page {
        max-width: 1450px;
        margin: 0 auto;
        padding: 40px 32px;
        background: #F8FAFC;
        min-height: 100vh;
        box-sizing: border-box;
    }

    .page-header {
        margin-bottom: 28px;
    }

    .page-header h1 {
        font-size: 30px;
        font-weight: 700;
        color: #0F172A;
        margin: 0 0 8px;
    }

    .page-header p {
        font-size: 15px;
        color: #64748B;
        margin: 0;
    }

    .page-grid {
        display: grid;
        grid-template-columns: 2fr 1fr;
        gap: 30px;
        align-items: start;
    }

    .student-form-section {
    width: 100%;
}  

    .ai-reader-section {
        width: 100%;
    }

    @media (max-width: 1000px) {
        .page-grid {
            grid-template-columns: 1fr;
        }
    }
</style>