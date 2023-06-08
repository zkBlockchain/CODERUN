import sys


def main():
    compress_string = sys.stdin.readline().rstrip()
    inputs = int(sys.stdin.readline().rstrip())

    numbers = []
    for _ in range(inputs):
        query_string = sys.stdin.readline().rstrip()
        numbers.append([int(x) for x in query_string.split()])

    counts = ''
    positions = []
    compress_pos = []
    symbols_lengths = []
    symbols_flags = False

    for i in range(len(compress_string)):
        if symbols_flags:
            if (compress_string[i].isdigit()):
                counts += compress_string[i]
            else:
                lens = int(counts)
                
                if len(compress_pos) == 0:
                    starts = 1
                else:
                    starts = positions[-1] + symbols_lengths[-1]

                positions.append(starts)
                symbols_lengths.append(lens)
                compress_pos.append(i - len(counts))

                symbols_flags = False
                counts = ''
        else:
            if (compress_string[i].isdigit()):
                counts += compress_string[i]
                symbols_flags = True
            else:
                if len(compress_pos) == 0:
                    starts, lens = 1, 1
                else:
                    lens = 1
                    starts = positions[-1] + symbols_lengths[-1]

                positions.append(starts)
                symbols_lengths.append(lens)
                compress_pos.append(i - len(counts))

    for nums in numbers:
        if nums[0] == nums[1]:
            sys.stdout.write(str(1) + '\n')
            continue

        array_len = len(positions)

        starts, ends = 0, 0
        is_starts, is_ends = True, True
        
        low_s, low_e = 0, 0
        high_s,  high_e = array_len - 1, array_len - 1

        while is_starts or is_ends: # Binary Searching for Starts & Ends Sections
            mid_s = (low_s + high_s) // 2
            mid_e = (low_e + high_e) // 2

            section_s_s = positions[mid_s]
            section_s_len = symbols_lengths[mid_s]

            if is_starts:
                if (section_s_s + section_s_len) > nums[0] and section_s_s <= nums[0]:
                    starts = mid_s
                    is_starts = False
                    if is_ends == False:
                        break
                elif section_s_s > nums[0]:
                    high_s = mid_s - 1
                else:
                    low_s = mid_s + 1
            
            section_e_s = positions[mid_e]
            section_e_len = symbols_lengths[mid_e]

            if is_ends:
                if (section_e_s + section_e_len) > nums[1] and section_e_s <= nums[1]:
                    ends = mid_e
                    is_ends = False
                    if is_starts == False:
                        break
                elif section_e_s > nums[1]:
                    high_e = mid_e - 1
                else:
                    low_e = mid_e + 1

        first_cut_length = (positions[starts] + symbols_lengths[starts]) - nums[0]
        last_cut_length = (nums[1] + 1 - positions[ends])

        difference = 0
        if positions[starts] == positions[ends]:
            first_cut_length = (nums[1] - nums[0]) + 1
            last_cut_length = 0
        else:
            difference += compress_pos[ends] - compress_pos[starts + 1]

        sum_len_starts = 1
        if first_cut_length != 1 and first_cut_length != 0:
            sum_len_starts = len(str(abs(first_cut_length))) + 1
        
        sum_len_ends = 1
        if last_cut_length != 1 and last_cut_length != 0:
            sum_len_ends = len(str(abs(last_cut_length))) + 1
        elif last_cut_length == 0:
            sum_len_ends = 0

        results = sum_len_starts + difference + sum_len_ends
        sys.stdout.write(str(results) + '\n')


if __name__ == '__main__':
    main()


