import itertools

def permutate(num, pos_1, pos_2):
    num_array = list(str(num))
    num_array[pos_1], num_array[pos_2] = num_array[pos_2], num_array[pos_1]
    return int(''.join(num_array))

number = input()
k = int(input())

divisors = [5, 6, 10]
indices = list(itertools.combinations(range(len(number)), 2))

array_nums = [int(number)]
for i in range(k):
	new_array = []
	for n in range(len(array_nums)):
		for pair in indices:
			new_num = permutate(array_nums[n], pair[0], pair[1])
			new_array.append(new_num)
	array_nums.clear()
	array_nums.extend(new_array)

counts = 0
for item in array_nums:
	for divisor in divisors:
		if item % divisor == 0:
			counts += 1
			break

probability = counts / len(array_nums)
print(probability)
