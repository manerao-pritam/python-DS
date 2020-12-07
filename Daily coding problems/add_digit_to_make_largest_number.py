"""
Interview question:
add digit to a number to any place to make a largest number possible. 

For example:

input: 
    0
    -999
    286
    388244
    8883

output:
    50
    -5999
    5286
    5388244
    88853
"""

# import sys

# sys.stdin = open("input", "r")
# sys.stdout = open("output", "w")


# get the position to add the digit in digits list
def get_pos(digits, digit, pos, multiplier):
    tmp = pos
    while tmp < len(digits):
        if digits[tmp] * multiplier < digit * multiplier:
            pos = tmp + 1
        tmp += 1

    return pos


# insert the digit to the correct position
def insert_digit(digits, digit, multiplier):
    i, pos, flag = 0, 0, True

    while i < len(digits):
        if flag and digits[i] * multiplier < digit * multiplier:
            flag = False
            pos = get_pos(digits, digit, i + 1, multiplier)

        i += 1

    # print(pos)
    digits.insert(pos, digit)


# convert the number to a list
# we could also do the same by converting num to string
# this is just for iterating through each digit
def number_to_digits(num, digits=None):
    while num:
        d, num, = (
            num % 10,
            num // 10,
        )

        digits += [d]


def get_max(num, digit=5):
    if not num:
        return digit * 10

    multiplier = -1 if num < 0 else 1

    # convert the negative number to positive
    num *= multiplier

    # number to digits array
    digits = []
    number_to_digits(num, digits)

    # insert the digit at the correct index
    insert_digit(digits, digit, multiplier)

    # make answer
    i, ans = 0, 0
    for d in digits:
        ans += d * (10 ** i)
        i += 1

    return ans * multiplier


def main():
    # t = int(input())
    # while t > 0:
    #     t -= 1
      num = int(input())
      print(get_max(num))


if __name__ == "__main__":
    main()
