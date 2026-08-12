import { API } from '$lib/config/api';

export interface InstitutionRegisterData {
	institution_name: string;
	institution_type: string;
	admin_name: string;
	email: string;
	phone: string;
	password: string;
}

export async function registerInstitution(
	data: InstitutionRegisterData
) {
	const response = await fetch(API.register, {
		method: 'POST',
		headers: {
			'Content-Type': 'application/json'
		},
		body: JSON.stringify(data)
	});

	const result = await response.json();

	if (!response.ok) {
		throw new Error(result.detail || 'Registration failed');
	}

	return result;
}