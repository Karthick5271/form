"""
Script to create standalone executable for Django Employee Management System
"""
import os
import sys

print("=" * 60)
print("Employee Management System - EXE Builder")
print("=" * 60)
print()

# Check if PyInstaller is installed
try:
    import PyInstaller
    print("✓ PyInstaller is installed")
except ImportError:
    print("✗ PyInstaller not found. Installing...")
    os.system("pip install pyinstaller")
    print("✓ PyInstaller installed successfully")

print()
print("Creating executable...")
print("This may take a few minutes...")
print()

# Create the executable
cmd = """
pyinstaller --onefile --noconsole ^
    --add-data "uploader;uploader" ^
    --add-data "drive_sheets_project;drive_sheets_project" ^
    --add-data "credentials.json;." ^
    --add-data ".env;." ^
    --hidden-import django ^
    --hidden-import google ^
    --hidden-import googleapiclient ^
    --name EmployeeManagementSystem ^
    manage.py
"""

os.system(cmd)

print()
print("=" * 60)
print("Build Complete!")
print("=" * 60)
print()
print("Your .exe file is in the 'dist' folder")
print("File: dist/EmployeeManagementSystem.exe")
print()
