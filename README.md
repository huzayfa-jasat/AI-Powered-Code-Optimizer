# AI-Powered-Code-Optimizer
**Optimization Process**
The AI optimizer follows a structured approach:
1. User Inputs Code – Users paste their Python script into a Streamlit web app.
2. Performance Measurement (Before Optimization) – The performance.py module measures execution time and memory usage.
3. AI Optimization – The script is sent to Google’s Gemini AI for enhancement. The AI refactors the code to improve efficiency while preserving functionality.
4. Performance Measurement (After Optimization) – The improved code is evaluated again.
5. Visualization – Performance differences are displayed using Matplotlib graphs and Streamlit metrics.
<br/>

**Assumptions and Constraints**

The AI optimization strictly avoids unnecessary complexity (e.g., no replacing simple loops with recursion).
The model does not refactor algorithm logic beyond improving execution/memory performance.
The tool works best with general Python scripts, but optimizations may vary depending on input complexity.
<br/>
<br/>

**How It Works**


1. Web Interface (Streamlit App) <br/>

📁File: app.py

The Streamlit-based web app provides an interactive way for users to paste their Python scripts and receive optimized versions. It also visualizes improvements in execution time and memory usage.

Features: <br/>
✅ Code input area for user scripts<br/>
✅ AI-powered optimization using Google Gemini <br/>
✅ Pre- and post-optimization performance comparison <br/>
✅ Performance visualization using Matplotlib

![image](https://github.com/user-attachments/assets/379965f8-442d-4afe-9083-93b6d8a85a29)

2. AI-Powered Code Optimization <br/>

📁File: optimizer.py
<br/>

The optimize_code function sends the user’s script to Google Gemini AI, which generates a more efficient version.

Key Optimization Factors:

✅Loop unrolling and efficiency – Reduces redundant operations. <br/>
✅Memory management – Improves variable storage and access. <br/>
✅Function optimizations – Reduces unnecessary function calls. <br/>
✅Example Optimized Output: (Consider adding a before/after code snippet screenshot.) <br/>

3. Performance Measurement <br/>

📁File: performance.py

Before and after optimization, the tool measures:

Execution Time (in seconds)<br/>
Memory Usage (in MB)<br/>
📊 Graph Showing Performance Comparison (Consider adding a sample Matplotlib graph here.)<br/>

**Results & Accuracy** <br/>

To evaluate the optimizer, a sample script was tested:<br/>

Example Test:  <br/>
```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

arr = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(arr)
```

Optimized Code: <br/>
```python
def optimized_bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        last_swap = 0  # Track the last swap position

        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
                last_swap = j  # Update last swap position

        if not swapped:  # If no swaps, the array is sorted
            break

        n = last_swap + 1  # Reduce comparisons based on last swap

    return arr

arr = [64, 34, 25, 12, 22, 11, 90]
optimized_bubble_sort(arr)
```

Original Execution Time: 0.00177 sec <br/>
Optimized Execution Time: 0.00031 sec <br/>
Original Memory Usage: 0.1172 MB <br/>
Optimized Memory Usage: 0 MB <br/>
🚀 Performance Improved by 82.5%!<br/>
![Screenshot 2025-02-06 220037](https://github.com/user-attachments/assets/743c9255-537f-4040-9b3f-4f630131f5b1)


**Potential Improvements** <br/>
✅ More Advanced AI Models – Integrate models fine-tuned for code optimization, such as OpenAI Codex or specialized ML models. <br/>
✅ Support for More Languages – Extend support to C++, Java, or JavaScript. <br/>
✅ User-Defined Constraints – Allow users to specify optimization preferences (e.g., prioritize speed over memory). <br/>
✅ IDE Plugin – Develop VS Code/PyCharm plugins for real-time AI-powered code suggestions. <br/>

**References** <br/>
Google AI (Gemini API) - https://ai.google.dev/<br/>
Streamlit Docs - https://docs.streamlit.io/<br/>
Python Performance Optimization - https://realpython.com/python-performance/<br/>
