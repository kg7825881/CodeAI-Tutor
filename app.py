import streamlit as st
import ollama

# --- Page Configuration ---
st.set_page_config(
    page_title="CodeAI Tutor",
    page_icon="🧑‍🏫",
    layout="wide"
)

# --- Sidebar ---
with st.sidebar:
    st.title("🧑‍🏫 CodeAI Tutor")
    st.info("This app uses an AI tutor to help you understand your Python code. Paste your code, get a hint, and learn by discovering the solution yourself!")
    st.markdown("---")
    st.header("About")
    st.write("This tool is a research prototype designed to explore how AI can assist in programming education.")

# --- System Prompt ---
SYSTEM_PROMPT = """
You are an expert Python programming tutor. Your primary goal is to help students learn by guiding them to a solution, not by giving it to them directly. Follow these rules strictly:
1.  Analyze the student's code for any syntax errors, logical flaws, or conceptual misunderstandings.
2.  Identify the single most important issue.
3.  Do NOT provide the corrected code or the direct answer.
4.  Instead, ask a single, concise Socratic question that makes the student think about the specific issue and helps them discover the solution on their own.
5.  Your tone should be encouraging and helpful.
"""

# --- App Layout ---
st.title("CodeAI Python Tutor")
st.markdown("Get a hint for your Python code without getting the direct answer!")

# --- Example Code ---
example_code = """
numbers = [1, 2, 2, 3, 4, 5, 6, 8]

# Goal: Remove all even numbers from the list
for number in numbers:
  if number % 2 == 0:
    numbers.remove(number)

print(numbers)
"""

# --- Input and Output Containers ---
input_container = st.container(border=True)
output_container = st.container(border=True)

# Initialize session state for the code input if it doesn't exist
if 'code_input' not in st.session_state:
    st.session_state.code_input = ""

with input_container:
    col1, col2 = st.columns([0.7, 0.3])
    
    with col2:
        if st.button("Load Example Code", use_container_width=True):
            st.session_state.code_input = example_code
        
        
        submit_button = st.button("Get Feedback", type="primary", use_container_width=True)

    with col1:
        student_code = st.text_area(
            "Enter your Python code here:", 
            height=250, 
            key="code_input" 
        )


if submit_button:
    if student_code.strip():
        with output_container:
            with st.spinner("🧑‍🏫 The tutor is thinking..."):
                try:
                    response = ollama.chat(
                        model='codellama:7b',
                        messages=[
                            {'role': 'system', 'content': SYSTEM_PROMPT},
                            {'role': 'user', 'content': f"Can you review my Python code, please?\n\n```python\n{student_code}\n```"},
                        ],
                    )
                    with st.chat_message("ai", avatar="🧑‍🏫"):
                        st.markdown(response['message']['content'])
                except Exception as e:
                    st.error(f"An error occurred: {e}")
    else:
        with output_container:
            st.warning("Please enter some code to get feedback.")