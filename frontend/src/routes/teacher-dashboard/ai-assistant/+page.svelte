<script lang="ts">
	import { Bot, Send, Sparkles, GraduationCap, CalendarDays, BookOpen } from '@lucide/svelte';
	import { API } from '$lib/config/api';

	let message = $state('');
	let isLoading = $state(false);
	let error = $state('');
	type ChatMessage = { sender: 'user' | 'assistant'; text: string };
	let messages = $state<ChatMessage[]>([]);

	async function sendMessage() {
		if (!message.trim()) return;
		const question = message.trim();
		const token = localStorage.getItem('access_token');
		if (!token) {
			error = 'Please sign in again to use the AI Assistant.';
			return;
		}
		messages.push({ sender: 'user', text: question });
		message = '';
		isLoading = true;
		error = '';
		try {
			const response = await fetch(API.aiChat, {
				method: 'POST',
				headers: {
					'Content-Type': 'application/json',
					Authorization: `Bearer ${token}`
				},
				body: JSON.stringify({ message: question })
			});
			const result = await response.json();
			if (!response.ok) {
				throw new Error(result.detail || 'The assistant could not respond.');
			}
			messages.push({ sender: 'assistant', text: result.answer });
		} catch (err) {
			error = err instanceof Error ? err.message : 'Unable to reach the AI Assistant.';
		} finally {
			isLoading = false;
		}
	}

	function usePrompt(prompt: string) {
		message = prompt;
	}
</script>

<svelte:head>
	<title>AI Assistant | PaperBuddy</title>
</svelte:head>

<div class="assistant-page">
	<div class="page-header">
		<div class="title-section">
			<div class="title-icon">
				<Bot size={26} />
			</div>

			<div>
				<h1>AI Assistant</h1>
				<p>Your intelligent teaching assistant.</p>
			</div>
		</div>

		<div class="ai-status">
			<span class="status-dot"></span>
			AI Assistant
		</div>
	</div>

	<section class="assistant-card">
		<div class="welcome-area">
			<div class="assistant-icon">
				<Sparkles size={32} />
			</div>

			<h2>How can I help you?</h2>

			<p>
				Ask questions about your classes, students, timetable,
				attendance, or other school information.
			</p>
		</div>

		<div class="quick-actions">
			<button
				type="button"
				class="quick-action"
				onclick={() => usePrompt('Suggest ways to improve attendance in my classes.')}
			>
				<GraduationCap size={18} />
				<div>
					<strong>Class Insights</strong>
					<span>Improve class engagement</span>
				</div>
			</button>

			<button
				type="button"
				class="quick-action"
				onclick={() => usePrompt('How can I prepare effective lesson plans?')}
			>
				<BookOpen size={18} />
				<div>
					<strong>Lesson Help</strong>
					<span>Plan your lessons</span>
				</div>
			</button>

			<button
				type="button"
				class="quick-action"
				onclick={() => usePrompt('What should I focus on this week with my timetable?')}
			>
				<CalendarDays size={18} />
				<div>
					<strong>Teaching Schedule</strong>
					<span>Plan your teaching week</span>
				</div>
			</button>
		</div>

		<div class="chat-area">
			{#each messages as msg}
				<div class:user={msg.sender === 'user'} class:assistant={msg.sender === 'assistant'} class="message">
					<div class="message-avatar">
						{#if msg.sender === 'user'}
							👤
						{:else}
							<Bot size={18} />
						{/if}
					</div>

					<div class="message-text">{msg.text}</div>
				</div>
			{/each}

			{#if isLoading}
				<div class="message assistant">
					<div class="message-avatar">
						<Bot size={18} />
					</div>
					<div class="message-text">Thinking...</div>
				</div>
			{/if}

			{#if error}
				<div class="error-text">{error}</div>
			{/if}
		</div>

		<div class="input-area">
			<input
				type="text"
				placeholder="Type your question..."
				bind:value={message}
				onkeydown={(e) => {
					if (e.key === 'Enter') sendMessage();
				}}
			/>

			<button
				type="button"
				class="send-btn"
				onclick={sendMessage}
				disabled={isLoading || !message.trim()}
			>
				<Send size={18} />
			</button>
		</div>
	</section>
</div>

<style>
	.assistant-page {
		padding: 36px;
		max-width: 900px;
	}

	.page-header {
		display: flex;
		align-items: center;
		justify-content: space-between;
		margin-bottom: 28px;
	}

	.title-section {
		display: flex;
		align-items: center;
		gap: 14px;
	}

	.title-icon {
		width: 52px;
		height: 52px;
		display: flex;
		align-items: center;
		justify-content: center;
		background: #2563eb;
		color: white;
		border-radius: 14px;
	}

	.page-header h1 {
		margin: 0 0 5px;
		font-size: 26px;
		font-weight: 800;
		color: #0f172a;
	}

	.page-header p {
		margin: 0;
		font-size: 14px;
		color: #64748b;
	}

	.ai-status {
		display: flex;
		align-items: center;
		gap: 8px;
		padding: 9px 14px;
		background: #ecfdf5;
		color: #059669;
		border-radius: 20px;
		font-size: 13px;
		font-weight: 700;
	}

	.status-dot {
		width: 9px;
		height: 9px;
		background: #059669;
		border-radius: 50%;
	}

	.assistant-card {
		background: white;
		border: 1px solid #e2e8f0;
		border-radius: 18px;
		padding: 28px;
		box-shadow: 0 4px 15px rgba(15, 23, 42, 0.04);
	}

	.welcome-area {
		text-align: center;
		margin-bottom: 24px;
	}

	.assistant-icon {
		width: 64px;
		height: 64px;
		margin: 0 auto 14px;
		display: flex;
		align-items: center;
		justify-content: center;
		background: #eef4ff;
		color: #2563eb;
		border-radius: 18px;
	}

	.welcome-area h2 {
		margin: 0 0 8px;
		font-size: 22px;
		font-weight: 800;
		color: #0f172a;
	}

	.welcome-area p {
		margin: 0 auto;
		max-width: 520px;
		font-size: 14px;
		color: #64748b;
	}

	.quick-actions {
		display: grid;
		grid-template-columns: repeat(3, 1fr);
		gap: 14px;
		margin-bottom: 24px;
	}

	.quick-action {
		display: flex;
		align-items: center;
		gap: 12px;
		padding: 14px;
		background: #f8fafc;
		border: 1px solid #e2e8f0;
		border-radius: 12px;
		text-align: left;
		cursor: pointer;
		transition: 0.2s;
	}

	.quick-action:hover {
		border-color: #bfdbfe;
		background: #eef4ff;
		color: #2563eb;
	}

	.quick-action svg {
		color: #2563eb;
		flex-shrink: 0;
	}

	.quick-action strong {
		display: block;
		font-size: 13px;
		color: #0f172a;
	}

	.quick-action span {
		display: block;
		margin-top: 2px;
		font-size: 11px;
		color: #64748b;
	}

	.chat-area {
		display: flex;
		flex-direction: column;
		gap: 14px;
		max-height: 420px;
		overflow-y: auto;
		margin-bottom: 18px;
		padding-right: 4px;
	}

	.message {
		display: flex;
		align-items: flex-start;
		gap: 12px;
	}

	.message.user {
		flex-direction: row-reverse;
	}

	.message-avatar {
		width: 38px;
		height: 38px;
		flex-shrink: 0;
		display: flex;
		align-items: center;
		justify-content: center;
		background: #eef4ff;
		color: #2563eb;
		border-radius: 10px;
		font-size: 17px;
	}

	.message.user .message-avatar {
		background: #f1f5f9;
	}

	.message-text {
		max-width: 75%;
		padding: 13px 16px;
		background: #f8fafc;
		border: 1px solid #e2e8f0;
		border-radius: 14px;
		font-size: 14px;
		line-height: 1.55;
		color: #0f172a;
		white-space: pre-wrap;
	}

	.message.user .message-text {
		background: #2563eb;
		border-color: #2563eb;
		color: white;
	}

	.error-text {
		padding: 12px;
		background: #fef2f2;
		border-radius: 10px;
		color: #dc2626;
		font-size: 13px;
	}

	.input-area {
		display: flex;
		align-items: center;
		gap: 12px;
	}

	.input-area input {
		flex: 1;
		height: 50px;
		padding: 0 16px;
		background: #f8fafc;
		border: 1px solid #e2e8f0;
		border-radius: 13px;
		font-size: 14px;
		color: #0f172a;
		outline: none;
	}

	.input-area input:focus {
		border-color: #2563eb;
		background: white;
	}

	.send-btn {
		width: 50px;
		height: 50px;
		flex-shrink: 0;
		display: flex;
		align-items: center;
		justify-content: center;
		background: #2563eb;
		border: none;
		border-radius: 13px;
		color: white;
		cursor: pointer;
		transition: 0.2s;
	}

	.send-btn:hover {
		background: #1d4ed8;
	}

	.send-btn:disabled {
		opacity: 0.5;
		cursor: not-allowed;
	}

	@media (max-width: 700px) {
		.quick-actions {
			grid-template-columns: 1fr;
		}
	}
</style>