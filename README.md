# 🎯 Employee Management System

Django-based employee management system with Google Drive and Google Sheets integration.

## ✨ Features

- ✅ Add employees with Name, ID, Phone, Address
- ✅ Upload PDF documents to Google Drive
- ✅ Upload multiple photos (max 5) to Google Drive
- ✅ Store all data in Google Sheets (no local database)
- ✅ View all employees with search functionality
- ✅ Duplicate ID detection with highlighting
- ✅ Clickable file and photo links
- ✅ Download PDF files directly
- ✅ Responsive web interface

## 📋 Requirements

- Python 3.8 or higher
- Google Account with Drive and Sheets access
- Google OAuth credentials (credentials.json)

## 🚀 Quick Start

### Method 1: Batch File (Easiest)
```
Double-click: start_server.bat
```

### Method 2: Command Line
```cmd
python manage.py runserver
```

Then open browser: http://127.0.0.1:8000

## 📦 Installation

1. Install Python dependencies:
```cmd
pip install -r requirements.txt
```

2. Configure Google credentials:
   - Place `credentials.json` in project root
   - Update `.env` file with your Google Sheet ID and Drive Folder ID

3. Run the server:
```cmd
python manage.py runserver
```

## 🔧 Configuration

Edit `.env` file:
```
GOOGLE_DRIVE_FOLDER_ID=your_folder_id
GOOGLE_SHEET_ID=your_sheet_id
```

## 📁 Project Structure

```
Form/
├── manage.py                    # Django management
├── start_server.bat            # Easy server starter
├── requirements.txt            # Dependencies
├── .env                        # Configuration
├── credentials.json            # Google OAuth
│
├── drive_sheets_project/       # Django settings
│   ├── settings.py
│   ├── urls.py
│   └── ...
│
└── uploader/                   # Main application
    ├── views.py               # Business logic
    ├── forms.py               # Employee form
    ├── google_services.py     # Google API
    └── templates/
        └── uploader/
            ├── base.html
            ├── upload.html    # Add employee
            └── list.html      # View employees
```

## 🌐 URLs

- **Home/Add Employee**: http://127.0.0.1:8000/
- **View Employees**: http://127.0.0.1:8000/list/

## 🎨 Features Details

### Add Employee
- Form validation
- Duplicate ID check
- PDF upload (any size)
- Multiple photo upload (max 5, each max 5MB)
- Automatic Google Drive upload
- Automatic Google Sheets logging

### View Employees
- Display all employees from Google Sheet
- Search by Name, ID, or Phone
- Duplicate ID highlighting (yellow background)
- Clickable PDF links (opens in Drive)
- Clickable photo links (opens folder in Drive)
- Download button for PDFs
- Responsive table design

## 🗑️ Cleanup

To remove old/unnecessary files:
```
Double-click: cleanup_project.bat
```

This will delete:
- COMPLETE-SOLUTION folder
- employee-system folder
- Old HTML files
- Duplicate token files

## 📝 Notes

- Data is stored ONLY in Google Sheets (not in local database)
- Files are stored in Google Drive
- OAuth authentication required on first run
- Token is saved for future use (token.pickle)

## 🔒 Security

- OAuth 2.0 authentication
- Credentials stored locally
- No hardcoded passwords
- Environment variables for configuration

## 🐛 Troubleshooting

### Server won't start
```cmd
python manage.py migrate
python manage.py runserver
```

### Google authentication error
- Delete `token.pickle`
- Run server again
- Complete OAuth flow

### Files not uploading
- Check Google Drive folder permissions
- Verify credentials.json is valid
- Check internet connection

## 📄 License

This project is for internal use.

## 👨‍💻 Support

For issues or questions, check:
- PROJECT_STRUCTURE.md - Detailed structure
- BUILD_INSTRUCTIONS.md - Build instructions
- Console output for error messages

---

**Current Status**: ✅ Working and tested
**Last Updated**: February 2026
