# test_tokengateway.py
"""
Tests for TokenGateway module.
"""

import unittest
from tokengateway import TokenGateway

class TestTokenGateway(unittest.TestCase):
    """Test cases for TokenGateway class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = TokenGateway()
        self.assertIsInstance(instance, TokenGateway)
        
    def test_run_method(self):
        """Test the run method."""
        instance = TokenGateway()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
