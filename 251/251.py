def main():
	set_string = input()
	sub_string = input()

	if len(set_string) < len(sub_string):
		print(0)
		return

	min_length = len(sub_string)

	counts = 0
	for n in range(min_string, len(set_string) + 1):
		for s in range(len(set_string)):
			for i in range(len(sub_string)):
				if sub_string[i] in set_string[s:n + s]:
					counts += 1
				else:
					counts = 0
					break
			if counts == len(sub_string):

				for k in range(len(set_string[s:n + s])):
					if not set_string[s:n + s][k] in sub_string:
						print(0)
						return

				print(len(set_string[s:n + s]))
				return

	print(0)
	return


if __name__ == '__main__':
	main()

