import time
import memory_profiler
import psutil

def measure_performance(code):
    """
    Runs the given Python code and measures:
    - Execution time (in seconds)
    - Memory usage (in MB)
    """
    mem_before = memory_profiler.memory_usage()[0]
    
    start_time = time.time()
    try:
        exec(compile(code, '<string>', 'exec'))
    
    except Exception as e:
        print(f"An error occurred: {e}")
    end_time = time.time()
    
    mem_after = memory_profiler.memory_usage()[0]
    
    execution_time = round(end_time - start_time, 5)
    memory_used = round(mem_after - mem_before, 5)

    return execution_time, memory_used
