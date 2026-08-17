import { API } from '$lib/config/api';
import { apiFetch } from '$lib/services/apiClient';

export interface DocumentExtraction {
	document_type?: string;
	confidence?: number;
	data: Record<string, unknown>;
}

export interface ExtractResult {
	status: string;
	message: string;
	filename?: string;
	data?: DocumentExtraction;
}

export async function extractDocument(file: File): Promise<ExtractResult> {
	const form = new FormData();
	form.append('file', file);
	return apiFetch<ExtractResult>(`${API.baseUrl}/api/documents/extract`, {
		method: 'POST',
		body: form
	});
}

export async function saveDocument(payload: {
	file: File;
	institutionId: string;
	documentType: string;
	data: Record<string, unknown>;
	confidence?: number;
	uploadedBy?: string;
}): Promise<{ status: string; message: string; data?: unknown }> {
	const form = new FormData();
	form.append('file', payload.file);
	form.append('institution_id', payload.institutionId);
	form.append('document_type', payload.documentType);
	form.append('data', JSON.stringify(payload.data));
	if (payload.confidence !== undefined) {
		form.append('confidence', String(payload.confidence));
	}
	if (payload.uploadedBy) {
		form.append('uploaded_by', payload.uploadedBy);
	}
	return apiFetch(`${API.baseUrl}/api/documents/save`, {
		method: 'POST',
		body: form
	});
}