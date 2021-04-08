import sys
import re

'''
Return min swaps required to bring items less than or equal to k together
https://www.geeksforgeeks.org/minimum-swaps-required-bring-elements-less-equal-k-together/

Input:
    9
    4 16 3 8 13 2 19 4 12 2 7 17 4 19 1
    6
    {2 7 9 5 8 7 4}
    6
    20 12 17
    3
    {2 1, 5, 6, 3}

Output:
    3
    2
    0
    1
'''


class Solution:
    '''
    O(n**2) time
    constant space
    '''

    def brute_min_swaps(self, nums, k):
        # count items which are <= k
        less_equal_k_count = 0
        for n in nums:
            less_equal_k_count += 1 if n <= k else 0

        result = float('inf')

        # window will be of less_equal_k_count size
        for i in range(len(nums) - less_equal_k_count):
            swaps = 0

            # window_start is i
            # window_end will be i + less_equal_k_count
            for j in range(i, i + less_equal_k_count):
                swaps += 1 if nums[j] > k else 0

            result = min(result, swaps)

        return 0 if result == float('inf') else result

    '''
    O(n) time
    constant space
    '''

    def min_swaps(self, nums, k):
        # this can be solved using sliding window
        # count the no. of items <= k, that will be our window size
        window_size = 0
        for n in nums:
            window_size += 1 if n <= k else 0

        # now slide the window, check the swaps required for each window and get the min of them
        result, swaps = float('inf'), 0
        left_idx = 0

        for right_idx in range(len(nums)):
            # swap count will be increamented if the current item is greater that k
            swaps += 1 if nums[right_idx] > k else 0

            # within the window
            if right_idx - left_idx + 1 == window_size:
                # total min swaps
                result = min(result, swaps)

                # decrement swaps if the item on the left index was greater than k, as now the window will be shifted by 1
                swaps -= 1 if nums[left_idx] > k else 0
                left_idx += 1

        return 0 if result == float('inf') else result


def main():
    s1 = Solution()
    for _ in range(int(input())):
        k = int(input())
        nums = [int(n) for n in re.sub(
            '[^a-zA-Z0-9-]', ' ', input()).strip().split()]
        # print(s1.brute_min_swaps(nums, k))
        print(s1.min_swaps(nums, k))


if __name__ == '__main__':
    sys.stdin = open('./in', 'r')
    sys.stdout = open('./out', 'w')
    main()
