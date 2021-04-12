import sys
import re

'''
Return kth smallest element from an unsorted list
Example:
Input:
    2
    7 4 6 3 9 1
Output:
    3

Input:
    3  
    7 10 4 3 20 15
Output:
    7

Input:
    4
    7 10 4 20 15
Output:
    15
'''


# decorator for timing
def my_timer(original_function):
    from time import time

    def wrapper(*args, **kwargs):
        t = time()
        result = original_function(*args, **kwargs)
        print(f'Took {time() - t} seconds')
        return result

    return wrapper


class Solution:
    '''
    Sorting
    O(nlog n)
    O(n)
    '''
    # @my_timer
    # def kth_smallest(self, nums, k):
    #     return sorted(nums)[k-1]

    '''
    Max Heap
    O(nlog k)
    O(k)
    '''
    # @my_timer
    # def kth_smallest(self, nums, k):
    #     from heapq import heappush, heappushpop

    #     maxheap = []
    #     for n in nums[:k]:
    #         heappush(maxheap, n * -1)

    #     for n in nums[k:]:
    #         heappushpop(maxheap, n * -1)

    #     return maxheap[0] * -1

    '''
    QuickSelect - with randomized pivot 
    O(n) .. worst rarely O(n2)
    O(1)
    '''
    @my_timer
    def kth_smallest(self, nums, k):
        def partition(l, r):
            # last item
            pivot = nums[r]

            # start from l
            idx = l

            for i in range(l, r):
                # swap if ith item les than or equal to pivot
                if nums[i] <= pivot:
                    nums[i], nums[idx] = nums[idx], nums[i]
                    idx += 1

            # move pivot to the end
            nums[r], nums[idx] = nums[idx], nums[r]
            return idx

        def helper(l, r):
            idx = partition(l, r)

            if k == idx:
                return nums[idx]

            if k < idx:
                return helper(l, idx - 1)

            return helper(idx + 1, r)

        # 0 based indexing so need to remove 1
        k -= 1 if k else 0
        return helper(0, len(nums)-1)


def main():
    for _ in range(int(input())):
        s1 = Solution()
        k = int(input())
        nums = [int(n) for n in re.sub(
            '[^a-zA-Z0-9-]', ' ', input()).strip().split()]
        print(s1.kth_smallest(nums, k))


if __name__ == '__main__':
    sys.stdin = open('./in', 'r')
    sys.stdout = open('./out', 'w')
    main()
