import { API } from '$lib/config/api';
import { apiFetch } from '$lib/services/apiClient';

export interface SubstituteSuggestion {
	leave_application_id: string;
	teacher_id?: string | null;
	substitute_teacher_id: string;
	substitute_name: string;
	class_id: string;
	class_name?: string | null;
	subject_id?: string | null;
	subject_name?: string | null;
	day_of_week: string;
	period: number;
	score?: number | null;
	reason?: string | null;
}

export interface Substitution {
	id: string;
	institution_id?: string | null;
	leave_application_id?: string | null;
	teacher_id?: string | null;
	substitute_teacher_id?: string | null;
	class_id?: string | null;
	subject_id?: string | null;
	day_of_week?: string | null;
	period?: number | null;
	status?: string | null;
	confirmed_by?: string | null;
	created_at?: string | null;
	teacher_name?: string | null;
	substitute_name?: string | null;
	class_name?: string | null;
	subject_name?: string | null;
	leave_type?: string | null;
	leave_start?: string | null;
	leave_end?: string | null;
}

const base = `${API.baseUrl}/api/substitutions`;

export async function suggestSubstitutes(leaveApplicationId: string): Promise<SubstituteSuggestion[]> {
	return apiFetch<SubstituteSuggestion[]>(`${base}/suggest`, {
		method: 'POST',
		body: JSON.stringify({ leave_application_id: leaveApplicationId })
	});
}

export async function confirmSubstitution(data: {
	leave_application_id: string;
	teacher_id?: string;
	substitute_teacher_id: string;
	class_id: string;
	subject_id?: string;
	day_of_week: string;
	period: number;
}): Promise<Substitution> {
	return apiFetch<Substitution>(base, {
		method: 'POST',
		body: JSON.stringify(data)
	});
}

export async function getSubstitutions(status?: string): Promise<Substitution[]> {
	const qs = status ? `?status_filter=${encodeURIComponent(status)}` : '';
	return apiFetch<Substitution[]>(`${base}${qs}`);
}