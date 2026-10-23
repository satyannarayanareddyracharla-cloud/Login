# Login and Registration UI Automation

Playwright tests for the Login and Registration Forms section on QA Practice Hub.
The tests use reusable page objects in `pages/` for login and registration actions.

## Setup

Requires Python 3.9 or newer.

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m playwright install chrome
```

## Run

```powershell
python -m pytest
```

The login tests use the demo credentials shown on the page: `tester` / `password123`.
Registration is simulated by the practice site; the test uses sample data and does not
create an account on a production service.

## Current site behavior

The malformed-email test documents current behavior: the input is invalid, but the page
still reports registration success after submitting `not-an-email`.
