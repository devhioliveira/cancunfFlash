@echo off
net session >nul 2>&1
if %errorlevel% neq 0 (
    powershell -Command "Start-Process '%~f0' -Verb RunAs"
    exit /b
)

set SCRIPT_PATH=%~dp0scripts\setup.py
where python >nul 2>nul || exit /b
python "%SCRIPT_PATH%"
exit /b
