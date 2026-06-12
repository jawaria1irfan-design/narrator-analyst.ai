"""Configuration settings for Narrator Analyst AI."""

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# OpenAI Configuration
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
OPENAI_MODEL = os.getenv('OPENAI_MODEL', 'gpt-3.5-turbo')
OPENAI_MAX_TOKENS = int(os.getenv('OPENAI_MAX_TOKENS', 1000))
OPENAI_TEMPERATURE = float(os.getenv('OPENAI_TEMPERATURE', 0.7))

# Application Settings
APP_NAME = "Narrator Analyst AI"
APP_DESCRIPTION = "Transform your data into creative stories and insights"
APP_VERSION = "1.0.0"

# Data Processing
MAX_UPLOAD_SIZE = 50  # MB
SUPPORTED_FORMATS = ['csv', 'xlsx', 'xls']

# UI Settings
PAGE_TITLE = "Narrator Analyst AI 🤖📊"
PAGE_ICON = "📊"

# Sample data paths
SAMPLE_DATA_DIR = 'sample_data'

# Error messages
ERROR_NO_API_KEY = "⚠️ OpenAI API key not configured. Please add OPENAI_API_KEY to your .env file."
ERROR_FILE_UPLOAD = "❌ Error uploading file. Please check the file format."
ERROR_ANALYSIS = "❌ Error analyzing data. Please try again."
ERROR_NARRATIVE = "❌ Error generating narrative. Please try again."

# Success messages
SUCCESS_UPLOAD = "✅ File uploaded successfully!"
SUCCESS_ANALYSIS = "✅ Data analysis complete!"
SUCCESS_NARRATIVE = "✅ Narrative generated successfully!"
