# 🚀 FastAPI Photo & Video Sharing App

A full-stack social media style app built with **FastAPI + Streamlit** that allows users to:

- Register & login with JWT authentication
- Upload images & videos
- Share captions
- View a social feed
- Delete their own posts
- Media transformation using ImageKit

This project demonstrates a real-world FastAPI backend integrated with a Streamlit frontend.

---

## 🌐 Live Demo (Optional)

If running locally:

👉 Replace:

https://fastapiphotovideosharing.onrender.com

with:

http://localhost:8000

inside `frontend.py`

This ensures the frontend connects to your local backend.

---

## 🧱 Tech Stack

Backend:
- FastAPI
- FastAPI Users (authentication)
- SQLAlchemy
- SQLite
- Uvicorn
- ImageKit
- JWT Auth

Frontend:
- Streamlit

Dev Tools:
- Python 3.13+
- uv (modern package manager)

---

## 📦 Installation (Local Setup)

### 1. Clone repository

```bash
git clone https://github.com/riteshbhadana/FastAPIPhotoVideoSharing.git
cd FastAPIPhotoVideoSharing
```

---

### 2. Install Python

Requires **Python 3.13 or newer**

Check version:

```bash
python --version
```

If needed, download from:
https://www.python.org/downloads/

---

### 3. Install uv

```bash
pip install uv
```

---

### 4. Install dependencies

```bash
uv sync
```

This creates `.venv` and installs all packages.

---

### 5. Create environment variables

Create `.env` file in project root:

```env
JWT_SECRET=change-this-secret
IMAGEKIT_PRIVATE_KEY=your_key
IMAGEKIT_PUBLIC_KEY=your_key
IMAGEKIT_URL_ENDPOINT=your_url
```

⚠ Do NOT commit `.env` to GitHub

---

## ▶ Running the App

### Terminal 1 — Start FastAPI backend

```bash
uv run uvicorn app.app:app --reload
```

Backend runs at:

http://127.0.0.1:8000

Swagger API docs:

http://127.0.0.1:8000/docs

---

### Terminal 2 — Start Streamlit frontend

```bash
uv run streamlit run frontend.py
```

---

## 🔐 Authentication Flow

- Register → `/auth/register`
- Login → `/auth/jwt/login`
- Token stored in session
- Protected routes use Bearer token

---

## 📁 Project Structure

```
FastAPIPhotoVideoSharing/
│
├── app/
│   ├── app.py          # FastAPI app instance
│   ├── db.py           # Database models
│   ├── users.py        # Authentication logic
│   ├── schemas.py      # Pydantic models
│   └── images.py       # Media endpoints
│
├── frontend.py         # Streamlit UI
├── main.py             # Entry point
├── pyproject.toml      # Dependencies
├── .env                # Secrets (not committed)
└── README.md
```

---

## 🧠 Learning Goals

This project demonstrates:

- JWT authentication
- Dependency injection
- Async FastAPI backend
- Frontend-backend integration
- File upload handling
- Production-ready structure

---

## 🧪 Common Issues

### Backend not running

Error:

```
Connection refused localhost:8000
```

Fix:

Start FastAPI first:

```
uv run uvicorn app.app:app --reload
```

---

### Python version error

Requires Python ≥ 3.13

Use:

```
py -3.14 -m uv sync
```

---

## 🚀 Future Improvements

- Comments & likes
- User profiles
- Pagination
- Notifications
- Docker deployment
- Cloud storage

---

## 👨‍💻 Author

Ritesh Bhadana  
AI / Backend Developer

GitHub: https://github.com/riteshbhadana

---

## ⭐ Support

If this project helped you:

⭐ Star the repo  
🍴 Fork it  
🧠 Learn from it

---

## 📜 License

MIT License
