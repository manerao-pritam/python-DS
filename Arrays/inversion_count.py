import sys
import re
from collections import Counter

'''
Count Inversions
Count the occurrences where a[i] > a[j] and i < j
https://www.geeksforgeeks.org/counting-inversions/

Input:
3
8 4 2 1
2 1 1 3 2 3 4 5 6 7 8 9
5 3 2 4 1

Output:
6
6
8
'''


class Solution:
    count = 0

    '''
    Using modified merge sort
    O(nlog n) time
    O(n) space
    '''

    def get_inversion_count(self, nums):
        def merge(left, right, nums):
            i = j = k = 0

            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    nums[k] = left[i]
                    i += 1
                else:
                    nums[k] = right[j]
                    # count inversions
                    self.count += (len(left) - i)
                    j += 1

                k += 1

            while i < len(left):
                nums[k] = left[i]
                i += 1
                k += 1

            while j < len(right):
                nums[k] = right[j]
                j += 1
                k += 1

        def partition(nums):
            if len(nums) <= 1:
                return

            mid = len(nums) // 2
            left = nums[:mid]
            right = nums[mid:]

            partition(left)
            partition(right)

            return merge(left, right, nums)

        partition(nums)
        return self.count

    '''
    Using Binary Indexed (or Fenwick) Tree
    O(nlog n) time 
    O(n) space
    '''

    def fenwick_tree(self, nums):
        def LSB(i):
            return i & (-i)

        def get_sum(i):
            sum = 0

            while i:
                sum += tree[i]
                i -= LSB(i)

            return sum

        def update(i, x):
            while i <= max__:
                tree[i] += x
                i += LSB(i)

        if not nums:
            return 0

        # if nos are greater than 10**5, then we can compress the array
        tmp = Counter(nums)

        # map large nos with small nos.
        i = 1
        for k in sorted(tmp.keys()):
            tmp[k] = i
            i += 1

        # compressed array
        for i in range(len(nums)):
            nums[i] = tmp[nums[i]]

        # Fenwick tree
        max__ = max(nums)
        tree = [0] * (max__ + 1)

        for n in nums[::-1]:
            self.count += get_sum(n)
            update(n, 1)

        return self.count


def main():
    for _ in range(int(input())):
        nums = [int(n) for n in re.sub(
            '[^a-zA-Z0-9-]', ' ', input()).strip().split()]
        s1 = Solution()
        print(s1.get_inversion_count(nums))
        # print(s1.fenwick_tree(nums))


if __name__ == '__main__':
    sys.stdin = open('./in', 'r')
    sys.stdout = open('./out', 'w')
    main()
