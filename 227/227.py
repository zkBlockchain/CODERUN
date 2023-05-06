def get_days(days):
	return int((days + 1) * days / 2)


def get_result(days, library_books, week_day, my_books):
	result = days // 7 * 5

	if days % 7 == 0:
		return library_books * result + my_books

	week_ending = week_day + days % 7
	result += week_ending - week_day

	if (week_day <= 6 and week_ending >= 8):
		result -= 2
	elif (week_day == 7 or week_ending == 7):
		result -= 1

	if (result > 0):
		return library_books * result + my_books

	return my_books


def get_estimate(library_books, my_books, week_day):
	weeks = ((2 * library_books) - 1) // 7
	result = ((2 * library_books) - 1) - (weeks * 2)

	while (my_books >= result + 1):
		if (my_books >= result + 1):
			result += 1
			week_day += 1
			my_books -= result
			
			if (week_day != 6 and week_day != 7):
				my_books += library_books
				if (week_day > 7):
					week_day %= 7

	return result


def main():
	library_books, my_books, week_day = [int(x) for x in input().split()]

	count = 0
	reads = 1
	
	if ((week_day == 6 or week_day == 7) and (my_books == 0)):
		print(0)
		return

	if (week_day == 6 and (my_books == 1 or my_books == 2)):
		print(1)
		return
	
	# (2 * Library Books - 1) - ((2 * Library Books - 1) // 7 * 2) = Estimate Days - O(1)
	if (library_books >= 1 or my_books >= 0) or True: # False - Other Algorithm, True - O(1)
		estimate_days = get_estimate(library_books, my_books, week_day) 

		if (estimate_days < 10):
			estimate_days = 10
		
		for i in range(estimate_days - 10, estimate_days + 10):
			if (get_result(i, library_books, week_day, my_books) < get_days(i)):
				count = i - 1
				break
		
		print(count)
		return
	
	# Other Algorithm (Time Limits) - O(n)
	while (True):

		if (week_day < 6):
			my_books += library_books
		
		my_books = my_books - reads

		if (my_books < 0):
			break
		

		week_day = (week_day % 7) + 1
		count += 1
		reads += 1
	
	print(count)
	return 0


if __name__ == '__main__':
	main()

