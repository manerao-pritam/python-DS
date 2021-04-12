import sys
import re
from collections import namedtuple

'''
Minimum number of jumps
https://practice.geeksforgeeks.org/problems/minimum-number-of-jumps-1587115620/1

Examples:
Input: 1 3 5 8 9 2 6 7 6 8 9
Output: 3

Input: 1 4 3 2 6 7
Output: 2
'''


class Solution:
    Interval = namedtuple('Interval', ('start', 'end'))

    def min_jumps(self, nums):
        # can't reach
        if not nums or not nums[0]:
            return -1

        jumps = nextpos = 0
        interval = self.Interval(0, 0)

        while True:
            # each time the loop iterates, we consider a jump
            jumps += 1

            # check the max between the interval range
            for i in range(interval.start, interval.end + 1):
                nextpos = max(nextpos, i + nums[i])

            # has nextpos reached to the end?
            if nextpos >= len(nums)-1:
                return jumps    # yes; return total jumps

            # end hasn't reached yet
            # calculate next Interval
            # end of prev interval + 1 to nextpos
            interval = self.Interval(interval.end + 1, nextpos)

            # start can't be greater than end
            if interval.start > interval.end:
                return -1


def main():
    for _ in range(int(input())):
        s1 = Solution()
        nums = [int(n) for n in re.sub(
            '[^a-zA-Z0-9-]', ' ', input()).strip().split()]
        print(s1.min_jumps(nums))


if __name__ == '__main__':
    sys.stdin = open('./in', 'r')
    sys.stdout = open('./out', 'w')
    main()
