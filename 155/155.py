def main():
	length = int(input())
	array = sorted([int(x) for x in input().split()]) # Average - O(n), Worst - O(n*log(n))
	
	unique_elems = 0
	unique_flags = True
	for i in range(length): # Always O(n)
		if unique_flags:
			if i != length - 1 and array[i] == array[i + 1]:
				unique_flags = False
			else:
				unique_elems += 1
		else:
			if i != length - 1 and array[i] == array[i + 1]:
				unique_flags = False 
			else:
				unique_flags = True

	print(unique_elems)


if __name__ == '__main__':
	main()
