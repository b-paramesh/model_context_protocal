#!/usr/bin/env python3
"""
Run script for MCP Learning Path Generator
This script provides an easy way to start the application.
"""

import subprocess
import sys
import os
from pathlib import Path

def check_virtual_environment():
    """Check if virtual environment exists"""
    venv_path = Path("venv")
    if not venv_path.exists():
        print("❌ Virtual environment not found!")
        print("Please run 'python setup.py' first to set up the project.")
        return False
    return True

def check_dependencies():
    """Check if required packages are installed"""
    try:
        import streamlit
        import langchain
        import langgraph
        return True
    except ImportError as e:
        print(f"❌ Missing dependencies: {e}")
        print("Please run 'python setup.py' to install dependencies.")
        return False

def run_streamlit():
    """Run the Streamlit application"""
    print("🚀 Starting MCP Learning Path Generator...")
    print("📱 The app will open in your browser at http://localhost:8501")
    print("🛑 Press Ctrl+C to stop the application")
    print("-" * 50)
    
    # Determine the correct python command based on OS
    if os.name == 'nt':  # Windows
        python_cmd = "venv\\Scripts\\python"
    else:  # Unix/Linux/Mac
        python_cmd = "venv/bin/python"
    
    try:
        # Run streamlit
        subprocess.run([python_cmd, "-m", "streamlit", "run", "app.py"], check=True)
    except KeyboardInterrupt:
        print("\n🛑 Application stopped by user")
    except subprocess.CalledProcessError as e:
        print(f"❌ Error running application: {e}")
        return False
    except FileNotFoundError:
        print("❌ Python executable not found in virtual environment")
        print("Please run 'python setup.py' to set up the project properly.")
        return False
    
    return True

def main():
    """Main function"""
    print("🤖 MCP Learning Path Generator")
    print("=" * 40)
    
    # Check if we're in the right directory
    if not Path("app.py").exists():
        print("❌ app.py not found!")
        print("Please run this script from the project root directory.")
        sys.exit(1)
    
    # Check virtual environment
    if not check_virtual_environment():
        sys.exit(1)
    
    # Check dependencies
    if not check_dependencies():
        sys.exit(1)
    
    # Run the application
    if not run_streamlit():
        sys.exit(1)

if __name__ == "__main__":
    main()