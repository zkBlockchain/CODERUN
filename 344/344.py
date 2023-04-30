def can_step(step_array, stop_array, board):
	for i in range(len(step_array)):
		x = step_array[i][0]
		y = step_array[i][1]

		bit_array = []
		bit_array_step = []

		bit_array.append([x - 1, y + 1])
		bit_array.append([x - 1, y - 1])
		bit_array.append([x + 1, y + 1])
		bit_array.append([x + 1, y - 1])

		bit_array_step.append([x - 2, y + 2])
		bit_array_step.append([x - 2, y - 2])
		bit_array_step.append([x + 2, y + 2])
		bit_array_step.append([x + 2, y - 2])
		
		for s in range(len(bit_array)):
			if bit_array[s] in stop_array:
				if bit_array_step[s][0] >= 1 and bit_array_step[s][0] <= board[0]:
					if bit_array_step[s][1] >= 1 and bit_array_step[s][1] <= board[1]:
						if not bit_array_step[s] in stop_array and not bit_array_step[s] in step_array:
							return "Yes"

	return "No"


def main():
	board = [int(x) for x in input().split()]

	white_array = []
	white_counts = int(input())
	for i in range(white_counts):
		xy = [int(x) for x in input().split()]

		white_array.append(xy)

	black_array = []
	black_counts = int(input())

	for i in range(black_counts):
		xy = [int(x) for x in input().split()]

		black_array.append(xy)

	step = input()
	if step == 'white':
		print(can_step(white_array, black_array, board))
	else:
		print(can_step(black_array, white_array, board))


if __name__ == '__main__':
	main()




