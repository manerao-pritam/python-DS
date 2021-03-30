import sys

'''
function to return nth palindromic prime no.
1 to 11st palindromic primes are: 2 3 5 7 11 101 131 151 181 191
'''


class Solution:
    def get_nth_palindromic_prime(self, n):
        def is_palindrome(num):
            return str(num)[::-1] == str(num)

        def is_prime(num):
            for i in range(2, int(num ** 0.5) + 1):
                if not num % i:
                    return False

            return True

        # sanity check
        if n <= 0:
            return 0

        # 2 is the first prime no.
        result = num = 2

        while n:
            if is_palindrome(num) and is_prime(num):
                n -= 1
                result = num

            num += 1

        return result


def main():
    s1 = Solution()
    for _ in range(int(input())):
        n = int(input())
        print(f'{n}th palindromic prime is: {s1.get_nth_palindromic_prime(n)}')


if __name__ == '__main__':
    sys.stdin = open('./in', 'r')
    sys.stdout = open('./out', 'w')
    main()
