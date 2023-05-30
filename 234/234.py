import urllib3


array = []
for i in range(4):
	array.append(input())

flags = True

HTTP = urllib3.PoolManager()
variables1 = [('X-Cat-Variable', array[0] + ', ' + array[1])] # 1 2
variables2 = [('X-Cat-Variable', array[0] + ', ' + array[2])] # 1 3
variables3 = [('X-Cat-Variable', array[2] + ', ' + array[3])] # 3 4

response = HTTP.request('MEW', 'http://127.0.0.1:7777/', headers=variables1)
array1 = response.headers['X-Cat-Value'].split(', ')

response = HTTP.request('MEW', 'http://127.0.0.1:7777/', headers=variables2)
array2 = response.headers['X-Cat-Value'].split(', ')


if array1 == array2:
	variables3 = [('X-Cat-Variable', array[1] + ', ' + array[2] + ', ' + array[3])] # 2 3 4
	flags = False

response = HTTP.request('MEW', 'http://127.0.0.1:7777/', headers=variables3)
array3 = response.headers['X-Cat-Value'].split(', ')


if flags:
	# array1: 1 2
	# array2: 1 3
	# array3: 3 4

	first_elem = array1[0]
	second_elem = array1[1]
	third_elem = array2[1]
	fourth_elem = array3[1]

	if array1[0] == array1[1]:
		if third_elem == first_elem:
			third_elem = array2[0]
		if fourth_elem == third_elem:
			fourth_elem = array3[0]
	elif array2[0] == array2[1]:
		first_elem = array2[0]
		third_elem = first_elem

		if second_elem == first_elem:
			second_elem = array1[0]
		if fourth_elem == third_elem:
			fourth_elem = array3[0]
	elif array3[0] == array3[1]:
		third_elem = array3[0]
		fourth_elem = third_elem

		first_elem = array2[0]
		if first_elem == third_elem:
			first_elem = array2[1]

		if second_elem == first_elem:
			second_elem = array1[0]
	else: # 1 != 2; 1 != 3; 3 != 4
		if array1 == array2 and array2 != array3:
			if array3[0] in array2:
				third_elem = array3[0]
				fourth_elem = array3[1]
			else:
				third_elem = array3[1]
				fourth_elem = array3[0]
			second_elem = third_elem

			if first_elem == second_elem:
				first_elem = array1[1]
		else:
			if first_elem not in array2:
				first_elem = array1[1]
				second_elem = array1[0]

				if third_elem == first_elem:
					third_elem = array2[0]
				if fourth_elem == third_elem:
					fourth_elem = array3[0]
			else:
				if third_elem == first_elem:
					third_elem = array2[0]
				if fourth_elem == third_elem:
					fourth_elem = array3[0]
else: 
	# array1: 1 2
	# array2: 1 3
	# array3: 2 3 4
	# array1 == array2

	first_elem = array1[0]
	second_elem = array1[1]
	fourth_elem = array3[0]

	if first_elem == second_elem: # 1 == 2 == 3
		third_elem = first_elem
		if fourth_elem == second_elem or fourth_elem == third_elem:
			fourth_elem = array3[1]
		if fourth_elem == second_elem or fourth_elem == third_elem:
			fourth_elem = array3[2]
	
	else:
		if array3[0] == array3[1] == array3[2]:
			second_elem = array3[0]
			third_elem = second_elem
			fourth_elem = second_elem

			if first_elem == second_elem:
				first_elem = array1[1]
		else:
			if array3[0] == array3[1]:
				fourth_elem = array3[2]
				second_elem = array3[0]
				third_elem = second_elem
			elif array3[0] == array3[2]:
				fourth_elem = array3[1]
				second_elem = array3[0]
				third_elem = second_elem
			elif array3[1] == array3[2]:
				fourth_elem = array3[0]
				second_elem = array3[1]
				third_elem = second_elem
			
			if first_elem == second_elem:
				first_elem = array1[1]

print(first_elem)
print(second_elem)
print(third_elem)
print(fourth_elem)
