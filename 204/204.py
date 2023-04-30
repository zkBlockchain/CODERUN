def main():
	array = []
	summary = 0.0
	length = int(input())

	for i in range(length):
		item = sorted([float(x) for x in input().split()])
		summary += item[0] * item[1]
		array.append(item[0] * item[1])

	for item in array:
		result = round((item / summary), 12)
		print(result)


if __name__ == '__main__':
	main()

