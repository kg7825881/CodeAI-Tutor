# AI Tutor for Python Competence Analysis

This project is a prototype AI tutor that uses open-source models to analyze student-written Python code and provide Socratic feedback to encourage deeper learning.

## Core Features
- Interactive web interface built with Streamlit.
- Powered by the `Code Llama` large language model running locally via Ollama.
- Provides guided hints instead of direct solutions.
- Includes a sample dataset (`dataset.jsonl`) for potential fine-tuning.

---

## Research Plan

Our research will identify and evaluate open-source language models for their capacity to analyze student competence in Python programming...

---

## Reasoning

#### 1. What makes a model suitable for high-level competence analysis?
A model suitable for competence analysis must go far beyond simple syntax checking. Its key attributes are...

#### 2. How would you test whether a model generates meaningful prompts?
Testing for "meaningful" prompts is a qualitative challenge that cannot be fully captured by automated metrics...

#### 3. What trade-offs might exist between accuracy, interpretability, and cost?
Significant trade-offs exist between these three factors...

#### 4. Why did you choose the model you evaluated (Code Llama)?
Code Llama was chosen as the primary candidate for this task due to a strategic combination of factors...

---

## Setup and Installation

Follow these steps to run the application locally.

**Prerequisites:**
- Python 3.9+
- [Ollama](https://ollama.com) installed and running.

**Instructions:**
1.  **Clone the repository:**
    ```bash
    git clone https://github.com/kg7825881/CodeAI-Tutor.git
    cd CodeAI-Tutor
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    # For macOS/Linux
    python3 -m venv venv
    source venv/bin/activate

    # For Windows
    python -m venv venv
    .\venv\Scripts\activate
    ```

3.  **Download the Code Llama model via Ollama:**
    ```bash
    ollama pull codellama:7b
    ```

4.  **Run the Streamlit application:**
    ```bash
    streamlit run app.py
    ```
