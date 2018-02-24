import unittest

class unitest(unittest.TestCase):
    def testEmptylist(self):
        Input = []
        Output = []
        self.assertEqual(Solution().moveZeroes(Input),Output);
    def testSample(self):
        Input = [0, 1, 0, 3, 12]
        Output = [1, 3, 12, 0, 0]
        self.assertEqual(Solution().moveZeroes(Input),Output);
    def testDoubleZero(self):
        Input = [0,0,1]
        Output = [1,0,0]
        self.assertEqual(Solution().moveZeroes(Input),Output);
class Solution():
    def moveZeroes(self, nums):
        zero = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[zero] = nums[zero], nums[i]
                zero += 1
        return nums

if __name__ == '__main__':
    unittest.main()
