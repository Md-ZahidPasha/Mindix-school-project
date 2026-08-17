# Mindix – AI-Powered School Operations Platform

Mindix is an AI-powered school operations platform designed to simplify and digitize everyday school management workflows.

It connects students, teachers, parents, staff, and administrators through a single platform with AI-assisted tools, attendance management, academic scheduling, document processing, library management, certificates, leave management, and more.

## 🚀 Key Features

### 🤖 AI Features
- AI School Assistant
- AI Document Reader
- AI-powered document extraction
- Role-aware AI responses for students, teachers, and parents
- Gemini AI integration

### 📚 Academic Management
- Smart Timetable
- Class and subject management
- Teacher timetable
- Student timetable
- Schedule conflict detection

### 📊 Attendance
- QR-based attendance
- Student ID-based attendance
- Attendance lookup
- Attendance records and statistics
- Duplicate-scan prevention

### 📖 Digital Library
- Book management
- Borrow and return workflow
- Library statistics
- Overdue book tracking
- Student borrowing records

### 📄 Certificates
- Certificate request creation
- Certificate status tracking
- Principal/admin review
- Approval and rejection workflow

### 📝 Leave & Substitution
- Leave request management
- Leave status tracking
- Teacher substitution management
- Substitute suggestions

### 👨‍👩‍👧 Parent Portal
- Parent profile
- Child information
- Child attendance
- Parent dashboard

### 👨‍🏫 Teacher Portal
- Teacher dashboard
- Classes
- Students
- Attendance
- Timetable
- Library
- Leave requests
- Notifications
- AI Assistant

### 🎓 Student Portal
- Student dashboard
- Attendance
- Timetable
- Certificates
- Library
- AI Assistant

### 🏫 Administration
- Admin dashboard
- Student management
- Class management
- Parent management
- Teacher/staff management
- School-wide statistics

## 🛠️ Technology Stack

### Frontend
- SvelteKit
- Svelte 5
- TypeScript
- Vite

### Backend
- Python
- FastAPI
- SQLAlchemy
- Uvicorn

### Database & Services
- Supabase
- PostgreSQL
- Google Gemini API

### Additional Technologies
- QR Code scanning
- REST APIs
- JWT authentication

## 🏗️ Architecture

```text
User
  │
  ▼
SvelteKit Frontend
  │
  ▼
REST API
  │
  ▼
FastAPI Backend
  │
  ├── Authentication
  ├── School Operations
  ├── Attendance
  ├── Library
  ├── Certificates
  ├── Leave & Substitution
  ├── Timetable
  ├── AI Services
  │     ├── Gemini
  │     └── Document Extraction
  │
  ▼
Supabase / PostgreSQL
🔐 Security

Sensitive configuration is stored using environment variables.

Example:

SUPABASE_URL=
SUPABASE_ANON_KEY=
SUPABASE_SERVICE_ROLE_KEY=
DATABASE_URL=
JWT_SECRET=
GEMINI_API_KEY=
GEMINI_MODEL=

API keys and secrets are not included in the repository.

💻 Local Development
Backend
cd backend


.venv\Scripts\python.exe -m uvicorn main:app --host 127.0.0.1 --port 8000
Frontend
cd frontend


npm install
npm run dev

The frontend can be configured to communicate with the backend using:

PUBLIC_API_BASE_URL=http://127.0.0.1:8000
✅ Verification

The project has been tested for:

Backend startup/import
Frontend type and Svelte checks
Production frontend build
API endpoint integration
AI Assistant
AI Document Reader
Smart Timetable
QR/Student-ID Attendance
Digital Library
Certificates
Leave & Substitution
Student Dashboard
Parent Portal
Teacher Dashboard
Admin Dashboard
🌐 Deployment
Backend

FastAPI backend can be deployed using Render or another Python-compatible hosting platform.

Frontend

SvelteKit frontend can be deployed using Vercel or another SvelteKit-compatible platform.

🎯 Project Goal

Mindix aims to replace fragmented and manual school processes with a unified digital platform that improves operational efficiency, reduces paperwork, and provides intelligent assistance to students, teachers, parents, and administrators.

👥 Team

Developed as part of the Future Ready Ops Innovation Challenge – PaperBuddy.

📌 Project Status

Working Prototype / Hackathon Build

The major frontend-backend workflows have been implemented and verified. Some advanced features may require further production hardening and deployment-specific configuration.
