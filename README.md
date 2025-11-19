Cursor AI QA Agent – Event Creation Automation
Overview

This project automates the login, event creation, and validation flow on
https://events.webmobi.com
 using Playwright + Python inside Cursor.

The agent logs in using environment variables, selects an AI template, sends a description, creates the event, and validates that the event appears in the My Events list.

Setup Instructions
1. Create Virtual Environment
python -m venv .venv
.venv\Scripts\activate

2. Install Dependencies
pip install -r requirements.txt
playwright install

3. Set Credentials

Inside Cursor terminal:

set WM_EMAIL=your_email_here
set WM_PASSWORD=your_password_here

4. Run Test
python test_event_creation.py


This will:

Log in

Create an event

Capture screenshot in /logs/eventcreated.png

GitHub Actions CI

A minimal GitHub Action is included at:
.github/workflows/test.yml

It runs:

pip install -r requirements.txt
playwright install
python test_event_creation.py

Files Included

test_event_creation.py — Main automation script

requirements.txt — Dependencies

.github/workflows/test.yml — GitHub CI workflow

/logs/eventcreated.png — Proof screenshot

README.md — Documentation

Proof of Execution

A screenshot of the successfully created event is saved at:
logs/eventcreated.png