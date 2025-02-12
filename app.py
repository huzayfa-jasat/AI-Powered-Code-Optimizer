import streamlit as st
import matplotlib.pyplot as plt
from performance import measure_performance  # Ensure this module is available
from optimizer import optimize_code  # Ensure this module is available

st.title("🚀 AI Code Optimizer")

# Define the input text area
code_input = st.text_area("Paste your Python code here:", height=200, key="unique_key_1")

if st.button("Optimize Code"):
        if code_input.strip():
            st.write("⏳ Optimizing your code with AI...")
            
            # Measure performance BEFORE optimization
            original_time, original_memory = measure_performance(code_input)

            optimized_code = optimize_code(code_input)  


            # Measure performance AFTER optimization
            optimized_time, optimized_memory = measure_performance(optimized_code)

            # Display optimized code
            st.subheader("Optimized Code:")
            st.code(optimized_code, language="python")  

            # Show performance improvement
            st.subheader("Performance Comparison:")
            col1, col2 = st.columns(2)

            col1.metric("Execution Time (Before)", f"{original_time} sec")
            col2.metric("Execution Time (After)", f"{optimized_time} sec")

            col1.metric("Memory Usage (Before)", f"{original_memory} MB")
            col2.metric("Memory Usage (After)", f"{optimized_memory} MB")

            improvement = round((original_time - optimized_time) / original_time * 100, 2)
            st.success(f"🚀 Performance Improved by **{improvement}%**!")


            fig, ax = plt.subplots(figsize=(10, 6))  
            metrics = ['Execution Time (Before)', 'Execution Time (After)', 'Memory Usage (Before)', 'Memory Usage (After)']
            values = [original_time, optimized_time, original_memory, optimized_memory]

            ax.bar(metrics, values, color=['red', 'green', 'red', 'green'])

            ax.set_ylabel('Value')
            ax.set_title('Performance Comparison Before and After Optimization')
            plt.xticks(rotation=45, ha='right')  

            st.pyplot(fig) 
        else:
            st.warning("Please enter some code to optimize.")
