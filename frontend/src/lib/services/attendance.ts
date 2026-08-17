import { API } from '$lib/config/api';
import { apiFetch } from '$lib/services/apiClient';

export interface ScanLookupResult {
	student_id: string;
	code: string;
	roll_number?: string | null;
	full_name?: string | null;
	email?: string | null;
	class_name?: string | null;
	section?: string | null;
	attendance_date: string;
	already_marked: boolean;
	today_status?: string | null;
}

export interface ScanRecordResult {
	status: string;
	message: string;
	attendance_id: string;
	attendance_date: string;
	student?: {
		id: string;
		code?: string | null;
		full_name?: string | null;
	} | null;
}

const base = `${API.baseUrl}/api/attendance`;

export async function scanLookup(
	studentId: string,
	institutionId: string
): Promise<ScanLookupResult> {
	const qs = new URLSearchParams({
		student_id: studentId,
		institution_id: institutionId
	});
	return apiFetch<ScanLookupResult>(`${base}/scan/lookup?${qs.toString()}`);
}

export async function scanRecord(
	studentId: string,
	institutionId: string,
	classId?: string
): Promise<ScanRecordResult> {
	const qs = new URLSearchParams({ student_id: studentId, institution_id: institutionId });
	if (classId) {
		qs.set('class_id', classId);
	}
	return apiFetch<ScanRecordResult>(`${base}/scan?${qs.toString()}`, { method: 'POST' });
}