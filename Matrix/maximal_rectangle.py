import sys
from maximal_rectangle_in_histogram import Solution as histogram_area_class

'''
85. Maximal Rectangle
https://leetcode.com/problems/maximal-rectangle/

Input:
1
8 14
0 0 0 0 1 0 1 0 1 0 1 0 0 1 1 1 0 0 1 0 0 1 0 1 0 1 1 1 0 0 0 1 0 1 0 1 0 1 0 0 0 1 1 0 0 0 1 0 1 1 1 1 1 0 0 1 0 1 0 1 1 1 1 1 1 1 0 0 0 1 0 0 0 0 0 1 1 0 1 1 1 1 1 1 0 1 0 1 0 1 1 1 1 1 1 1 0 0 0 1 1 0 0 0 1 1 0 1 0 0 1 0

Output:
8

O(r * c) time
O(c) time for histogram area stack
'''


class Solution:
    def maximal_rectangle(self, matrix) -> int:

        if not matrix:
            return 0

        '''
        Main funtion to convert matrix to row wise histograms
        O(r*c) time and constant space
        '''
        # converting chars to int in first row
        for c, item in enumerate(matrix[0]):
            matrix[0][c] = int(item)

        # histogram class object
        histogram_area = histogram_area_class()

        # maxarea of first row
        # result = histogram_area.largest_rectangle_area(matrix[0])
        result = histogram_area.largest_rectangle_area(matrix[0])

        for r in range(1, len(matrix)):
            for c in range(len(matrix[r])):
                # char to int
                matrix[r][c] = int(matrix[r][c])

                if not matrix[r][c]:
                    matrix[r][c] = 0
                else:
                    matrix[r][c] += matrix[r-1][c]

            # result = max(
            #     result, histogram_area.largest_rectangle_area(matrix[r]))
            result = max(
                result, histogram_area.largest_rectangle_area(matrix[r]))

        return result


def main():
    for _ in range(int(input())):
        R, C = map(int, input().strip().split())
        values = list(map(int, input().strip().split()))

        k = 0
        matrix = []
        for _ in range(R):
            row = []
            for _ in range(C):
                row += [values[k]]
                k += 1

            matrix += [row]

        s1 = Solution()
        print(s1.maximal_rectangle(matrix))


if __name__ == '__main__':
    sys.stdin = open('./in', 'r')
    sys.stdout = open('./out', 'w')
    main()
