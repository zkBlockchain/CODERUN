from sys import stdin, stdout


def main():
    items = int(stdin.readline().rstrip())

    items_array = []
    for i in range(items):
        item = stdin.readline().rstrip().split()
        width, length = int(item[0]), int(item[1])
        if width < length:
            width, length = length, int(item[0])

        items_array.append([width, length])
            
    items_array.sort(key=lambda x: (x[0], -x[1]))

    items_empty = [0] * len(items_array)
    max_value = float('-inf')
    for i in range(len(items_array) - 1, -1, -1):
        max_value = max(max_value, items_array[i][1])
        items_empty[i] = max_value
    
    summary = 0
    for i in range(len(items_array)):
        starts, ends = i + 1, len(items_array) - 1
        while starts <= ends:
            middle = (starts + ends) // 2
            if items_array[middle][0] > items_array[i][0]:
                ends = middle - 1
            else:
                starts = middle + 1
        if starts >= len(items_empty) or items_empty[starts] <= items_array[i][1]:
            summary += 1
            
    stdout.write(str(summary) + "\n")


if __name__ == "__main__":
    main()