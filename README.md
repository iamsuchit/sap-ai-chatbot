# 🤖 AI WhatsApp Chatbot (RAG-based)

🚀 Live Demo: https://ai-chatbot-4k3o.onrender.com  

An AI-powered WhatsApp chatbot that answers user queries using business data (PDFs) and simulates a Swiggy/Zomato-style assistant.

---

## ✨ Features
- 📄 Multi-PDF Knowledge Base
- 🧠 Retrieval-Augmented Generation (RAG)
- 💬 WhatsApp Integration (Twilio)
- ⚡ FastAPI Backend
- ☁️ Cloud Deployment (Render)
- 🤖 Conversational AI Responses

---


## 🧠 Architecture

User → WhatsApp → Twilio → FastAPI → LangChain → OpenAI → FAISS → Response

---

## 🚀 Tech Stack
- FastAPI
- LangChain
- OpenAI
- FAISS
- Twilio
- Python


# 🤖 SAP AI Chatbot (WhatsApp + FastAPI + RAG)

An intelligent **AI-powered WhatsApp chatbot** built using **FastAPI, LangChain, and OpenAI**, capable of answering business-related queries from multiple PDF documents and simulating a **Swiggy/Zomato-style conversational assistant**.

---

## 🚀 Features

* 📄 Multi-PDF document processing
* 🧠 Retrieval-Augmented Generation (RAG)
* 🤖 Conversational AI (natural responses)
* 💬 WhatsApp webhook integration
* 🛒 Basic order handling flow
* 🧩 Modular and scalable architecture
* 👥 Per-user memory (session-based)

---

## 🏗️ Project Structure

```
sap-ai-chatbot/
│
├── app/
│   ├── main.py                # FastAPI entry point
│   ├── config.py              # Environment config
│   │
│   ├── services/
│   │   ├── pdf_loader.py      # Load multiple PDFs
│   │   ├── vector_store.py    # FAISS + embeddings
│   │   ├── ai_chain.py        # LLM + prompt logic
│   │
│   ├── routes/
│   │   └── webhook.py         # WhatsApp webhook logic
│   │
│   ├── utils/
│
├── data/                      # PDF files
├── .env                       # API keys
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone <your-repo-url>
cd sap-ai-chatbot
```

### 2. Create virtual environment

```bash
python -m venv .venv
.venv\Scripts\activate   # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Setup

Create a `.env` file in the root directory:

```env
OPENAI_API_KEY=your_openai_api_key_here
```

---

## 📄 Add PDF Data

1. Create a `data/` folder
2. Add your business PDFs:

Example:

```
data/
├── menu.pdf
├── faq.pdf
├── policies.pdf
├── company_overview.pdf
```

---

## ▶️ Run the Application

```bash
uvicorn app.main:app --reload
```

Server will run at:

```
http://127.0.0.1:8000
```

---

## 🔌 API Endpoints

### Health Check

```
GET /
```

Response:

```json
{
  "message": "✅ AI Bot Running"
}
```

---

### WhatsApp Webhook

```
POST /webhook
```

Handles incoming WhatsApp messages and returns AI-generated responses.

---

## 🧠 How It Works

### 1. PDF Processing

* Reads all PDFs from `data/`
* Extracts text using PyPDF2
* Splits into chunks

### 2. Vector Database

* Converts text into embeddings
* Stores in FAISS for fast retrieval

### 3. AI Response

* Retrieves relevant chunks
* Sends context to OpenAI model
* Generates conversational response

### 4. Memory Handling

* Stores last messages per user
* Provides context-aware replies

---

## 💬 Example Conversations

**User:**

> Show menu

**Bot:**

> Hey! 👋 We have coffee, shakes, snacks & desserts.
> Our Cold Coffee ☕ is a favorite! Want suggestions?

---

**User:**

> Suggest something

**Bot:**

> You should try our Chocolate Frappe 🍫 — super popular!
> Want something to eat with it?

---

**User:**

> I want cold coffee

**Bot:**

> Great choice! 😊 Adding Cold Coffee ☕
> Would you like to add fries or a brownie?

---

## ⚠️ Important Notes

* Ensure PDFs are valid (not renamed `.txt`)
* Use Python 3.10 or 3.11 (recommended)
* API key must be correctly set in `.env`
* Restart server after changes

---

## 🔥 Future Improvements

* 🛒 Full cart & checkout system
* 💳 Payment integration
* 📊 Admin dashboard
* 📤 Upload PDFs via API
* ☁️ Cloud deployment
* 📲 WhatsApp interactive buttons

---

## 🧪 Tech Stack

* FastAPI
* LangChain
* OpenAI API
* FAISS (Vector DB)
* PyPDF2
* Python

---

## 💼 Why This Project Matters

This project demonstrates:

- End-to-end AI system design
- Real-world API integration (WhatsApp)
- Deployment & debugging in production
- Building scalable backend architecture


## 👨‍💻 Author

Developed by **Suchit Kesarwani**

---

## 📜 License

This project is for educational and development purposes.
