from dotenv import load_dotenv
import streamlit as st
import os
import sqlite3
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Configure Gemini API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to load Gemini model and generate SQL query
def get_gemini_response(question, prompt):
    model = genai.GenerativeModel('gemini-pro')
    full_prompt = prompt + "\n\nUser Query: " + question  # Better structuring
    response = model.generate_content(full_prompt)
    sql_query = response.text.strip()  # Clean the response
    return sql_query

# Function to retrieve query results from the database
def read_sql_query(sql, db):
    try:
        conn = sqlite3.connect(db)
        cur = conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()
        conn.close()
        return rows
    except Exception as e:
        return [("Error:", str(e))]  # Return error message if query fails

# Define prompt
prompt = """
You are an expert in SQL query generation. Your task is to convert natural language questions into valid SQL queries based on the given database schema.

Instructions:
- The SQL database schema will be provided.
- Generate a syntactically correct SQL query based on the input question.
- The SQL query should be optimized and free from unnecessary clauses.
- Do not include SQL keywords or formatting like triple backticks (```) in the response.
- If the question is ambiguous, generate the most probable SQL query.

Example:

Input: "How many students are in the database?"
Output: SELECT COUNT(*) FROM STUDENT_INFO;

Input: "List all students in CLASS 10 section A."
Output: SELECT * FROM STUDENT_INFO WHERE CLASS = '10' AND SECTION = 'A';

Input: "Show the names of students in Data Science Section."
Output: SELECT NAME FROM STUDENT_INFO WHERE SECTION = 'Data Science';
"""

# Streamlit App
st.set_page_config(page_title="SQL Query Generator")
st.header("Gemini App To Retrieve SQL Data")

question = st.text_input("Enter your question:", key="input")
submit = st.button("Generate SQL Query")

# If submit is clicked
if submit:
    sql_query = get_gemini_response(question, prompt)
    st.subheader("Generated SQL Query")
    st.code(sql_query, language="sql")  # Show SQL query

    response = read_sql_query(sql_query, "student.db")

