"""Core agent logic for Narrator Analyst AI."""

import pandas as pd
import openai
from config import (
    OPENAI_API_KEY,
    OPENAI_MODEL,
    OPENAI_MAX_TOKENS,
    OPENAI_TEMPERATURE,
    ERROR_NO_API_KEY
)

# Set OpenAI API key
openai.api_key = OPENAI_API_KEY


class NarratorAnalyst:
    """AI Agent for analyzing data and generating narratives."""
    
    def __init__(self):
        """Initialize the Narrator Analyst agent."""
        if not OPENAI_API_KEY:
            raise ValueError(ERROR_NO_API_KEY)
        self.model = OPENAI_MODEL
        self.max_tokens = OPENAI_MAX_TOKENS
        self.temperature = OPENAI_TEMPERATURE
    
    def analyze_data(self, df: pd.DataFrame) -> dict:
        """Analyze a DataFrame and return key statistics.
        
        Args:
            df: Pandas DataFrame to analyze
            
        Returns:
            Dictionary containing data analysis results
        """
        try:
            analysis = {
                'shape': df.shape,
                'columns': list(df.columns),
                'dtypes': df.dtypes.to_dict(),
                'missing_values': df.isnull().sum().to_dict(),
                'basic_stats': df.describe().to_dict(),
                'info': str(df.info()),
            }
            return analysis
        except Exception as e:
            print(f"Error during data analysis: {e}")
            return {}
    
    def generate_narrative(self, df: pd.DataFrame, analysis: dict) -> str:
        """Generate a creative narrative about the data using OpenAI.
        
        Args:
            df: Pandas DataFrame to analyze
            analysis: Dictionary containing analysis results
            
        Returns:
            Generated narrative string
        """
        try:
            # Prepare data summary
            data_summary = f"""
            Dataset Shape: {analysis.get('shape', 'Unknown')}
            Columns: {', '.join(analysis.get('columns', []))}
            Total Records: {df.shape[0]}
            
            Data Preview:
            {df.head().to_string()}
            
            Basic Statistics:
            {df.describe().to_string()}
            """
            
            # Create prompt for OpenAI
            prompt = f"""You are a creative data storyteller. Analyze the following data and create an engaging narrative that tells the story of this data. 
            
Data:
{data_summary}

Please create:
1. An engaging title for this data story
2. A 3-4 paragraph narrative that explains:
   - What the data is about
   - Key patterns and trends
   - Interesting insights
   - Business implications

Make it creative, informative, and easy to understand.
            """
            
            # Call OpenAI API
            response = openai.ChatCompletion.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": "You are a creative data analyst who tells compelling stories from data."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=self.max_tokens,
                temperature=self.temperature
            )
            
            narrative = response.choices[0].message['content']
            return narrative
            
        except openai.error.APIError as e:
            print(f"OpenAI API Error: {e}")
            return "Error generating narrative. Please check your API key and try again."
        except Exception as e:
            print(f"Error generating narrative: {e}")
            return f"Error: {str(e)}"
    
    def answer_question(self, df: pd.DataFrame, question: str) -> str:
        """Answer a user's question about the data.
        
        Args:
            df: Pandas DataFrame
            question: User's question about the data
            
        Returns:
            Answer from the AI agent
        """
        try:
            # Prepare data context
            data_context = f"""
            I have a dataset with the following information:
            {df.head(10).to_string()}
            
            Column names: {', '.join(df.columns)}
            Data types: {df.dtypes.to_dict()}
            Shape: {df.shape}
            """
            
            # Create prompt
            prompt = f"""Based on this dataset, please answer the following question:
            
{data_context}

Question: {question}

Provide a clear, concise answer with specific insights from the data.
            """
            
            # Call OpenAI API
            response = openai.ChatCompletion.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": "You are a helpful data analyst assistant. Answer questions about data with specific, data-driven insights."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=500,
                temperature=0.7
            )
            
            answer = response.choices[0].message['content']
            return answer
            
        except Exception as e:
            print(f"Error answering question: {e}")
            return f"Error: Unable to answer your question. Please try again."
    
    def get_key_insights(self, df: pd.DataFrame) -> list:
        """Extract key insights from the data.
        
        Args:
            df: Pandas DataFrame
            
        Returns:
            List of key insights
        """
        try:
            insights = []
            
            # Numeric insights
            numeric_cols = df.select_dtypes(include=['number']).columns
            for col in numeric_cols[:3]:
                max_val = df[col].max()
                min_val = df[col].min()
                mean_val = df[col].mean()
                insights.append(f"{col}: Range {min_val:.2f} to {max_val:.2f}, Average {mean_val:.2f}")
            
            return insights
        except Exception as e:
            print(f"Error getting insights: {e}")
            return []
