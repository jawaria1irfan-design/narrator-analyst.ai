# Narrator Analyst AI 🤖📊

A Data Storyteller AI Agent that transforms raw CSV data into creative narratives and actionable insights using multi-step reasoning.

## 🎯 Project Overview

Narrator Analyst AI is an intelligent reasoning agent built for the **Microsoft Agents League Hackathon** that:

- **Analyzes CSV data** using advanced data processing
- **Generates creative narratives** from raw data
- **Provides multi-step reasoning** for complex insights
- **Answers natural language questions** about your data
- **Creates visualizations** to tell your data story

## ✨ Features

✅ **CSV File Upload** - Upload and analyze your own data files
✅ **Data Analysis** - Automatic data exploration and profiling
✅ **AI-Powered Narratives** - Get creative stories from your data
✅ **Q&A Interface** - Ask questions and get instant insights
✅ **Sample Datasets** - Test with pre-loaded example data
✅ **User-Friendly UI** - Built with Streamlit for ease of use

## 🛠️ Tech Stack

- **Python 3.8+** - Core programming language
- **Pandas** - Data analysis and manipulation
- **OpenAI API** - GPT for reasoning and narrative generation
- **Streamlit** - Web interface
- **Python-dotenv** - Environment variable management

## 📁 Project Structure

```
narrator-analyst.ai/
├── main.py                 # Streamlit app entry point
├── agent.py               # Core agent logic
├── config.py              # Configuration settings
├── requirements.txt       # Python dependencies
├── .env.example           # Environment template
├── .gitignore            # Git ignore file
├── README.md             # This file
└── sample_data/          # Sample CSV files for testing
    ├── sales_data.csv
    └── company_metrics.csv
```

## 🚀 Quick Start

### 1. Clone the Repository
```bash
git clone https://github.com/jawaria1irfan-design/narrator-analyst.ai.git
cd narrator-analyst.ai
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Set Up Environment Variables
```bash
# Create .env file
cp .env.example .env

# Edit .env and add your OpenAI API key
# OPENAI_API_KEY=sk-proj-your-key-here
```

### 4. Run the Application
```bash
streamlit run main.py
```

The app will open in your browser at `http://localhost:8501`

## 💡 How to Use

1. **Upload a CSV File** - Click "Browse files" and select your CSV
2. **View Data Analysis** - See automatic data profiling and statistics
3. **Generate Narrative** - Click "Generate Story" to create AI-powered insights
4. **Ask Questions** - Use the Q&A section to ask questions about your data
5. **Get Visualizations** - View charts and graphs of key insights

## 📊 Example Workflow

```
User Input: Upload sales_data.csv
    ↓
Agent Analysis: Reads and profiles the data
    ↓
Reasoning: Identifies patterns, trends, anomalies
    ↓
Narrative Generation: Creates story about the data
    ↓
User Output: Creative insights + visualizations
```

## 🔧 Configuration

Edit `config.py` to customize:
- OpenAI model selection
- Narrative style preferences
- Analysis parameters
- UI settings

## 📈 Sample Data

The project includes sample CSV files:
- **sales_data.csv** - Monthly sales data across regions
- **company_metrics.csv** - Company performance metrics

Use these to test the agent before using your own data.

## 🎓 Learning Path

This project teaches you:
1. ✅ AI/LLM API integration
2. ✅ Data analysis with Pandas
3. ✅ Multi-step reasoning with AI
4. ✅ Web app development with Streamlit
5. ✅ Environment management and best practices

## 🐛 Troubleshooting

**Issue**: "API key not found"
- **Solution**: Make sure your `.env` file has `OPENAI_API_KEY=your-key`

**Issue**: "Module not found"
- **Solution**: Run `pip install -r requirements.txt`

**Issue**: "Port already in use"
- **Solution**: Run `streamlit run main.py --server.port 8502`

## 📚 Documentation

- [OpenAI API Docs](https://platform.openai.com/docs)
- [Streamlit Docs](https://docs.streamlit.io)
- [Pandas Docs](https://pandas.pydata.org/docs)

## 🏆 Hackathon Track

**Track**: Reasoning Agents
**Tool**: GitHub Copilot
**Challenge**: Create intelligent agents that solve complex problems through multi-step reasoning

## 📄 License

MIT License - Feel free to use this project for learning and development!

## 👩‍💻 Author

**Jawaria Irfan**
- GitHub: [@jawaria1irfan-design](https://github.com/jawaria1irfan-design)
- Project: Microsoft Agents League Hackathon 2026

## ✨ Contributing

Feel free to fork, modify, and improve this project!

---

**Happy Data Storytelling!** 🎉📊
