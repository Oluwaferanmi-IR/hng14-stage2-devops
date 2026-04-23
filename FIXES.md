# FIXES.md

All bugs found in the starter code and how they were fixed.

---

## Bug 1
- **File:** api/main.py
- **Line:** 8
- **Problem:** Redis host hardcoded as "localhost". Inside 
  Docker containers communicate by service name not localhost.
  API could not connect to Redis.
- **Fix:** Changed to use REDIS_HOST and REDIS_PORT 
  environment variables with defaults.

## Bug 2
- **File:** api/main.py
- **Line:** N/A (missing)
- **Problem:** No /health endpoint. Required for Docker 
  HEALTHCHECK and depends_on health conditions.
- **Fix:** Added GET /health returning {"status": "ok"}.

## Bug 3
- **File:** api/main.py
- **Line:** 17
- **Problem:** Job not found returned HTTP 200 with error 
  message instead of HTTP 404.
- **Fix:** Changed to raise HTTPException with status 404.

## Bug 4
- **File:** worker/worker.py
- **Line:** 6
- **Problem:** Redis host hardcoded as "localhost". Worker 
  could not connect to Redis inside Docker.
- **Fix:** Changed to use REDIS_HOST and REDIS_PORT 
  environment variables.

## Bug 5
- **File:** worker/worker.py
- **Line:** 4
- **Problem:** signal module imported but never used.
  Causes flake8 lint failure.
- **Fix:** Removed unused import.

## Bug 6
- **File:** worker/worker.py
- **Line:** 8-12
- **Problem:** No error handling in process_job. Any 
  exception crashes the worker permanently.
- **Fix:** Added try/except, marks job as failed on error.

## Bug 7
- **File:** worker/worker.py
- **Line:** 14-17
- **Problem:** No error handling in main loop. Redis 
  disconnection crashes worker with no recovery.
- **Fix:** Wrapped loop in try/except with 5s retry delay.

## Bug 8
- **File:** frontend/
- **Line:** N/A
- **Problem:** File named apps.js but package.json and 
  start script reference app.js. App would fail to start.
- **Fix:** Renamed apps.js to app.js.

## Bug 9
- **File:** frontend/app.js
- **Line:** 6
- **Problem:** API URL hardcoded as "http://localhost:8000".
  Frontend container cannot reach API container via localhost.
- **Fix:** Changed to use API_URL environment variable.

## Bug 10
- **File:** frontend/app.js
- **Line:** N/A (missing)
- **Problem:** No /health endpoint for Docker HEALTHCHECK.
- **Fix:** Added GET /health returning {"status": "ok"}.

## Bug 11
- **File:** frontend/app.js
- **Line:** 27
- **Problem:** Port hardcoded as 3000.
- **Fix:** Changed to use PORT environment variable.

## Bug 12
- **File:** frontend/app.js
- **Line:** 13-16, 21-24
- **Problem:** Errors caught but not logged making 
  debugging impossible.
- **Fix:** Added console.error(err.message) in catch blocks.

## Bug 13
- **File:** api/.env
- **Line:** 1-2
- **Problem:** .env file committed to repo containing 
  hardcoded Redis password. Critical security vulnerability.
- **Fix:** Deleted api/.env, added to .gitignore, moved 
  to .env.example as placeholder.

## Bug 14
- **File:** frontend/Dockerfile
- **Line:** 8
- **Problem:** npm ci requires a package-lock.json file 
  which was missing from the repo. Also --only=production 
  flag is deprecated in newer npm versions.
- **Fix:** Generated package-lock.json by running npm 
  install locally. Changed --only=production to --omit=dev.
