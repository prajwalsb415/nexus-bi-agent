# NexusBI: Autonomous Enterprise BI & Compliance Agent

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://nexus-bi-agent.streamlit.app)
[![Python 3.11+](https://img.shields.io/badge/python-3.11%2B-blue.svg)](https://www.python.org/)
[![Groq LPU](https://img.shields.io/badge/Accelerated_by-Groq_LPUs-orange.svg)](https://groq.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**NexusBI** is an enterprise-grade autonomous Business Intelligence and Compliance agent designed to bridge structured transactional databases with unstructured corporate policy documentation. Powered by ultra-low-latency Groq LPUs, NexusBI processes natural language inquiries, generates schema-aware SQLite queries, and performs semantic BM25 document retrieval to synthesize real-time executive reports.

🚀 **Live App URL:** [https://nexus-bi-agent.streamlit.app](https://nexus-bi-agent.streamlit.app)

---

## 🚀 Quick Execution Steps (Run Locally)

Execute these commands sequentially in your terminal to set up, build, and launch the application locally:

```bash
# 1. Clone the repository
git clone [https://github.com/prajwalsb415/nexus-bi-agent.git](https://github.com/prajwalsb415/nexus-bi-agent.git)
cd nexus-bi-agent

# 2. Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate

# 3. Install required dependencies
pip install -r requirements.txt

# 4. Set your Groq API key environment variable
export GROQ_API_KEY="your_groq_api_key_here"

# 5. Launch the Streamlit dashboard
streamlit run app.py
*Core Capabilities
1. Dynamic Query Routing: Intelligently classifies requests to determine whether to query transactional databases, retrieve compliance documentation, or perform cross-system hybrid analysis.

2. Autonomous Text-to-SQL: Schema-aware query synthesis capable of managing complex relational joins across customer tiers, order statuses, and financial performance metrics.

3. In-Memory Policy RAG: Zero-overhead, high-speed BM25 semantic retrieval for internal SLAs, uptime penalties, refund rules, and freight terms.

4. Sub-Second Latency: Accelerated enterprise analytics utilizing Groq's high-speed inference engine.

**Architecture & Tech Stack
1. Language & Frameworks: Python, Streamlit, LangChain, LangChain-Community

2. Inference Engine: Groq API (openai/gpt-oss-20b)

3. Database Layer: SQLite3

4. Retrieval Engine: BM25Okapi (rank_bm25)

Data Processing: Pandas
5. Executive Control Center: A responsive Streamlit interface featuring live telemetry metrics, deep compliance inspection drawers, and clear analytical formatting.
Example Queries to Test


These questions u can verify for testing 
*Structured SQL Analytics
"What is the total revenue generated from Enterprise tier customers?"

"Which customer has placed the highest single order, and what is the status of that purchase?"

"Show me a breakdown of all orders grouped by status with total count and revenue."

"List all customers located in Europe along with their tier."


*Policy & Compliance Inquiries (RAG)
"What is our official return and refund policy for Pro vs. Enterprise tier clients?"

"What uptime percentage is guaranteed under our Enterprise SLA, and what credits apply if violated?"

"What are our freight shipping charges, and at what order value does shipping become free?"

*Hybrid Cross-System Queries (SQL + RAG)
"Check the order history for Apex Logistics and confirm if their order total qualifies them for free expedited shipping under our policy."

"Which customer had an order refunded, and what restocking fee rule applies to them based on their tier?"




cat << 'EOF' > LICENSE
MIT License

Copyright (c) 2026 Prajwal Bashetti

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
EOF
