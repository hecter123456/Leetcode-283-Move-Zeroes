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

class Solution():
    def moveZeroes(self, nums):
        if nums == []:
            return nums
        n = len(nums)
        zero = 0
        for node in nums:
            if node == 0:
                zero += 1
                nums.remove(0)
        for i in range(zero):
            nums.append(0)
        #print(nums)
        return nums

if __name__ == '__main__':
    unittest.main()
