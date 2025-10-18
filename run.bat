@echo off
REM Windows batch file to run MCP Learning Path Generator
echo 🤖 MCP Learning Path Generator
echo ================================

REM Check if app.py exists
if not exist "app.py" (
    echo ❌ app.py not found!
    echo Please run this script from the project root directory.
    pause
    exit /b 1
)

REM Check if virtual environment exists
if not exist "venv" (
    echo ❌ Virtual environment not found!
    echo Please run 'python setup.py' first to set up the project.
    pause
    exit /b 1
)

REM Run the application
echo 🚀 Starting MCP Learning Path Generator...
echo 📱 The app will open in your browser at http://localhost:8501
echo 🛑 Press Ctrl+C to stop the application
echo ----------------------------------------

venv\Scripts\python -m streamlit run app.py

pause