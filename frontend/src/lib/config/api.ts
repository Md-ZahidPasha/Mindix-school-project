const BASE_URL = (import.meta.env.PUBLIC_API_BASE_URL || 'http://127.0.0.1:8000').replace(/\/$/, '');

export const API = {
    baseUrl: BASE_URL,

    register: `${BASE_URL}/api/institution/register`,

    login: `${BASE_URL}/api/auth/login`,

    dashboard: `${BASE_URL}/api/dashboard`,
    aiChat: `${BASE_URL}/api/ai/chat`,
    documentExtract: `${BASE_URL}/api/documents/extract`
};
