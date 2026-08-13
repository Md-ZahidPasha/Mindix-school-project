<script lang="ts">
    import {
        User,
        Mail,
        Phone,
        MapPin,
        Briefcase,
        Building2,
        CalendarDays,
        ShieldCheck,
        Edit3,
        Save,
        LockKeyhole,
        Eye,
        EyeOff,
        FileText
    } from '@lucide/svelte';

    let isEditing = $state(false);

    let showCurrentPassword = $state(false);
    let showNewPassword = $state(false);
    let showConfirmPassword = $state(false);

    let employee = $state({
        employeeId: 'EMP001',
        name: 'Arjun Kumar',
        email: 'arjun.kumar@example.com',
        phone: '+91 98765 43210',
        alternatePhone: '+91 91234 56789',
        department: 'Driving',
        designation: 'Driver',
        joiningDate: '15 June 2024',
        employeeType: 'Full Time',
        address: '12-4-56, Green Park Colony',
        city: 'Hyderabad',
        state: 'Telangana',
        pincode: '500001'
    });

    let passwordData = $state({
        currentPassword: '',
        newPassword: '',
        confirmPassword: ''
    });

    function saveProfile() {
        isEditing = false;

        alert(
            'Profile changes will be connected to the backend API during integration.'
        );
    }

    function changePassword() {
        if (
            !passwordData.currentPassword ||
            !passwordData.newPassword ||
            !passwordData.confirmPassword
        ) {
            alert('Please fill all password fields.');
            return;
        }

        if (
            passwordData.newPassword !==
            passwordData.confirmPassword
        ) {
            alert('New password and confirm password do not match.');
            return;
        }

        alert(
            'Password change will be connected to the backend API during integration.'
        );

        passwordData.currentPassword = '';
        passwordData.newPassword = '';
        passwordData.confirmPassword = '';
    }
</script>

<svelte:head>
    <title>My Profile | Employee Dashboard</title>
</svelte:head>

<div class="profile-page">

    <!-- HEADER -->
    <div class="page-header">

        <div class="title-row">

            <div class="title-icon">
                <User size={24} />
            </div>

            <div>
                <h1>My Profile</h1>

                <p>
                    View and manage your employee profile information.
                </p>
            </div>

        </div>


        {#if !isEditing}

            <button
                class="edit-button"
                onclick={() => isEditing = true}
            >
                <Edit3 size={16} />
                Edit Profile
            </button>

        {:else}

            <div class="header-actions">

                <button
                    class="cancel-button"
                    onclick={() => isEditing = false}
                >
                    Cancel
                </button>

                <button
                    class="save-button"
                    onclick={saveProfile}
                >
                    <Save size={16} />
                    Save Changes
                </button>

            </div>

        {/if}

    </div>


    <!-- PROFILE OVERVIEW -->
    <section class="profile-overview">

        <div class="profile-avatar">
            {employee.name.charAt(0)}
        </div>

        <div class="profile-main">

            <h2>{employee.name}</h2>

            <p>
                Employee ID:
                <strong>{employee.employeeId}</strong>
            </p>

            <span class="employee-badge">
                <ShieldCheck size={13} />
                Active Employee
            </span>

        </div>


        <div class="department-card">

            <Building2 size={21} />

            <div>

                <span>Department</span>

                <strong>
                    {employee.department}
                </strong>

            </div>

        </div>

    </section>


    <!-- PERSONAL INFORMATION -->
    <section class="card">

        <div class="card-header">

            <div class="header-icon blue">
                <User size={19} />
            </div>

            <div>

                <h2>Personal Information</h2>

                <p>
                    Your basic employee account information.
                </p>

            </div>

        </div>


        <div class="form-grid">

            <!-- NAME -->
            <div class="form-group">

                <label for="employeeName">
                    Full Name
                </label>

                <div class="input-wrapper">

                    <User size={16} />

                    <input
                        id="employeeName"
                        type="text"
                        bind:value={employee.name}
                        disabled={!isEditing}
                    />

                </div>

            </div>


            <!-- EMPLOYEE ID -->
            <div class="form-group">

                <label for="employeeId">
                    Employee ID
                </label>

                <div class="input-wrapper">

                    <ShieldCheck size={16} />

                    <input
                        id="employeeId"
                        type="text"
                        value={employee.employeeId}
                        disabled
                    />

                </div>

                <small>
                    Employee ID is assigned by the school administration.
                </small>

            </div>


            <!-- EMAIL -->
            <div class="form-group">

                <label for="email">
                    Email Address
                </label>

                <div class="input-wrapper">

                    <Mail size={16} />

                    <input
                        id="email"
                        type="email"
                        bind:value={employee.email}
                        disabled={!isEditing}
                    />

                </div>

            </div>


            <!-- PHONE -->
            <div class="form-group">

                <label for="phone">
                    Primary Phone
                </label>

                <div class="input-wrapper">

                    <Phone size={16} />

                    <input
                        id="phone"
                        type="tel"
                        bind:value={employee.phone}
                        disabled={!isEditing}
                    />

                </div>

            </div>


            <!-- ALTERNATE PHONE -->
            <div class="form-group">

                <label for="alternatePhone">
                    Alternate Phone
                </label>

                <div class="input-wrapper">

                    <Phone size={16} />

                    <input
                        id="alternatePhone"
                        type="tel"
                        bind:value={employee.alternatePhone}
                        disabled={!isEditing}
                    />

                </div>

            </div>


            <!-- EMPLOYEE TYPE -->
            <div class="form-group">

                <label for="employeeType">
                    Employment Type
                </label>

                <div class="input-wrapper">

                    <Briefcase size={16} />

                    <input
                        id="employeeType"
                        type="text"
                        bind:value={employee.employeeType}
                        disabled={!isEditing}
                    />

                </div>

            </div>

        </div>

    </section>


    <!-- EMPLOYMENT INFORMATION -->
    <section class="card">

        <div class="card-header">

            <div class="header-icon purple">
                <Briefcase size={19} />
            </div>

            <div>

                <h2>Employment Information</h2>

                <p>
                    Your department and employment details.
                </p>

            </div>

        </div>


        <div class="form-grid">

            <!-- DEPARTMENT -->
            <div class="form-group">

                <label for="department">
                    Department
                </label>

                <div class="input-wrapper">

                    <Building2 size={16} />

                    <input
                        id="department"
                        type="text"
                        value={employee.department}
                        disabled
                    />

                </div>

            </div>


            <!-- DESIGNATION -->
            <div class="form-group">

                <label for="designation">
                    Designation
                </label>

                <div class="input-wrapper">

                    <Briefcase size={16} />

                    <input
                        id="designation"
                        type="text"
                        value={employee.designation}
                        disabled
                    />

                </div>

            </div>


            <!-- JOINING DATE -->
            <div class="form-group">

                <label for="joiningDate">
                    Joining Date
                </label>

                <div class="input-wrapper">

                    <CalendarDays size={16} />

                    <input
                        id="joiningDate"
                        type="text"
                        value={employee.joiningDate}
                        disabled
                    />

                </div>

            </div>


            <!-- STATUS -->
            <div class="form-group">

                <label for="status">
                    Employment Status
                </label>

                <div class="input-wrapper">

                    <ShieldCheck size={16} />

                    <input
                        id="status"
                        type="text"
                        value="Active"
                        disabled
                    />

                </div>

            </div>

        </div>

    </section>


    <!-- ADDRESS -->
    <section class="card">

        <div class="card-header">

            <div class="header-icon orange">
                <MapPin size={19} />
            </div>

            <div>

                <h2>Address</h2>

                <p>
                    Your registered residential address.
                </p>

            </div>

        </div>


        <div class="form-grid">

            <div class="form-group full">

                <label for="address">
                    Address
                </label>

                <div class="input-wrapper">

                    <MapPin size={16} />

                    <input
                        id="address"
                        type="text"
                        bind:value={employee.address}
                        disabled={!isEditing}
                    />

                </div>

            </div>


            <div class="form-group">

                <label for="city">
                    City
                </label>

                <div class="input-wrapper">

                    <MapPin size={16} />

                    <input
                        id="city"
                        type="text"
                        bind:value={employee.city}
                        disabled={!isEditing}
                    />

                </div>

            </div>


            <div class="form-group">

                <label for="state">
                    State
                </label>

                <div class="input-wrapper">

                    <MapPin size={16} />

                    <input
                        id="state"
                        type="text"
                        bind:value={employee.state}
                        disabled={!isEditing}
                    />

                </div>

            </div>


            <div class="form-group">

                <label for="pincode">
                    PIN Code
                </label>

                <div class="input-wrapper">

                    <MapPin size={16} />

                    <input
                        id="pincode"
                        type="text"
                        bind:value={employee.pincode}
                        disabled={!isEditing}
                    />

                </div>

            </div>

        </div>

    </section>


    <!-- ACCOUNT SECURITY -->
    <section class="card">

        <div class="card-header">

            <div class="header-icon red">
                <LockKeyhole size={19} />
            </div>

            <div>

                <h2>Account Security</h2>

                <p>
                    Change your employee account password.
                </p>

            </div>

        </div>


        <div class="password-section">

            <!-- CURRENT PASSWORD -->
            <div class="password-field">

                <label for="currentPassword">
                    Current Password
                </label>

                <div class="password-wrapper">

                    <LockKeyhole size={16} />

                    <input
                        id="currentPassword"
                        type={
                            showCurrentPassword
                                ? 'text'
                                : 'password'
                        }
                        bind:value={passwordData.currentPassword}
                        placeholder="Enter current password"
                    />

                    <button
                        type="button"
                        class="visibility-button"
                        onclick={() =>
                            showCurrentPassword =
                                !showCurrentPassword
                        }
                    >
                        {#if showCurrentPassword}
                            <EyeOff size={16} />
                        {:else}
                            <Eye size={16} />
                        {/if}
                    </button>

                </div>

            </div>


            <!-- NEW PASSWORD -->
            <div class="password-field">

                <label for="newPassword">
                    New Password
                </label>

                <div class="password-wrapper">

                    <LockKeyhole size={16} />

                    <input
                        id="newPassword"
                        type={
                            showNewPassword
                                ? 'text'
                                : 'password'
                        }
                        bind:value={passwordData.newPassword}
                        placeholder="Enter new password"
                    />

                    <button
                        type="button"
                        class="visibility-button"
                        onclick={() =>
                            showNewPassword =
                                !showNewPassword
                        }
                    >
                        {#if showNewPassword}
                            <EyeOff size={16} />
                        {:else}
                            <Eye size={16} />
                        {/if}
                    </button>

                </div>

            </div>


            <!-- CONFIRM PASSWORD -->
            <div class="password-field">

                <label for="confirmPassword">
                    Confirm New Password
                </label>

                <div class="password-wrapper">

                    <LockKeyhole size={16} />

                    <input
                        id="confirmPassword"
                        type={
                            showConfirmPassword
                                ? 'text'
                                : 'password'
                        }
                        bind:value={passwordData.confirmPassword}
                        placeholder="Confirm new password"
                    />

                    <button
                        type="button"
                        class="visibility-button"
                        onclick={() =>
                            showConfirmPassword =
                                !showConfirmPassword
                        }
                    >
                        {#if showConfirmPassword}
                            <EyeOff size={16} />
                        {:else}
                            <Eye size={16} />
                        {/if}
                    </button>

                </div>

            </div>

        </div>


        <div class="security-actions">

            <button
                class="change-password-button"
                onclick={changePassword}
            >
                <LockKeyhole size={15} />
                Change Password
            </button>

        </div>

    </section>


    <!-- EMPLOYEE INFORMATION NOTE -->
    <section class="employee-note">

        <div class="note-icon">
            <ShieldCheck size={19} />
        </div>

        <div>

            <strong>
                Employee Account
            </strong>

            <p>
                Your Employee ID, department, designation and
                employment details are managed by the school
                administration.
            </p>

        </div>

    </section>


    <!-- API NOTE -->
    <div class="info-note">

        <div class="info-icon">
            <FileText size={18} />
        </div>

        <div>

            <strong>
                Profile Information
            </strong>

            <p>
                This page currently uses demo data. During API
                integration, employee details and account
                information will be loaded from the backend.
            </p>

        </div>

    </div>

</div>


<style>
    .profile-page {
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


    /* BUTTONS */

    .edit-button,
    .save-button,
    .cancel-button {
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 7px;
        padding: 9px 14px;
        border-radius: 9px;
        font-size: 10px;
        font-weight: 700;
        cursor: pointer;
    }

    .edit-button {
        border: 1px solid #bfdbfe;
        background: #eff6ff;
        color: #2563eb;
    }

    .edit-button:hover {
        background: #dbeafe;
    }

    .header-actions {
        display: flex;
        align-items: center;
        gap: 8px;
    }

    .cancel-button {
        border: 1px solid #dbe3ef;
        background: white;
        color: #64748b;
    }

    .save-button {
        border: 1px solid #2563eb;
        background: #2563eb;
        color: white;
    }

    .save-button:hover {
        background: #1d4ed8;
    }


    /* PROFILE OVERVIEW */

    .profile-overview {
        display: flex;
        align-items: center;
        gap: 16px;
        padding: 22px;
        margin-bottom: 20px;
        border: 1px solid #dbe5f2;
        border-radius: 15px;
        background: white;
        box-shadow: 0 3px 12px rgba(15, 23, 42, 0.03);
    }

    .profile-avatar {
        width: 68px;
        height: 68px;
        display: flex;
        align-items: center;
        justify-content: center;
        flex-shrink: 0;
        border-radius: 50%;
        background: #2563eb;
        color: white;
        font-size: 26px;
        font-weight: 800;
    }

    .profile-main {
        flex: 1;
    }

    .profile-main h2 {
        margin: 0;
        color: #0f172a;
        font-size: 20px;
    }

    .profile-main p {
        margin: 5px 0 8px;
        color: #64748b;
        font-size: 11px;
    }

    .profile-main strong {
        color: #334155;
    }

    .employee-badge {
        display: inline-flex;
        align-items: center;
        gap: 4px;
        padding: 5px 8px;
        border-radius: 7px;
        background: #ecfdf5;
        color: #059669;
        font-size: 9px;
        font-weight: 700;
    }

    .department-card {
        display: flex;
        align-items: center;
        gap: 10px;
        min-width: 150px;
        padding: 12px 15px;
        border-radius: 11px;
        background: #eef4ff;
        color: #2563eb;
    }

    .department-card span {
        display: block;
        color: #64748b;
        font-size: 9px;
    }

    .department-card strong {
        display: block;
        margin-top: 2px;
        color: #2563eb;
        font-size: 14px;
    }


    /* CARD */

    .card {
        padding: 22px;
        margin-bottom: 20px;
        border: 1px solid #e2e8f0;
        border-radius: 15px;
        background: white;
        box-shadow: 0 3px 12px rgba(15, 23, 42, 0.03);
    }

    .card-header {
        display: flex;
        align-items: center;
        gap: 11px;
        margin-bottom: 20px;
    }

    .header-icon {
        width: 39px;
        height: 39px;
        display: flex;
        align-items: center;
        justify-content: center;
        flex-shrink: 0;
        border-radius: 10px;
    }

    .header-icon.blue {
        background: #eef4ff;
        color: #2563eb;
    }

    .header-icon.purple {
        background: #f5f3ff;
        color: #7c3aed;
    }

    .header-icon.orange {
        background: #fff7ed;
        color: #ea580c;
    }

    .header-icon.red {
        background: #fef2f2;
        color: #dc2626;
    }

    .card-header h2 {
        margin: 0;
        color: #0f172a;
        font-size: 16px;
    }

    .card-header p {
        margin: 3px 0 0;
        color: #64748b;
        font-size: 10px;
    }


    /* FORM */

    .form-grid {
        display: grid;
        grid-template-columns: repeat(2, 1fr);
        gap: 17px;
    }

    .form-group {
        min-width: 0;
    }

    .form-group.full {
        grid-column: 1 / -1;
    }

    .form-group label,
    .password-field label {
        display: block;
        margin-bottom: 6px;
        color: #475569;
        font-size: 10px;
        font-weight: 700;
    }

    .input-wrapper {
        position: relative;
        display: flex;
        align-items: center;
    }

    .input-wrapper input {
        width: 100%;
        height: 42px;
        box-sizing: border-box;
        padding: 0 12px 0 36px;
        border: 1px solid #dbe3ef;
        border-radius: 9px;
        outline: none;
        background: white;
        color: #334155;
        font-size: 11px;
    }

    .input-wrapper input:focus {
        border-color: #93c5fd;
        box-shadow: 0 0 0 3px #eff6ff;
    }

    .input-wrapper input:disabled {
        background: #f8fafc;
        color: #64748b;
        cursor: not-allowed;
    }

    .form-group small {
        display: block;
        margin-top: 5px;
        color: #94a3b8;
        font-size: 8px;
    }


    /* PASSWORD */

    .password-section {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 15px;
    }

    .password-field {
        min-width: 0;
    }

    .password-wrapper {
        position: relative;
        display: flex;
        align-items: center;
    }

    .password-wrapper input {
        width: 100%;
        height: 42px;
        box-sizing: border-box;
        padding: 0 38px 0 36px;
        border: 1px solid #dbe3ef;
        border-radius: 9px;
        outline: none;
        background: white;
        color: #334155;
        font-size: 11px;
    }

    .password-wrapper input:focus {
        border-color: #93c5fd;
        box-shadow: 0 0 0 3px #eff6ff;
    }

    .visibility-button {
        position: absolute;
        right: 8px;
        width: 28px;
        height: 28px;
        display: flex;
        align-items: center;
        justify-content: center;
        border: 0;
        background: transparent;
        color: #64748b;
        cursor: pointer;
    }

    .visibility-button:hover {
        color: #2563eb;
    }

    .security-actions {
        display: flex;
        justify-content: flex-end;
        margin-top: 17px;
    }

    .change-password-button {
        display: flex;
        align-items: center;
        gap: 6px;
        padding: 9px 13px;
        border: 1px solid #2563eb;
        border-radius: 8px;
        background: #2563eb;
        color: white;
        font-size: 10px;
        font-weight: 700;
        cursor: pointer;
    }

    .change-password-button:hover {
        background: #1d4ed8;
    }


    /* NOTES */

    .employee-note,
    .info-note {
        display: flex;
        align-items: flex-start;
        gap: 11px;
        padding: 15px;
        margin-bottom: 12px;
        border: 1px solid #bfdbfe;
        border-radius: 11px;
        background: #eff6ff;
    }

    .note-icon,
    .info-icon {
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

    .employee-note strong,
    .info-note strong {
        display: block;
        color: #1e3a8a;
        font-size: 11px;
    }

    .employee-note p,
    .info-note p {
        margin: 4px 0 0;
        color: #475569;
        font-size: 10px;
        line-height: 1.5;
    }

    .info-note {
        margin-bottom: 0;
        border-color: #dbe5f2;
        background: #f8fbff;
    }

    .info-note .info-icon {
        background: #eef4ff;
    }

    .info-note strong {
        color: #334155;
    }

    .info-note p {
        color: #64748b;
    }


    /* RESPONSIVE */

    @media (max-width: 1000px) {

        .profile-page {
            padding: 24px;
        }

        .password-section {
            grid-template-columns: 1fr;
        }
    }


    @media (max-width: 700px) {

        .profile-page {
            padding: 18px;
        }

        .page-header {
            align-items: flex-start;
            flex-direction: column;
        }

        .profile-overview {
            align-items: flex-start;
            flex-wrap: wrap;
        }

        .department-card {
            width: 100%;
        }

        .form-grid {
            grid-template-columns: 1fr;
        }

        .form-group.full {
            grid-column: auto;
        }

        .header-actions {
            width: 100%;
        }

        .header-actions button {
            flex: 1;
        }
    }
</style>