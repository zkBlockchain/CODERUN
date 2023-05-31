import heapq


def main():
    N, M, Q = map(int, input().split()) # N - DCentres, M - Servers, Q - Queries

    # Arrays:
    active = [M] * N # Every Online (From Starts)
    offline = [0] * N # No Offline (From Starts)
    restarts = [0] * N # No Restarts (From Starts)
    products = [0] * N # No Multiplication Info (From Starts)
    
    # Heaps: 
    min_values = [(0, i) for i in range(N)] # Generating pairs for min values
    max_values = [(0, i) for i in range(N)] # Generating pairs for max values
    
    for _ in range(Q):
        query, *cs = input().split() # Getting query, DC & Server numbers

        if query == 'RESET':
            center = int(cs[0]) # Getting Center for resetting
            i = center - 1 # Arrays starting from 0
            restarts[i] += 1 # Incrementing array of resets for center with i number
            offline[i] = 0 # This server is online after resetting
            active[i] = M # Whole center is online after resetting

            products[i] = restarts[i] * active[i] # Counting for our multiplications
            heapq.heappush(min_values, (products[i], i)) # Add info to heap for min values
            heapq.heappush(max_values, (-products[i], i)) # Add info to heap for max values

        elif query == 'DISABLE':
            center, server = map(int, cs) # Getting Center & Server for Disabling
            c, s = center - 1, server - 1 # Arrays starting from 0
            shifts = 1 << s # Make shifts for server Number (Using Bitwise Operations for Faster results)

            if offline[c] & shifts: continue # Skipping if Already Offline
            products[c] -= restarts[c] # Updating Multiplication Values for current center
            offline[c] |= shifts # Updating Offline Array Values
            active[c] -= 1 # Decrementing Active Servers

            heapq.heappush(min_values, (products[c], c)) # Add info to heap for min values
            heapq.heappush(max_values, (-products[c], c)) # Add info to heap for max values

        elif query == 'GETMAX':
            while -max_values[0][0] != products[max_values[0][1]]: # Searching for MAX multiplication value
                heapq.heappop(max_values) # Remove from Heap less values until getting MAX
            
            print(max_values[0][1] + 1) # Outing Results

        elif query == 'GETMIN':
            while min_values[0][0] != products[min_values[0][1]]: # Searching for MIN multiplication value
                heapq.heappop(min_values) # Remove from Heap big values until getting MIN

            print(min_values[0][1] + 1) # Outing Results


if __name__ == '__main__':
    main()

