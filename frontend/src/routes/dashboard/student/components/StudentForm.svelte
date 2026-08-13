<script lang="ts">

    // -------------------------------------------------------
    // Student Details
    // -------------------------------------------------------

    let admissionNo = $state('');
    let studentName = $state('');
    let email = $state('');
    let phone = $state('');
    let gender = $state('');
    let dob = $state('');


    // -------------------------------------------------------
    // Academic Details
    // -------------------------------------------------------

    let classGrade = $state('');
    let section = $state('');
    let studentId = $state('');
    let previousSchoolName = $state('');
    let previousAcademicMarks = $state('');


    // -------------------------------------------------------
    // Parent Details
    // -------------------------------------------------------
    let parentId = $state('');
    let fatherName = $state('');
    let fatherOccupation = $state('');
    let motherName = $state('');
    let motherOccupation = $state('');
    let parentPassword = $state('');
    let confirmParentPassword = $state('');


    // -------------------------------------------------------
    // Student Account
    // -------------------------------------------------------

    let studentPassword = $state('');
    let confirmStudentPassword = $state('');


    // -------------------------------------------------------
    // Profile Photo
    // -------------------------------------------------------

    let profileImage = $state<string | null>(null);

    let imageInput: HTMLInputElement;


    // -------------------------------------------------------
    // Transfer Certificate
    // -------------------------------------------------------

    let transferCertificate=$state<File | null >(null);


    // -------------------------------------------------------
    // Password Visibility
    // -------------------------------------------------------

    let showParentPassword = $state(false);
    let showConfirmParentPassword = $state(false);

    let showStudentPassword = $state(false);
    let showConfirmStudentPassword = $state(false);

    let errors = $state({
    admissionNo: '',
    studentName: '',
    email: '',
    phone: '',
    gender: '',
    dob: '',
    classGrade: '',
    section: '',
    studentId: '',
    fatherName: '',
    motherName: '',
    parentPassword: '',
    confirmParentPassword: '',
    studentPassword: '',
    confirmStudentPassword: ''
});

    // -------------------------------------------------------
    // Profile Image Upload
    // -------------------------------------------------------

    function handleImageChange(event: Event) {

        const input = event.target as HTMLInputElement;

        if (input.files?.length) {

            profileImage = URL.createObjectURL(
                input.files[0]
            );

        }

    }


    // -------------------------------------------------------
    // Transfer Certificate Upload
    // -------------------------------------------------------

    function handleTransferCertificate(event: Event) {

        const input = event.target as HTMLInputElement;

        if (input.files?.length) {

            transferCertificate = input.files[0];

        }

    }

    function validateForm(): boolean {

    errors.admissionNo = admissionNo.trim()
        ? ''
        : 'Admission number is required';

    errors.studentName = studentName.trim()
        ? ''
        : 'Student name is required';

    errors.email = email.trim()
        ? /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)
            ? ''
            : 'Please enter a valid email address'
        : 'Email address is required';

    errors.phone =
    phone.trim() === ''
        ? 'Phone number / father\'s number is required'
        : /^[6-9]\d{9}$/.test(phone)
            ? ''
            : 'Please enter a valid 10-digit phone number';
            
    errors.gender = gender
        ? ''
        : 'Please select gender';

    errors.dob = dob
        ? ''
        : 'Date of birth is required';

    errors.classGrade = classGrade.trim()
        ? ''
        : 'Class / Grade is required';

    errors.section = section.trim()
        ? ''
        : 'Section is required';

    errors.studentId = studentId.trim()
        ? ''
        : 'Student ID / Roll No. is required';

    errors.fatherName = fatherName.trim()
        ? ''
        : 'Father name is required';

    errors.motherName = motherName.trim()
        ? ''
        : 'Mother name is required';

    errors.parentPassword =
        parentPassword.length >= 8
            ? ''
            : 'Parent password must be at least 8 characters';

    errors.confirmParentPassword =
        confirmParentPassword === ''
            ? 'Please confirm parent password'
            : parentPassword === confirmParentPassword
                ? ''
                : 'Parent passwords do not match';

    errors.studentPassword =
        studentPassword.length >= 8
            ? ''
            : 'Student password must be at least 8 characters';

    errors.confirmStudentPassword =
        confirmStudentPassword === ''
            ? 'Please confirm student password'
            : studentPassword === confirmStudentPassword
                ? ''
                : 'Student passwords do not match';

    return Object.values(errors).every(
        error => error === ''
    );
}
    // -------------------------------------------------------
    // Submit
    // -------------------------------------------------------

function handleSubmit() {

    if (!validateForm()) {
        return;
    }

    console.log({
        admissionNo,
        studentName,
        email,
        phone,
        gender,
        dob,

        classGrade,
        section,
        studentId,
        previousSchoolName,
        previousAcademicMarks,

        parentId,
        fatherName,
        fatherOccupation,
        motherName,
        motherOccupation,

        parentPassword,

        studentPassword
    });

}
</script>
<div class="form-card">

    <h2>Student Details</h2>

    <!-- Profile Photo -->
    <div class="photo-section">

        {#if profileImage}
            <img
                src={profileImage}
                alt="Student Profile"
                class="profile-photo"
            />
        {:else}
            <div class="photo-placeholder">
                👤
            </div>
        {/if}

        <button
            type="button"
            class="upload-photo-btn"
            onclick={() => imageInput?.click()}
        >
            Upload Student Photo
        </button>

        <input
            bind:this={imageInput}
            type="file"
            accept="image/*"
            onchange={handleImageChange}
            hidden
        />

    </div>


    <!-- Student Fields -->
    <div class="form-grid">

        <!-- Admission Number -->
        <div class="form-group">
            <label for="admissionNo">Admission No.</label>

            <input
                id="admissionNo"
                type="text"
                bind:value={admissionNo}
                placeholder="Enter Admission Number"
            />
    {#if errors.admissionNo}
        <p class="error">{errors.admissionNo}</p>
    {/if}

        </div>


        <!-- Student Name -->
        <div class="form-group">
            <label for="studentName">Student Name</label>

            <input
                id="studentName"
                type="text"
                bind:value={studentName}
                placeholder="Enter Student Name"
            />
         {#if errors.studentName}
            <p class="error">{errors.studentName}</p>   
          {/if}

        </div>


        <!-- Email -->
        <div class="form-group">
            <label for="email">Email Address</label>

            <input
                id="email"
                type="email"
                bind:value={email}
                placeholder="student@example.com"
            />
         {#if errors.email}
            <p class="error">{errors.email}</p>
        {/if}

        </div>


        <!-- Phone -->
        <div class="form-group">
            <label for="phone">Phone Number (if available / Father's No.)</label>

            <input
                id="phone"
                type="tel"
                bind:value={phone}
                placeholder="Enter phone number"
            />
         {#if errors.phone}
        <p class="error">{errors.phone}</p>
    {/if}

        </div>


        <!-- Gender -->
        <div class="form-group">
            <label for="gender">Gender</label>

            <select
                id="gender"
                bind:value={gender}
            >
                <option value="">Select Gender</option>
                <option value="Male">Male</option>
                <option value="Female">Female</option>
                <option value="Other">Other</option>
            </select>
             {#if errors.gender}
        <p class="error">{errors.gender}</p>
    {/if}

        </div>


        <!-- Date of Birth -->
        <div class="form-group">
            <label for="dob">Date of Birth</label>

            <input
                id="dob"
                type="date"
                bind:value={dob}
            />
             {#if errors.dob}
        <p class="error">{errors.dob}</p>
    {/if}

        </div>

    </div>
</div>
    <!-- Academic Details -->
<div class="form-card">
       
    <h2>Academic Details</h2>

    <div class="form-grid">

        <!-- Class / Grade -->
        <div class="form-group">
            <label for="classGrade">Class / Grade</label>

            <input
                id="classGrade"
                type="text"
                bind:value={classGrade}
                placeholder="e.g. 8th Grade"
            />
             {#if errors.classGrade}
        <p class="error">{errors.classGrade}</p>
    {/if}

        </div>


        <!-- Section -->
        <div class="form-group">
            <label for="section">Section</label>

            <input
                id="section"
                type="text"
                bind:value={section}
                placeholder="e.g. A"
            />
             {#if errors.section}
        <p class="error">{errors.section}</p>
    {/if}

        </div>


        <!-- Student ID -->
        <div class="form-group full-width">
            <label for="studentId">
                Create Student ID / Roll No. / Hall Ticket No.
            </label>

            <input
                id="studentId"
                type="text"
                bind:value={studentId}
                placeholder="Create Student ID / Roll No. / Hall Ticket No."
            />
             {#if errors.studentId}
        <p class="error">{errors.studentId}</p>
    {/if}

        </div>


        <!-- Previous School -->
        <div class="form-group full-width">
            <label for="previousSchoolName">
                Previous School Name
                <span>(if applicable)</span>
            </label>

            <input
                id="previousSchoolName"
                type="text"
                bind:value={previousSchoolName}
                placeholder="Enter previous school name"
            />
        </div>


        <!-- Previous Academic Marks -->
        <div class="form-group full-width">
            <label for="previousAcademicMarks">
                Previous Academic Year Marks
                <span>(if applicable)</span>
            </label>

            <input
                id="previousAcademicMarks"
                type="text"
                bind:value={previousAcademicMarks}
                placeholder="e.g. 85% or 425 / 500"
            />
        </div>

    </div>

</div>
<!-- Parent Details -->
<div class="form-card">

    <h2>Parent Details</h2>
    <div class="form-group">
    <label for="parentId">Parent ID</label>

    <input
        id="parentId"
        type="text"
        bind:value={parentId}
        placeholder="e.g. PAR001"
    />
</div>

    <div class="form-grid">

        <!-- Father Name -->
        <div class="form-group">
            <label for="fatherName">Father Name</label>

            <input
                id="fatherName"
                type="text"
                bind:value={fatherName}
                placeholder="Enter Father Name"
            />
             {#if errors.fatherName}
        <p class="error">{errors.fatherName}</p>
    {/if}

        </div>

        <!-- Father Occupation -->
        <div class="form-group">
            <label for="fatherOccupation">Father Occupation</label>

            <input
                id="fatherOccupation"
                type="text"
                bind:value={fatherOccupation}
                placeholder="e.g. Business, Teacher, Driver"
            />
        </div>

        <!-- Mother Name -->
        <div class="form-group">
            <label for="motherName">Mother Name</label>

          <input
             id="motherName"
            type="text"
            bind:value={motherName}
        placeholder="Enter Mother Name"
        />

{#if errors.motherName}
    <p class="error">{errors.motherName}</p>
{/if}
        </div>

        <!-- Mother Occupation -->
        <div class="form-group">
            <label for="motherOccupation">Mother Occupation</label>

            <input
                id="motherOccupation"
                type="text"
                bind:value={motherOccupation}
                placeholder="e.g. Homemaker, Teacher, Business"
            />
        </div>

        <!-- Create Parent Password -->
        <div class="form-group">
            <label for="parentPassword">
                Create Parent Password
            </label>

            <div class="password-field">
                <input
                    id="parentPassword"
                    type={showParentPassword ? 'text' : 'password'}
                    bind:value={parentPassword}
                    placeholder="Create Parent Password"
                />
                {#if errors.parentPassword}
    <p class="error">{errors.parentPassword}</p>
{/if}

                <button
                    type="button"
                    class="eye-button"
                    onclick={() =>
                        showParentPassword = !showParentPassword
                    }
                    aria-label="Toggle parent password visibility"
                >
                    {showParentPassword ? '🙈' : '👁'}
                </button>
            </div>
        </div>

        <!-- Confirm Parent Password -->
        <div class="form-group">
            <label for="confirmParentPassword">
                Confirm Parent Password
            </label>

            <div class="password-field">
                <input
                    id="confirmParentPassword"
                    type={showConfirmParentPassword ? 'text' : 'password'}
                    bind:value={confirmParentPassword}
                    placeholder="Confirm Parent Password"
                />
                {#if errors.confirmParentPassword}
    <p class="error">{errors.confirmParentPassword}</p>
{/if}

                <button
                    type="button"
                    class="eye-button"
                    onclick={() =>
                        showConfirmParentPassword =
                            !showConfirmParentPassword
                    }
                    aria-label="Toggle confirm parent password visibility"
                >
                    {showConfirmParentPassword ? '🙈' : '👁'}
                </button>
            </div>
        </div>

    </div>

</div>
<!-- Student Account -->
<div class="form-card">

    <h2>Student Account</h2>

    <div class="form-grid">

        <!-- Create Student Password -->
        <div class="form-group">
            <label for="studentPassword">
                Create Student Password
            </label>

            <div class="password-field">

                <input
                    id="studentPassword"
                    type={showStudentPassword ? 'text' : 'password'}
                    bind:value={studentPassword}
                    placeholder="Create Student Password"
                />
                {#if errors.studentPassword}
    <p class="error">{errors.studentPassword}</p>
{/if}
                <button
                    type="button"
                    class="eye-button"
                    onclick={() =>
                        showStudentPassword = !showStudentPassword
                    }
                    aria-label="Toggle student password visibility"
                >
                    {showStudentPassword ? '🙈' : '👁'}
                </button>

            </div>
        </div>


        <!-- Confirm Student Password -->
        <div class="form-group">
            <label for="confirmStudentPassword">
                Confirm Student Password
            </label>

            <div class="password-field">

                <input
                    id="confirmStudentPassword"
                    type={showConfirmStudentPassword ? 'text' : 'password'}
                    bind:value={confirmStudentPassword}
                    placeholder="Confirm Student Password"
                />
                {#if errors.confirmStudentPassword}
    <p class="error">{errors.confirmStudentPassword}</p>
{/if}

                <button
                    type="button"
                    class="eye-button"
                    onclick={() =>
                        showConfirmStudentPassword =
                            !showConfirmStudentPassword
                    }
                    aria-label="Toggle confirm student password visibility"
                >
                    {showConfirmStudentPassword ? '🙈' : '👁'}
                </button>

            </div>
        </div>

    </div>

</div>


<!-- Transfer Certificate -->
<div class="form-card">

    <h2>Transfer Certificate</h2>

    <div class="form-group">

        <label for="transferCertificate">
            Transfer Certificate
            <span>(if applicable)</span>
        </label>

        <div class="file-upload-box">

            <input
                id="transferCertificate"
                type="file"
                accept=".pdf,.jpg,.jpeg,.png"
                onchange={handleTransferCertificate}
                hidden
            />

            <label
                for="transferCertificate"
                class="choose-file-btn"
            >
                Choose File
            </label>

            {#if transferCertificate}

                <div class="selected-file">

                    <div class="file-info">
                        <span class="file-icon">📄</span>

                        <div>
                            <strong>
                                {transferCertificate.name}
                            </strong>

                            <small>
                                {(transferCertificate.size / 1024 / 1024).toFixed(2)} MB
                            </small>
                        </div>
                    </div>

                    <button
                        type="button"
                        class="remove-file-btn"
                        onclick={() => transferCertificate = null}
                    >
                        Remove
                    </button>

                </div>

            {:else}

                <p class="file-hint">
                    No Transfer Certificate selected
                </p>

            {/if}

        </div>

        <small class="file-format">
            Accepted formats: PDF, JPG, JPEG, PNG
        </small>

    </div>

</div>

<div class="button-row">

    <button
        type="button"
        class="submit-btn"
        onclick={handleSubmit}
    >
        Create Student Account
    </button>

</div>
<style lang="scss">

.form-card {
    background: white;
    border: 1px solid #E2E8F0;
    border-radius: 24px;
    padding: 32px;
    margin-bottom: 24px;
    box-shadow: 0 10px 25px rgba(15,23,42,.05);
}
.form-card h2 {
    font-size: 24px;
    font-weight: 700;
    color: #0F172A;
    margin-bottom: 28px;
}

.form-grid {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 22px;
}

.form-group {
    display: flex;
    flex-direction: column;
    gap: 8px;
}

label {
    font-size: 14px;
    font-weight: 600;
    color: #334155;
}

input,
select {
    width: 100%;
    height: 50px;
    padding: 0 16px;
    border: 1px solid #CBD5E1;
    border-radius: 12px;
    font-size: 15px;
    background: white;
    outline: none;
    transition: .25s;
    box-sizing: border-box;
}

input:focus,
select:focus {
    border-color: #2563EB;
    box-shadow: 0 0 0 3px rgba(37,99,235,.12);
}

.photo-section {
    display: flex;
    flex-direction: column;
    align-items: center;
    margin-bottom: 28px;
}

.photo-placeholder,
.profile-photo {
    width: 120px;
    height: 120px;
    border-radius: 50%;
    border: 2px dashed #CBD5E1;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 52px;
    background: #F8FAFC;
    object-fit: cover;
    margin-bottom: 16px;
}

.upload-photo-btn {
    background: #2563EB;
    color: white;
    border: none;
    padding: 12px 24px;
    border-radius: 12px;
    cursor: pointer;
    font-weight: 600;
    transition: .25s;
}

.upload-photo-btn:hover {
    background: #1D4ED8;
}

@media(max-width: 900px) {

    .form-grid {
        grid-template-columns: 1fr;
    }

}
.full-width {
    grid-column: 1 / -1;
}

label span {
    font-weight: 400;
    color: #64748B;
}
.password-field {
    position: relative;
}

.password-field input {
    padding-right: 48px;
}

.eye-button {
    position: absolute;
    right: 14px;
    top: 50%;
    transform: translateY(-50%);
    background: none;
    border: none;
    cursor: pointer;
    color: #64748B;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 18px;
}
.button-row {
    margin-top: 8px;
    display: flex;
    justify-content: center;
}

.submit-btn {
    width: 100%;
    height: 52px;
    background: #2563EB;
    color: white;
    border: none;
    border-radius: 12px;
    font-size: 16px;
    font-weight: 700;
    cursor: pointer;
    transition: .25s;
}

.submit-btn:hover {
    background: #1D4ED8;
}
.error {
    color: #DC2626;
    font-size: 13px;
    font-weight: 500;
    margin-top: 6px;
}
input.error-input,
select.error-input {
    border-color: #DC2626;
    box-shadow: 0 0 0 3px rgba(220, 38, 38, .12);
}
.file-upload-box {
    border: 2px dashed #CBD5E1;
    border-radius: 14px;
    padding: 20px;
    background: #F8FAFC;
}

.choose-file-btn {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    background: #2563EB;
    color: white;
    padding: 11px 20px;
    border-radius: 10px;
    font-size: 14px;
    font-weight: 600;
    cursor: pointer;
    transition: .25s;
}

.choose-file-btn:hover {
    background: #1D4ED8;
}

.file-hint {
    color: #64748B;
    font-size: 13px;
    margin: 12px 0 0;
}

.file-format {
    color: #64748B;
    font-size: 12px;
    margin-top: 8px;
    display: block;
}

.selected-file {
    margin-top: 14px;
    padding: 12px;
    background: white;
    border: 1px solid #E2E8F0;
    border-radius: 10px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 12px;
}

.file-info {
    display: flex;
    align-items: center;
    gap: 10px;
    min-width: 0;
}

.file-icon {
    font-size: 24px;
}

.file-info strong {
    display: block;
    color: #0F172A;
    font-size: 13px;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
    max-width: 280px;
}

.file-info small {
    display: block;
    color: #64748B;
    font-size: 11px;
    margin-top: 3px;
}

.remove-file-btn {
    background: none;
    border: none;
    color: #DC2626;
    font-size: 13px;
    font-weight: 600;
    cursor: pointer;
    white-space: nowrap;
}

.remove-file-btn:hover {
    text-decoration: underline;
}
</style>