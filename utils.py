import numpy as np
import time

def benchmark_compression(data: np.ndarray, bits: int = 8, iterations: int = 10) -> dict:
    
    from .core import UltraFastEngine
    
    times = []
    for _ in range(iterations):
        start = time.time()
        compressed, _, _ = UltraFastEngine.compress(data, bits)
        times.append(time.time() - start)
    
    avg_time = np.mean(times) * 1000  # milliseconds
    
    return {
        "avg_time_ms": avg_time,
        "min_time_ms": np.min(times) * 1000,
        "max_time_ms": np.max(times) * 1000,
        "iterations": iterations
    }

def print_compression_stats(original: np.ndarray, compressed: np.ndarray):
    
    ratio = original.nbytes / compressed.nbytes
    saving = (1 - 1/ratio) * 100
    
    print(f"Original: {original.nbytes / 1024:.2f} KB")
    print(f"Compressed: {compressed.nbytes / 1024:.2f} KB")
    print(f"Ratio: {ratio:.2f}x")
    print(f"Saving: {saving:.1f}%")
