# 🤖 MCP Learning Path Generator

A powerful Streamlit-based web application that generates personalized learning paths using the Model Context Protocol (MCP). It integrates with YouTube, Google Drive, and Notion to create comprehensive, structured learning experiences tailored to your goals.

## ✨ Features

- 🎯 **Personalized Learning Paths** - Generate day-by-day learning plans based on your specific goals
- 🎥 **YouTube Integration** - Automatically curate educational videos and create playlists
- 📁 **Google Drive Integration** - Create structured learning documents
- 📝 **Notion Integration** - Organize learning materials in Notion pages
- 🚀 **Real-time Progress Tracking** - Visual progress indicators and status updates
- 🎨 **User-friendly Interface** - Clean, intuitive Streamlit interface
- 🔧 **Easy Setup** - One-command installation and setup

## 🚀 Quick Start

### Option 1: Automated Setup (Recommended)

1. **Clone or download the project**
2. **Run the setup script:**
   ```bash
   python setup.py
   ```
3. **Configure your environment:**
   - Copy `.env.template` to `.env`
   - Fill in your API keys and URLs
4. **Run the application:**
   ```bash
   python run.py
   ```
   Or on Windows: double-click `run.bat`
   Or on Mac/Linux: `./run.sh`

### Option 2: Manual Setup

1. **Create virtual environment:**
   ```bash
   python -m venv venv
   ```

2. **Activate virtual environment:**
   - Windows: `venv\Scripts\activate`
   - Mac/Linux: `source venv/bin/activate`

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application:**
   ```bash
   streamlit run app.py
   ```

## 📋 Prerequisites

- **Python 3.8+** (3.10+ recommended)
- **Google AI Studio API Key** - Get from [Google AI Studio](https://aistudio.google.com/)
- **Pipedream URLs** for integrations:
  - YouTube (required)
  - Google Drive or Notion (choose one)

## ⚙️ Configuration

### 1. Google API Key
- Visit [Google AI Studio](https://aistudio.google.com/)
- Create a new API key
- Copy the key for use in the application

### 2. Pipedream URLs
You'll need to create Pipedream workflows for:
- **YouTube Integration** (required)
- **Google Drive Integration** (optional)
- **Notion Integration** (optional)

### 3. Environment Variables
Create a `.env` file (copy from `.env.template`):
```env
GOOGLE_API_KEY=your_google_api_key_here
YOUTUBE_PIPEDREAM_URL=your_youtube_pipedream_url_here
DRIVE_PIPEDREAM_URL=your_drive_pipedream_url_here
NOTION_PIPEDREAM_URL=your_notion_pipedream_url_here
```

## 🎯 Usage

1. **Start the application** using one of the methods above
2. **Open your browser** to `http://localhost:8501`
3. **Configure the sidebar:**
   - Enter your Google API key
   - Enter your YouTube Pipedream URL
   - Choose either Drive or Notion
   - Enter the corresponding Pipedream URL
4. **Enter your learning goal** (e.g., "I want to learn Python basics in 3 days")
5. **Click "Generate Learning Path"** and watch the magic happen!

## 📁 Project Structure

```
mcp-learning-path-demo-main/
├── app.py                 # Main Streamlit application
├── utils.py              # Utility functions and MCP integration
├── prompt.py             # AI prompt templates
├── requirements.txt      # Python dependencies
├── setup.py             # Automated setup script
├── run.py               # Cross-platform run script
├── run.bat              # Windows batch file
├── run.sh               # Unix/Linux/Mac shell script
├── .env.template        # Environment variables template
├── .gitignore           # Git ignore file
└── README.md            # This file
```

## 🔧 Development

### Adding New Features
1. Make your changes to the relevant files
2. Test thoroughly
3. Update documentation if needed
4. Commit your changes

### Running Tests
```bash
python -m pytest tests/
```

### Building for Production
```bash
python setup.py
```

## 🐛 Troubleshooting

### Common Issues

1. **"No module named streamlit"**
   - Run `python setup.py` to install dependencies
   - Or manually: `pip install -r requirements.txt`

2. **"File does not exist: app.py"**
   - Make sure you're in the project root directory
   - Check that all files are present

3. **Port 8501 already in use**
   - Stop other Streamlit applications
   - Or specify a different port: `streamlit run app.py --server.port 8502`

4. **API Key errors**
   - Verify your Google API key is correct
   - Check that Pipedream URLs are valid and active

### Getting Help

- Check the console output for error messages
- Verify all prerequisites are installed
- Ensure API keys and URLs are correctly configured

## 📄 License

This project is open source and available under the MIT License.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📞 Support

If you encounter any issues or have questions, please open an issue on the project repository.
