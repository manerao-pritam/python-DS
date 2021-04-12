import sys
import re

'''
Spirally traversing a matrix 
https://practice.geeksforgeeks.org/problems/spirally-traversing-a-matrix-1587115621/1

Input:
2
3 3
1 2 3 4 5 6 7 8 9
4 4
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16

Ouput:
[1, 2, 3, 6, 9, 8, 7, 4, 5]
[1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10]

O(n) time and space (considering the result list for output)
'''


class Solution:
    '''
    Using matrix Transpose
    '''

    def traverse_using_transpose(self, matrix):
        result = []

        while matrix:
            # add the topmost row in the result
            result += matrix[0]

            # remove the topmost row from the matrix
            del matrix[0]

            # transpose
            matrix = list(map(list, zip(*matrix)))
            '''
            Ex: 
            Input: ([1, 2, 3],)
                    ([4, 5, 6],)
                    ([7, 8, 9],)
            Output: (1, 4, 7)
                    (2, 5, 8)
                    (3, 6, 9)
            '''

            # swap cols
            matrix = matrix[::-1]

        return result

    '''
    simple spiral order traversal
    '''

    def traverse(self, matrix):
        result = []

        # traversal directions map to remove magic nos.
        directions = {
            'left_to_right': 0,
            'top_to_bottom': 1,
            'right_to_left': 2,
            'bottom_to_top': 3
        }

        top = left = 0
        bottom, right = len(matrix)-1, len(matrix[0])-1
        direction = directions['left_to_right']

        while top <= bottom and left <= right:
            if not direction:
                for i in range(top, right + 1):
                    result += [matrix[top][i]]
                top += 1

            if direction == directions['top_to_bottom']:
                for i in range(top, bottom+1):
                    result += [matrix[i][right]]
                right -= 1

            if direction == directions['right_to_left']:
                for i in range(right, left-1, -1):
                    result += [matrix[bottom][i]]
                bottom -= 1

            if direction == directions['bottom_to_top']:
                for i in range(bottom, top-1, -1):
                    result += [matrix[i][left]]
                left += 1

            direction += 1
            direction %= 4

        return result


def main():
    for _ in range(int(input())):
        R, C = map(int, input().strip().split())
        values = [int(n) for n in re.sub(
            '[^a-zA-Z0-9-]', ' ', input()).strip().split()]

        i = 0
        matrix = []
        for _ in range(R):
            row = []
            for _ in range(C):
                row += [values[i]]
                i += 1

            matrix += [row]

        s1 = Solution()
        print(s1.traverse(matrix))


if __name__ == '__main__':
    sys.stdin = open('./in', 'r')
    sys.stdout = open('./out', 'w')
    main()
