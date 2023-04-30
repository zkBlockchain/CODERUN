def main():
	length = [int(x) for x in input().split()]
	sellers = sorted([int(x) for x in input().split()])
	buyers = sorted([int(x) for x in input().split()])

	lesser = length[1] if length[0] > length[1] else length[0]
	total_income = 0

	for i in range(lesser):
		income = buyers[length[1] - i - 1] - sellers[i]
		if income > 0:
			total_income += income

	print(total_income)


if __name__ == '__main__':
	main()

