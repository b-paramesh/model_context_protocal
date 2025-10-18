#!/bin/bash
# Unix/Linux/Mac shell script to run MCP Learning Path Generator

echo "🤖 MCP Learning Path Generator"
echo "================================"

# Check if app.py exists
if [ ! -f "app.py" ]; then
    echo "❌ app.py not found!"
    echo "Please run this script from the project root directory."
    exit 1
fi

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "❌ Virtual environment not found!"
    echo "Please run 'python setup.py' first to set up the project."
    exit 1
fi

# Run the application
echo "🚀 Starting MCP Learning Path Generator..."
echo "📱 The app will open in your browser at http://localhost:8501"
echo "🛑 Press Ctrl+C to stop the application"
echo "----------------------------------------"

venv/bin/python -m streamlit run app.py