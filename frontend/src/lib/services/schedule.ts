import { API } from '$lib/config/api';
import { apiFetch } from '$lib/services/apiClient';

export interface ScheduleClass {
	id: string;
	name: string;
	section?: string | null;
}

export interface ScheduleTeacher {
	id: string;
	name?: string | null;
}

export interface ScheduleSubject {
	id: string;
	name?: string | null;
}

export interface ScheduleEntry {
	id?: string | null;
	institution_id: string;
	class_id: string;
	class_name?: string | null;
	section?: string | null;
	subject_id?: string | null;
	subject_name: string;
	teacher_id?: string | null;
	teacher_name?: string | null;
	room_id?: string | null;
	room_name?: string | null;
	day: string;
	period: number;
	source?: string;
}

export interface GenerateRequest {
	class_ids?: string[] | null;
	working_days: string[];
	periods_per_day: number;
	sessions_per_week: number;
	persist: boolean;
}

export interface GenerateResult {
	status: string;
	message: string;
	generated: ScheduleEntry[];
	skipped: { class?: string; subject?: string | null; reason?: string }[];
	conflicts: number;
}

export interface ScheduleConflict {
	type: string;
	day: string;
	period: number;
	value: string;
	entries: string[];
}

const base = `${API.baseUrl}/api/schedule`;

export async function getScheduleClasses(): Promise<ScheduleClass[]> {
	return apiFetch<ScheduleClass[]>(`${base}/classes`);
}

export async function getScheduleTeachers(): Promise<ScheduleTeacher[]> {
	return apiFetch<ScheduleTeacher[]>(`${base}/teachers`);
}

export async function getScheduleSubjects(): Promise<ScheduleSubject[]> {
	return apiFetch<ScheduleSubject[]>(`${base}/subjects`);
}

export async function getTimetable(
	options: { class_id?: string; teacher_id?: string; day?: string } = {}
): Promise<ScheduleEntry[]> {
	const params = new URLSearchParams();
	if (options.class_id) params.set('class_id', options.class_id);
	if (options.teacher_id) params.set('teacher_id', options.teacher_id);
	if (options.day) params.set('day', options.day);
	const qs = params.toString();
	return apiFetch<ScheduleEntry[]>(`${base}${qs ? `?${qs}` : ''}`);
}

export async function getTimetableForClass(classId: string): Promise<ScheduleEntry[]> {
	return apiFetch<ScheduleEntry[]>(`${base}/class/${classId}`);
}

export async function getTimetableForTeacher(teacherId: string): Promise<ScheduleEntry[]> {
	return apiFetch<ScheduleEntry[]>(`${base}/teacher/${teacherId}`);
}

export async function getScheduleConflicts(): Promise<ScheduleConflict[]> {
	const result = await apiFetch<{ institution_id: string; conflicts: ScheduleConflict[] }>(
		`${base}/conflicts`
	);
	return result.conflicts;
}

export async function generateTimetable(request: GenerateRequest): Promise<GenerateResult> {
	return apiFetch<GenerateResult>(`${base}/generate`, {
		method: 'POST',
		body: JSON.stringify(request)
	});
}

export async function deleteScheduleEntry(entryId: string): Promise<void> {
	await apiFetch(`${base}/${entryId}`, { method: 'DELETE' });
}