import numpy as np
import time
from .core import UltraFastEngine

class EliteCompressionAPI:
    def __init__(self):
        self._history = []
        self._stats = {"compressions": 0, "decompressions": 0}
    
    def compress(self, data: np.ndarray, bits: int = 8) -> np.ndarray:
        self._stats["compressions"] += 1
        result, _, _ = UltraFastEngine.compress(data, bits)
        return result
    
    def decompress(self, data: np.ndarray, bits: int = 8) -> np.ndarray:
        self._stats["decompressions"] += 1
        return UltraFastEngine.decompress(data, bits)
    
    def get_stats(self) -> dict:
        return self._stats
