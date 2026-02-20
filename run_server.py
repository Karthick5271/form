"""
Simple launcher script for the Employee Management System
This will be converted to .exe
"""
import os
import sys
import webbrowser
import time
from threading import Timer

def open_browser():
    """Open browser after server starts"""
    time.sleep(2)
    webbrowser.open('http://127.0.0.1:8000')

if __name__ == '__main__':
    print("=" * 60)
    print("Employee Management System")
    print("=" * 60)
    print()
    print("Starting server at http://127.0.0.1:8000")
    print("Browser will open automatically...")
    print()
    print("Press Ctrl+C to stop the server")
    print("=" * 60)
    print()
    
    # Open browser after 2 seconds
    Timer(2, open_browser).start()
    
    # Start Django server
    os.system('python manage.py runserver')
