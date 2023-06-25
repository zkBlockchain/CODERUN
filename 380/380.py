def check_wait_sit(place, row, seats):
    time = 0
    if place == 0:
        if seats[row][place + 1] != '' and seats[row][place + 2] != '':
            time += 15
        elif seats[row][place + 1] != '':
            time += 5
        elif seats[row][place + 2] != '':
            time += 5
    elif place == 1:
        if seats[row][place + 1] != '':
            time += 5
    elif place == 4:
        if seats[row][place - 1] != '':
            time += 5
    elif place == 5:
        if seats[row][place - 1] != '' and seats[row][place - 2] != '':
            time += 15
        elif seats[row][place - 1] != '':
            time += 5
        elif seats[row][place - 2] != '':
            time += 5
    return time


def calculate_time(n, passengers):
    seats = [[''] * 6 for _ in range(30)]

    time = 0
    sits_counter = 0
    while sits_counter != n:
        for i in range(n):
            if not passengers[i]['sit']:
                if passengers[i]['pos'] == passengers[i]['row']:
                    if (passengers[i]['await'] == False):
                        passengers[i]['waits'] += check_wait_sit(passengers[i]['place'], passengers[i]['row'], seats)
                        if passengers[i]['waits'] == 0:
                            seats[passengers[i]['row']][passengers[i]['place']] = i
                            passengers[i]['sit'] = True
                            sits_counter += 1
                        else:
                            passengers[i]['await'] = True
                    else:
                        passengers[i]['waits'] -= 1
                        if passengers[i]['waits'] <= 0:
                            seats[passengers[i]['row']][passengers[i]['place']] = i
                            passengers[i]['sit'] = True
                            sits_counter += 1
                else:
                    criteria_1 = passengers[i - 1]['pos'] == passengers[i]['pos'] + 1
                    criteria_2 = passengers[i - 1]['sit'] == False
                    criteria_3 = passengers[i - 1]['pos'] == -1
                    if i == 0:
                        passengers[i]['pos'] += 1
                        continue
                    if (criteria_1 and criteria_2) or criteria_3:
                        continue
                    else:
                        passengers[i]['pos'] += 1
        if sits_counter != n:
            time += 1
    return time


def main():
    n = int(input())
    passengers = []
    for i in range(n): 
        waits, seat = input().split()
        row, place = int(seat[:-1]) - 1, ord(seat[-1]) - ord('A')
        passengers.append({'row': row, 'place': place, 'pos': -1, 'waits': int(waits), 'await': False, 'sit': False})

    result_time = calculate_time(n, passengers)
    print(result_time)


if __name__ == '__main__':
    main()

