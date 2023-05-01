from sys import stdin, stdout 


def main():
	words = int(stdin.readline().rstrip())

	graph_array = {}
	peaks_array = {}

	for i in range(words):
		word = stdin.readline().rstrip()

		for s in range(len(word) - 3):
			first_part = word[s:s + 3]
			second_part = word[s + 1:s + 3 + 1]

			peaks = first_part + second_part
			peaks_array.update({first_part: None, second_part: None})

			if peaks in graph_array:
				graph_array[peaks] += 1
			else:
				graph_array.update({peaks: 1})


	stdout.write((str(len(peaks_array))) + '\n')
	stdout.write(str(len(graph_array)) + '\n')

	for graph in graph_array:
		stdout.write(graph[:3] + ' ' + graph[3:] + ' ' + str(graph_array[graph]) + '\n')


if __name__ == '__main__':
	main()
