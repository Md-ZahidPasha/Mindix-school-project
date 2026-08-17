import { API } from '$lib/config/api';
import { apiFetch } from '$lib/services/apiClient';

const base = `${API.baseUrl}/api/students`;

interface StudentAttendance {
	percentage: number;
	present: number;
	absent: number;
	late: number;
	upcoming: number;
	pending: number;
}

interface DashboardTimetable {
	slots: {
		day?: string | null;
		period: number;
		subject: string;
		teacher: string;
		room?: string | null;
	}[];
}

export interface StudentDashboard {
	student: {
		name: string;
		class: string | null;
		section: string | null;
		roll_number: string;
		student_id: string;
	};
	attendance: StudentAttendance;
	timetable: DashboardTimetable;
}

export interface StudentProfile {
	student_id: string;
	full_name: string | null;
	email: string | null;
	phone: string | null;
	roll_number: string;
	admission_number: string | null;
	date_of_birth: string | null;
	gender: string | null;
	class_id: string | null;
	class_name: string | null;
	section: string | null;
	institution_id: string | null;
}

/* ================================
   STUDENT DASHBOARD
================================ */

export async function getDashboard(): Promise<StudentDashboard> {
	return apiFetch<StudentDashboard>(`${base}/dashboard`);
}

/* ================================
   STUDENT PROFILE
================================ */

export async function getProfile(): Promise<StudentProfile> {
	return apiFetch<StudentProfile>(`${base}/me`);
}

/* ================================
   ATTENDANCE
================================ */

export async function getAttendance(): Promise<StudentAttendance> {
	const dashboard = await getDashboard();
	return dashboard.attendance;
}

/* ================================
   TIMETABLE
================================ */

export async function getTimetable(): Promise<DashboardTimetable> {
	const dashboard = await getDashboard();
	return dashboard.timetable;
}