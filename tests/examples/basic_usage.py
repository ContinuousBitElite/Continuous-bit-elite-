from continuous_bit_elite import EliteCompressionAPI
import numpy as np

print("="*50)
print("🧠 Continuous Bit Elite - Basic Usage")
print("="*50)

# 
api = EliteCompressionAPI()

# 
data = np.random.rand(1000, 1000).astype(np.float32)
print(f"Original size: {data.nbytes / 1024:.2f} KB")

# 
compressed = api.compress(data)
print(f"Compressed size: {compressed.nbytes / 1024:.2f} KB")

# 
ratio = data.nbytes / compressed.nbytes
print(f"Ratio: {ratio:.2f}x")
print(f"Saving: {(1 - 1/ratio) * 100:.1f}%")
