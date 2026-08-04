import numpy as np
import hashlib
import time
from typing import Tuple, Optional

class UltraFastEngine:
    """محرك الضغط فائق السرعة"""
    
    @staticmethod
    def compress(data: np.ndarray, bits: int = 8) -> Tuple[np.ndarray, float, float]:
        if data.ndim == 1:
            data = data.reshape(1, -1)
        data_float = data.astype(np.float32)
        min_val = data_float.min()
        max_val = data_float.max()
        normalized = (data_float - min_val) / (max_val - min_val + 1e-8)
        result = (normalized * (2**bits - 1)).astype(np.uint8)
        return result, min_val, max_val
    
    @staticmethod
    def decompress(data: np.ndarray, min_val: float, max_val: float, bits: int = 8) -> np.ndarray:
        if data.ndim == 1:
            data = data.reshape(1, -1)
        normalized = data.astype(np.float32) / (2**bits - 1)
        result = normalized * (max_val - min_val) + min_val
        return result
