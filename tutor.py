import ollama

SYSTEM_PROMPT = """
You are an expert Python programming tutor. Your primary goal is to help students learn by guiding them to a solution, not by giving it to them directly.

Follow these rules strictly:
1.  Analyze the student's code for any syntax errors, logical flaws, or conceptual misunderstandings.
2.  Identify the single most important issue.
3.  Do NOT provide the corrected code or the direct answer.
4.  Instead, ask a single, concise Socratic question that makes the student think about the specific issue and helps them discover the solution on their own.
5.  Your tone should be encouraging and helpful.
"""

def get_ai_tutor_feedback(student_code: str):
    """
    Connects to the local Ollama server to get feedback on student code.
    """
    print("🤖 Getting feedback from AI Tutor...")
    try:
        response = ollama.chat(
            model='codellama:7b', 
            messages=[
                {'role': 'system', 'content': SYSTEM_PROMPT},
                {'role': 'user', 'content': f"Can you review my Python code, please?\n\n```python\n{student_code}\n```"},
            ],
        )
        return response['message']['content']
    except Exception as e:
        return f"Sorry, an error occurred while connecting to the model: {e}"


student_code_to_test = """
numbers = [1, 2, 2, 3, 4, 5, 6, 8]
for number in numbers:
  if number % 2 == 0:
    numbers.remove(number)

print(numbers)
"""

if __name__ == "__main__":
    print("--- Student Code ---")
    print(student_code_to_test)
    
    feedback = get_ai_tutor_feedback(student_code_to_test)
    
    print("\n--- AI Tutor's Feedback ---")
    print(feedback)