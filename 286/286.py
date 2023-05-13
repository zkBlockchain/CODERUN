from sys import stdin, stdout


def caesar(item, shift):
	result = ""
	for i in range(len(item)):
		char = item[i]
		result += chr((ord(char) + shift - 97) % 26 + 97)
	return result


def main():
	english_source = "abcdefghijklmnopqrstuvwxyz"

	words_source = {}
	source_string = stdin.readline().rstrip()
	for x in source_string.split():
		words_source.update({x: None})

	words_count = int(stdin.readline().rstrip())

	for n in range(words_count):
		x = stdin.readline().rstrip()

		for i in range(len(english_source)):
			item = caesar(x, i)
			if item in words_source:
				stdout.write(item + '\n')
				break


if __name__ == '__main__':
	main()

