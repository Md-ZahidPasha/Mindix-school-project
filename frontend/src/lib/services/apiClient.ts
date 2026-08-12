import { browser } from '$app/environment';

interface ApiOptions extends RequestInit {
	auth?: boolean;
}

export async function apiFetch<T>(
	url: string,
	options: ApiOptions = {}
): Promise<T> {
	const { auth = true, ...fetchOptions } = options;

	const headers = new Headers(fetchOptions.headers);

	if (!headers.has('Content-Type')) {
		headers.set('Content-Type', 'application/json');
	}

	if (auth && browser) {
		const token = localStorage.getItem('access_token');

		if (token) {
			headers.set('Authorization', `Bearer ${token}`);
		}
	}

	const response = await fetch(url, {
		...fetchOptions,
		headers
	});

	const contentType = response.headers.get('content-type');

	let data: unknown;

	if (contentType?.includes('application/json')) {
		data = await response.json();
	} else {
		data = await response.text();
	}

	if (!response.ok) {
		let message = `API request failed with status ${response.status}`;

		if (
			typeof data === 'object' &&
			data !== null &&
			'detail' in data
		) {
			message = String(
				(data as { detail: unknown }).detail
			);
		}

		throw new Error(message);
	}

	return data as T;
}