"""
Continuous Bit Elite - Ultra-fast compression with blockchain integration
"""

# استيراد مباشر من الملفات الموجودة
from .core import UltraFastEngine
from .blockchain import MerkleTree, ZeroKnowledgeProof, BlockchainVerifier
from .compression import EliteCompressionAPI

__version__ = "4.0.4"
__all__ = [
    "UltraFastEngine",
    "MerkleTree",
    "ZeroKnowledgeProof",
    "BlockchainVerifier",
    "EliteCompressionAPI"
]
