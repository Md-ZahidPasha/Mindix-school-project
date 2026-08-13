const API_BASE_URL = 'http://localhost:5000/api';

async function apiRequest(
    endpoint: string,
    options: RequestInit = {}
) {
    const response = await fetch(`${API_BASE_URL}${endpoint}`, {
        ...options,
        headers: {
            'Content-Type': 'application/json',
            ...(options.headers || {})
        },
        credentials: 'include'
    });

    if (!response.ok) {
        throw new Error(
            `API request failed: ${response.status} ${response.statusText}`
        );
    }

    return response.json();
}


/* ================================
   STUDENT DASHBOARD
================================ */

export async function getDashboard() {
    return apiRequest('/students/dashboard');
}


/* ================================
   STUDENT PROFILE
================================ */

export async function getProfile() {
    return apiRequest('/students/me');
}


/* ================================
   ATTENDANCE
================================ */

export async function getAttendance() {
    return apiRequest('/students/attendance');
}


/* ================================
   TIMETABLE
================================ */

export async function getTimetable() {
    return apiRequest('/students/timetable');
}


/* ================================
   ASSIGNMENTS
================================ */

export async function getAssignments() {
    return apiRequest('/students/assignments');
}


/* ================================
   EXAMS
================================ */

export async function getExams() {
    return apiRequest('/students/exams');
}


/* ================================
   RESULTS
================================ */

export async function getResults() {
    return apiRequest('/students/results');
}


/* ================================
   FEES
================================ */

export async function getFees() {
    return apiRequest('/students/fees');
}


/* ================================
   CERTIFICATES
================================ */

export async function getCertificates() {
    return apiRequest('/students/certificates');
}


/* ================================
   LIBRARY
================================ */

export async function getLibrary() {
    return apiRequest('/students/library');
}


/* ================================
   NOTIFICATIONS
================================ */

export async function getNotifications() {
    return apiRequest('/students/notifications');
}