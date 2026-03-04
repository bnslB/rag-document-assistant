# Enterprise RAG Document Assistant

## 🚀 Project Overview
Organizations often struggle to query large unstructured documents efficiently.  
This project implements a **Retrieval-Augmented Generation (RAG) system** that allows accurate, context-aware Q&A over enterprise documents like PDFs, manuals, or internal reports.

---

## 🏗 Architecture Diagram
![Architecture Diagram](./docs/rag_architecture.png)

**Pipeline:**

1. **User Query** → Input from user  
2. **Embedding Model** → Converts text chunks into vectors  
3. **Vector Database (Chroma/FAISS)** → Retrieves top-k relevant documents  
4. **Prompt Augmentation** → Combines retrieved chunks with query  
5. **LLM (OpenAI / HuggingFace)** → Generates final response  
6. **Output** → Returns answer to user

---

## 💻 Tech Stack
- **Python 3.10+**
- **LangChain** – Orchestration framework for RAG  
- **Chroma** – Vector database for similarity search  
- **OpenAI / Hugging Face Transformers** – LLMs for text generation  
- **draw.io / Excalidraw** – Architecture diagrams  

---

## ⚙️ How to Run
1. Clone the repo:

```bash
git clone https://github.com/yourusername/rag-document-assistant.git
cd rag-document-assistant
