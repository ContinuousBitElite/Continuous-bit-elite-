# Continuous Bit Elite - Getting Started

Welcome to **Continuous Bit Elite**! This guide will help you get started with the ultra-fast compression library with blockchain integration.

## Installation

### From PyPI (Recommended)

```bash
pip install continuous-bit-elite
```

### From GitHub

```bash
git clone https://github.com/ContinuousBitElite/Continuous-bit-elite-.git
cd Continuous-bit-elite-
pip install -e .
```

## Quick Start

### Basic Compression & Decompression

```python
import numpy as np
from continuous_bit_elite import EliteCompressionAPI

# Create API instance
api = EliteCompressionAPI()

# Create sample data
data = np.random.rand(100, 100).astype(np.float32)

# Compress
compressed = api.compress(data)
print(f"Original size: {data.nbytes} bytes")
print(f"Compressed size: {compressed.nbytes} bytes")
print(f"Ratio: {data.nbytes / compressed.nbytes:.2f}x")

# Decompress
decompressed = api.decompress(compressed)
print(f"Decompressed shape: {decompressed.shape}")
```

### Using the Core Engine

```python
from continuous_bit_elite import UltraFastEngine
import numpy as np

# Create data
data = np.random.rand(1000, 1000).astype(np.float32)

# Compress with 8-bit precision
compressed, min_val, max_val = UltraFastEngine.compress(data, bits=8)

# Decompress
decompressed = UltraFastEngine.decompress(compressed, min_val, max_val, bits=8)
```

## Blockchain Features

### Merkle Trees

```python
from continuous_bit_elite import MerkleTree

# Create Merkle tree from data blocks
data_blocks = [b"block1", b"block2", b"block3", b"block4"]
tree = MerkleTree(data_blocks)

print(f"Merkle root: {tree.root.hex()}")

# Verify proof for a block
proof = tree.get_proof(0)
is_valid = tree.verify_proof(data_blocks[0], proof, 0)
print(f"Proof valid: {is_valid}")
```

### Zero-Knowledge Proofs

```python
from continuous_bit_elite import ZeroKnowledgeProof

# Create ZKP instance
zkp = ZeroKnowledgeProof()

# Commit to a secret
secret = b"my_secret_password"
commitment = zkp.commit(secret)

# Generate and verify proof
data = b"message_to_prove"
proof, commit = zkp.prove(data)
is_valid = zkp.verify(data, proof, commit)
print(f"ZKP valid: {is_valid}")
```

### Blockchain Verifier

```python
from continuous_bit_elite import BlockchainVerifier
import hashlib

# Create verifier
verifier = BlockchainVerifier()

# Create and verify data with hash
data = b"important_data"
data_hash = hashlib.sha256(data).digest()

# Verify integrity
is_intact = verifier.verify_integrity(data, data_hash)
print(f"Data integrity verified: {is_intact}")
```

## Performance

### Compression Speed

- **3122× faster** than traditional loops
- Processes large datasets in milliseconds
- Efficient NumPy-based implementation

### Compression Ratio

- **4× compression ratio** (75% space saving)
- Works best with:
  - Floating-point data
  - Machine learning models
  - Scientific data
  - Image data

## Configuration

### Compression Bits

Control precision vs compression trade-off:

```python
api = EliteCompressionAPI()

# Default: 8-bit precision
compressed_8bit = api.compress(data, bits=8)

# Higher precision: 16-bit
compressed_16bit = api.compress(data, bits=16)

# Lower precision, higher compression: 4-bit
compressed_4bit = api.compress(data, bits=4)
```

## Statistics

Track compression statistics:

```python
api = EliteCompressionAPI()

# Perform operations
compressed = api.compress(data)
decompressed = api.decompress(compressed)

# Get statistics
stats = api.get_stats()
print(f"Compression count: {stats['compressions']}")
print(f"Decompression count: {stats['decompressions']}")
```

## Testing

Run the test suite:

```bash
# Run all tests
pytest tests/

# Run with coverage
pytest tests/ --cov=continuous_bit_elite --cov-report=html

# Run specific tests
pytest tests/test_compression.py
pytest tests/test_blockchain.py
```

## Examples

Check out the `tests/examples/` directory for complete working examples:

- `basic_usage.py` - Basic compression examples
- `blockchain_demo.py` - Blockchain feature demonstrations

## Performance Tips

1. **Use 8-bit or 16-bit precision** for best balance
2. **Batch compress** large datasets for better performance
3. **Use NumPy arrays** for input data
4. **Pre-allocate arrays** when possible

## Troubleshooting

### Common Issues

**Q: Compression doesn't work as expected?**
- Ensure input is NumPy array with float32 dtype
- Check that data range is appropriate
- Verify min and max values are correctly stored

**Q: Decompression fails?**
- Make sure you use the same `min_val` and `max_val` from compression
- Verify `bits` parameter matches compression settings
- Check data hasn't been corrupted

## Next Steps

- Read the [API Documentation](./API.md)
- Check [Contributing Guidelines](../CONTRIBUTING.md)
- Review [Changelog](../CHANGELOG.md)
- Report issues on [GitHub](https://github.com/ContinuousBitElite/Continuous-bit-elite-/issues)

## Support

For questions or issues:
- Open an issue on GitHub
- Email: continuous.bit.elite@gmail.com
- Check existing documentation and examples

## License

This project is licensed under the MIT License - see [LICENSE](../LICENSE) file for details.
