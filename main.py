"""Main Streamlit application for Narrator Analyst AI."""

import streamlit as st
import pandas as pd
import os
from agent import NarratorAnalyst
from config import (
    PAGE_TITLE,
    PAGE_ICON,
    APP_DESCRIPTION,
    ERROR_NO_API_KEY,
    ERROR_FILE_UPLOAD,
    ERROR_ANALYSIS,
    ERROR_NARRATIVE,
    SUCCESS_UPLOAD,
    SUCCESS_ANALYSIS,
    SUCCESS_NARRATIVE,
    OPENAI_API_KEY
)

# Page configuration
st.set_page_config(
    page_title=PAGE_TITLE,
    page_icon=PAGE_ICON,
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom styling
st.markdown("""
    <style>
    .main-header {
        color: #1f77b4;
        text-align: center;
        padding: 20px;
    }
    .sidebar-header {
        color: #ff7f0e;
    }
    </style>
    """, unsafe_allow_html=True)


def load_sample_data():
    """Load sample CSV files."""
    sample_files = {}
    sample_dir = 'sample_data'
    
    if os.path.exists(sample_dir):
        for file in os.listdir(sample_dir):
            if file.endswith('.csv'):
                file_path = os.path.join(sample_dir, file)
                try:
                    sample_files[file] = pd.read_csv(file_path)
                except Exception as e:
                    st.warning(f"Could not load {file}: {e}")
    
    return sample_files


def display_data_analysis(df: pd.DataFrame, agent: NarratorAnalyst):
    """Display data analysis results."""
    st.subheader("📊 Data Analysis")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Total Rows", df.shape[0])
    with col2:
        st.metric("Total Columns", df.shape[1])
    with col3:
        st.metric("Missing Values", df.isnull().sum().sum())
    
    # Data preview
    st.write("**Data Preview:**")
    st.dataframe(df.head(), use_container_width=True)
    
    # Data statistics
    st.write("**Statistical Summary:**")
    st.dataframe(df.describe(), use_container_width=True)
    
    # Data info
    st.write("**Column Information:**")
    col_info = pd.DataFrame({
        'Column': df.columns,
        'Type': df.dtypes.values,
        'Non-Null Count': df.count().values,
        'Missing': df.isnull().sum().values
    })
    st.dataframe(col_info, use_container_width=True)


def main():
    """Main application logic."""
    
    # Header
    st.markdown(f"# {PAGE_ICON} {PAGE_TITLE}")
    st.write(APP_DESCRIPTION)
    st.divider()
    
    # Check API key
    if not OPENAI_API_KEY:
        st.error(ERROR_NO_API_KEY)
        st.info("Please create a `.env` file with your OpenAI API key to get started.")
        return
    
    # Initialize agent
    try:
        agent = NarratorAnalyst()
    except Exception as e:
        st.error(f"Failed to initialize agent: {e}")
        return
    
    # Sidebar
    with st.sidebar:
        st.markdown("### ⚙️ Configuration")
        
        data_source = st.radio(
            "Choose data source:",
            ("Upload CSV", "Use Sample Data")
        )
    
    # Main content
    df = None
    
    if data_source == "Upload CSV":
        st.subheader("📁 Upload Your Data")
        uploaded_file = st.file_uploader(
            "Choose a CSV file",
            type=["csv", "xlsx"],
            help="Upload a CSV or Excel file for analysis"
        )
        
        if uploaded_file is not None:
            try:
                if uploaded_file.name.endswith('.csv'):
                    df = pd.read_csv(uploaded_file)
                else:
                    df = pd.read_excel(uploaded_file)
                st.success(SUCCESS_UPLOAD)
            except Exception as e:
                st.error(f"{ERROR_FILE_UPLOAD}: {e}")
    
    else:  # Use Sample Data
        st.subheader("📦 Sample Datasets")
        sample_data = load_sample_data()
        
        if sample_data:
            selected_sample = st.selectbox(
                "Select a sample dataset:",
                list(sample_data.keys())
            )
            df = sample_data[selected_sample]
            st.success(f"Loaded {selected_sample}")
        else:
            st.info("No sample datasets found. Please create sample_data directory and add CSV files.")
    
    # Data Processing and Display
    if df is not None:
        st.divider()
        
        # Tabs for different views
        tab1, tab2, tab3 = st.tabs(["📊 Analysis", "📖 Story", "❓ Q&A"])
        
        with tab1:
            display_data_analysis(df, agent)
        
        with tab2:
            st.subheader("📖 Data Story")
            
            if st.button("✨ Generate Story", key="generate_story"):
                with st.spinner("🤖 Generating narrative..."):
                    try:
                        analysis = agent.analyze_data(df)
                        narrative = agent.generate_narrative(df, analysis)
                        st.success(SUCCESS_NARRATIVE)
                        st.markdown(narrative)
                    except Exception as e:
                        st.error(f"{ERROR_NARRATIVE}: {e}")
        
        with tab3:
            st.subheader("❓ Ask Questions About Your Data")
            
            question = st.text_input(
                "Ask a question about your data:",
                placeholder="e.g., What is the average sales per region?"
            )
            
            if question:
                if st.button("Get Answer", key="get_answer"):
                    with st.spinner("🤔 Analyzing..."):
                        try:
                            answer = agent.answer_question(df, question)
                            st.success("✅ Answer:")
                            st.write(answer)
                        except Exception as e:
                            st.error(f"Error: {e}")
    
    # Footer
    st.divider()
    st.markdown("""
        <div style="text-align: center; color: gray; margin-top: 20px;">
            <p>🤖 Narrator Analyst AI | Built with ❤️ for Microsoft Agents League Hackathon</p>
            <p>GitHub: <a href="https://github.com/jawaria1irfan-design/narrator-analyst.ai">jawaria1irfan-design/narrator-analyst.ai</a></p>
        </div>
    """, unsafe_allow_html=True)


if __name__ == "__main__":
    main()
