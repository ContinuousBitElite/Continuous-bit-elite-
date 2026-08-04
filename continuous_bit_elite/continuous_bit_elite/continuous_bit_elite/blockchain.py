import hashlib
from typing import List, Tuple

class MerkleTree:
    def __init__(self, data: List[bytes]):
        self.data = data
        self.tree = self._build_tree(data)
        self.root = self.tree[-1][0] if self.tree and self.tree[-1] else None
    
    def _build_tree(self, data: List[bytes]) -> List[List[bytes]]:
        if not data:
            return []
        leaves = [hashlib.sha256(d).digest() for d in data]
        tree = [leaves]
        current_level = leaves
        while len(current_level) > 1:
            next_level = []
            for i in range(0, len(current_level), 2):
                if i + 1 < len(current_level):
                    combined = current_level[i] + current_level[i + 1]
                else:
                    combined = current_level[i] + current_level[i]
                next_level.append(hashlib.sha256(combined).digest())
            tree.append(next_level)
            current_level = next_level
        return tree
    
    def get_proof(self, index: int) -> List[bytes]:
        if not self.tree or index >= len(self.tree[0]):
            return []
        proof = []
        current_index = index
        for level in range(len(self.tree) - 1):
            sibling_index = current_index ^ 1
            if sibling_index < len(self.tree[level]):
                proof.append(self.tree[level][sibling_index])
            current_index //= 2
        return proof
    
    def verify_proof(self, data: bytes, proof: List[bytes], index: int) -> bool:
        current_hash = hashlib.sha256(data).digest()
        current_index = index
        for sibling_hash in proof:
            if current_index % 2 == 0:
                combined = current_hash + sibling_hash
            else:
                combined = sibling_hash + current_hash
            current_hash = hashlib.sha256(combined).digest()
            current_index //= 2
        return current_hash == self.root

class ZeroKnowledgeProof:
    def __init__(self):
        self._secret = None
        self._commitment = None
    
    def commit(self, secret: bytes) -> bytes:
        self._secret = secret
        self._commitment = hashlib.sha256(secret + b"zkp_salt").digest()
        return self._commitment
    
    def prove(self, data: bytes) -> Tuple[bytes, bytes]:
        if self._secret is None:
            raise ValueError("No secret committed")
        proof = hashlib.sha256(data + self._secret).digest()
        return proof, self._commitment
    
    def verify(self, data: bytes, proof: bytes, commitment: bytes) -> bool:
        expected_proof = hashlib.sha256(data + self._secret).digest()
        expected_commitment = hashlib.sha256(self._secret + b"zkp_salt").digest()
        return proof == expected_proof and commitment == expected_commitment
