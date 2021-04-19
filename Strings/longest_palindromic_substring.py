import sys

'''
Longest palindrome in a string 
https://practice.geeksforgeeks.org/problems/longest-palindrome-in-a-string3411/1

Input:
S = "aaaabbaa"
Output: aabbaa

Input: 
S = "abccbc"
Output: bccb
'''


class Solution:
    '''
    Brute - generate all strings and check if its longer palindrome than the prev one
    O(n**3) time
    constant space
    '''

    def brute_longest_palindromic_substr(self, s):
        def is_longer_palindrome(tmp):
            if len(tmp) < len(longest):
                return False

            for i in range(len(tmp)//2):
                if tmp[i] != tmp[~i]:
                    return False

            return True

        longest = ''
        # if longest is a single char then the ans needs to be the first char, so iterate backward
        for i in range(len(s)-1, -1, -1):
            for j in range(i, len(s)):
                longest = s[i: j +
                            1] if is_longer_palindrome(s[i:j+1]) else longest

        return longest

    '''
    Optimal solution - expand from middle
    O(n**2) time
    constant space
    '''

    def longest_palindromic_substr(self, s):
        def get_palindrome_len(start, end):
            if start > end:
                return 0

            # expand to the left and to the right until the chars match
            while start >= 0 and end < len(s) and s[start] == s[end]:
                start -= 1
                end += 1

            return end - start - 1

        start = end = 0
        # if longest is a single char then the ans needs to be the first char, so iterate backward
        for i in range(len(s)-1, -1, -1):
            l1 = get_palindrome_len(i, i)   # odd len string
            l2 = get_palindrome_len(i, i+1)  # even len string

            longest = max(l1, l2)

            if longest > end - start:
                # i is curr char, left and right will total len // 2
                # start = left to i
                start = i - (longest - 1) // 2
                # end = i to right
                end = i + longest // 2

        return s[start: end + 1]


def main():
    for _ in range(int(input())):
        s = input().strip()
        s1 = Solution()
        print(s1.longest_palindromic_substr(s))
        print(s1.brute_longest_palindromic_substr(s))


if __name__ == '__main__':
    sys.stdin = open('./in', 'r')
    sys.stdout = open('./out', 'w')
    main()
