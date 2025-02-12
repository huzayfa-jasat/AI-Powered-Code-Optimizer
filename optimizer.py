import google.generativeai as genai
import os
import re



def optimize_code(code, language="Python"):
    """
    Optimizes the given code using AI and returns:
    - Optimized code
    - Time & space complexity (before & after)
    """
    api_key = os.getenv("API_KEY")  # Fetch API key from environment variable

    if not api_key:
        return "Error: API key not found. Set the environment variable 'API_KEY'."

    genai.configure(api_key=api_key)
    prompt = f"""
    Optimize the following {language} code for better performance and efficiency.
    - DO NOT add unnecessary operations.
    - DO NOT replace simple loops with complex recursion.
    - Focus on reducing execution time AND memory usage.
    - Both memory usage and execution time are equally important.
    - Both should be improved as much as possible.
    - Optimize loops, function calls, and memory allocations.
    - Just output the optimized code. No need to explain the changes.
    Code:
    {code}
    """

    try:
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(prompt)

        optimized_code = response.text.strip()
        if not isinstance(optimized_code, str):
            raise ValueError("The response is not a valid string.")

        return optimized_code  

    except Exception as e:
        return f"Error: {str(e)}"
