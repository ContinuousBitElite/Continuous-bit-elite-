from continuous_bit_elite import MerkleTree, ZeroKnowledgeProof
import hashlib

print("="*50)
print("🔗 Continuous Bit Elite - Blockchain Demo")
print("="*50)

# Merkle Tree
data = [b"block1", b"block2", b"block3", b"block4"]
tree = MerkleTree(data)
print(f"Merkle Root: {tree.root.hex()[:32]}...")

# ZK-Proof
zkp = ZeroKnowledgeProof()
secret = b"secret"
zkp.commit(secret)
proof, commit = zkp.prove(b"data")
print(f"ZK-Proof Verified: {zkp.verify(b'data', proof, commit)}")
