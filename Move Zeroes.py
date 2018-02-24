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
        if nums == []:
            return nums
        n = len(nums)
        for i in range(n):
            if nums[i] == 0:
                for j in range(i+1,n):
                    if nums[j] != 0:
                        nums[i], nums[j] = nums[j], nums[i]
                        break
        return nums

if __name__ == '__main__':
    unittest.main()
