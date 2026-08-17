-- Safe additive migration for PaperBuddy face attendance.
-- Run once against the EXISTING Supabase Postgres database. It does not modify
-- or delete current tables or records.
CREATE TABLE IF NOT EXISTS public.student_face_profiles (
    student_id uuid PRIMARY KEY REFERENCES public.students(id) ON DELETE CASCADE,
    institution_id uuid NOT NULL REFERENCES public.institutions(id),
    embedding jsonb NOT NULL,
    created_at timestamptz NOT NULL DEFAULT now(),
    updated_at timestamptz NOT NULL DEFAULT now()
);
CREATE INDEX IF NOT EXISTS idx_student_face_profiles_institution
    ON public.student_face_profiles (institution_id);
