def generate_array(n, m):
	centres = []

	for c in range(1, n + 1):
		servers = []
		for s in range(1, m + 1):
			servers.append([s, 1])

		current_server = [c, m, 0, servers]
		centres.append(current_server)

	return centres


def reset(center):
	global M, status_array
	status_array[center - 1][1] = M
	status_array[center - 1][2] += 1

	for s in range(M):
		status_array[center - 1][3][s][1] = 1
	return


def disable(center, server):
	global M, status_array
	for servers in status_array:
		if servers[0] == center:
			for s in range(M):
				if servers[3][s][0] == server:
					if servers[3][s][1] == 1:
						servers[1] -= 1
						servers[3][s][1] = 0
						return


def getmax():
	global status_array
	max_value = -1

	for servers in status_array:
		Ri = servers[1]
		Ai = servers[2]
		result = Ri * Ai

		if max_value < result:
			max_value = result
			server = servers[0]
			
	print(server)
	return


def getmin():
	global status_array
	min_value = 10**8
	server = 1

	for servers in status_array:
		Ri = servers[1]
		Ai = servers[2]
		result = Ri * Ai

		if min_value > Ri * Ai:
			min_value = result
			server = servers[0]

	print(server)
	return


N, M, Q = map(int, input().split())
status_array = generate_array(N, M)

for _ in range(Q):
	query, *cs = input().split()

	if query == 'DISABLE':
		center, server = map(int, cs)
		disable(center, server)

	elif query == 'RESET':
		center = int(cs[0])
		reset(center)

	elif query == 'GETMAX':
		getmax()

	elif query == 'GETMIN':
		getmin()