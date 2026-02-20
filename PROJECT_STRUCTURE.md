# Employee Management System - Project Structure

## ✅ MAIN PROJECT FILES (Required)

```
D:\git\Form\
│
├── manage.py                          # Django management script
├── requirements.txt                   # Python dependencies
├── .env                              # Configuration (Google IDs)
├── credentials.json                   # Google OAuth credentials
├── token.pickle                       # Google authentication token
├── db.sqlite3                        # Database (not used, but Django needs it)
│
├── drive_sheets_project/             # Django project settings
│   ├── __init__.py
│   ├── settings.py                   # Main settings
│   ├── urls.py                       # URL routing
│   ├── wsgi.py                       # WSGI config
│   └── asgi.py                       # ASGI config
│
├── uploader/                         # Main application
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── forms.py                      # Employee form
│   ├── views.py                      # Main logic
│   ├── urls.py                       # App URLs
│   ├── google_services.py            # Google API integration
│   │
│   ├── templates/
│   │   └── uploader/
│   │       ├── base.html             # Base template
│   │       ├── upload.html           # Add employee form
│   │       └── list.html             # View employees
│   │
│   └── migrations/
│       ├── __init__.py
│       └── 0001_initial.py
│
├── start_server.bat                  # Easy server starter
├── run_server.py                     # Python server launcher
├── build_exe.py                      # EXE builder script
└── BUILD_INSTRUCTIONS.md             # Build instructions
```

## ❌ UNNECESSARY FILES (Can be deleted)

```
├── COMPLETE-SOLUTION/                # Old solution - not needed
│   ├── Code.gs
│   ├── index.html
│   ├── view.html
│   └── SETUP_GUIDE.md
│
├── employee-system/                  # Old files - not needed
│   ├── Code.gs
│   └── index.html
│
├── employee-viewer-fast.html         # Old HTML - not needed
├── employee-viewer-final.html        # Old HTML - not needed
├── token.json                        # Duplicate token file
└── .env.example                      # Example file - optional
```

## 📁 FOLDER PURPOSES

### drive_sheets_project/
- Django project configuration
- Settings, URLs, WSGI/ASGI config

### uploader/
- Main application code
- Forms, views, Google API integration
- Templates for UI

### uploader/templates/uploader/
- HTML templates
- base.html: Common layout
- upload.html: Add employee form
- list.html: View all employees

## 🔑 IMPORTANT FILES

### .env
```
SECRET_KEY=...
DEBUG=True
GOOGLE_DRIVE_FOLDER_ID=1fqqDP0G3SqwHk4DlzRT81V-7m_Jc0FQx
GOOGLE_SHEET_ID=1MULbch5DagDaH5jdqb_8XYfgztXWRn5t8p26SpegkH0
```

### credentials.json
- Google OAuth credentials
- Required for Google Drive/Sheets access

### token.pickle
- Saved authentication token
- Auto-generated after first login

## 🚀 HOW TO RUN

### Method 1: Batch File (Easiest)
```
Double-click: start_server.bat
```

### Method 2: Command Line
```cmd
python manage.py runserver
```

### Method 3: Python Script
```cmd
python run_server.py
```

## 📦 DEPENDENCIES (requirements.txt)

```
Django==4.2.7
google-auth==2.23.4
google-auth-oauthlib==1.1.0
google-auth-httplib2==0.1.1
google-api-python-client==2.108.0
python-dotenv==1.0.0
```

## 🌐 ACCESS URLS

- Home/Upload: http://127.0.0.1:8000/
- View Employees: http://127.0.0.1:8000/list/
- Admin: http://127.0.0.1:8000/admin/ (not configured)

## ✅ CURRENT STATUS

All files are in correct locations:
- ✓ Django project structure is correct
- ✓ Templates are in proper folder
- ✓ Google credentials are in root
- ✓ Configuration files are in root
- ✓ Batch file for easy startup

## 🗑️ CLEANUP RECOMMENDATION

You can safely delete these folders/files:
1. COMPLETE-SOLUTION/
2. employee-system/
3. employee-viewer-fast.html
4. employee-viewer-final.html
5. token.json (duplicate of token.pickle)

These are old files from previous attempts and not used by the current working project.
