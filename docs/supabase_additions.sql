-- ============================================================
-- PaperBuddy: Additive migrations for certificates + substitutions
-- Safe to run multiple times (uses IF NOT EXISTS / DO blocks).
-- Does NOT modify or drop existing tables.
-- ============================================================

-- 1) Extend certificates table (additive)
ALTER TABLE certificates ADD COLUMN IF NOT EXISTS certificate_type TEXT;
ALTER TABLE certificates ADD COLUMN IF NOT EXISTS purpose TEXT;
ALTER TABLE certificates ADD COLUMN IF NOT EXISTS status TEXT DEFAULT 'pending';
ALTER TABLE certificates ADD COLUMN IF NOT EXISTS certificate_number TEXT;
ALTER TABLE certificates ADD COLUMN IF NOT EXISTS requested_by UUID REFERENCES users(id);
ALTER TABLE certificates ADD COLUMN IF NOT EXISTS approved_by UUID REFERENCES users(id);
ALTER TABLE certificates ADD COLUMN IF NOT EXISTS rejection_reason TEXT;
ALTER TABLE certificates ADD COLUMN IF NOT EXISTS reviewed_at TIMESTAMPTZ;

-- 2) Substitutions table (Smart Substitution)
CREATE TABLE IF NOT EXISTS substitutions (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    institution_id UUID REFERENCES institutions(id),
    leave_application_id UUID REFERENCES leave_applications(id),
    teacher_id UUID REFERENCES teachers(id),
    substitute_teacher_id UUID REFERENCES teachers(id),
    class_id UUID REFERENCES classes(id),
    subject_id UUID REFERENCES subjects(id),
    day_of_week TEXT,
    period INTEGER,
    status TEXT DEFAULT 'suggested',
    confirmed_by UUID REFERENCES users(id),
    created_at TIMESTAMPTZ DEFAULT now()
);

CREATE INDEX IF NOT EXISTS idx_substitutions_institution ON substitutions(institution_id);
CREATE INDEX IF NOT EXISTS idx_substitutions_leave ON substitutions(leave_application_id);

-- 3) Indexes on existing tables used by the new features
CREATE INDEX IF NOT EXISTS idx_certificates_student ON certificates(student_id);
CREATE INDEX IF NOT EXISTS idx_certificates_status ON certificates(status);
CREATE INDEX IF NOT EXISTS idx_library_transactions_status ON library_transactions(status);
CREATE INDEX IF NOT EXISTS idx_library_transactions_student ON library_transactions(student_id);