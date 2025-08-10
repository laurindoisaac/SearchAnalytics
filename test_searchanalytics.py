# test_searchanalytics.py
"""
Tests for SearchAnalytics module.
"""

import unittest
from searchanalytics import SearchAnalytics

class TestSearchAnalytics(unittest.TestCase):
    """Test cases for SearchAnalytics class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = SearchAnalytics()
        self.assertIsInstance(instance, SearchAnalytics)
        
    def test_run_method(self):
        """Test the run method."""
        instance = SearchAnalytics()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
