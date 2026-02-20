# Employee Management System - EXE Build Instructions

## Option 1: Simple Batch File (Recommended - Easiest)

### Usage:
1. Double-click `start_server.bat`
2. Server will start automatically
3. Open browser and go to: http://127.0.0.1:8000
4. Press Ctrl+C to stop

### Requirements:
- Python must be installed on the computer

---

## Option 2: Create Standalone EXE (Advanced)

### Step 1: Install PyInstaller
```cmd
pip install pyinstaller
```

### Step 2: Build the EXE
```cmd
python build_exe.py
```

OR manually:

```cmd
pyinstaller --onefile --add-data "uploader;uploader" --add-data "drive_sheets_project;drive_sheets_project" --add-data "credentials.json;." --add-data ".env;." --hidden-import django --hidden-import google --hidden-import googleapiclient --name EmployeeManagementSystem run_server.py
```

### Step 3: Find Your EXE
- Location: `dist/EmployeeManagementSystem.exe`
- Double-click to run
- Browser will open automatically

---

## Option 3: Create Installer (Most Professional)

### Using Inno Setup:

1. Download Inno Setup: https://jrsoftware.org/isdl.php
2. Create installer script
3. Package everything together

---

## Important Notes:

### Files Needed for Distribution:
- `credentials.json` (Google OAuth credentials)
- `.env` (Configuration file)
- `db.sqlite3` (Database - optional since we use Google Sheet)
- All project files

### For Other Computers:
If you want to run on a computer without Python:

1. Use PyInstaller to create standalone .exe
2. Include all dependencies
3. Package with installer

### Limitations:
- Django is a web framework, not a desktop app
- Server must run in background
- Browser needed to access the interface

### Alternative Solution:
Convert to a desktop app using:
- **Electron** + Django backend
- **PyQt/Tkinter** for true desktop GUI
- **Flask** (lighter than Django) + PyInstaller

---

## Quick Start (Easiest Method):

1. **Just use the batch file**: `start_server.bat`
2. Share the entire project folder
3. Recipient needs Python installed
4. Double-click batch file to run

---

## For Production Deployment:

Consider deploying to:
- **Heroku** (Free tier available)
- **PythonAnywhere** (Free tier available)
- **Google Cloud Run**
- **AWS EC2**

This way, users can access via web browser without installing anything!
