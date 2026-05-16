# 🚀 Multi-Agent Financial Assistant (Google ADK)

## 📌 Overview

This project implements a **privacy-aware multi-agent AI system** using Google ADK and Gemini LLM.
It is designed to handle **sensitive financial queries securely** by separating private data processing from external knowledge retrieval.

Unlike traditional chatbots, this system uses **LLM orchestration with specialized agents** to deliver accurate, real-time, and reliable financial insights.

---

## 🎯 Problem Statement

General-purpose LLMs (like ChatGPT) are not ideal for handling **sensitive user data** such as financial records. When directly connected to databases, they are vulnerable to:

* Prompt Injection
* Data Leakage
* Uncontrolled Tool Access

This makes them risky for real-world applications like banking or financial advisory systems.

---

## 💡 Solution

This project solves the above problem by implementing a **multi-agent architecture** with controlled responsibilities:

* 🔐 **Private Data Handling** → Accessed only via secure custom tools
* 🌐 **External Knowledge** → Retrieved using Google Search (grounded data)
* 🧠 **Orchestrator Agent** → Controls workflow and decision-making
* ⚙️ **Agent Handoff** → Delegates tasks to specialized agents

This ensures **secure, modular, and scalable AI workflows**.

---

## 🧠 Architecture

### 👇 System Flow

```
User Query
   ↓
Orchestrator Agent (Planner)
   ↓
 ┌───────────────┬────────────────┐
 ↓                               ↓
Finance Agent                Investment Agent
(Private Data)              (Google Search)
 ↓                               ↓
 └───────────────┬────────────────┘
                 ↓
        Final Response (Streamed via SSE)
```

---

## ⚙️ Tech Stack

* **Framework**: Google Agent Development Kit (ADK)
* **Language**: Python 3.13
* **LLM**: Gemini 1.5 Flash / 2.5 Flash Lite
* **Backend**: FastAPI + Uvicorn
* **Streaming**: Server-Sent Events (SSE)
* **Tools**: Google Search API, Custom Python Tools
* **Data Models**: Pydantic
* **Concepts**: Multi-Agent Systems, LLM Orchestration, Tool Calling

---

## 🛠️ Quick Start

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd <repository-name>
   ```

2. **Create a virtual environment & install dependencies**
   ```bash
   python -m venv .venv
   # On Windows:
   .venv\Scripts\activate
   # On macOS/Linux:
   source .venv/bin/activate
   
   pip install -r requirements.txt
   ```

3. **Set up Environment Variables**
   Create a `.env` file in the root directory and add your API key:
   ```env
   GOOGLE_API_KEY=your_google_gemini_api_key_here
   ```

4. **Run the Application**
   *(Specify your run command here based on your entry point)*
   ```bash
   python main.py
   # or if using FastAPI directly: uvicorn main:app --reload
   ```

---

## 🔄 Query Flow

1. User sends query via ADK Web UI
2. Request hits FastAPI `/run_sse` endpoint
3. **Runner** initializes and manages:

   * Context (conversation memory)
   * Tool execution
   * Agent routing
4. If needed:

   * Calls custom tools (finance data)
   * Performs agent handoff (investment research)
5. Response is streamed in real-time using SSE
6. Session state is stored for follow-up queries

---

## 📈 Example Use Case

**User Query:**

> "I want to save for a $50k down payment. Based on my spending, how long will it take?"

### System Execution:

* Fetches user financial data
* Calculates savings capacity
* Searches real-time investment options
* Generates a personalized plan

### Output:

* Savings timeline
* Investment recommendations
* Optimized financial strategy

---

## 🔐 Key Features

* ✅ Secure handling of sensitive financial data
* ✅ Multi-agent task specialization
* ✅ Real-time data integration (Google Search)
* ✅ Streaming responses (ChatGPT-like UX)
* ✅ Modular and scalable architecture
* ✅ Reduced hallucination via grounded responses

---
<img width="1536" height="1024" alt="Multi-Agent Financial Assistant workflow__endoftext__" src="https://github.com/user-attachments/assets/8fc4a57d-67e6-40cd-ae75-b051b0aacdbf" />


## 🚀 Why Multi-Agent Instead of Single LLM?

| Single LLM                    | Multi-Agent System          |
| ----------------------------- | --------------------------- |
| ❌ No control over data access | ✅ Controlled tool usage     |
| ❌ Prone to hallucination      | ✅ Grounded with real data   |
| ❌ Security risks              | ✅ Isolated responsibilities |
| ❌ Monolithic                  | ✅ Modular & scalable        |

---

## 🧪 Future Improvements

* Add persistent database (PostgreSQL / MongoDB)
* Implement user authentication & role-based access
* Add memory (long-term context)
* Deploy on cloud (Render / GCP / AWS)
* Build frontend dashboard (React / Streamlit)

---

## 🏆 Key Learning Outcomes

* Designing **multi-agent AI architectures**
* Implementing **LLM orchestration**
* Building **secure AI pipelines**
* Integrating **real-time external tools**
* Managing **context & streaming responses**

