const BASE_URL = 'http://127.0.0.1:8000';

export const API = {
    baseUrl: BASE_URL,

    register: `${BASE_URL}/api/institution/register`,

    login: `${BASE_URL}/api/auth/login`,

    dashboard: `${BASE_URL}/api/dashboard`
};