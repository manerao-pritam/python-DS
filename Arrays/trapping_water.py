import sys
import re

'''
Trapping rain water
https://practice.geeksforgeeks.org/problems/trapping-rain-water-1587115621/1#

Input:
8 8 2 4 5 5 1
1 1 5 2 7 6 1 4 2 3

Output:
4
7
'''


class Solution:
    def trapping_water(self, nums):
        '''
        Brute Method
        O(n**2) time
        constant space
        '''
        # def get_left_right_max(i):
        #     leftmax = rightmax = 0

        #     # copy of main 'i'
        #     idx = i
        #     while i >= 0:
        #         leftmax = max(leftmax, nums[i])
        #         i -= 1

        #     while idx < len(nums):
        #         rightmax = max(rightmax, nums[idx])
        #         idx += 1

        #     return leftmax, rightmax

        # result = 0
        # for i in range(len(nums)):
        #     # min of left and right
        #     curr_min = min(get_left_right_max(i))

        #     # substract current from the min
        #     curr_min -= nums[i]

        #     result += curr_min

        # return result

        '''
        Prefix/Suffix max
        O(n) time and space
        '''
        # # prefix max
        # def get_prefix_max():
        #     tmp = 0
        #     prefix_max = []

        #     for n in nums:
        #         tmp = max(tmp, n)
        #         prefix_max += [tmp]

        #     return prefix_max

        # # suffix max
        # def get_suffix_max():
        #     tmp = nums[-1]
        #     suffix_max = [0] * len(nums)

        #     for i in range(len(nums)-1, -1, -1):
        #         tmp = max(tmp, nums[i])
        #         suffix_max[i] = tmp

        #     return suffix_max

        # prefix_max = get_prefix_max()
        # suffix_max = get_suffix_max()

        # result = 0
        # for i in range(len(nums)):
        #     # min of left and right
        #     curr_min = min(prefix_max[i], suffix_max[i])

        #     # substract current from the min
        #     curr_min -= nums[i]

        #     result += curr_min

        # return result

        '''
        Two pointer -- optimal
        O(n) time 
        constant space
        '''
        leftmax = rightmax = result = 0
        left, right = 0, len(nums)-1

        while left <= right:
            leftval, rightval = nums[left], nums[right]

            if leftval <= rightval:
                leftmax = max(leftmax, leftval)
                result += max(leftmax - leftval, 0)

                left += 1
            else:
                rightmax = max(rightmax, rightval)
                result += max(rightmax - rightval, 0)

                right -= 1

        return result


def main():
    s1 = Solution()
    for _ in range(int(input())):
        nums = [int(n) for n in re.sub(
            '[^a-zA-Z0-9-]', ' ', input()).strip().split()]
        print(s1.trapping_water(nums))


if __name__ == '__main__':
    sys.stdin = open('./in', 'r')
    sys.stdout = open('./out', 'w')
    main()
