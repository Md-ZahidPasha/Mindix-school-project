<script lang="ts">
    import PrincipalSidebar from '$lib/components/principal/PrincipalSidebar.svelte';

    let isEditing = $state(false);
    let showPasswordForm = $state(false);

    let fullName = $state('Principal');
    let email = $state('principal@school.edu');
    let phone = $state('+91 98765 43210');

    let newPassword = $state('');
    let confirmPassword = $state('');

    let message = $state('');

    function saveProfile() {
        isEditing = false;
        message = 'Profile details updated successfully.';
    }

    function changePassword() {
        message = '';

        if (!newPassword || !confirmPassword) {
            message = 'Please enter the new password in both fields.';
            return;
        }

        if (newPassword !== confirmPassword) {
            message = 'Passwords do not match.';
            return;
        }

        message = 'Password updated successfully.';
        newPassword = '';
        confirmPassword = '';
        showPasswordForm = false;
    }
</script>


<div class="principal-layout">

    <PrincipalSidebar />

    <main class="main-content">

        <div class="profile-page">

            <!-- PAGE HEADER -->

            <header class="page-header">
                <div>
                    <h1>Profile</h1>

                    <p>
                        View and manage your principal account information.
                    </p>
                </div>
            </header>


            <!-- PROFILE HEADER -->

            <section class="profile-card">

                <div class="profile-avatar">
                    P
                </div>

                <div class="profile-main-info">

                    <h2>{fullName}</h2>

                    <span class="designation">
                        Principal
                    </span>

                    <p>
                        PaperBuddy School
                    </p>

                </div>

                <div class="profile-status">
                    <span class="status-dot"></span>
                    Active
                </div>

            </section>


            <!-- MESSAGE -->

            {#if message}
                <div class="message">
                    {message}
                </div>
            {/if}


            <!-- PERSONAL INFORMATION -->

            <section class="information-card">

                <div class="card-header">

                    <div>
                        <h2>Personal Information</h2>

                        <p>
                            Your personal and contact details.
                        </p>
                    </div>

                    <button
                        type="button"
                        class="edit-button"
                        onclick={() => {
                            isEditing = !isEditing;
                            message = '';
                        }}
                    >
                        {isEditing ? 'Cancel' : 'Edit Profile'}
                    </button>

                </div>


                <div class="details-grid">

                    <!-- FULL NAME -->

                    <div class="detail-field">

                        <label for="full-name">
                            Full Name
                        </label>

                        {#if isEditing}

                            <input
                                id="full-name"
                                type="text"
                                bind:value={fullName}
                            />

                        {:else}

                            <div class="detail-value">
                                {fullName}
                            </div>

                        {/if}

                    </div>


                    <!-- PRINCIPAL ID -->

                    <div class="detail-field">

                        <span class="detail-label">
                            Principal ID
                        </span>

                        <div class="detail-value">
                            PRN001
                        </div>

                    </div>


                    <!-- EMAIL -->

                    <div class="detail-field">

                        <label for="email">
                            Email Address
                        </label>

                        {#if isEditing}

                            <input
                                id="email"
                                type="email"
                                bind:value={email}
                            />

                        {:else}

                            <div class="detail-value">
                                {email}
                            </div>

                        {/if}

                    </div>


                    <!-- PHONE -->

                    <div class="detail-field">

                        <label for="phone">
                            Phone Number
                        </label>

                        {#if isEditing}

                            <input
                                id="phone"
                                type="tel"
                                bind:value={phone}
                            />

                        {:else}

                            <div class="detail-value">
                                {phone}
                            </div>

                        {/if}

                    </div>


                    <!-- DATE OF BIRTH -->

                    <div class="detail-field">

                        <span class="detail-label">
                            Date of Birth
                        </span>

                        <div class="detail-value">
                            15 June 1980
                        </div>

                    </div>


                    <!-- GENDER -->

                    <div class="detail-field">

                        <span class="detail-label">
                            Gender
                        </span>

                        <div class="detail-value">
                            Not Specified
                        </div>

                    </div>

                </div>


                <!-- EDIT ACTIONS -->

                {#if isEditing}

                    <div class="form-actions">

                        <button
                            type="button"
                            class="cancel-button"
                            onclick={() => {
                                isEditing = false;
                                message = '';
                            }}
                        >
                            Cancel
                        </button>

                        <button
                            type="button"
                            class="save-button"
                            onclick={saveProfile}
                        >
                            Save Changes
                        </button>

                    </div>

                {/if}

            </section>


            <!-- INSTITUTION INFORMATION -->

            <section class="information-card">

                <div class="card-header">

                    <div>
                        <h2>Institution Information</h2>

                        <p>
                            Information about your school and designation.
                        </p>
                    </div>

                </div>


                <div class="details-grid">

                    <!-- SCHOOL NAME -->

                    <div class="detail-field">

                        <span class="detail-label">
                            School Name
                        </span>

                        <div class="detail-value">
                            PaperBuddy School
                        </div>

                    </div>


                    <!-- SCHOOL ID -->

                    <div class="detail-field">

                        <span class="detail-label">
                            School ID
                        </span>

                        <div class="detail-value">
                            SCH001
                        </div>

                    </div>


                    <!-- DESIGNATION -->

                    <div class="detail-field">

                        <span class="detail-label">
                            Designation
                        </span>

                        <div class="detail-value">
                            Principal
                        </div>

                    </div>


                    <!-- JOINING DATE -->

                    <div class="detail-field">

                        <span class="detail-label">
                            Joining Date
                        </span>

                        <div class="detail-value">
                            01 June 2018
                        </div>

                    </div>


                    <!-- ACADEMIC YEAR -->

                    <div class="detail-field">

                        <span class="detail-label">
                            Academic Year
                        </span>

                        <div class="detail-value">
                            2026 - 2027
                        </div>

                    </div>


                    <!-- INSTITUTION TYPE -->

                    <div class="detail-field">

                        <span class="detail-label">
                            Institution Type
                        </span>

                        <div class="detail-value">
                            School
                        </div>

                    </div>

                </div>

            </section>


            <!-- CONTACT INFORMATION -->

            <section class="information-card">

                <div class="card-header">

                    <div>
                        <h2>Contact Information</h2>

                        <p>
                            Your registered contact address.
                        </p>
                    </div>

                </div>


                <div class="details-grid">

                    <!-- ADDRESS -->

                    <div class="detail-field full-width">

                        <span class="detail-label">
                            Address
                        </span>

                        <div class="detail-value">
                            School Administration Office
                        </div>

                    </div>


                    <!-- CITY -->

                    <div class="detail-field">

                        <span class="detail-label">
                            City
                        </span>

                        <div class="detail-value">
                            Siddipet
                        </div>

                    </div>


                    <!-- STATE -->

                    <div class="detail-field">

                        <span class="detail-label">
                            State
                        </span>

                        <div class="detail-value">
                            Telangana
                        </div>

                    </div>


                    <!-- PIN CODE -->

                    <div class="detail-field">

                        <span class="detail-label">
                            PIN Code
                        </span>

                        <div class="detail-value">
                            502103
                        </div>

                    </div>

                </div>

            </section>


            <!-- ACCOUNT SECURITY -->

            <section class="information-card security-card">

                <div class="card-header">

                    <div>
                        <h2>Account Security</h2>

                        <p>
                            Manage your account password.
                        </p>
                    </div>

                    <button
                        type="button"
                        class="edit-button"
                        onclick={() => {
                            showPasswordForm = !showPasswordForm;
                            message = '';
                        }}
                    >
                        {showPasswordForm
                            ? 'Cancel'
                            : 'Change Password'}
                    </button>

                </div>


                {#if showPasswordForm}

                    <div class="password-form">

                        <!-- NEW PASSWORD -->

                        <div class="detail-field">

                            <label for="new-password">
                                New Password
                            </label>

                            <input
                                id="new-password"
                                type="password"
                                bind:value={newPassword}
                                placeholder="Enter new password"
                            />

                        </div>


                        <!-- CONFIRM PASSWORD -->

                        <div class="detail-field">

                            <label for="confirm-password">
                                Confirm Password
                            </label>

                            <input
                                id="confirm-password"
                                type="password"
                                bind:value={confirmPassword}
                                placeholder="Confirm new password"
                            />

                        </div>


                        <button
                            type="button"
                            class="save-button"
                            onclick={changePassword}
                        >
                            Update Password
                        </button>

                    </div>

                {:else}

                    <div class="security-info">

                        <div class="security-icon">
                            🔒
                        </div>

                        <div>

                            <strong>
                                Password protected
                            </strong>

                            <p>
                                Your account password is securely protected.
                            </p>

                        </div>

                    </div>

                {/if}

            </section>

        </div>

    </main>

</div>


<style>

    .principal-layout {
        display: flex;
        min-height: 100vh;
        background: #f7f9fc;
    }


    .main-content {
        flex: 1;
        min-width: 0;
    }


    .profile-page {
        min-height: 100vh;
        padding: 28px 32px;
        box-sizing: border-box;
        background: #f7f9fc;
    }


    /* PAGE HEADER */

    .page-header {
        margin-bottom: 24px;
    }


    .page-header h1 {
        margin: 0;
        color: #14213d;
        font-size: 30px;
    }


    .page-header p {
        margin: 7px 0 0;
        color: #64748b;
        font-size: 15px;
    }


    /* PROFILE CARD */

    .profile-card {
        display: flex;
        align-items: center;
        gap: 18px;
        padding: 24px;
        background: white;
        border: 1px solid #e5eaf2;
        border-radius: 16px;
        box-shadow: 0 4px 14px rgba(15, 23, 42, 0.03);
    }


    .profile-avatar {
        width: 72px;
        height: 72px;
        flex-shrink: 0;
        display: flex;
        align-items: center;
        justify-content: center;
        border-radius: 50%;
        background: #e8f0ff;
        color: #2563eb;
        font-size: 30px;
        font-weight: 700;
    }


    .profile-main-info {
        flex: 1;
    }


    .profile-main-info h2 {
        margin: 0;
        color: #14213d;
        font-size: 21px;
    }


    .designation {
        display: inline-block;
        margin-top: 4px;
        color: #2563eb;
        font-size: 12px;
        font-weight: 600;
    }


    .profile-main-info p {
        margin: 4px 0 0;
        color: #64748b;
        font-size: 12px;
    }


    .profile-status {
        display: flex;
        align-items: center;
        gap: 7px;
        padding: 7px 10px;
        border-radius: 8px;
        background: #f0fdf4;
        color: #16a34a;
        font-size: 11px;
        font-weight: 600;
    }


    .status-dot {
        width: 7px;
        height: 7px;
        border-radius: 50%;
        background: #22c55e;
    }


    /* MESSAGE */

    .message {
        margin-top: 14px;
        padding: 11px 13px;
        border: 1px solid #bfdbfe;
        border-radius: 9px;
        background: #eff6ff;
        color: #2563eb;
        font-size: 11px;
    }


    /* INFORMATION CARD */

    .information-card {
        margin-top: 20px;
        padding: 22px;
        background: white;
        border: 1px solid #e5eaf2;
        border-radius: 16px;
        box-shadow: 0 4px 14px rgba(15, 23, 42, 0.03);
    }


    .card-header {
        display: flex;
        align-items: flex-start;
        justify-content: space-between;
        gap: 20px;
        margin-bottom: 20px;
        padding-bottom: 15px;
        border-bottom: 1px solid #edf1f6;
    }


    .card-header h2 {
        margin: 0;
        color: #14213d;
        font-size: 17px;
    }


    .card-header p {
        margin: 4px 0 0;
        color: #64748b;
        font-size: 11px;
    }


    /* BUTTON */

    .edit-button {
        height: 36px;
        padding: 0 13px;
        border: 1px solid #dbe3ef;
        border-radius: 8px;
        background: white;
        color: #2563eb;
        font-size: 11px;
        font-weight: 600;
        cursor: pointer;
    }


    .edit-button:hover {
        background: #eef4ff;
    }


    /* DETAILS */

    .details-grid {
        display: grid;
        grid-template-columns: repeat(2, 1fr);
        gap: 18px 24px;
    }


    .detail-field {
        min-width: 0;
    }


    .detail-field.full-width {
        grid-column: span 2;
    }


    .detail-label {
        display: block;
        margin-bottom: 6px;
        color: #64748b;
        font-size: 10px;
        font-weight: 600;
    }


    .detail-field label {
        display: block;
        margin-bottom: 6px;
        color: #64748b;
        font-size: 10px;
        font-weight: 600;
    }


    .detail-value {
        min-height: 40px;
        display: flex;
        align-items: center;
        padding: 0 11px;
        box-sizing: border-box;
        border: 1px solid #e5eaf2;
        border-radius: 8px;
        background: #f8fafc;
        color: #1e293b;
        font-size: 12px;
    }


    .detail-field input {
        width: 100%;
        height: 40px;
        padding: 0 11px;
        box-sizing: border-box;
        border: 1px solid #dbe3ef;
        border-radius: 8px;
        background: white;
        color: #1e293b;
        font-size: 12px;
        outline: none;
    }


    .detail-field input:focus {
        border-color: #2563eb;
        box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.1);
    }


    /* FORM ACTIONS */

    .form-actions {
        display: flex;
        justify-content: flex-end;
        gap: 8px;
        margin-top: 18px;
        padding-top: 15px;
        border-top: 1px solid #edf1f6;
    }


    .cancel-button,
    .save-button {
        height: 38px;
        padding: 0 15px;
        border-radius: 8px;
        font-size: 11px;
        font-weight: 600;
        cursor: pointer;
    }


    .cancel-button {
        border: 1px solid #dbe3ef;
        background: white;
        color: #64748b;
    }


    .save-button {
        border: none;
        background: #2563eb;
        color: white;
    }


    .save-button:hover {
        background: #1d4ed8;
    }


    /* SECURITY */

    .security-info {
        display: flex;
        align-items: center;
        gap: 12px;
        padding: 14px;
        border: 1px solid #e5eaf2;
        border-radius: 10px;
        background: #f8fafc;
    }


    .security-icon {
        width: 38px;
        height: 38px;
        display: flex;
        align-items: center;
        justify-content: center;
        border-radius: 9px;
        background: #eef4ff;
        font-size: 16px;
    }


    .security-info strong {
        display: block;
        color: #334155;
        font-size: 12px;
    }


    .security-info p {
        margin: 3px 0 0;
        color: #64748b;
        font-size: 10px;
    }


    /* PASSWORD */

    .password-form {
        display: grid;
        grid-template-columns: 1fr 1fr auto;
        align-items: end;
        gap: 14px;
    }


    .password-form .save-button {
        height: 40px;
        white-space: nowrap;
    }


    /* RESPONSIVE */

    @media (max-width: 850px) {

        .profile-page {
            padding: 22px;
        }

        .password-form {
            grid-template-columns: 1fr 1fr;
        }

        .password-form .save-button {
            grid-column: span 2;
        }

    }


    @media (max-width: 600px) {

        .profile-page {
            padding: 18px;
        }

        .profile-card {
            align-items: flex-start;
            flex-wrap: wrap;
        }

        .profile-status {
            width: 100%;
            box-sizing: border-box;
        }

        .details-grid {
            grid-template-columns: 1fr;
        }

        .detail-field.full-width {
            grid-column: span 1;
        }

        .card-header {
            align-items: flex-start;
            flex-direction: column;
        }

        .edit-button {
            width: 100%;
        }

        .password-form {
            grid-template-columns: 1fr;
        }

        .password-form .save-button {
            grid-column: span 1;
            width: 100%;
        }

    }

</style>