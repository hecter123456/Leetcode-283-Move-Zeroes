import unittest

class unitest(unittest.TestCase):
    def testEmptylist(self):
        Input = []
        Output = []
        self.assertEqual(Solution().moveZeroes(Input),Output);

class Solution():
    def moveZeroes(self, nums):
        if nums == []:
            return []
        return None

if __name__ == '__main__':
    unittest.main()
