import { API } from '$lib/config/api';
import { apiFetch } from '$lib/services/apiClient';

export interface ParentProfile {
	parent_id: string;
	user_id: string;
	institution_id: string;
	full_name?: string | null;
	email?: string | null;
	phone?: string | null;
}

export interface Child {
	id: string;
	student_id: string;
	full_name?: string | null;
	roll_number?: string | null;
	class_name?: string | null;
	attendance_present?: number | null;
	attendance_total?: number | null;
	attendance_percentage?: number | null;
}

export async function getParentProfile(): Promise<ParentProfile> {
	return apiFetch<ParentProfile>(`${API.baseUrl}/api/parents/me`);
}

export async function getMyChildren(): Promise<Child[]> {
	return apiFetch<Child[]>(`${API.baseUrl}/api/parents/me/children`);
}