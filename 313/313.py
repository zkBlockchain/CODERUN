import math
import bisect


def main():
    items = int(input())
    items_array = [int(x) for x in input().split()]

    summary = 0
    elem_lists = []
    for i in range(0, len(items_array)):
        bisect.insort(elem_lists, items_array[i])
        summary += elem_lists[math.ceil(len(elem_lists) / 2) - 1]
    print(summary)


if __name__ == "__main__":
    main()


