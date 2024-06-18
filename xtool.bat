@echo off

rem install & run
if "%1"=="install" (
    call pip install colorama
) else (
    python ./src/main.py %*
)
