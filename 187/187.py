def main():
	tests = int(input())

	for i in range(tests):
		longues = int(input())
		array = sorted([int(x) for x in input().split()])

		min_value = 10**10
		for s in range(len(array) - 1):
			near_values = array[s] ^ array[s + 1]
			if near_values < min_value:
				min_value = near_values

		print(min_value)


if __name__ == '__main__':
	main()

