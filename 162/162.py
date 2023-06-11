import itertools


def five_div(number):
	amounts = number.count('5') + number.count('0')

	if amounts > 0:
		return amounts
	else:
		return 0


def six_div(number):
	amounts = 0
	array = ['0', '2', '4', '6', '8']
	
	for i in range(len(array)):
		temp_counts = number.count(array[i])
		if temp_counts > 0:
			amounts += temp_counts
	if amounts > 0:
		number_sum = 0
		for i in range(len(number)):
			number_sum += int(number[i])
		if number_sum % 3 == 0:
			return amounts
		else:
			return 0
	else:
		return 0


def ten_div(number):
	amounts = number.count('0')
	if amounts > 0:
		return amounts
	else:
		return 0


def is_num_lucky(number):
	is_lucky = False
	if int(number) % 5 == 0 or int(number) % 6 == 0 or int(number) % 10 == 0:
		is_lucky = True
	return is_lucky


def permutate(num, pos_1, pos_2):
    num_array = list(str(num))
    num_array[pos_1], num_array[pos_2] = num_array[pos_2], num_array[pos_1]
    return int(''.join(num_array))


def main():
	number = input()
	mutations = int(input())
	#divisors = [5, 6, 10]

	if not (five_div(number) or six_div(number) or ten_div(number)): # Numbers is not passes criteria
		print(0.0)
		return
	
	if mutations == 0: # No any swaps
		if is_num_lucky(number):
			print(1.0)
			return
		else:
			print(0.0)
			return

	indices = list(itertools.combinations(range(len(number)), 2))
	variants = len(indices)

	lucky, unlucky = '', ''
	lucky_pass, unlucky_pass = 0, 0

	if is_num_lucky(number):
		lucky = number
	else:
		unlucky = number

	for pair in indices: # Searching for Example of lucky & unlucky
		new_num = permutate(number, pair[0], pair[1])
		if lucky:
			if not (is_num_lucky(new_num)):
				unlucky = str(new_num)
				break
		else:
			if (is_num_lucky(new_num)):
				lucky = str(new_num)
				break

	for pair in indices: # Searching for Probability of lucky & unlucky
		lucky_num = permutate(lucky, pair[0], pair[1])
		unlucky_num = permutate(unlucky, pair[0], pair[1])

		if (is_num_lucky(lucky_num)):
			lucky_pass += 1
		if (is_num_lucky(unlucky_num)):
			unlucky_pass += 1

	previous_lucky = lucky_pass
	if not is_num_lucky(number):
		previous_lucky = unlucky_pass

	if mutations == 1:
		print(previous_lucky / variants)
		return

	for i in range(2, mutations + 1):
		lucky_results = lucky_pass * previous_lucky
		unlucky_results = unlucky_pass * ((variants ** (i - 1))- previous_lucky)
		previous_lucky = lucky_results + unlucky_results
		if (i == mutations):
			print((lucky_results + unlucky_results) / (variants ** i))


if __name__ == '__main__':
	main()
