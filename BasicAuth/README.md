# FastAPI Basic Auth Example

A minimal **FastAPI** app demonstrating **HTTP Basic Authentication** with **bcrypt** password hashing and environment-based credentials.

## 🚀 Features

- Secure endpoints with HTTP Basic Auth
- Password hashing using bcrypt
- Credentials managed via `.env`
- Simple config management with `pydantic-settings`

## 🛠 Tech Stack

- **Framework**: FastAPI
- **Server**: Uvicorn
- **Config**: pydantic-settings
- **Hashing**: bcrypt

## 📂 Structure

```
.
├── main.py
├── config.py
├── .env
```

## 📋 Setup

### 1. Clone & Install

```bash
git clone https://github.com/yohaboy/fastapiAuth.git
cd fastapiAuth
pip install fastapi uvicorn bcrypt pydantic-settings
```

### 2. Create `.env`

```env
USERNAME=yourusername
PASSWORD=yourpassword
```

## ▶️ Run

```bash
fastapi run main.py
# or
uvicorn main:app --reload
```

## 🔗 Usage

```bash
curl -u yourusername:yourpassword http://localhost:8000/
```

✅ On success:

```json
{ "body": "access granted" }
```

❌ On failure: **401 Unauthorized**

## ⚠️ Notes

- Do **not** commit `.env` or credentials
- Runtime hashing is for demo; use securely stored hashes in production
