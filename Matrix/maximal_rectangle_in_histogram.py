import sys
import re

'''
84. Largest Rectangle in Histogram
https://leetcode.com/problems/largest-rectangle-in-histogram/

Input:
2
[2,1,5,6,2,3]
[2,4]

Output:
10
4

O(n) time and space
'''


class Solution:
    def brute_largest_rectangle_area(self, nums) -> int:
        '''
        brute force O(n**2)
        '''
        result = 0

        for i in range(len(nums)):
            curr_min = nums[i]
            for j in range(i, len(nums)):
                curr_min = min(curr_min, nums[j])
                result = max(result, (j - i + 1) * curr_min)

        return result

    def largest_rectangle_area(self, nums) -> int:
        '''
        using stack O(n) time and space
        '''
        # if we append 0 at the end of the row, it makes the code assume that its the end of the row, which helps in removing the extra emptying stack steps
        nums += [0]

        # stack to start with -1 to maintain the boundaries of row
        indices_stk = [-1]

        result = 0

        for i in range(len(nums)):
            while nums[indices_stk[-1]] > nums[i]:
                curr_min = nums[indices_stk.pop()]
                width = (i - indices_stk[-1] - 1)

                # area = width * min of heights within this width
                result = max(result, width * curr_min)

            # store indx if the value at this index is less than stack top index value
            indices_stk += [i]

        return result


def main():
    for _ in range(int(input())):
        nums = [int(n) for n in re.sub(
            '[^a-zA-Z0-9-]', ' ', input()).strip().split()]

        s1 = Solution()
        print(s1.largest_rectangle_area(nums))
        # print(s1.brute_largest_rectangle_area(nums))


if __name__ == '__main__':
    sys.stdin = open('./in', 'r')
    sys.stdout = open('./out', 'w')
    main()
