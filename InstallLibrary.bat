@echo off
goto check_Permissions

:check_Permissions
echo Administrative permissions required. Detecting permissions...

net session >nul 2>&1
if %errorLevel% == 0 (
    echo Success: Administrative permissions confirmed.
    goto main
) else (
    echo Failure: Current permissions inadequate.
    goto end
)

:main
echo Installing Pygame
python -m pip install -U pygame==2.5.0 --user
echo Secondly it's Customtkinter
python -m pip install -U customtkinter --user
echo That's all
:end
pause
