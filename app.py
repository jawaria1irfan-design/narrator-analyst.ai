import streamlit as st
import pandas as pd
from groq import Groq
import os
import io
from dotenv import load_dotenv

# 1. Page Configuration
st.set_page_config(
    page_title="Narrator Analyst AI",
    page_icon="🎙️",
    layout="wide",
    initial_sidebar_state="expanded"
)
# Custom styling to change the background colors of the input widgets
st.markdown("""
    <style>
    /* 1. Target the Dropdown Selector Container */
    div[data-baseweb="select"] > div {
        background-color: #ffffff !important;
        color: #000000 !important;
        border-radius: 8px !important;
        border: 1px solid #ffffff !important;
    }
    
    /* 2. Target the File Drag-and-Drop Area Container */
    div[data-testid="stFileUploader"] > section {
        background-color: #ffffff !important;
        border: 2px dashed rgb(106, 1, 86) !important;
        border-radius: 12px !important;
        padding: 20px !important;
    }
    
    /* Force the upload button inside the tray to match your brand style */
    div[data-testid="stFileUploader"] button {
        background-color: rgb(106, 1, 86) !important;
        color: white !important;
        border-radius: 6px !important;
    }
    </style>
""", unsafe_allow_html=True)

# Load environment configurations
load_dotenv()
api_credential = os.getenv("GROQ_API_KEY")

# Initialize Native Client Connection
client = None
if api_credential:
    client = Groq(api_key=api_credential)

# 2. Sidebar Layout Configuration Panel
with st.sidebar:
    st.title("⚙️ Configuration")
    st.write("Fine-tune processing parameters globally.")
    st.divider()
    
    selected_model = st.selectbox(
        "Processing Model",
        options=["llama-3.3-70b-versatile", "llama-3.1-8b-instant"],
        index=0
    )
    
    ai_creativity = st.slider(
        "Narrator Expression",
        min_value=0.0,
        max_value=1.0,
        value=0.4,
        step=0.1,
        help="Higher positions unlock advanced vocabulary structures."
    )
    st.divider()
    st.caption("🔒 Workspace runtime active.")

# 3. Principal Dashboard Viewport Header
st.title("🎙️ Narrator Analyst AI")
st.subheader("Synthesize multi-dimensional datasets into clear corporate narratives.")
st.caption("Microsoft AI Agent League Hackathon 2026")
st.divider()

# 4. Engine Core Logic Validation Flow
if not api_credential:
    st.error("🔒 **Environment Exception:** Core runtime credential keys could not be resolved.")
else:
    # Clean File Uploader
    uploaded_file = st.file_uploader("Upload your data matrix (CSV format) below to initialize analysis", type=["csv"])
    
    if uploaded_file is not None:
        try:
            # Load file in-memory
            df = pd.read_csv(uploaded_file)
            st.toast("Data Matrix Imported Cleanly", icon="✨")
            
            st.write("### 📈 Operational Workspace Streams")
            
            # Premium Native Minimalist Metric Cards
            m_col1, m_col2, m_col3 = st.columns(3)
            with m_col1:
                st.metric(label="Total Records (Rows)", value=f"{df.shape[0]:,}")
            with m_col2:
                st.metric(label="Feature Matrix (Columns)", value=df.shape[1])
            with m_col3:
                st.metric(label="Unpopulated Cells (Nulls)", value=f"{df.isna().sum().sum():,}")
            
            st.markdown("<br>", unsafe_allow_html=True)
            
            # Executive Dashboard Tabs Design Setup
            tab_view, tab_story, tab_qa = st.tabs(["📉 Interactive Inspector", "📚 Narrative Story Generation", "Interactive Q&A Panel📍"])
            
            # TAB 1: FILE MATRIX INSPECTION PANEL
            with tab_view:
                st.write("#### Data Snapshot View")
                st.dataframe(df.head(10), use_container_width=True)
                
                with st.expander("🔍 Inspect Dimensional Distribution Aggregates"):
                    st.dataframe(df.describe(include='all'), use_container_width=True)
            
            # TAB 2: CONTEXT-AWARE STORY REPORTING PASS
            with tab_story:
                st.write("## Analytical Storytelling Studio")
                st.write("Authorize the AI agent cluster to compile distribution skews, columns, and patterns into deep reporting.")
                
                if st.button("✨ Compile & Narrate Data Story", type="primary", use_container_width=True):
                    with st.spinner("⚡ Correlating variables... Writing analytical data story summaries..."):
                        buffer = io.StringIO()
                        df.info(buf=buffer)
                        schema_summary = buffer.getvalue()
                        statistical_matrix = df.describe(include='all').to_string()
                        data_sample = df.head(5).to_string()
                        
                        inference_prompt = f"""
                        You are the premium 'Narrator Analyst AI' module designed for the Microsoft AI Agent League Hackathon.
                        Process statistical summaries and convert them into beautiful markdown text reporting.
                        
                        Dataset Overview:
                        - Size: {df.shape[0]} rows x {df.shape[1]} columns.
                        - Schema: {schema_summary}
                        - Distribution Matrix: {statistical_matrix}
                        - Snippet: {data_sample}
                        
                        Provide:
                        1. A distinct, elegant title headline explaining what the data story tracks.
                        2. Executive Abstract Overview (Domain overview modeling).
                        3. Core Pattern Discoveries & Feature Anomalies.
                        4. Strategic Business Impacts & Takeaways.
                        """
                        completion = client.chat.completions.create(
                            model=selected_model,
                            messages=[
                                {"role": "system", "content": "You are an executive data storyteller who delivers crisp, professional insights."},
                                {"role": "user", "content": inference_prompt}
                            ],
                            temperature=ai_creativity
                        )
                        st.success("🌟 Story Synthesis Complete!")
                        st.divider()
                        st.markdown(completion.choices[0].message.content)
                        st.divider()
            
            # TAB 3: MATRIX-BASED CONVERSATIONAL Q&A FIELD
            with tab_qa:
                st.write("#### Conversational Data Sandbox")
                user_question = st.text_input("Pose a targeted query about the loaded schema structure:", placeholder="e.g., Which columns show the highest value deviations?")
                
                if user_question:
                    if st.button("🤔 Execute Context Extraction", key="qa_btn", use_container_width=True):
                        with st.spinner("🤖 Evaluating metrics data arrays..."):
                            data_context = f"Rows: {df.shape[0]}, Columns: {df.shape[1]}\nColumns List: {', '.join(df.columns)}\nPreview:\n{df.head(5).to_string()}"
                            qa_prompt = f"Using this data context:\n{data_context}\n\nAnswer this question: {user_question}"
                            
                            qa_completion = client.chat.completions.create(
                                model=selected_model,
                                messages=[
                                    {"role": "system", "content": "You are a pragmatic, data-driven analytical assistant."},
                                    {"role": "user", "content": qa_prompt}
                                ]
                            )
                            st.write("#### ✅ Extracted System Insights:")
                            st.info(qa_completion.choices[0].message.content)
                            
        except Exception as e:
            st.error(f"Workspace Runtime Halt Exception: {str(e)}")

# 5. Clean, Professional Footer Banner Row
st.divider()
st.center = st.caption("Narrator Analyst AI • Crafted for the Microsoft AI Agent League Hackathon 2026")
