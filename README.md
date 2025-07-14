# 🚀 Task – FastAPI Backend

This project is a backend API built with **FastAPI**. It uses **PostgreSQL** for data storage and **uv** (an ultra-fast Python package manager written in Rust) for dependency management.

---

## 📦 Tech Stack

- ⚙️ FastAPI
- 🛢️ PostgreSQL
- 🐍 Python 3.9
- ⚡ `uv` for dependency and virtual environment management
- 🔄 SQLAlchemy ORM

---

## 🔧 Prerequisites

- Python 3.9
- PostgreSQL database
- [`uv`](https://github.com/astral-sh/uv) installed

---

## 🛠️ Installation Guide

### 📥 1. Install `uv`

#### For Linux / macOS / WSL:
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh

```

#### 🪟 For Windows:
```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

#### 🪟 Check uv version:
```
uv --version
```
#### 🪟 Clone repo:
```
git clone https://github.com/nitin-soni7566/wheel-specification-API.git

```

#### 🪟 Change directory:
```
cd wheel-specification-API
```

#### 🪟  Install dependencies:
```
uv sync
```


#### 🪟 Create .env file:
```
.env

DATABASE_URL=postgresql://username:password@localhost:5432/dbname
```

#### 🪟 Run server:
```
uv run uvicorn src.main:app --reload
```

#### 🪟  API Swagger docs:

Swagger UI: http://localhost:8000/docs


👤 Author
Built with ❤️ by Nitin soni
📧 nitinsoni815@gmail.com