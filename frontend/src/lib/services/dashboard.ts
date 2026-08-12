import { API } from '$lib/config/api';
import { apiFetch } from '$lib/services/apiClient';

export interface DashboardData {
	institution_name: string;
	students: number;
	teachers: number;
	parents: number;
	classes: number;
	departments: number;
}

export async function getDashboard(): Promise<DashboardData> {
	return apiFetch<DashboardData>(API.dashboard);
}