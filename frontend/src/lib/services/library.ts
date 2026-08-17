import { API } from '$lib/config/api';
import { apiFetch } from '$lib/services/apiClient';

export interface Book {
	id: string;
	institution_id?: string | null;
	title: string;
	author?: string | null;
	isbn?: string | null;
	total_copies?: number | null;
	available_copies?: number | null;
	created_at?: string | null;
}

export interface BookInput {
	title: string;
	author?: string;
	isbn?: string;
	total_copies: number;
	available_copies?: number;
}

export interface Transaction {
	id: string;
	student_id: string;
	book_id: string;
	institution_id?: string | null;
	issue_date?: string | null;
	due_date?: string | null;
	return_date?: string | null;
	status?: string | null;
	created_at?: string | null;
	book_title?: string | null;
	book_author?: string | null;
	student_name?: string | null;
	student_roll?: string | null;
	fine?: number | null;
	days_overdue?: number | null;
}

export interface LibraryStats {
	total_books: number;
	total_copies: number;
	available_copies: number;
	issued_books: number;
	overdue_books: number;
	active_borrowers: number;
}

const base = `${API.baseUrl}/api/library`;

export async function getBooks(search?: string): Promise<Book[]> {
	const qs = search ? `?search=${encodeURIComponent(search)}` : '';
	return apiFetch<Book[]>(`${base}/books${qs}`);
}

export async function createBook(data: BookInput): Promise<Book> {
	return apiFetch<Book>(`${base}/books`, {
		method: 'POST',
		body: JSON.stringify(data)
	});
}

export async function updateBook(id: string, data: Partial<BookInput>): Promise<Book> {
	return apiFetch<Book>(`${base}/books/${id}`, {
		method: 'PUT',
		body: JSON.stringify(data)
	});
}

export async function deleteBook(id: string): Promise<void> {
	await apiFetch(`${base}/books/${id}`, { method: 'DELETE' });
}

export async function borrowBook(studentId: string, bookId: string): Promise<Transaction> {
	const body: Record<string, string> = { book_id: bookId };
	if (studentId) {
		body.student_id = studentId;
	}
	return apiFetch<Transaction>(`${base}/borrow`, {
		method: 'POST',
		body: JSON.stringify(body)
	});
}

export async function returnBook(transactionId: string): Promise<Transaction> {
	return apiFetch<Transaction>(`${base}/return`, {
		method: 'POST',
		body: JSON.stringify({ transaction_id: transactionId })
	});
}

export async function getBorrowed(): Promise<Transaction[]> {
	return apiFetch<Transaction[]>(`${base}/borrowed`);
}

export async function getLibraryHistory(): Promise<Transaction[]> {
	return apiFetch<Transaction[]>(`${base}/history`);
}

export async function getOverdueBooks(): Promise<Transaction[]> {
	return apiFetch<Transaction[]>(`${base}/overdue`);
}

export async function getLibraryStats(): Promise<LibraryStats> {
	return apiFetch<LibraryStats>(`${base}/stats`);
}