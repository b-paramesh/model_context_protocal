#!/usr/bin/env python3
"""
Setup script for MCP Learning Path Generator
This script helps set up the project environment and install dependencies.
"""

import subprocess
import sys
import os
from pathlib import Path

def run_command(command, description):
    """Run a command and handle errors"""
    print(f"🔄 {description}...")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} completed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error during {description}:")
        print(f"Command: {command}")
        print(f"Error: {e.stderr}")
        return False

def check_python_version():
    """Check if Python version is compatible"""
    print("🐍 Checking Python version...")
    version = sys.version_info
    if version.major < 3 or (version.major == 3 and version.minor < 8):
        print("❌ Python 3.8 or higher is required")
        print(f"Current version: {version.major}.{version.minor}.{version.micro}")
        return False
    print(f"✅ Python {version.major}.{version.minor}.{version.micro} is compatible")
    return True

def create_virtual_environment():
    """Create virtual environment if it doesn't exist"""
    venv_path = Path("venv")
    if venv_path.exists():
        print("✅ Virtual environment already exists")
        return True
    
    print("🔄 Creating virtual environment...")
    return run_command("python -m venv venv", "Virtual environment creation")

def install_dependencies():
    """Install required dependencies"""
    # Determine the correct pip command based on OS
    if os.name == 'nt':  # Windows
        pip_cmd = "venv\\Scripts\\pip"
    else:  # Unix/Linux/Mac
        pip_cmd = "venv/bin/pip"
    
    # Upgrade pip first
    run_command(f"{pip_cmd} install --upgrade pip", "Pip upgrade")
    
    # Install requirements
    return run_command(f"{pip_cmd} install -r requirements.txt", "Dependencies installation")

def create_env_template():
    """Create environment template file"""
    env_template = """# MCP Learning Path Generator - Environment Configuration
# Copy this file to .env and fill in your actual values

# Google API Configuration
GOOGLE_API_KEY=your_google_api_key_here

# Pipedream URLs (get these from your Pipedream workflows)
YOUTUBE_PIPEDREAM_URL=your_youtube_pipedream_url_here
DRIVE_PIPEDREAM_URL=your_drive_pipedream_url_here
NOTION_PIPEDREAM_URL=your_notion_pipedream_url_here

# Optional: Streamlit Configuration
STREAMLIT_SERVER_PORT=8501
STREAMLIT_SERVER_ADDRESS=localhost
"""
    
    with open("env.template", "w") as f:
        f.write(env_template)
    print("✅ Created env.template file")

def main():
    """Main setup function"""
    print("🚀 Setting up MCP Learning Path Generator...")
    print("=" * 50)
    
    # Check Python version
    if not check_python_version():
        sys.exit(1)
    
    # Create virtual environment
    if not create_virtual_environment():
        print("❌ Failed to create virtual environment")
        sys.exit(1)
    
    # Install dependencies
    if not install_dependencies():
        print("❌ Failed to install dependencies")
        sys.exit(1)
    
    # Create environment template
    create_env_template()
    
    print("\n" + "=" * 50)
    print("🎉 Setup completed successfully!")
    print("\n📋 Next steps:")
    print("1. Copy env.template to .env and fill in your API keys")
    print("2. Run the application with: python run.py")
    print("3. Open your browser to http://localhost:8501")
    print("\n📚 For detailed instructions, see README.md")

if __name__ == "__main__":
    main()