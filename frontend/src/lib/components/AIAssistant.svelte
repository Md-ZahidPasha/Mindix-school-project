<script lang="ts">
	import { Bot, Send, Sparkles, BookOpen, GraduationCap, CalendarDays, HelpCircle } from '@lucide/svelte';
	import { API } from '$lib/config/api';

	let { title = 'AI Assistant', subtitle = 'Your intelligent academic assistant.' } = $props();

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
				headers: { 'Content-Type': 'application/json', Authorization: `Bearer ${token}` },
				body: JSON.stringify({ message: question })
			});
			const result = await response.json();
			if (!response.ok) throw new Error(result.detail || 'The assistant could not respond.');
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

<div class="assistant-page">
	<div class="page-header">
		<div class="title-section">
			<div class="title-icon">
				<Bot size={26} />
			</div>
			<div>
				<h1>{title}</h1>
				<p>{subtitle}</p>
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
			<p>Ask about attendance, timetable, academic work or institutional operations.</p>
		</div>

		<div class="quick-actions">
			<button type="button" class="quick-action" onclick={() => usePrompt('Help me plan my academic week.')}>
				<BookOpen size={18} />
				<div>
					<strong>Planning</strong>
					<span>Plan your academic week</span>
				</div>
			</button>
			<button type="button" class="quick-action" onclick={() => usePrompt('How can I prepare effectively for upcoming exams?')}>
				<GraduationCap size={18} />
				<div>
					<strong>Exam Prep</strong>
					<span>Prepare for exams</span>
				</div>
			</button>
			<button type="button" class="quick-action" onclick={() => usePrompt('What should I check in my schedule this week?')}>
				<CalendarDays size={18} />
				<div>
					<strong>Schedule</strong>
					<span>Ask about your schedule</span>
				</div>
			</button>
			<button type="button" class="quick-action" onclick={() => usePrompt('What can you help me with in PaperBuddy?')}>
				<HelpCircle size={18} />
				<div>
					<strong>Questions</strong>
					<span>Ask the assistant anything</span>
				</div>
			</button>
		</div>

		<div class="chat-area">
			{#if messages.length === 0}
				<div class="empty-chat">
					<Bot size={28} />
					<h3>Start a conversation</h3>
					<p>Your conversation with the AI Assistant will appear here.</p>
				</div>
			{:else}
				<div class="messages">
					{#each messages as chatMessage}
						<div class:from-user={chatMessage.sender === 'user'} class="chat-message">{chatMessage.text}</div>
					{/each}
					{#if isLoading}<div class="chat-message">Thinking…</div>{/if}
				</div>
			{/if}
		</div>

		<div class="message-box">
			<input
				bind:value={message}
				type="text"
				placeholder="Ask your AI Assistant..."
				aria-label="Ask your AI Assistant"
				onkeydown={(event) => {
					if (event.key === 'Enter') sendMessage();
				}}
			/>
			<button type="button" class="send-button" aria-label="Send message" onclick={sendMessage} disabled={!message.trim() || isLoading}>
				<Send size={18} />
			</button>
		</div>

		<div class="assistant-note">
			<Sparkles size={13} />
			<span>Responses are generated securely by PaperBuddy's backend AI service.</span>
		</div>
		{#if error}<p class="chat-error">{error}</p>{/if}
	</section>
</div>

<style>
	.assistant-page {
		min-height: 100vh;
		padding: 36px;
		box-sizing: border-box;
		background: #f8fafc;
	}

	.page-header {
		display: flex;
		align-items: center;
		justify-content: space-between;
		gap: 20px;
		margin-bottom: 24px;
	}

	.title-section {
		display: flex;
		align-items: center;
		gap: 14px;
	}

	.title-icon {
		display: flex;
		align-items: center;
		justify-content: center;
		width: 50px;
		height: 50px;
		color: #2563eb;
		background: #eff6ff;
		border-radius: 13px;
	}

	.page-header h1 {
		margin: 0;
		color: #0f172a;
		font-size: 30px;
		font-weight: 800;
	}

	.page-header p {
		margin: 6px 0 0;
		color: #64748b;
		font-size: 13px;
	}

	.ai-status {
		display: flex;
		align-items: center;
		gap: 7px;
		padding: 8px 12px;
		color: #16a34a;
		background: #f0fdf4;
		border: 1px solid #dcfce7;
		border-radius: 9px;
		font-size: 11px;
		font-weight: 700;
	}

	.status-dot {
		width: 7px;
		height: 7px;
		background: #22c55e;
		border-radius: 50%;
	}

	.assistant-card {
		min-height: calc(100vh - 170px);
		padding: 30px;
		box-sizing: border-box;
		background: white;
		border: 1px solid #e2e8f0;
		border-radius: 18px;
		box-shadow: 0 5px 18px rgba(15, 23, 42, 0.04);
	}

	.welcome-area {
		display: flex;
		align-items: center;
		flex-direction: column;
		max-width: 620px;
		margin: 15px auto 28px;
		text-align: center;
	}

	.assistant-icon {
		display: flex;
		align-items: center;
		justify-content: center;
		width: 68px;
		height: 68px;
		color: #2563eb;
		background: #eff6ff;
		border-radius: 18px;
	}

	.welcome-area h2 {
		margin: 18px 0 8px;
		color: #0f172a;
		font-size: 22px;
		font-weight: 800;
	}

	.welcome-area p {
		max-width: 540px;
		margin: 0;
		color: #64748b;
		font-size: 12px;
		line-height: 1.7;
	}

	.quick-actions {
		display: grid;
		grid-template-columns: repeat(4, 1fr);
		gap: 12px;
		max-width: 900px;
		margin: 0 auto 25px;
	}

	.quick-action {
		display: flex;
		align-items: flex-start;
		gap: 10px;
		min-height: 78px;
		padding: 14px;
		color: #2563eb;
		text-align: left;
		background: #f8fafc;
		border: 1px solid #e2e8f0;
		border-radius: 12px;
		cursor: pointer;
		transition: background 0.2s ease, border-color 0.2s ease, transform 0.2s ease;
	}

	.quick-action:hover {
		background: #eff6ff;
		border-color: #bfdbfe;
		transform: translateY(-1px);
	}

	.quick-action strong {
		display: block;
		color: #0f172a;
		font-size: 11px;
	}

	.quick-action span {
		display: block;
		margin-top: 4px;
		color: #64748b;
		font-size: 9px;
		line-height: 1.4;
	}

	.chat-area {
		display: flex;
		align-items: center;
		justify-content: center;
		min-height: 260px;
		padding: 20px;
		background: #f8fafc;
		border: 1px solid #e2e8f0;
		border-radius: 14px;
	}

	.empty-chat {
		display: flex;
		align-items: center;
		flex-direction: column;
		color: #94a3b8;
		text-align: center;
	}

	.empty-chat h3 {
		margin: 12px 0 5px;
		color: #475569;
		font-size: 14px;
	}

	.empty-chat p {
		margin: 0;
		color: #94a3b8;
		font-size: 11px;
	}

	.messages {
		width: 100%;
		max-width: 850px;
		display: flex;
		flex-direction: column;
		gap: 10px;
	}

	.chat-message {
		align-self: flex-start;
		max-width: 80%;
		white-space: pre-wrap;
		padding: 11px 14px;
		color: #1e293b;
		background: white;
		border: 1px solid #e2e8f0;
		border-radius: 12px;
		font-size: 13px;
		line-height: 1.5;
	}

	.chat-message.from-user {
		align-self: flex-end;
		color: white;
		background: #2563eb;
		border-color: #2563eb;
	}

	.chat-error {
		margin: 10px auto 0;
		max-width: 900px;
		color: #b91c1c;
		font-size: 12px;
	}

	.message-box {
		display: flex;
		align-items: center;
		gap: 10px;
		max-width: 900px;
		margin: 18px auto 0;
		padding: 8px 8px 8px 16px;
		background: white;
		border: 1px solid #cbd5e1;
		border-radius: 12px;
		box-shadow: 0 4px 12px rgba(15, 23, 42, 0.05);
	}

	.message-box:focus-within {
		border-color: #93c5fd;
		box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.08);
	}

	.message-box input {
		flex: 1;
		min-width: 0;
		padding: 7px 0;
		color: #0f172a;
		background: transparent;
		border: none;
		outline: none;
		font-size: 12px;
	}

	.message-box input::placeholder {
		color: #94a3b8;
	}

	.send-button {
		display: flex;
		align-items: center;
		justify-content: center;
		width: 38px;
		height: 38px;
		flex-shrink: 0;
		color: white;
		background: #2563eb;
		border: none;
		border-radius: 9px;
		cursor: pointer;
	}

	.send-button:hover:not(:disabled) {
		background: #1d4ed8;
	}

	.send-button:disabled {
		background: #cbd5e1;
		cursor: not-allowed;
	}

	.assistant-note {
		display: flex;
		align-items: center;
		justify-content: center;
		gap: 6px;
		margin-top: 12px;
		color: #94a3b8;
		font-size: 9px;
		text-align: center;
	}

	@media (max-width: 1100px) {
		.assistant-page {
			padding: 24px;
		}

		.quick-actions {
			grid-template-columns: repeat(2, 1fr);
		}
	}

	@media (max-width: 700px) {
		.assistant-page {
			padding: 18px;
		}

		.page-header {
			align-items: flex-start;
			flex-direction: column;
		}

		.assistant-card {
			padding: 18px;
		}

		.quick-actions {
			grid-template-columns: 1fr;
		}

		.chat-area {
			min-height: 220px;
		}
	}
</style>