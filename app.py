import os
import sqlite3
import pandas as pd
import streamlit as st
from src.config import get_groq_api_key, DB_PATH
from src.database import init_mock_database, get_connection
from src.vector_store import build_vector_store
from src.agent import build_agent_executor

st.set_page_config(
    page_title="NexusBI | Enterprise Autonomous Agent",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Polished High-Contrast Enterprise Styling
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
    html, body, [class*="css"] { font-family: 'Inter', sans-serif; }
    .stApp { background: #0b0f17; color: #f0f6fc; }
    
    .metric-container { display: flex; gap: 1rem; margin-bottom: 1.5rem; }
    .metric-card {
        background: #161b22;
        border: 1px solid #30363d;
        border-radius: 10px;
        padding: 1rem 1.25rem;
        flex: 1;
    }
    .metric-title { color: #8b949e; font-size: 0.78rem; font-weight: 600; text-transform: uppercase; }
    .metric-value { font-size: 1.5rem; font-weight: 700; color: #58a6ff; margin-top: 0.25rem; }
    .metric-badge {
        font-size: 0.75rem; padding: 0.2rem 0.5rem; border-radius: 20px;
        background: rgba(46, 160, 67, 0.2); color: #3fb950; display: inline-block; margin-top: 0.4rem;
    }
    
    /* Ensure chat message text is crisp, white, and always readable */
    [data-testid="stChatMessage"] {
        background: #161b22 !important;
        border: 1px solid #30363d !important;
        border-radius: 10px !important;
        padding: 1rem !important;
        margin-bottom: 0.75rem !important;
        color: #ffffff !important;
    }
    [data-testid="stChatMessage"] p, [data-testid="stChatMessage"] li {
        color: #f0f6fc !important;
        font-size: 0.95rem !important;
        line-height: 1.6 !important;
    }
</style>
""", unsafe_allow_html=True)

init_mock_database()

@st.cache_resource
def get_cached_retriever():
    return build_vector_store()

retriever = get_cached_retriever()

with st.sidebar:
    st.image("https://img.icons8.com/isometric/100/database-administrator.png", width=64)
    st.markdown("### **NexusBI Enterprise Core**")
    st.caption("Agentic Data Mesh & Policy Governance")
    st.divider()

    api_key = get_groq_api_key()
    if not api_key:
        api_key = st.text_input("Enter Groq API Key:", type="password")

    st.markdown("#### ⚡ Quick Questions")
    selected_query = None
    if st.button("📊 Enterprise Revenue (SQL)"):
        selected_query = "What is the total revenue generated from Enterprise tier customers?"
    if st.button("📄 SLA & Uptime Rules (RAG)"):
        selected_query = "What is the uptime SLA guarantee and what credits are issued if violated?"
    if st.button("🔀 Policy & Order Join (Hybrid)"):
        selected_query = "Does customer 'Apex Logistics' order volume qualify them for free expedited shipping under policy rules?"

    st.divider()
    with st.expander("🔍 View Raw Database Tables"):
        conn = get_connection()
        st.markdown("**Customers**")
        st.dataframe(pd.read_sql_query("SELECT * FROM customers", conn), hide_index=True)
        st.markdown("**Orders**")
        st.dataframe(pd.read_sql_query("SELECT * FROM orders LIMIT 5", conn), hide_index=True)
        conn.close()

st.title("⚡ NexusBI: Autonomous Enterprise Agent")

conn = get_connection()
cur = conn.cursor()
cur.execute("SELECT SUM(amount) FROM orders WHERE status = 'Completed'")
total_rev = cur.fetchone()[0] or 0.0
cur.execute("SELECT COUNT(DISTINCT customer_id) FROM customers")
total_clients = cur.fetchone()[0] or 0
conn.close()

st.markdown(f"""
<div class="metric-container">
    <div class="metric-card">
        <div class="metric-title">Tracked Revenue</div>
        <div class="metric-value">${total_rev:,.2f}</div>
        <span class="metric-badge">● Live Synced</span>
    </div>
    <div class="metric-card">
        <div class="metric-title">Active Clients</div>
        <div class="metric-value">{total_clients} Accounts</div>
        <span class="metric-badge">● SQL Verified</span>
    </div>
    <div class="metric-card">
        <div class="metric-title">Latency</div>
        <div class="metric-value">&lt; 1.2s</div>
        <span class="metric-badge">● Groq LPU Engine</span>
    </div>
</div>
""", unsafe_allow_html=True)

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Welcome to NexusBI. Ask any financial or compliance question across our customer database and SLA documents."}
    ]

# Render chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

user_input = st.chat_input("Enter natural language business inquiry...")
query = selected_query or user_input

if query:
    if not api_key:
        st.error("Please provide a Groq API Key in the left sidebar.")
    else:
        st.session_state.messages.append({"role": "user", "content": query})
        with st.chat_message("user"):
            st.markdown(query)

        with st.chat_message("assistant"):
            with st.spinner("Analyzing and querying enterprise systems..."):
                try:
                    executor = build_agent_executor(api_key, retriever)
                    response_payload = executor.invoke({"input": query})
                    output_text = response_payload["output"]

                    st.markdown(output_text)
                    st.session_state.messages.append({"role": "assistant", "content": output_text})
                except Exception as e:
                    st.error(f"Execution Error: {str(e)}")
