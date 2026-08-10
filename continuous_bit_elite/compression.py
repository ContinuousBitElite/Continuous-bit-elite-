import numpy as np
import time
from .core import UltraFastEngine

class EliteCompressionAPI:
    def __init__(self):
        self._history = []
        self._stats = {"compressions": 0, "decompressions": 0}
        self._last_min_val = None
        self._last_max_val = None
    
    def compress(self, data: np.ndarray, bits: int = 8) -> np.ndarray:
        self._stats["compressions"] += 1
        result, min_val, max_val = UltraFastEngine.compress(data, bits)
        # Store metadata for decompression
        self._last_min_val = min_val
        self._last_max_val = max_val
        return result
    
    def decompress(self, data: np.ndarray, bits: int = 8) -> np.ndarray:
        self._stats["decompressions"] += 1
        return UltraFastEngine.decompress(data, self._last_min_val, self._last_max_val, bits)
    
    def get_stats(self) -> dict:
        return self._stats
