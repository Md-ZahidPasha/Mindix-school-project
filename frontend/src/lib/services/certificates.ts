import { API } from '$lib/config/api';
import { apiFetch } from '$lib/services/apiClient';

export interface Certificate {
	id: string;
	student_id: string;
	institution_id?: string | null;
	requested_by?: string | null;
	certificate_name: string;
	certificate_type?: string | null;
	purpose?: string | null;
	status?: string | null;
	certificate_number?: string | null;
	approved_by?: string | null;
	rejection_reason?: string | null;
	issue_date?: string | null;
	reviewed_at?: string | null;
	created_at?: string | null;
	student_name?: string | null;
	student_roll?: string | null;
	class_name?: string | null;
	section?: string | null;
	institution_name?: string | null;
}

export interface CertificateCreate {
	student_id: string;
	institution_id: string;
	certificate_name: string;
	certificate_type?: string;
	purpose?: string;
}

const base = `${API.baseUrl}/api/certificates`;

export async function getCertificates(status?: string): Promise<Certificate[]> {
	const qs = status ? `?status_filter=${encodeURIComponent(status)}` : '';
	return apiFetch<Certificate[]>(`${base}${qs}`);
}

export async function getCertificate(id: string): Promise<Certificate> {
	return apiFetch<Certificate>(`${base}/${id}`);
}

export async function requestCertificate(data: CertificateCreate): Promise<Certificate> {
	return apiFetch<Certificate>(base, {
		method: 'POST',
		body: JSON.stringify(data)
	});
}

export async function reviewCertificate(
	id: string,
	data: { status: string; rejection_reason?: string; certificate_number?: string; issue_date?: string }
): Promise<Certificate> {
	return apiFetch<Certificate>(`${base}/${id}/status`, {
		method: 'PUT',
		body: JSON.stringify(data)
	});
}