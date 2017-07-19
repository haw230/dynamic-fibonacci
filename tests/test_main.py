import unittest
import sys
sys.path.insert(0, '/home/ubuntu/workspace/linear_search')
from main import search

class TestLinearSearch(unittest.TestCase):
    def testing(self):
        self.assertEqual(search([0,1,2], 1), 1)
        self.assertEqual(search([1,2,3], 2), 1)
        self.assertEqual(search([1,2,3], 3), 3)

def main():
    unittest.main()

if __name__ == '__main__':
    main()