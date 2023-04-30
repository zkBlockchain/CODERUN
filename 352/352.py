def main():
	jewelry = input()
	stones = input()
	
	already_done = ''
	jewelry_counts = 0

	for i in range(len(jewelry)):
		if jewelry[i] in already_done:
			continue

		for s in range(len(stones)):
			if jewelry[i] == stones[s]:
				jewelry_counts += 1

		already_done += jewelry[i]

	print(jewelry_counts)


if __name__ == '__main__':
	main()