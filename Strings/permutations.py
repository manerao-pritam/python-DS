import sys
from collections import deque


class Solution:
    '''
    Start with first char as perm and then keep adding next char at each pos all the prev perms
    123
    perms = [1]
            [1] -> 2 => [2,1], [1,2]
            [2,1] -> 2 => [3,2,1], [2,3,1], [2,1,3]
            [1,2] -> 3 => [3,1,2], [1,3,2], [1,2,3]

    O(n! * n) time and space
    '''

    def get_permutations(self, s):
        if not s:
            return []

        perms = deque(s[0])
        result = []

        for nextchar in s[1:]:
            perms_count = len(perms)

            for _ in range(perms_count):
                perm = perms.popleft()

                # len(perm) + 1 because we will be putting the nextchar at the end of current permutation
                for idx in range(len(perm) + 1):
                    tmp = list(perm)
                    tmp.insert(idx, nextchar)
                    tmp = ''.join(tmp)

                    if len(tmp) == len(s):
                        result += [tmp]
                    else:
                        perms += [tmp]

        return sorted(result)

    '''
    Same as above
    O(n! * n) time and space
    '''

    def get_permutations_recursive(self, s):
        result = []

        def helper(idx, perm):
            if idx == len(s):
                result.append(perm)
            else:
                for i in range(len(perm) + 1):
                    tmp = list(perm)
                    tmp.insert(i, s[idx])
                    tmp = ''.join(tmp)
                    helper(idx + 1, tmp)

        helper(0, '')
        return sorted(result)

    '''
    O(n! * n) time and space
    '''

    def get_permutations_backtracking(self, s):
        s = list(s)

        def helper(l, r):
            if l == r:
                perm = ''.join(s)
                perms.append(perm)
            else:
                for i in range(l, r + 1):
                    s[i], s[l] = s[l], s[i]

                    helper(l + 1, r)

                    # backtrack to the prev s
                    s[i], s[l] = s[l], s[i]

        perms = []
        helper(0, len(s) - 1)
        return perms

    '''
    O(n) time
    constant space
    '''

    def next_permutation(self, perm):
        if not perm:
            return ''

        perm = list(perm)

        # left right to left check the index where the increasing order breaks
        k = len(perm) - 1
        while k and perm[k] < perm[k-1]:
            k -= 1

        # reached the start/end of the string i.e. the perm is sorted i.e. first/last perm
        # either return '' or reverse of the perm
        if not k or k == len(perm) - 1:
            return ''.join(perm[::-1])

        k -= 1
        # from right to left check the first item that is less than kth item, replace these two numbers and then reverse the list from k+1 to end
        for i in range(k + 1, len(perm)):
            if perm[k] > perm[i]:
                perm[k], perm[i] = perm[i], perm[k]
                break

        # reverse k+1 to end
        perm[k+1:] = perm[k+1:][::-1]

        return ''.join(perm)

    '''
    O(n) time amd space (for result, and pre-calculated factorials)
    '''

    def get_kth_permutation(self, s, k):
        if not s:
            return ''

        # factorials that we will need for finding idexes
        def fact_helper(k):
            tmp = 1

            for i in range(2, k + 1):
                tmp *= i
                fact[i] = tmp

        # fact[0] is 1
        fact = [1] + [1] * k
        fact_helper(k)

        # in case if the k is larger than the total no. of permutations
        k %= fact[len(s)]

        s = list(s)
        result = []

        while s:
            n = len(s)

            # get the index based on the range where the result char will be available
            idx = k // fact[n-1]

            # in case the index is found to be on the next range, adjust it
            if not k % fact[n-1]:
                idx -= 1

            # add the char to the result
            result += s[idx]
            del s[idx]

            # decrement k based on the prev index
            k -= fact[n-1] * idx

        return ''.join(result)


def main():
    for _ in range(int(input())):
        s = input().strip()
        s1 = Solution()
        print(s1.get_permutations(s))
        print(s1.get_permutations_recursive(s))
        print(s1.get_permutations_backtracking(s))
        print(s1.next_permutation(s))

        k = 11
        print(s1.get_kth_permutation(s, k))


if __name__ == '__main__':
    sys.stdin = open('./in', 'r')
    sys.stdout = open('./out', 'w')
    main()
