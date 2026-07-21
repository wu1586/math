@echo off
cd /d "%~dp0"

echo Checking Git installation...
where git >nul 2>&1
if %errorlevel% neq 0 (
    echo Error: Git not found
    echo Please install Git first
    pause
    exit /b 1
)

echo.
echo Current directory: %cd%
echo.

echo Checking if this is a git repository...
git rev-parse --git-dir >nul 2>&1
if %errorlevel% neq 0 (
    echo This is not a git repository. Initializing...
    git init
    git remote add origin https://github.com/wu1586/math.git
    echo Git repository initialized.
)

echo.
echo Adding all files...
git add .

echo.
echo Files to be committed:
git status

echo.
set /p confirm=Confirm commit? (y/n):
if /i not "%confirm%"=="y" (
    echo Commit cancelled
    pause
    exit /b 0
)

echo.
echo Committing changes...
git commit -m "Add model list and detail pages with 3 MATLAB examples"

echo.
echo Pushing to GitHub...
git push -u origin main

if %errorlevel% equ 0 (
    echo.
    echo Success! GitHub Actions will build the new version.
    echo Visit: https://github.com/wu1586/math/actions
) else (
    echo.
    echo Push failed. You may need to pull first or resolve conflicts.
    echo Try: git pull origin main --rebase
    echo Then run this script again.
)

echo.
pause
