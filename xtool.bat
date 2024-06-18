@echo off

rem Check if the script is called with 'install'
if "%1"=="install" (
    call pip install colorama cryptography tqdm
    exit /b
)

rem Get the directory of the current script
set SCRIPT_DIR=%~dp0

rem Run the Python script with the provided arguments
python "%SCRIPT_DIR%src\main.py" %*
