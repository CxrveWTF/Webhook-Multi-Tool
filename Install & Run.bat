@echo off

:: Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Python is not installed. Please install Python 3.7 or later.
    pause
    exit /b
)

:: Install required Python libraries
echo Installing required Python libraries...
pip install --quiet colorama requests
if %errorlevel% neq 0 (
    echo Error occurred while installing dependencies.
    pause
    exit /b
)

:: Clear the console screen
cls

:: Run the Python script
echo Starting the script...
python WebhookMultiTool.py

:: Pause the console when the script ends
pause
