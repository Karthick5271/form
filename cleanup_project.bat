@echo off
echo ========================================
echo Employee Management System - Cleanup
echo ========================================
echo.
echo This will delete old/unnecessary files:
echo - COMPLETE-SOLUTION folder
echo - employee-system folder
echo - employee-viewer-fast.html
echo - employee-viewer-final.html
echo - token.json
echo.
echo Your main project files will NOT be deleted.
echo.
pause
echo.
echo Cleaning up...
echo.

if exist "COMPLETE-SOLUTION" (
    rmdir /s /q "COMPLETE-SOLUTION"
    echo [DELETED] COMPLETE-SOLUTION folder
)

if exist "employee-system" (
    rmdir /s /q "employee-system"
    echo [DELETED] employee-system folder
)

if exist "employee-viewer-fast.html" (
    del /q "employee-viewer-fast.html"
    echo [DELETED] employee-viewer-fast.html
)

if exist "employee-viewer-final.html" (
    del /q "employee-viewer-final.html"
    echo [DELETED] employee-viewer-final.html
)

if exist "token.json" (
    del /q "token.json"
    echo [DELETED] token.json
)

echo.
echo ========================================
echo Cleanup Complete!
echo ========================================
echo.
echo Your project is now clean and organized.
echo All working files are intact.
echo.
pause
