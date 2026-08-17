import { API } from '$lib/config/api';

export async function apiFetch(path: string, options: RequestInit = {}) {
    const token = typeof localStorage === 'undefined' ? null : localStorage.getItem('access_token');
    const headers = new Headers(options.headers);
    if (token) headers.set('Authorization', `Bearer ${token}`);
    const response = await fetch(`${API.baseUrl}${path}`, { ...options, headers });
    if (!response.ok) {
        const body = await response.json().catch(() => ({}));
        throw new Error(body.detail || 'Request failed.');
    }
    return response;
}
