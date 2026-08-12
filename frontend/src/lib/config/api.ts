const BASE_URL = 'http://192.168.1.108:8000';

export const API = {
    baseUrl: BASE_URL,

    register: `${BASE_URL}/api/institution/register`,

    login: `${BASE_URL}/api/auth/login`,

    dashboard: `${BASE_URL}/api/dashboard`
};