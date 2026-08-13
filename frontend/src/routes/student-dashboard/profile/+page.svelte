<script lang="ts">
    import { getProfile } from '$lib/services/studentApi';
    import {
        UserCircle,
        Mail,
        Phone,
        GraduationCap,
        CalendarDays,
        MapPin,
        Hash,
        User
    } from '@lucide/svelte';

    let profileData = $state<any>(null);
    let loading = $state(true);
    let error = $state('');

    async function loadProfile() {
        try {
            loading = true;
            error = '';

            profileData = await getProfile();
        } catch (err) {
            console.error('Failed to load student profile:', err);
            error = 'Unable to load profile data.';
        } finally {
            loading = false;
        }
    }

    loadProfile();
</script>

<svelte:head>
    <title>My Profile | PaperBuddy</title>
</svelte:head>

<div class="profile-page">
    <div class="page-header">
        <div>
            <h1>My Profile</h1>
            <p>View your personal and academic information.</p>
        </div>
    </div>

    {#if loading}
        <div class="state-card">
            <p>Loading profile...</p>
        </div>
    {:else if error}
        <div class="state-card error-card">
            <p>{error}</p>
        </div>
    {:else if profileData}
        <section class="profile-card">
            <div class="profile-top">
                <div class="avatar">
                    <UserCircle size={48} />
                </div>

                <div>
                    <h2>{profileData.name ?? 'Student'}</h2>
                    <p>Student</p>
                </div>
            </div>

            <div class="profile-grid">
                <div class="info-item">
                    <div class="icon-box">
                        <Mail size={19} />
                    </div>
                    <div>
                        <span>Email</span>
                        <strong>{profileData.email ?? '-'}</strong>
                    </div>
                </div>

                <div class="info-item">
                    <div class="icon-box">
                        <Phone size={19} />
                    </div>
                    <div>
                        <span>Phone</span>
                        <strong>{profileData.phone ?? '-'}</strong>
                    </div>
                </div>

                <div class="info-item">
                    <div class="icon-box">
                        <Hash size={19} />
                    </div>
                    <div>
                        <span>Roll Number</span>
                        <strong>{profileData.roll_number ?? '-'}</strong>
                    </div>
                </div>

                <div class="info-item">
                    <div class="icon-box">
                        <Hash size={19} />
                    </div>
                    <div>
                        <span>Admission Number</span>
                        <strong>{profileData.admission_number ?? '-'}</strong>
                    </div>
                </div>

                <div class="info-item">
                    <div class="icon-box">
                        <GraduationCap size={19} />
                    </div>
                    <div>
                        <span>Class</span>
                        <strong>
                            {profileData.class ?? '-'}
                            {profileData.section
                                ? ` - ${profileData.section}`
                                : ''}
                        </strong>
                    </div>
                </div>

                <div class="info-item">
                    <div class="icon-box">
                        <CalendarDays size={19} />
                    </div>
                    <div>
                        <span>Date of Birth</span>
                        <strong>{profileData.date_of_birth ?? '-'}</strong>
                    </div>
                </div>

                <div class="info-item">
                    <div class="icon-box">
                        <User size={19} />
                    </div>
                    <div>
                        <span>Gender</span>
                        <strong>{profileData.gender ?? '-'}</strong>
                    </div>
                </div>

                <div class="info-item">
                    <div class="icon-box">
                        <MapPin size={19} />
                    </div>
                    <div>
                        <span>Institution</span>
                        <strong>{profileData.institution ?? '-'}</strong>
                    </div>
                </div>
            </div>
        </section>
    {:else}
        <div class="state-card">
            <p>No profile information available.</p>
        </div>
    {/if}
</div>

<style>
    .profile-page {
        min-height: 100vh;
        padding: 32px;
        background: #f8fafc;
    }

    .page-header {
        margin-bottom: 24px;
    }

    .page-header h1 {
        margin: 0;
        color: #0f172a;
        font-size: 30px;
        font-weight: 800;
    }

    .page-header p {
        margin: 8px 0 0;
        color: #64748b;
        font-size: 14px;
    }

    .profile-card {
        padding: 28px;
        background: white;
        border: 1px solid #e2e8f0;
        border-radius: 18px;
        box-shadow: 0 8px 25px rgba(15, 23, 42, 0.05);
    }

    .profile-top {
        display: flex;
        align-items: center;
        gap: 16px;
        padding-bottom: 24px;
        border-bottom: 1px solid #e2e8f0;
    }

    .avatar {
        display: flex;
        align-items: center;
        justify-content: center;
        width: 72px;
        height: 72px;
        color: #2563eb;
        background: #eff6ff;
        border-radius: 18px;
    }

    .profile-top h2 {
        margin: 0;
        color: #0f172a;
        font-size: 22px;
        font-weight: 800;
    }

    .profile-top p {
        margin: 5px 0 0;
        color: #64748b;
        font-size: 13px;
    }

    .profile-grid {
        display: grid;
        grid-template-columns: repeat(2, 1fr);
        gap: 16px;
        margin-top: 24px;
    }

    .info-item {
        display: flex;
        align-items: center;
        gap: 13px;
        padding: 17px;
        background: #f8fafc;
        border: 1px solid #e2e8f0;
        border-radius: 13px;
    }

    .icon-box {
        display: flex;
        align-items: center;
        justify-content: center;
        flex-shrink: 0;
        width: 40px;
        height: 40px;
        color: #2563eb;
        background: #eff6ff;
        border-radius: 10px;
    }

    .info-item span {
        display: block;
        margin-bottom: 5px;
        color: #64748b;
        font-size: 11px;
    }

    .info-item strong {
        display: block;
        color: #0f172a;
        font-size: 14px;
    }

    .state-card {
        display: flex;
        align-items: center;
        justify-content: center;
        min-height: 180px;
        padding: 30px;
        background: white;
        border: 1px solid #e2e8f0;
        border-radius: 18px;
        color: #64748b;
        text-align: center;
    }

    .state-card p {
        margin: 0;
        font-size: 14px;
    }

    .error-card {
        color: #dc2626;
        background: #fef2f2;
        border-color: #fecaca;
    }

    @media (max-width: 800px) {
        .profile-page {
            padding: 22px;
        }

        .profile-grid {
            grid-template-columns: 1fr;
        }
    }

    @media (max-width: 500px) {
        .profile-page {
            padding: 16px;
        }

        .profile-card {
            padding: 20px;
        }
    }
</style>