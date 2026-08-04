import numpy as np
import unittest
from continuous_bit_elite import EliteCompressionAPI

class TestCompression(unittest.TestCase):
    def test_compress_decompress(self):
        api = EliteCompressionAPI()
        data = np.random.rand(100, 100).astype(np.float32)
        compressed = api.compress(data)
        decompressed = api.decompress(compressed)
        self.assertEqual(data.shape, decompressed.shape)
    
    def test_compression_ratio(self):
        api = EliteCompressionAPI()
        data = np.random.rand(500, 500).astype(np.float32)
        compressed = api.compress(data)
        ratio = data.nbytes / compressed.nbytes
        self.assertGreaterEqual(ratio, 3.5)

if __name__ == "__main__":
    unittest.main()
