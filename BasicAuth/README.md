```markdown
# FastAPI Basic Auth Example

A minimal FastAPI application demonstrating HTTP Basic Authentication using environment variables and bcrypt password hashing.

## Features

- HTTP Basic Authentication for endpoint security
- Secure password hashing with bcrypt
- User credentials configured via a `.env` file
- Easy project settings management with pydantic-settings

## File Structure
```

.
├── main.py
├── config.py
├── .env

```

## Setup

### 1. Clone the Repository

```

git clone https://github.com/yohaboy/fastapiAuth.git
cd BasicAuth

```

### 2. Create a `.env` File

Add a `.env` file with your credentials:

```

USERNAME=yourusername
PASSWORD=yourpassword

```

### 3. Install Dependencies

```

pip install fastapi uvicorn bcrypt pydantic-settings

```

## Running the Application

Start the FastAPI app with:

```

fastapi run main.py

```

## Usage

You can test the protected endpoint using curl (replace with your credentials):

```

curl -u yourusername:yourpassword http://localhost:8000/

```

On correct credentials, you’ll get:

```

{"body": "access granted"}

```

Otherwise, you will receive a 401 error.

## Notes

- **Never commit the `.env` file or sensitive credentials to version control.**
- This example hashes the password at runtime. For production, use securely stored hashed passwords.

```
