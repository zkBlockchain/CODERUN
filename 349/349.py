import json


def main():
	main_json = json.loads('{"offers":[]}')
	shops, feeds = [int(x) for x in input().split()]

	counter = 0
	array = []

	for i in range(shops):
		array.append(json.loads(str(input())))

	for i in range(len(array)):
		for s in range(len(array[i]["offers"])):
			output = {"market_sku":array[i]["offers"][s]["market_sku"], 
						"offer_id": array[i]["offers"][s]["offer_id"],
							"price": array[i]["offers"][s]["price"]}
			
			main_json["offers"].append(output)

			counter += 1
			if counter == feeds:
				print(json.dumps(main_json))
				return

	print(json.dumps(main_json))


if __name__ == '__main__':
	main()



