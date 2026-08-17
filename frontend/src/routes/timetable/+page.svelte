<script lang="ts">
	import { onMount } from 'svelte';
	import {
		CalendarDays,
		RefreshCw,
		Sparkles,
		AlertTriangle,
		CheckCircle2,
		Clock,
		Users,
		BookOpen,
		Bot
	} from '@lucide/svelte';
	import { API } from '$lib/config/api';
	import {
		getScheduleClasses,
		getScheduleTeachers,
		getTimetableForClass,
		getTimetableForTeacher,
		getScheduleConflicts,
		generateTimetable,
		type ScheduleClass,
		type ScheduleTeacher,
		type ScheduleEntry,
		type GenerateResult,
		type ScheduleConflict
	} from '$lib/services/schedule';

	const DAY_OPTIONS = [
		'Monday',
		'Tuesday',
		'Wednesday',
		'Thursday',
		'Friday',
		'Saturday',
		'Sunday'
	];

	let classes = $state<ScheduleClass[]>([]);
	let teachers = $state<ScheduleTeacher[]>([]);
	let classesLoading = $state(true);
	let teachersLoading = $state(false);

	let selectedClassIds = $state<string[]>([]);
	let selectedDays = $state<string[]>(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']);
	let periodsPerDay = $state(6);
	let sessionsPerWeek = $state(1);

	let generating = $state(false);
	let generationError = $state('');
	let generationResult = $state<GenerateResult | null>(null);

	let viewClassId = $state('');
	let viewTeacherId = $state('');
	let viewedEntries = $state<ScheduleEntry[]>([]);
	let viewing = $state(false);
	let viewError = $state('');

	let conflicts = $state<ScheduleConflict[]>([]);
	let conflictsLoading = $state(false);

	let aiAdvice = $state('');
	let aiLoading = $state(false);
	let aiError = $state('');

	function buildAiPrompt(): string {
		const lines: string[] = [];
		if (entries.length > 0) {
			lines.push(
				`The generated timetable has ${entries.length} slots over ${gridDays.length} day(s) and ${gridPeriods.length} period(s) per day.`
			);
			const byClass = new Map<string, number>();
			for (const entry of entries) {
				const key = entry.class_name ?? entry.class_id;
				byClass.set(key, (byClass.get(key) ?? 0) + 1);
			}
			for (const [cls, count] of byClass) {
				lines.push(`- ${cls}: ${count} lesson(s)`);
			}
		}
		if (conflicts.length > 0) {
			lines.push('Scheduling conflicts detected:');
			for (const conflict of conflicts) {
				lines.push(
					`- ${conflict.type === 'teacher' ? 'Teacher' : conflict.type === 'class' ? 'Class' : 'Room'} "${conflict.value}" is booked twice on ${conflict.day} period ${conflict.period}.`
				);
			}
		}
		return lines.join('\n');
	}

	async function getAiAdvice() {
		const token = localStorage.getItem('access_token');
		if (!token) {
			aiError = 'Please sign in again to use AI advice.';
			return;
		}
		if (entries.length === 0 && conflicts.length === 0) return;
		aiLoading = true;
		aiError = '';
		aiAdvice = '';
		const prompt = `I am a school administrator using PaperBuddy. Review this timetable and give practical advice (max ~120 words): how balanced it looks, whether teachers are overloaded, and how to fix any conflicts.\n\n${buildAiPrompt()}`;
		try {
			const response = await fetch(API.aiChat, {
				method: 'POST',
				headers: { 'Content-Type': 'application/json', Authorization: `Bearer ${token}` },
				body: JSON.stringify({ message: prompt })
			});
			const result = await response.json();
			if (!response.ok) throw new Error(result.detail || 'AI could not respond.');
			aiAdvice = result.answer;
		} catch (err) {
			aiError = err instanceof Error ? err.message : 'AI advice is unavailable right now.';
		} finally {
			aiLoading = false;
		}
	}

	async function loadClasses() {
		classesLoading = true;
		try {
			classes = await getScheduleClasses();
		} catch (err) {
			generationError = err instanceof Error ? err.message : 'Could not load classes.';
		} finally {
			classesLoading = false;
		}
	}

	async function loadTeachers() {
		teachersLoading = true;
		try {
			teachers = await getScheduleTeachers();
		} catch {
			teachers = [];
		} finally {
			teachersLoading = false;
		}
	}

	async function loadConflicts() {
		conflictsLoading = true;
		try {
			conflicts = await getScheduleConflicts();
		} catch {
			conflicts = [];
		} finally {
			conflictsLoading = false;
		}
	}

	onMount(() => {
		loadClasses();
		loadConflicts();
	});

	function toggleClass(id: string) {
		if (selectedClassIds.includes(id)) {
			selectedClassIds = selectedClassIds.filter((item) => item !== id);
		} else {
			selectedClassIds = [...selectedClassIds, id];
		}
	}

	function toggleDay(day: string) {
		if (selectedDays.includes(day)) {
			selectedDays = selectedDays.filter((item) => item !== day);
		} else {
			selectedDays = [...selectedDays, day];
		}
	}

	async function handleGenerate() {
		generating = true;
		generationError = '';
		generationResult = null;
		viewedEntries = [];
		try {
			generationResult = await generateTimetable({
				class_ids: selectedClassIds.length > 0 ? selectedClassIds : null,
				working_days: selectedDays,
				periods_per_day: periodsPerDay,
				sessions_per_week: sessionsPerWeek,
				persist: true
			});
			await loadConflicts();
		} catch (err) {
			generationError =
				err instanceof Error ? err.message : 'The timetable could not be generated.';
		} finally {
			generating = false;
		}
	}

	async function handleViewClass() {
		if (!viewClassId) return;
		viewing = true;
		viewError = '';
		generationResult = null;
		try {
			viewedEntries = await getTimetableForClass(viewClassId);
		} catch (err) {
			viewError = err instanceof Error ? err.message : 'Could not load this timetable.';
		} finally {
			viewing = false;
		}
	}

	async function handleViewTeacher() {
		if (!viewTeacherId) return;
		if (!teachersLoading && teachers.length === 0) await loadTeachers();
		viewing = true;
		viewError = '';
		generationResult = null;
		try {
			viewedEntries = await getTimetableForTeacher(viewTeacherId);
		} catch (err) {
			viewError = err instanceof Error ? err.message : 'Could not load this timetable.';
		} finally {
			viewing = false;
		}
	}

	function displayEntries(): ScheduleEntry[] {
		if (generationResult && generationResult.generated.length > 0) {
			return generationResult.generated;
		}
		return viewedEntries;
	}

	const entries = $derived(displayEntries());

	const gridDays = $derived.by(() => {
		if (entries.length === 0) return [];
		const days = [...new Set(entries.map((entry) => entry.day))];
		return DAY_OPTIONS.filter((day) => days.includes(day));
	});

	const gridPeriods = $derived.by(() => {
		if (entries.length === 0) return [];
		let max = 0;
		for (const entry of entries) {
			if (entry.period > max) max = entry.period;
		}
		return Array.from({ length: max }, (_, index) => index + 1);
	});

	function entryAt(day: string, period: number): ScheduleEntry | undefined {
		return entries.find((entry) => entry.day === day && entry.period === period);
	}

	function formatClassName(entry: ScheduleEntry): string {
		return entry.class_name ?? entry.class_id.slice(0, 8);
	}

	function selectedClassLabel(): string {
		if (selectedClassIds.length === 0) return 'All classes';
		const selected = classes.filter((cls) => selectedClassIds.includes(cls.id));
		return selected.map((cls) => `${cls.name}${cls.section ? ' ' + cls.section : ''}`).join(', ');
	}
</script>

<svelte:head>
	<title>Timetable | PaperBuddy</title>
</svelte:head>

<div class="timetable-page">
	<!-- =========================
		 PAGE HEADER
		 ========================= -->
	<div class="page-header">
		<div class="title-section">
			<div class="title-icon">
				<CalendarDays size={26} />
			</div>
			<div>
				<h1>Timetable</h1>
				<p>View and generate conflict-free class timetables.</p>
			</div>
		</div>
		<button type="button" class="refresh-button" onclick={() => { loadClasses(); loadConflicts(); }}>
			<RefreshCw size={15} />
			Refresh
		</button>
	</div>

	<!-- =========================
		 CONFLICT WARNINGS
		 ========================= -->
	{#if conflictsLoading}
		<div class="info-box">Checking for timetable conflicts…</div>
	{:else if conflicts.length > 0}
		<div class="conflict-box">
			<div class="conflict-title">
				<AlertTriangle size={17} />
				<span>{conflicts.length} scheduling conflict{conflicts.length > 1 ? 's' : ''} detected</span>
			</div>
			<ul>
				{#each conflicts as conflict}
					<li>
						{conflict.type === 'teacher' ? 'Teacher' : conflict.type === 'class' ? 'Class' : 'Room'} <strong>{conflict.value}</strong>
						is booked twice on {conflict.day} (period {conflict.period}).
					</li>
				{/each}
			</ul>
		</div>
	{:else if entries.length > 0}
		<div class="ok-box">
			<CheckCircle2 size={16} />
			<span>No scheduling conflicts detected.</span>
		</div>
	{/if}

	<!-- =========================
		 GENERATION CONTROLS
		 ========================= -->
	<section class="controls-card">
		<div class="card-heading">
			<Sparkles size={18} />
			<h2>Generate Timetable</h2>
			<p>Created automatically by the OR-Tools optimizer from real classes, subjects, teachers and rooms.</p>
		</div>

		{#if classesLoading}
			<p class="hint-text">Loading classes…</p>
		{:else if classes.length === 0}
			<div class="empty-box">
				<BookOpen size={20} />
				<p>No classes found for this institution. Add classes first, then generate a timetable.</p>
			</div>
		{:else}
			<div class="control-group">
				<span class="control-label">Classes</span>
				<div class="chip-list">
					<button
						type="button"
						class="chip"
						class:active={selectedClassIds.length === 0}
						onclick={() => (selectedClassIds = [])}
					>
						All
					</button>
					{#each classes as cls}
						<button
							type="button"
							class="chip"
							class:active={selectedClassIds.includes(cls.id)}
							onclick={() => toggleClass(cls.id)}
						>
							{cls.name}{cls.section ? ` ${cls.section}` : ''}
						</button>
					{/each}
				</div>
			</div>

			<div class="control-row">
				<div class="control-group">
					<span class="control-label">Working days</span>
					<div class="chip-list">
						{#each DAY_OPTIONS as day}
							<button
								type="button"
								class="chip"
								class:active={selectedDays.includes(day)}
								onclick={() => toggleDay(day)}
							>
								{day.slice(0, 3)}
							</button>
						{/each}
					</div>
				</div>

				<div class="control-group number-group">
					<span class="control-label">Periods per day</span>
					<input type="number" min="1" max="12" bind:value={periodsPerDay} />
				</div>

				<div class="control-group number-group">
					<span class="control-label">Sessions / subject / week</span>
					<input type="number" min="1" max="10" bind:value={sessionsPerWeek} />
				</div>
			</div>

			<div class="action-row">
				<button
					type="button"
					class="generate-button"
					disabled={generating || selectedDays.length === 0}
					onclick={handleGenerate}
				>
					<Sparkles size={16} />
					{generating ? 'Generating…' : 'Generate Timetable'}
				</button>
				<span class="selection-summary">Scheduling: {selectedClassLabel()}</span>
			</div>
		{/if}

		{#if generationError}<p class="error-text">{generationError}</p>{/if}

		{#if generationResult && generationResult.skipped.length > 0}
			<div class="skipped-box">
				<strong>Could not schedule {generationResult.skipped.length} lesson
				{generationResult.skipped.length > 1 ? 's' : ''}:</strong>
				<ul>
					{#each generationResult.skipped as skip}
						<li>
							{skip.class || 'Class'}
							{#if skip.subject}– {skip.subject}{/if}: {skip.reason}
						</li>
					{/each}
				</ul>
			</div>
		{/if}
	</section>

	<!-- =========================
		 VIEW EXISTING TIMETABLE
		 ========================= -->
	<section class="view-card">
		<div class="card-heading">
			<Clock size={18} />
			<h2>View Timetable</h2>
			<p>Browse the stored timetable for a class or teacher.</p>
		</div>

		<div class="view-controls">
			<select bind:value={viewClassId} aria-label="Select class">
				<option value="">Class timetable…</option>
				{#each classes as cls}
					<option value={cls.id}>{cls.name}{cls.section ? ` ${cls.section}` : ''}</option>
				{/each}
			</select>
			<button type="button" class="view-button" disabled={!viewClassId || viewing} onclick={handleViewClass}>
				<Users size={15} />
				{viewing ? 'Loading…' : 'View Class'}
			</button>

			<select bind:value={viewTeacherId} aria-label="Select teacher">
				<option value="">Teacher timetable…</option>
				{#each teachers as teacher}
					<option value={teacher.id}>{teacher.name ?? teacher.id.slice(0, 8)}</option>
				{/each}
			</select>
			<button type="button" class="view-button" disabled={!viewTeacherId || viewing} onclick={handleViewTeacher}>
				<Users size={15} />
				{viewing ? 'Loading…' : 'View Teacher'}
			</button>
		</div>

		{#if viewError}<p class="error-text">{viewError}</p>{/if}
	</section>

	<!-- =========================
		 TIMETABLE GRID
		 ========================= -->
	<section class="grid-card">
		{#if generating}
			<div class="empty-box">Optimizing a conflict-free timetable…</div>
		{:else if entries.length === 0}
			<div class="empty-box">
				<CalendarDays size={22} />
				<h3>No timetable yet</h3>
				<p>Generate a timetable above, or view an existing one for a class or teacher.</p>
			</div>
		{:else}
			<div class="table-scroll">
				<table class="timetable-grid">
					<thead>
						<tr>
							<th class="period-col">Period</th>
							{#each gridDays as day}
								<th>{day}</th>
							{/each}
						</tr>
					</thead>
					<tbody>
						{#each gridPeriods as period}
							<tr>
								<td class="period-col">{period}</td>
								{#each gridDays as day}
									{@const entry = entryAt(day, period)}
									<td>
										{#if entry}
											<div class="slot">
												<strong>{entry.subject_name}</strong>
												<span>{formatClassName(entry)}</span>
												<span>{entry.teacher_name ?? 'Teacher'}</span>
												{#if entry.room_name}<span class="room">{entry.room_name}</span>{/if}
											</div>
										{:else}
											<div class="empty-slot"></div>
										{/if}
									</td>
								{/each}
							</tr>
						{/each}
					</tbody>
				</table>
			</div>
			{#if generationResult}
				<p class="grid-note">{generationResult.message}</p>
			{/if}

			<div class="ai-advice-row">
				<button
					type="button"
					class="ai-advice-button"
					disabled={aiLoading || (entries.length === 0 && conflicts.length === 0)}
					onclick={getAiAdvice}
				>
					<Bot size={16} />
					{aiLoading ? 'Analyzing…' : 'Get AI Advice'}
				</button>
				{#if aiError}<span class="error-text">{aiError}</span>{/if}
			</div>

			{#if aiAdvice}
				<div class="ai-advice-box">
					<Sparkles size={15} />
					<p>{aiAdvice}</p>
				</div>
			{/if}
		{/if}
	</section>
</div>

<style>
	.timetable-page {
		min-height: 100vh;
		padding: 36px;
		box-sizing: border-box;
		background: #f8fafc;
	}

	/* =========================
	   HEADER
	   ========================= */
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

	.refresh-button {
		display: flex;
		align-items: center;
		gap: 7px;
		padding: 9px 14px;
		color: #2563eb;
		background: white;
		border: 1px solid #e2e8f0;
		border-radius: 10px;
		cursor: pointer;
		font-size: 12px;
		font-weight: 600;
	}

	.refresh-button:hover {
		background: #eff6ff;
		border-color: #bfdbfe;
	}

	/* =========================
	   STATUS BOXES
	   ========================= */
	.info-box,
	.ok-box,
	.conflict-box {
		display: flex;
		align-items: center;
		gap: 8px;
		margin-bottom: 16px;
		padding: 11px 14px;
		border-radius: 10px;
		font-size: 12px;
	}

	.info-box {
		color: #475569;
		background: #f1f5f9;
		border: 1px solid #e2e8f0;
	}

	.ok-box {
		color: #15803d;
		background: #f0fdf4;
		border: 1px solid #dcfce7;
	}

	.conflict-box {
		align-items: flex-start;
		flex-direction: column;
		color: #92400e;
		background: #fffbeb;
		border: 1px solid #fde68a;
	}

	.conflict-title {
		display: flex;
		align-items: center;
		gap: 7px;
		font-weight: 700;
	}

	.conflict-box ul,
	.skipped-box ul {
		margin: 4px 0 0;
		padding-left: 20px;
		line-height: 1.7;
	}

	/* =========================
	   CARDS
	   ========================= */
	.controls-card,
	.view-card,
	.grid-card {
		padding: 26px;
		margin-bottom: 18px;
		background: white;
		border: 1px solid #e2e8f0;
		border-radius: 16px;
		box-shadow: 0 5px 18px rgba(15, 23, 42, 0.04);
	}

	.card-heading {
		display: flex;
		align-items: center;
		gap: 10px;
		color: #2563eb;
	}

	.card-heading h2 {
		margin: 0;
		color: #0f172a;
		font-size: 17px;
		font-weight: 800;
	}

	.card-heading p {
		margin: 2px 0 0;
		color: #64748b;
		font-size: 11px;
	}

	.control-group {
		margin-top: 18px;
	}

	.control-label {
		display: block;
		margin-bottom: 8px;
		color: #475569;
		font-size: 11px;
		font-weight: 700;
	}

	.chip-list {
		display: flex;
		flex-wrap: wrap;
		gap: 8px;
	}

	.chip {
		padding: 7px 13px;
		color: #475569;
		background: #f8fafc;
		border: 1px solid #e2e8f0;
		border-radius: 999px;
		cursor: pointer;
		font-size: 11px;
		font-weight: 600;
		transition: background 0.15s ease, border-color 0.15s ease, color 0.15s ease;
	}

	.chip:hover {
		background: #eff6ff;
		border-color: #bfdbfe;
	}

	.chip.active {
		color: white;
		background: #2563eb;
		border-color: #2563eb;
	}

	.control-row {
		display: flex;
		flex-wrap: wrap;
		gap: 26px;
		align-items: flex-end;
	}

	.number-group input {
		width: 96px;
		padding: 9px 11px;
		color: #0f172a;
		background: #f8fafc;
		border: 1px solid #e2e8f0;
		border-radius: 10px;
		font-size: 13px;
	}

	.action-row {
		display: flex;
		align-items: center;
		gap: 14px;
		margin-top: 22px;
	}

	.generate-button,
	.view-button {
		display: inline-flex;
		align-items: center;
		gap: 8px;
		padding: 11px 18px;
		color: white;
		background: #2563eb;
		border: none;
		border-radius: 10px;
		cursor: pointer;
		font-size: 13px;
		font-weight: 700;
	}

	.generate-button:hover:not(:disabled),
	.view-button:hover:not(:disabled) {
		background: #1d4ed8;
	}

	.generate-button:disabled,
	.view-button:disabled {
		background: #cbd5e1;
		cursor: not-allowed;
	}

	.selection-summary {
		color: #64748b;
		font-size: 11px;
	}

	.error-text {
		margin: 12px 0 0;
		color: #b91c1c;
		font-size: 12px;
	}

	.skipped-box {
		margin-top: 16px;
		padding: 12px 14px;
		color: #92400e;
		background: #fffbeb;
		border: 1px solid #fde68a;
		border-radius: 10px;
		font-size: 11px;
		line-height: 1.6;
	}

	.hint-text {
		color: #64748b;
		font-size: 12px;
	}

	.empty-box {
		display: flex;
		align-items: center;
		flex-direction: column;
		gap: 6px;
		padding: 34px 20px;
		color: #94a3b8;
		text-align: center;
	}

	.empty-box h3 {
		margin: 6px 0 0;
		color: #475569;
		font-size: 14px;
	}

	.empty-box p {
		margin: 0;
		font-size: 11px;
	}

	/* =========================
	   VIEW CONTROLS
	   ========================= */
	.view-controls {
		display: flex;
		flex-wrap: wrap;
		align-items: center;
		gap: 10px;
		margin-top: 16px;
	}

	.view-controls select {
		padding: 10px 12px;
		color: #0f172a;
		background: #f8fafc;
		border: 1px solid #e2e8f0;
		border-radius: 10px;
		font-size: 13px;
	}

	/* =========================
	   GRID
	   ========================= */
	.table-scroll {
		overflow-x: auto;
	}

	.timetable-grid {
		width: 100%;
		border-collapse: separate;
		border-spacing: 6px;
	}

	.timetable-grid th {
		padding: 9px 12px;
		color: #475569;
		background: #f1f5f9;
		border-radius: 8px;
		font-size: 11px;
		text-align: left;
		font-weight: 700;
	}

	.timetable-grid .period-col {
		color: #64748b;
		font-size: 11px;
		text-align: center;
		font-weight: 700;
	}

	.slot {
		display: flex;
		flex-direction: column;
		gap: 3px;
		min-width: 128px;
		padding: 9px 11px;
		background: #eff6ff;
		border: 1px solid #dbeafe;
		border-radius: 9px;
		font-size: 10px;
	}

	.slot strong {
		color: #1d4ed8;
		font-size: 11px;
	}

	.slot span {
		color: #475569;
	}

	.slot .room {
		color: #94a3b8;
	}

	.empty-slot {
		min-width: 128px;
		height: 34px;
		background: #f8fafc;
		border: 1px dashed #e2e8f0;
		border-radius: 9px;
	}

	.grid-note {
		margin: 14px 0 0;
		color: #16a34a;
		font-size: 12px;
		font-weight: 600;
	}

	.ai-advice-row {
		display: flex;
		align-items: center;
		gap: 12px;
		margin-top: 18px;
	}

	.ai-advice-button {
		display: inline-flex;
		align-items: center;
		gap: 8px;
		padding: 10px 16px;
		color: #7c3aed;
		background: #f5f3ff;
		border: 1px solid #ddd6fe;
		border-radius: 10px;
		cursor: pointer;
		font-size: 12px;
		font-weight: 700;
	}

	.ai-advice-button:hover:not(:disabled) {
		background: #ede9fe;
		border-color: #c4b5fd;
	}

	.ai-advice-button:disabled {
		color: #94a3b8;
		background: #f1f5f9;
		border-color: #e2e8f0;
		cursor: not-allowed;
	}

	.ai-advice-box {
		display: flex;
		gap: 10px;
		margin-top: 12px;
		padding: 14px 16px;
		color: #4c1d95;
		background: #f5f3ff;
		border: 1px solid #ddd6fe;
		border-radius: 12px;
		font-size: 12px;
		line-height: 1.6;
	}

	.ai-advice-box p {
		margin: 0;
		white-space: pre-wrap;
	}

	/* =========================
	   RESPONSIVE
	   ========================= */
	@media (max-width: 900px) {
		.timetable-page {
			padding: 22px;
		}
	}

	@media (max-width: 640px) {
		.page-header {
			align-items: flex-start;
			flex-direction: column;
		}

		.controls-card,
		.view-card,
		.grid-card {
			padding: 18px;
		}
	}
</style>