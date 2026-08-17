import { API } from '$lib/config/api';
import { apiFetch } from '$lib/services/apiClient';

export interface LeaveApplication {
	id: string;
	user_id: string;
	leave_type: string;
	start_date: string;
	end_date: string;
	reason?: string | null;
	status?: string | null;
	created_at?: string | null;
	institution_id?: string | null;
	employee_id?: string | null;
}

export interface LeaveCreate {
	user_id: string;
	institution_id: string;
	employee_id?: string;
	leave_type: string;
	start_date: string;
	end_date: string;
	reason?: string;
}

export interface LeaveUpdate {
	leave_type?: string;
	start_date?: string;
	end_date?: string;
	reason?: string;
	status?: string;
}

const base = `${API.baseUrl}/api/leave-applications`;

export async function getLeaveApplications(
	institutionId: string,
	employeeId?: string
): Promise<LeaveApplication[]> {
	const params = new URLSearchParams({ institution_id: institutionId });
	if (employeeId) params.set('employee_id', employeeId);
	return apiFetch<LeaveApplication[]>(`${base}?${params.toString()}`);
}

export async function createLeaveApplication(data: LeaveCreate): Promise<LeaveApplication> {
	return apiFetch<LeaveApplication>(base, {
		method: 'POST',
		body: JSON.stringify(data)
	});
}

export async function updateLeaveApplication(
	leaveId: string,
	institutionId: string,
	data: LeaveUpdate
): Promise<LeaveApplication> {
	return apiFetch<LeaveApplication>(
		`${base}/${leaveId}?institution_id=${encodeURIComponent(institutionId)}`,
		{
			method: 'PUT',
			body: JSON.stringify(data)
		}
	);
}