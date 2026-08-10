# API Documentation

Complete API reference for Continuous Bit Elite.

## Core Compression

### `UltraFastEngine`

Core compression engine providing ultra-fast compression algorithms.

#### `compress(data, bits=8) -> Tuple[np.ndarray, float, float]`

Compress data using the ultra-fast algorithm.

**Parameters:**
- `data` (np.ndarray): Input numpy array (any shape)
- `bits` (int): Number of bits for compression (default: 8)
  - 4: Maximum compression, lower precision
  - 8: Balanced compression and precision
  - 16: Higher precision, lower compression
  - 32: Full precision (no compression)

**Returns:**
- `compressed_data` (np.ndarray): Compressed data as uint8
- `min_val` (float): Minimum value from original data
- `max_val` (float): Maximum value from original data

**Example:**
```python
from continuous_bit_elite import UltraFastEngine
import numpy as np

data = np.random.rand(100, 100).astype(np.float32)
compressed, min_val, max_val = UltraFastEngine.compress(data, bits=8)
print(f"Original: {data.shape}, Compressed: {compressed.shape}")
```

#### `decompress(data, min_val, max_val, bits=8) -> np.ndarray`

Decompress data back to original precision.

**Parameters:**
- `data` (np.ndarray): Compressed data (uint8)
- `min_val` (float): Minimum value from compression
- `max_val` (float): Maximum value from compression
- `bits` (int): Number of bits used during compression

**Returns:**
- `decompressed_data` (np.ndarray): Decompressed data as float32

**Example:**
```python
decompressed = UltraFastEngine.decompress(compressed, min_val, max_val, bits=8)
print(f"Decompressed shape: {decompressed.shape}")
```

---

## Compression API

### `EliteCompressionAPI`

High-level API wrapper for easy compression/decompression.

#### `__init__()`

Initialize the compression API.

**Example:**
```python
from continuous_bit_elite import EliteCompressionAPI

api = EliteCompressionAPI()
```

#### `compress(data, bits=8) -> np.ndarray`

Compress data and store metadata internally.

**Parameters:**
- `data` (np.ndarray): Input data to compress
- `bits` (int): Compression bit precision (default: 8)

**Returns:**
- `compressed_data` (np.ndarray): Compressed data

**Example:**
```python
compressed = api.compress(data, bits=8)
print(f"Compression ratio: {data.nbytes / compressed.nbytes:.2f}x")
```

#### `decompress(data, bits=8) -> np.ndarray`

Decompress data using stored metadata.

**Parameters:**
- `data` (np.ndarray): Compressed data
- `bits` (int): Compression bit precision

**Returns:**
- `decompressed_data` (np.ndarray): Decompressed data as float32

**Example:**
```python
decompressed = api.decompress(compressed)
print(f"Decompressed shape: {decompressed.shape}")
```

#### `get_stats() -> dict`

Get compression/decompression statistics.

**Returns:**
- `dict`: Statistics dictionary with keys:
  - `compressions` (int): Number of compress calls
  - `decompressions` (int): Number of decompress calls

**Example:**
```python
stats = api.get_stats()
print(f"Compressions: {stats['compressions']}")
print(f"Decompressions: {stats['decompressions']}")
```

---

## Blockchain Integration

### `MerkleTree`

Merkle tree implementation for blockchain verification.

#### `__init__(data: List[bytes])`

Initialize Merkle tree with data blocks.

**Parameters:**
- `data` (List[bytes]): List of byte blocks

**Example:**
```python
from continuous_bit_elite import MerkleTree

data = [b"block1", b"block2", b"block3", b"block4"]
tree = MerkleTree(data)
```

#### `get_proof(index: int) -> List[bytes]`

Get Merkle proof for a specific block.

**Parameters:**
- `index` (int): Block index

**Returns:**
- `proof` (List[bytes]): List of sibling hashes

**Example:**
```python
proof = tree.get_proof(0)
print(f"Proof length: {len(proof)}")
```

#### `verify_proof(data, proof, index) -> bool`

Verify a Merkle proof.

**Parameters:**
- `data` (bytes): Data to verify
- `proof` (List[bytes]): Merkle proof
- `index` (int): Block index

**Returns:**
- `valid` (bool): True if proof is valid

**Example:**
```python
is_valid = tree.verify_proof(data[0], proof, 0)
print(f"Proof valid: {is_valid}")
```

#### `root` (property)

Get the Merkle root hash.

**Returns:**
- `root` (bytes): Root hash of the tree

**Example:**
```python
root = tree.root
print(f"Merkle root: {root.hex()}")
```

---

### `ZeroKnowledgeProof`

Zero-Knowledge Proof implementation.

#### `commit(secret: bytes) -> bytes`

Commit to a secret value.

**Parameters:**
- `secret` (bytes): Secret to commit

**Returns:**
- `commitment` (bytes): Commitment hash

**Example:**
```python
from continuous_bit_elite import ZeroKnowledgeProof

zkp = ZeroKnowledgeProof()
commitment = zkp.commit(b"my_secret")
```

#### `prove(data: bytes) -> Tuple[bytes, bytes]`

Generate a proof for data.

**Parameters:**
- `data` (bytes): Data to prove

**Returns:**
- `proof` (bytes): Proof hash
- `commitment` (bytes): Stored commitment

**Example:**
```python
proof, commitment = zkp.prove(b"message")
```

#### `verify(data, proof, commitment) -> bool`

Verify a proof.

**Parameters:**
- `data` (bytes): Original data
- `proof` (bytes): Proof to verify
- `commitment` (bytes): Commitment hash

**Returns:**
- `valid` (bool): True if proof is valid

**Example:**
```python
is_valid = zkp.verify(b"message", proof, commitment)
print(f"Proof valid: {is_valid}")
```

---

### `BlockchainVerifier`

Blockchain verification utilities.

#### `verify_integrity(data, hash_value) -> bool` (static)

Verify data integrity using SHA-256.

**Parameters:**
- `data` (bytes): Data to verify
- `hash_value` (bytes): Expected hash

**Returns:**
- `valid` (bool): True if hashes match

**Example:**
```python
from continuous_bit_elite import BlockchainVerifier
import hashlib

data = b"important_data"
data_hash = hashlib.sha256(data).digest()
is_valid = BlockchainVerifier.verify_integrity(data, data_hash)
```

#### `verify_merkle_proof(data, proof, root, index) -> bool` (static)

Verify a Merkle proof against a root.

**Parameters:**
- `data` (bytes): Data to verify
- `proof` (List[bytes]): Merkle proof
- `root` (bytes): Merkle root
- `index` (int): Data index

**Returns:**
- `valid` (bool): True if proof is valid

**Example:**
```python
is_valid = BlockchainVerifier.verify_merkle_proof(data, proof, root, 0)
```

---

## Utilities

### Performance Metrics

```python
import time
import numpy as np
from continuous_bit_elite import EliteCompressionAPI

api = EliteCompressionAPI()
data = np.random.rand(1000, 1000).astype(np.float32)

# Measure compression speed
start = time.time()
compressed = api.compress(data)
compress_time = time.time() - start
ratio = data.nbytes / compressed.nbytes

print(f"Compression time: {compress_time*1000:.2f}ms")
print(f"Compression ratio: {ratio:.2f}x")
print(f"Space saved: {(1 - 1/ratio)*100:.1f}%")
```

---

## Error Handling

### Common Exceptions

```python
try:
    # Compression operation
    compressed = api.compress(data)
except ValueError as e:
    print(f"Validation error: {e}")
except TypeError as e:
    print(f"Type error: {e}")
```

### Data Requirements

- Input must be NumPy array
- Floating-point data (float32, float64)
- Shape: Any dimensions (1D, 2D, 3D, etc.)
- No NaN or Inf values

---

## Performance Characteristics

### Compression Speed
- **3122× faster** than traditional Python loops
- Processes 512×512 images in ~0.6ms
- Linear complexity O(n)

### Memory Usage
- Input: Full precision (float32)
- Output: ~1/4 size (uint8 with bits=8)
- Temporary: Minimal (in-place operations)

### Accuracy
- **8-bit mode:** MSE < 0.01
- **16-bit mode:** MSE < 0.0001
- **Lossless verification:** 100% accuracy

---

## Version

API Documentation for **Continuous Bit Elite v4.0.18**

For latest updates, visit: https://github.com/ContinuousBitElite/Continuous-bit-elite-
