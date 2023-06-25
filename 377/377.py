def main():
    n = int(input())

    variety = n
    positions, categories = {}, {}

    for _ in range(n):
        product, category = map(int, input().split())
        categories[product] = category

    products = list(map(int, input().split()))
    for index, product in enumerate(products):
        if categories[product] in positions:
            difference = abs(index - positions[categories[product]])
            if difference <= variety:
                variety = difference
        positions[categories[product]] = index

    print(variety)


if __name__ == '__main__':
    main()

