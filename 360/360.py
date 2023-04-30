def main():
	length = int(input())
	array = sorted([int(x) for x in input().split()])

	counts_array = []
	unique_flags = True
	for i in range(length):
		if unique_flags:
			if i != length - 1 and array[i] == array[i + 1]:
				item = [array[i], 2]
				counts_array.append(item)
				unique_flags = False
			else:
				item = [array[i], 1]
				counts_array.append(item)
		else:
			if i != length - 1 and array[i] == array[i + 1]:
				unique_flags = False
				counts_array[len(counts_array) - 1][1] += 1
			else:
				unique_flags = True

	max_duplicates = [0, 0]
	for item in counts_array:
		if item[1] >= max_duplicates[1]:
			max_duplicates[1] = item[1]
			max_duplicates[0] = item[0]

	print(max_duplicates[0])


if __name__ == '__main__':
	main()

