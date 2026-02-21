# Commitment AI - Setup Complete ✓

## What's Been Initialized

### ✅ FastAPI Application
- Main FastAPI app configured in `main.py`
- CORS middleware enabled for frontend integration
- Health check endpoint at `/health`
- Automatic database initialization on startup

### ✅ Database Setup
- SQLAlchemy ORM configured
- PostgreSQL connection pool management
- Database session dependency injection
- All tables auto-created on first run

### ✅ Core Models (ORM)
1. **User** - Business owners/team members
   - Email, username, company info
   - Relationships to commitments and sales

2. **Commitment** - Core entity for tracking future obligations
   - Action description and deadline
   - Type classification (invoice, reorder, payment, followup, delivery, reminder)
   - Status tracking (pending, in_progress, completed, overdue, cancelled)
   - Party information (name, email, phone)
   - Source tracking (email, whatsapp, telegram, etc.)
   - Auto-drafted content management
   - Reminder and escalation tracking

3. **Sales** - Customer deals and opportunities
   - Customer contact information
   - Deal status and expected close date
   - Next action tracking
   - Amount and currency

### ✅ Pydantic Schemas
- Request/response validation schemas for all models
- Type-safe API contracts
- Enum definitions for statuses and types

### ✅ Configuration System
- Environment variable management via `.env`
- Settings class with sensible defaults
- Secret key management
- LLM configuration ready for Llama integration

---

## Quick Start

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Setup PostgreSQL Database

**Option A: Automated (Recommended)**
```bash
python setup.py
```
This will:
- Check PostgreSQL installation
- Create database and user
- Generate `.env` file
- Install Python dependencies

**Option B: Manual Setup**
```sql
CREATE DATABASE commit_ai;
CREATE USER commit_user WITH PASSWORD 'your_password';
ALTER ROLE commit_user SET client_encoding TO 'utf8';
GRANT ALL PRIVILEGES ON DATABASE commit_ai TO commit_user;
```

### 3. Create `.env` File
Copy from `.env.example`:
```bash
cp .env.example .env
```

Update `DATABASE_URL` with your PostgreSQL credentials:
```
DATABASE_URL=postgresql://commit_user:password@localhost:5432/commit_ai
```

### 4. Run the Application
```bash
python main.py
```

Output should show:
```
✓ Commitment AI started
✓ Database initialized
INFO:     Uvicorn running on http://0.0.0.0:8000
```

### 5. Test the App
- **Health Check**: http://localhost:8000/health
- **API Docs**: http://localhost:8000/api/docs (Swagger UI)
- **ReDoc**: http://localhost:8000/api/redoc

---

## Project Structure

| Folder | Purpose |
|--------|---------|
| `api/` | REST API endpoints (auth, commitments, sales, webhooks) |
| `core/` | Infrastructure (config, database, security) |
| `models/` | SQLAlchemy ORM models |
| `schemas/` | Pydantic validation schemas |
| `services/` | Business logic (AI engine, email reader, ETL, etc.) |
| `static/` | Frontend assets (CSS, JS) |
| `templates/` | HTML templates |

---

## What's Ready to Build Next

### 1. **Authentication API** (`api/auth.py`)
- User registration endpoint
- Login endpoint with JWT tokens
- Token refresh endpoint
- Password hashing and verification

### 2. **Commitments API** (`api/commitments.py`)
- CRUD operations for commitments
- List/filter commitments
- Update status
- Get overdue commitments
- Bulk operations

### 3. **Sales API** (`api/sales.py`)
- CRUD operations for sales
- Filter by status
- Update deal status

### 4. **AI Engine** (`services/ai_engine.py`)
- Llama integration for commitment detection
- Text analysis and entity extraction
- Confidence scoring

### 5. **Email/Webhook Handlers** (`services/email_reader.py`, `api/webhooks.py`)
- Receive emails via webhooks
- Parse commitment mentions
- Extract party information

### 6. **Frontend Dashboard** (`templates/dashboard.html`, `static/js/app.js`)
- Vanilla JS dashboard
- Commitment list view
- Add/edit commitments
- Status updates
- Search and filter

---

## Key Features Implemented

✅ Database models with relationships  
✅ Enum-based status/type tracking  
✅ Timestamp tracking (created, updated, completed)  
✅ Overdue detection logic  
✅ Party tracking (customer, supplier, contact)  
✅ Source tracking (email, whatsapp, telegram)  
✅ Auto-draft content storage  
✅ Reminder and escalation flags  
✅ Dependency injection for DB sessions  
✅ Environment-based configuration  

---

## Llama Setup (Local LLM)

When ready to implement AI commitment detection:

1. **Install Ollama**: https://ollama.ai
2. **Pull Llama2**:
   ```bash
   ollama pull llama2
   ```
3. **Start Ollama**:
   ```bash
   ollama serve
   ```
4. **Verify it's running**:
   ```
   http://localhost:11434
   ```

The `ai_engine.py` service will integrate with this once you're ready to implement commitment detection.

---

## Environment Variables

| Variable | Purpose | Default |
|----------|---------|---------|
| `DATABASE_URL` | PostgreSQL connection string | Required |
| `APP_NAME` | Application name | Commitment AI |
| `DEBUG` | Enable debug mode | True |
| `SECRET_KEY` | JWT signing key | Change in production |
| `LLM_MODEL` | Llama model to use | llama2 |
| `LLM_API_URL` | Llama server URL | http://localhost:11434 |

---

## Common Issues & Solutions

### "Database connection refused"
- Ensure PostgreSQL is running
- Check DATABASE_URL in `.env`
- Verify user/password are correct

### "ModuleNotFoundError"
- Run `pip install -r requirements.txt`
- Ensure all __init__.py files exist in packages

### "psql command not found"
- PostgreSQL is not in PATH (Windows)
- Install PostgreSQL with pg_Base checked
- Or use `setup.py` for guided setup

---

## Next Steps

1. **Build Authentication** - Implement user registration and login
2. **Create Commitment Endpoints** - Full CRUD operations
3. **Implement AI Engine** - Commitment detection with Llama
4. **Add Email Webhooks** - Automatic commitment detection from emails
5. **Build Dashboard** - Vanilla JS frontend for commitment management
6. **Add Reminders** - Background tasks for deadline alerts
7. **Telegram Integration** - WhatsApp/Telegram bot for commitment capture

---

## Architecture Diagram

```
FastAPI Server (port 8000)
    ├── API Routes
    │   ├── /auth/* (Authentication)
    │   ├── /commitments/* (CRUD)
    │   ├── /sales/* (CRUD)
    │   └── /webhooks/* (Email, Telegram, etc.)
    ├── Services
    │   ├── AI Engine (Llama commitment detection)
    │   ├── Email Reader (webhook handler)
    │   ├── ETL Pipeline (data processing)
    │   └── Sales Logic (deal management)
    └── Database (PostgreSQL)
        ├── users
        ├── commitments
        └── sales
```

---

## Support

For issues or questions, check:
1. `ARCHITECTURE.md` - Detailed architecture
2. `.env.example` - Configuration template
3. `main.py` - App initialization
4. FastAPI docs at `/api/docs` when running

---

**Status**: ✓ Backend infrastructure initialized and ready for API development
