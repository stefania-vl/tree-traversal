import unittest
from tree import Tree

class TestTree(unittest.TestCase):
    def setUp(self):
        self.tree = Tree()

    def test_find(self):
        self.tree.add(5)
        self.assertEqual(self.tree.find(5).data, 5)
    
    def test_find_not_found(self):
        self.tree.add(5)
        self.assertEqual(self.tree.find(6), None)

if __name__ == '__main__':
    unittest.main()