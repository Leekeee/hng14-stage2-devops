# FIXES.md

## Bug Fixes

### 1. api/.env — Secrets committed to repository
- **File:** `api/.env`
- **Line:** 1-2
- **Problem:** .env file containing Redis password was committed to the public repository, exposing secrets.
- **Fix:** Added `.env` to `.gitignore`, removed file from git tracking, created `.env.example` with placeholder values.

---

### 2. api/main.py — Hardcoded Redis connection
- **File:** `api/main.py`
- **Line:** 8
- **Problem:** Redis host set to `localhost` which doesn't work in Docker networking. Port hardcoded. No password provided.
- **Fix:** Replaced with `os.getenv()` for host, port and password.

---

### 3. api/main.py — Wrong HTTP status code
- **File:** `api/main.py`
- **Line:** 10
- **Problem:** POST endpoint returns default 200 instead of 201 when creating a resource.
- **Fix:** Added `status_code=201` to `@app.post` decorator.