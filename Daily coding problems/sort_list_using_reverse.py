import sys

sys.stdin = open("input", "r")
sys.stdout = open("output", "w")


def is_sorted(arr):
    i, len_ = 1, len(arr)
    while i < len_:
        if arr[i - 1] > arr[i]:
            return False

        i += 1

    return True


def reverse__(arr, i, j):
    while j >= i:
        arr[i], arr[j] = arr[j], arr[i]
        i, j = i + 1, j - 1
    return arr


def sort__(arr):
    i, j, len__ = 0, 1, len(arr)

    while not is_sorted(arr):
        while j < len__:
            if arr[i] <= arr[j]:
                i, j = i + 1, j + 1

            else:
                while j < len__ and arr[i] > arr[j]:
                    j += 1

                arr = reverse__(arr, i, j - 1)
                i, j = 0, 1
    return arr


def main():
    """
    DCP: 618
    Given a list, sort it using this method: reverse(lst, i, j), which reverses lst from i to j.
    """
    # input: 1 2 3 5 7 4 6 -11 9 10
    arr = [(int(n)) for n in input().strip().split()]
    print(sort__(arr))


if __name__ == "__main__":
    main()
