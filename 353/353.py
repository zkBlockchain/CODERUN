import requests, json


def main():
	array = []

	for i in range(4):
		array.append(input())

	response = requests.get(array[0] + ':' + array[1] + '?a=' + array[2] + '&b=' + array[3])
	response_array = sorted(json.loads(response.content))

	for i in range(1, len(response_array) + 1):
		if response_array[-i] >= 0:
			print(response_array[-i])


if __name__ == '__main__':
	main()

