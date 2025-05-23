@echo off
cd /d C:\users\dr744\projects\topstep_project

REM Get the current date and time
for /f "tokens=1-4 delims=/ " %%a in ("%date%") do (
    set day=%%a
    set month=%%b
    set year=%%c
)
for /f "tokens=1-2 delims=: " %%a in ("%time%") do (
    set hour=%%a
    set min=%%b
)

set commitmsg=Morning sync on %year%-%month%-%day% at %hour%:%min%

echo Adding all changes...
git add .

echo Committing changes...
git commit -m "%commitmsg%"

echo Pushing to origin...
git push

echo.
echo ✅ Morning sync complete. You're up to date.
pause
