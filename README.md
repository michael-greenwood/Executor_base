# Hello Executor – Setup Guide

This README provides instructions for setting up a minimal “Hello World” executor
using FastAPI, matching the required executor API structure.

---

## 1. Create a Python Virtual Environment

From the folder where the `executor/` directory exists, run:

```bash
python3 -m venv venv
```

### Activate the environment:

**Linux/macOS:**
```bash
source venv/bin/activate
```

**Windows (PowerShell):**
```powershell
venv\Scripts\activate
```

You should now see `(venv)` in your terminal prompt.

---

## 2. Install Dependencies

Install FastAPI, Uvicorn, and optional upload support:

```bash
pip install fastapi uvicorn python-multipart
```

---

## 3. Run the Executor

From inside the `executor/` directory, run:

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8001
```

Or simply:

```bash
uvicorn main:app --reload
```

A running executor will now be available at:

```
http://localhost:8001/
```

---

## 4. Test an Endpoint

You can test the basic “new experiment” endpoint:

```
http://localhost:8001/remote_ctrl/sim/experiment/new
```

This should return:

```json
{ "status": "ok", "id": "dummy-uuid" }
```

---

## Notes

- This executor base contains **empty stub endpoints only**.
- No storage, execution logic, or module code is included.
- Orchestrator integration can be tested immediately.
- You can expand functionality later (runtime, state, real outputs, etc.)

---

