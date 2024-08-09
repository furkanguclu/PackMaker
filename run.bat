@echo off
rem Pack.py için ayarlanmış .bat dosyası [Sys]
set "SYS_SCRIPT=pack.py"

if not defined PYTHON_PATH (
    set "PYTHON_COMMAND=python"
) else (
    set "PYTHON_COMMAND=%PYTHON_PATH%"
)

echo Running script with: %PYTHON_COMMAND% %SYS_SCRIPT%
%PYTHON_COMMAND% %SYS_SCRIPT%

pause
