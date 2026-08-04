import unittest
from continuous_bit_elite import MerkleTree, ZeroKnowledgeProof

class TestBlockchain(unittest.TestCase):
    def test_merkle_tree(self):
        data = [b"block1", b"block2", b"block3", b"block4"]
        tree = MerkleTree(data)
        self.assertIsNotNone(tree.root)
    
    def test_zk_proof(self):
        zkp = ZeroKnowledgeProof()
        secret = b"test_secret"
        commitment = zkp.commit(secret)
        proof, commit = zkp.prove(b"test_data")
        self.assertTrue(zkp.verify(b"test_data", proof, commit))

if __name__ == "__main__":
    unittest.main()
