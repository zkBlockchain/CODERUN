package main

import (
	"fmt"
	"strconv"
)

func main() {
	var compress_string string
	fmt.Scanln(&compress_string)

	counts := ""
	positions := []int{}
	compress_pos := []int{}
	symbols_lengths := []int{}
	symbols_flags := false

	for i := 0; i < len(compress_string); i++ {
		if symbols_flags {
			if compress_string[i] >= '0' && compress_string[i] <= '9' {
				counts += string(compress_string[i])
			} else {
				lens, _ := strconv.Atoi(counts)

				if len(compress_pos) == 0 {
					starts := 1
					positions = append(positions, starts)
				} else {
					starts := positions[len(positions)-1] + symbols_lengths[len(symbols_lengths)-1]
					positions = append(positions, starts)
				}

				symbols_lengths = append(symbols_lengths, lens)
				compress_pos = append(compress_pos, i-len(counts))

				symbols_flags = false
				counts = ""
			}
		} else {
			if compress_string[i] >= '0' && compress_string[i] <= '9' {
				counts += string(compress_string[i])
				symbols_flags = true
			} else {
				lens := 1
				if len(compress_pos) == 0 {
					starts := 1

					positions = append(positions, starts)
				} else {
					starts := positions[len(positions)-1] + symbols_lengths[len(symbols_lengths)-1]
					positions = append(positions, starts)
				}

				symbols_lengths = append(symbols_lengths, lens)
				compress_pos = append(compress_pos, i-len(counts))
			}
		}
	}

	var inputs int
	fmt.Scanln(&inputs)

	numbers := make([][2]int, inputs)
	for i := 0; i < inputs; i++ {
		var query [2]int
		fmt.Scanln(&query[0], &query[1])
		numbers[i] = query
	}

	for _, nums := range numbers {
		if nums[0] == nums[1] {
			fmt.Println(1)
			continue
		}

		array_len := len(positions)

		starts, ends := 0, 0
		is_starts, is_ends := true, true

		low_s, low_e := 0, 0
		high_s, high_e := array_len-1, array_len-1

		for is_starts || is_ends { // Binary Searching for Starts & Ends Sections
			mid_s := (low_s + high_s) / 2
			mid_e := (low_e + high_e) / 2

			section_s_s := positions[mid_s]
			section_s_len := symbols_lengths[mid_s]

			if is_starts {
				if (section_s_s+section_s_len) > nums[0] && section_s_s <= nums[0] {
					starts = mid_s
					is_starts = false
					if !is_ends {
						break
					}
				} else if section_s_s > nums[0] {
					high_s = mid_s - 1
				} else {
					low_s = mid_s + 1
				}
			}

			section_e_s := positions[mid_e]
			section_e_len := symbols_lengths[mid_e]

			if is_ends {
				if (section_e_s+section_e_len) > nums[1] && section_e_s <= nums[1] {
					ends = mid_e
					is_ends = false
					if !is_starts {
						break
					}
				} else if section_e_s > nums[1] {
					high_e = mid_e - 1
				} else {
					low_e = mid_e + 1
				}
			}
		}

		first_cut_length := (positions[starts] + symbols_lengths[starts]) - nums[0]
		last_cut_length := (nums[1] + 1 - positions[ends])

		difference := 0
		if positions[starts] == positions[ends] {
			difference = 0
			first_cut_length = (nums[1] - nums[0]) + 1
			last_cut_length = 0

		} else {
			difference = compress_pos[ends] - compress_pos[starts+1]
		}

		sum_len_starts := 1
		if first_cut_length != 1 {
			sum_len_starts = len(strconv.Itoa(first_cut_length)) + 1
		}

		sum_len_ends := 1
		if last_cut_length != 1 && last_cut_length != 0 {
			sum_len_ends = len(strconv.Itoa(last_cut_length)) + 1
		} else if last_cut_length == 0 {
			sum_len_ends = 0
		}

		results := sum_len_starts + difference + sum_len_ends
		fmt.Println(results)
	}
}
