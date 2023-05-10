monthly = {
	'January':31, 
	'February':28, 
	'March':31, 
	'April':30, 
	'May':31, 
	'June':30, 
	'July':31, 
	'August':31, 
	'September':30, 
	'October':31, 
	'November':30, 
	'December':31
}

weekly = [
	'Monday', 
	'Tuesday', 
	'Wednesday', 
	'Thursday', 
	'Friday', 
	'Saturday', 
	'Sunday'
]

monthly_array = list(monthly)


def check_leap(year):
	if (year % 400 == 0):
		return True
	elif (year % 4 == 0 and year % 100 != 0):
		return True
	return False


def get_days(year):
	leap_years = 0
	for i in range(1980, year):
		if check_leap(i):
			leap_years += 1

	results = ((year - 1980 - leap_years) * 365) + (leap_years * 366)
	return results


def get_current_days(day, month, year):
	days = 0
	for i in range(len(monthly_array)):
		if month == monthly_array[i]:
			days += day - 1
			return days
		else:
			days += monthly[monthly_array[i]]
			if check_leap(year):
				if monthly[monthly_array[i]] == 28: # February in leap year
					days += 1
	return days - 1


def main():
	starting_day = 2 # 1 January 1980 # Tuesday

	while True:
		try: # Checking EOF Ending
			reading_data = input().split()
			day = int(reading_data[0])
			month = reading_data[1]
			year = int(reading_data[2])
		except:
			break

		past_years = get_days(year)
		current_year = get_current_days(day, month, year)
		result_day = ((current_year + past_years) % 7) + starting_day

		print(weekly[((result_day) % 7) - 1])


if __name__ == '__main__':
	main()



