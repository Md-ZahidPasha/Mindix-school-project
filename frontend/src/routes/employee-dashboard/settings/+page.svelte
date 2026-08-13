<script lang="ts">
    import {
        Settings,
        User,
        Bell,
        Lock,
        Palette,
        Globe,
        ShieldCheck,
        Save,
        CheckCircle2,
        Info
    } from '@lucide/svelte';

    let notificationsEnabled = $state(true);
    let emailNotifications = $state(true);
    let taskNotifications = $state(true);
    let attendanceNotifications = $state(true);
    let darkMode = $state(false);
    let language = $state('English');

    let currentPassword = $state('');
    let newPassword = $state('');
    let confirmPassword = $state('');

    let saved = $state(false);

    function saveSettings() {
        saved = true;

        setTimeout(() => {
            saved = false;
        }, 2500);
    }

    function changePassword() {
        if (!currentPassword || !newPassword || !confirmPassword) {
            alert('Please fill in all password fields.');
            return;
        }

        if (newPassword !== confirmPassword) {
            alert('New password and confirm password do not match.');
            return;
        }

        alert('Password change will be connected to the backend later.');

        currentPassword = '';
        newPassword = '';
        confirmPassword = '';
    }
</script>

<svelte:head>
    <title>Settings | Employee Dashboard</title>
</svelte:head>

<div class="settings-page">

    <!-- HEADER -->
    <div class="page-header">

        <div class="title-row">

            <div class="title-icon">
                <Settings size={24} />
            </div>

            <div>
                <h1>Settings</h1>

                <p>
                    Manage your account, notifications and preferences.
                </p>
            </div>

        </div>

        {#if saved}
            <div class="saved-message">
                <CheckCircle2 size={15} />
                Settings saved
            </div>
        {/if}

    </div>


    <!-- ACCOUNT SETTINGS -->
    <section class="settings-card">

        <div class="card-heading">

            <div class="heading-icon blue">
                <User size={19} />
            </div>

            <div>
                <h2>Account Settings</h2>

                <p>
                    Manage your employee account information.
                </p>
            </div>

        </div>


        <div class="profile-row">

            <div class="avatar">
                A
            </div>

            <div class="profile-info">

                <strong>
                    Arjun Kumar
                </strong>

                <span>
                    Driving Department
                </span>

                <small>
                    Employee ID: EMP-2026-001
                </small>

            </div>

            <span class="account-status">
                <span></span>
                Active
            </span>

        </div>

    </section>


    <!-- NOTIFICATION SETTINGS -->
    <section class="settings-card">

        <div class="card-heading">

            <div class="heading-icon orange">
                <Bell size={19} />
            </div>

            <div>
                <h2>Notification Settings</h2>

                <p>
                    Choose which notifications you want to receive.
                </p>
            </div>

        </div>


        <div class="settings-list">

            <div class="setting-row">

                <div class="setting-text">

                    <strong>
                        Push Notifications
                    </strong>

                    <span>
                        Receive notifications inside the employee portal.
                    </span>

                </div>

                <label class="switch">
                    <input
                        type="checkbox"
                        bind:checked={notificationsEnabled}
                    />
                    <span class="slider"></span>
                </label>

            </div>


            <div class="setting-row">

                <div class="setting-text">

                    <strong>
                        Email Notifications
                    </strong>

                    <span>
                        Receive important updates through email.
                    </span>

                </div>

                <label class="switch">
                    <input
                        type="checkbox"
                        bind:checked={emailNotifications}
                    />
                    <span class="slider"></span>
                </label>

            </div>


            <div class="setting-row">

                <div class="setting-text">

                    <strong>
                        Task Notifications
                    </strong>

                    <span>
                        Get notified when a new task is assigned.
                    </span>

                </div>

                <label class="switch">
                    <input
                        type="checkbox"
                        bind:checked={taskNotifications}
                    />
                    <span class="slider"></span>
                </label>

            </div>


            <div class="setting-row">

                <div class="setting-text">

                    <strong>
                        Attendance Notifications
                    </strong>

                    <span>
                        Receive updates about attendance records.
                    </span>

                </div>

                <label class="switch">
                    <input
                        type="checkbox"
                        bind:checked={attendanceNotifications}
                    />
                    <span class="slider"></span>
                </label>

            </div>

        </div>

    </section>


    <!-- PREFERENCES -->
    <section class="settings-card">

        <div class="card-heading">

            <div class="heading-icon purple">
                <Palette size={19} />
            </div>

            <div>
                <h2>Preferences</h2>

                <p>
                    Customize your employee portal experience.
                </p>
            </div>

        </div>


        <div class="preference-grid">

            <div class="preference-item">

                <div class="preference-label">

                    <Globe size={16} />

                    <div>
                        <strong>Language</strong>
                        <span>Select your preferred language.</span>
                    </div>

                </div>

                <select bind:value={language}>
                    <option value="English">English</option>
                    <option value="Hindi">Hindi</option>
                    <option value="Telugu">Telugu</option>
                </select>

            </div>


            <div class="preference-item">

                <div class="preference-label">

                    <Palette size={16} />

                    <div>
                        <strong>Dark Mode</strong>
                        <span>Use a darker appearance for the portal.</span>
                    </div>

                </div>

                <label class="switch">
                    <input
                        type="checkbox"
                        bind:checked={darkMode}
                    />
                    <span class="slider"></span>
                </label>

            </div>

        </div>

    </section>


    <!-- CHANGE PASSWORD -->
    <section class="settings-card">

        <div class="card-heading">

            <div class="heading-icon red">
                <Lock size={19} />
            </div>

            <div>
                <h2>Change Password</h2>

                <p>
                    Update your employee account password.
                </p>
            </div>

        </div>


        <div class="password-grid">

            <div class="form-group">

                <label for="currentPassword">
                    Current Password
                </label>

                <input
                    id="currentPassword"
                    type="password"
                    placeholder="Enter current password"
                    bind:value={currentPassword}
                />

            </div>


            <div class="form-group">

                <label for="newPassword">
                    New Password
                </label>

                <input
                    id="newPassword"
                    type="password"
                    placeholder="Enter new password"
                    bind:value={newPassword}
                />

            </div>


            <div class="form-group">

                <label for="confirmPassword">
                    Confirm Password
                </label>

                <input
                    id="confirmPassword"
                    type="password"
                    placeholder="Confirm new password"
                    bind:value={confirmPassword}
                />

            </div>

        </div>


        <div class="password-actions">

            <button
                type="button"
                onclick={changePassword}
            >
                <Lock size={14} />
                Update Password
            </button>

        </div>

    </section>


    <!-- SAVE -->
    <div class="save-section">

        <button
            class="save-button"
            type="button"
            onclick={saveSettings}
        >
            <Save size={16} />
            Save Settings
        </button>

    </div>


    <!-- INFORMATION -->
    <section class="information-note">

        <div class="information-icon">
            <Info size={18} />
        </div>

        <div>

            <strong>
                Settings Information
            </strong>

            <p>
                Settings shown here are currently demo controls.
                During API integration, notification preferences,
                password changes and account settings will be securely
                stored in the backend.
            </p>

        </div>

    </section>

</div>


<style>
    .settings-page {
        width: 100%;
        min-height: 100vh;
        padding: 36px;
        box-sizing: border-box;
        background: #f8fafc;
    }


    /* HEADER */

    .page-header {
        display: flex;
        align-items: center;
        justify-content: space-between;
        gap: 20px;
        margin-bottom: 25px;
    }

    .title-row {
        display: flex;
        align-items: center;
        gap: 13px;
    }

    .title-icon {
        width: 48px;
        height: 48px;
        display: flex;
        align-items: center;
        justify-content: center;
        flex-shrink: 0;
        border-radius: 13px;
        background: #eef4ff;
        color: #2563eb;
    }

    .page-header h1 {
        margin: 0;
        color: #0f172a;
        font-size: 28px;
        font-weight: 800;
    }

    .page-header p {
        margin: 5px 0 0;
        color: #64748b;
        font-size: 13px;
    }

    .saved-message {
        display: flex;
        align-items: center;
        gap: 6px;
        padding: 8px 11px;
        border-radius: 8px;
        background: #ecfdf5;
        color: #059669;
        font-size: 9px;
        font-weight: 700;
    }


    /* CARD */

    .settings-card {
        padding: 20px;
        margin-bottom: 17px;
        border: 1px solid #e2e8f0;
        border-radius: 14px;
        background: white;
        box-shadow: 0 3px 12px rgba(15, 23, 42, 0.03);
    }

    .card-heading {
        display: flex;
        align-items: center;
        gap: 11px;
        margin-bottom: 19px;
    }

    .heading-icon {
        width: 40px;
        height: 40px;
        display: flex;
        align-items: center;
        justify-content: center;
        flex-shrink: 0;
        border-radius: 10px;
    }

    .heading-icon.blue {
        background: #eef4ff;
        color: #2563eb;
    }

    .heading-icon.orange {
        background: #fff7ed;
        color: #ea580c;
    }

    .heading-icon.purple {
        background: #f5f3ff;
        color: #7c3aed;
    }

    .heading-icon.red {
        background: #fef2f2;
        color: #dc2626;
    }

    .card-heading h2 {
        margin: 0;
        color: #0f172a;
        font-size: 15px;
    }

    .card-heading p {
        margin: 3px 0 0;
        color: #64748b;
        font-size: 9px;
    }


    /* ACCOUNT */

    .profile-row {
        display: flex;
        align-items: center;
        gap: 13px;
        padding: 14px;
        border: 1px solid #e2e8f0;
        border-radius: 11px;
        background: #f8fafc;
    }

    .avatar {
        width: 45px;
        height: 45px;
        display: flex;
        align-items: center;
        justify-content: center;
        flex-shrink: 0;
        border-radius: 50%;
        background: #2563eb;
        color: white;
        font-size: 17px;
        font-weight: 800;
    }

    .profile-info {
        flex: 1;
    }

    .profile-info strong {
        display: block;
        color: #0f172a;
        font-size: 12px;
    }

    .profile-info span {
        display: block;
        margin-top: 2px;
        color: #64748b;
        font-size: 9px;
    }

    .profile-info small {
        display: block;
        margin-top: 3px;
        color: #94a3b8;
        font-size: 8px;
    }

    .account-status {
        display: flex;
        align-items: center;
        gap: 5px;
        padding: 5px 8px;
        border-radius: 6px;
        background: #ecfdf5;
        color: #059669;
        font-size: 8px;
        font-weight: 700;
    }

    .account-status span {
        width: 6px;
        height: 6px;
        border-radius: 50%;
        background: #10b981;
    }


    /* SETTINGS LIST */

    .settings-list {
        display: flex;
        flex-direction: column;
    }

    .setting-row {
        display: flex;
        align-items: center;
        justify-content: space-between;
        gap: 20px;
        padding: 14px 0;
        border-bottom: 1px solid #f1f5f9;
    }

    .setting-row:first-child {
        padding-top: 0;
    }

    .setting-row:last-child {
        padding-bottom: 0;
        border-bottom: none;
    }

    .setting-text {
        display: flex;
        flex-direction: column;
        gap: 4px;
    }

    .setting-text strong {
        color: #334155;
        font-size: 10px;
    }

    .setting-text span {
        color: #94a3b8;
        font-size: 8px;
    }


    /* SWITCH */

    .switch {
        position: relative;
        width: 38px;
        height: 21px;
        display: inline-block;
        flex-shrink: 0;
    }

    .switch input {
        width: 0;
        height: 0;
        opacity: 0;
    }

    .slider {
        position: absolute;
        inset: 0;
        border-radius: 20px;
        background: #cbd5e1;
        cursor: pointer;
        transition: 0.2s;
    }

    .slider::before {
        content: '';
        position: absolute;
        width: 15px;
        height: 15px;
        left: 3px;
        top: 3px;
        border-radius: 50%;
        background: white;
        transition: 0.2s;
        box-shadow: 0 1px 3px rgba(0, 0, 0, 0.15);
    }

    .switch input:checked + .slider {
        background: #2563eb;
    }

    .switch input:checked + .slider::before {
        transform: translateX(17px);
    }


    /* PREFERENCES */

    .preference-grid {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 15px;
    }

    .preference-item {
        display: flex;
        align-items: center;
        justify-content: space-between;
        gap: 15px;
        padding: 14px;
        border: 1px solid #e2e8f0;
        border-radius: 10px;
    }

    .preference-label {
        display: flex;
        align-items: center;
        gap: 9px;
        color: #64748b;
    }

    .preference-label strong {
        display: block;
        color: #334155;
        font-size: 10px;
    }

    .preference-label span {
        display: block;
        margin-top: 3px;
        color: #94a3b8;
        font-size: 8px;
    }

    .preference-item select {
        padding: 7px 8px;
        border: 1px solid #dbe3ef;
        border-radius: 7px;
        outline: none;
        background: white;
        color: #475569;
        font-family: inherit;
        font-size: 8px;
    }


    /* PASSWORD */

    .password-grid {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 13px;
    }

    .form-group {
        display: flex;
        flex-direction: column;
        gap: 6px;
    }

    .form-group label {
        color: #475569;
        font-size: 9px;
        font-weight: 700;
    }

    .form-group input {
        width: 100%;
        box-sizing: border-box;
        padding: 10px;
        border: 1px solid #dbe3ef;
        border-radius: 8px;
        outline: none;
        background: white;
        color: #334155;
        font-family: inherit;
        font-size: 9px;
    }

    .form-group input:focus {
        border-color: #93c5fd;
        box-shadow: 0 0 0 3px #eff6ff;
    }

    .password-actions {
        display: flex;
        justify-content: flex-end;
        margin-top: 15px;
    }

    .password-actions button {
        display: flex;
        align-items: center;
        gap: 6px;
        padding: 9px 12px;
        border: 1px solid #dbe3ef;
        border-radius: 8px;
        background: white;
        color: #475569;
        font-size: 8px;
        font-weight: 700;
        cursor: pointer;
    }

    .password-actions button:hover {
        border-color: #2563eb;
        color: #2563eb;
        background: #eff6ff;
    }


    /* SAVE */

    .save-section {
        display: flex;
        justify-content: flex-end;
        margin-bottom: 20px;
    }

    .save-button {
        display: flex;
        align-items: center;
        gap: 7px;
        padding: 10px 16px;
        border: none;
        border-radius: 8px;
        background: #2563eb;
        color: white;
        font-size: 9px;
        font-weight: 700;
        cursor: pointer;
    }

    .save-button:hover {
        background: #1d4ed8;
    }


    /* INFORMATION */

    .information-note {
        display: flex;
        align-items: flex-start;
        gap: 11px;
        padding: 15px;
        border: 1px solid #bfdbfe;
        border-radius: 11px;
        background: #eff6ff;
    }

    .information-icon {
        width: 36px;
        height: 36px;
        display: flex;
        align-items: center;
        justify-content: center;
        flex-shrink: 0;
        border-radius: 9px;
        background: #dbeafe;
        color: #2563eb;
    }

    .information-note strong {
        display: block;
        color: #1e3a8a;
        font-size: 11px;
    }

    .information-note p {
        margin: 4px 0 0;
        color: #475569;
        font-size: 10px;
        line-height: 1.5;
    }


    /* RESPONSIVE */

    @media (max-width: 1000px) {

        .preference-grid,
        .password-grid {
            grid-template-columns: 1fr;
        }
    }


    @media (max-width: 700px) {

        .settings-page {
            padding: 18px;
        }

        .page-header {
            align-items: flex-start;
            flex-direction: column;
        }

        .profile-row {
            align-items: flex-start;
            flex-wrap: wrap;
        }

        .account-status {
            width: 100%;
            justify-content: center;
            box-sizing: border-box;
        }

        .setting-row {
            align-items: flex-start;
        }

        .preference-grid,
        .password-grid {
            grid-template-columns: 1fr;
        }

        .save-section {
            justify-content: stretch;
        }

        .save-button {
            width: 100%;
            justify-content: center;
        }
    }
</style>