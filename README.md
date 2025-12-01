# 🏥 Medical-RAG  

A Retrieval-Augmented Generation (RAG) based application designed for **medical use-cases** such as medical document lookup, clinical Q&A, policy assistance, and knowledge retrieval.  
This system combines **semantic search (FAISS vectorstore)** with a local **LLM (Ollama + Llama3.2)** to generate accurate and context-aware responses — all fully offline and free.

---

## 🚀 Features  
**💯 Fully open-source — zero cost**

- 🔍 **Semantic Search** powered by FAISS  
- 📄 **Document Retrieval** from medical PDFs, research papers, and knowledge bases  
- 🤖 **LLM-powered Answers** using Llama3.2 (via Ollama)  
- 🧠 **Chat History Awareness** for multi-turn reasoning  
- 🧩 **Modular Architecture** (`rag.py`, `vectorstore_data.py`, `main.py`)  
- ⚡ **Easily Extendable** to additional medical datasets or domains  

---
Ensure you have Ollama installed and the model downloaded:
    ```bash
    ollama pull llama3.2
    ```

## 🛠️ Steps to Reproduce

1. **Clone this repository**
   ```bash
   git clone https://github.com/Umesh94kr/Medical-use-RAG.git
   cd Medical-use-RAG
   ```

2. Create a .env file, and add your huggingface token to that
    - HF_TOKEN="your_hf_token"

3. **Create a virtual environment**
    ```bash
    python3 -m venv myenv
    ```

4. **Activate the environment**
    ```bash
    source myenv/bin/activate 
    ```

5. **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```

6. **Run RAG application**
    ```bash
    python3 Medical-RAG/main.py
    ```


## **Integrated FastAPI**
In your terminal go to project directory 

    uvicorn app:app

Server starts running, you can copy local server URL, and test it on POSTMAN

<img src="images/server-running.png" width="400">