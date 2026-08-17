import { API } from '$lib/config/api';
import { apiFetch } from '$lib/services/apiClient';

const base = `${API.baseUrl}/api/teachers`;

export interface TeacherProfile {
	id: string;
	user_id: string;
	full_name: string | null;
	email: string | null;
	phone: string | null;
	department_id: string | null;
	qualification: string | null;
	specialization: string | null;
	joining_date: string | null;
	institution_id: string | null;
	subject_ids: string[];
}

export interface TeacherClass {
	id: string;
	class_name: string;
	section: string | null;
	student_count: number;
}

export interface TeacherStudent {
	id: string;
	student_id: string;
	roll_number: string;
	full_name: string;
	email: string;
	class_id: string;
	class_name: string;
	section: string;
}

export interface TeacherScheduleSlot {
	day: string;
	period: number;
	subject: string;
	class_name: string;
	section: string | null;
	room: string | null;
}

export interface TeacherDashboard {
	teacher: {
		id: string;
		user_id: string;
		full_name: string;
		email: string | null;
		phone: string | null;
		qualification: string | null;
		specialization: string | null;
		joining_date: string | null;
	};
	stats: {
		classes: number;
		students: number;
		today_classes: number;
	};
	today_schedule: {
		period: number;
		subject: string;
		class_name: string;
		section: string | null;
		room: string | null;
	}[];
	attendance: {
		percentage: number;
		present: number;
		absent: number;
		total: number;
	};
	leave_requests: {
		id: string;
		leave_type: string;
		start_date: string;
		end_date: string;
		status: string;
	}[];
}

/* ================================
   TEACHER PROFILE
================================ */

export async function getTeacherProfile(): Promise<TeacherProfile> {
	return apiFetch<TeacherProfile>(`${base}/me`);
}

/* ================================
   TEACHER DASHBOARD
================================ */

export async function getTeacherDashboard(): Promise<TeacherDashboard> {
	return apiFetch<TeacherDashboard>(`${base}/me/dashboard`);
}

/* ================================
   TEACHER CLASSES
================================ */

export async function getTeacherClasses(): Promise<TeacherClass[]> {
	return apiFetch<TeacherClass[]>(`${base}/me/classes`);
}

/* ================================
   TEACHER STUDENTS
================================ */

export async function getTeacherStudents(): Promise<TeacherStudent[]> {
	return apiFetch<TeacherStudent[]>(`${base}/me/students`);
}

/* ================================
   TEACHER TIMETABLE
================================ */

export async function getTeacherTimetable(): Promise<TeacherScheduleSlot[]> {
	return apiFetch<TeacherScheduleSlot[]>(`${base}/me/timetable`);
}