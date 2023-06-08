#include <iostream>
#include <vector>
#include <string>
#include <sstream>


int main() {
    std::string compress_string;
    std::getline(std::cin, compress_string);

    int inputs;
    std::cin >> inputs;
    std::cin.ignore();

    std::vector<std::vector<int>> numbers(inputs);
    for (int i = 0; i < inputs; i++) {
        std::string query_string;
        std::getline(std::cin, query_string);
        std::istringstream iss(query_string);

        std::string num;
        while (iss >> num) {
            int query_num = std::stoi(num);
            numbers[i].push_back(query_num);
        }
    }

    std::string counts;
    std::vector<int> positions;
    std::vector<int> compress_pos;
    std::vector<int> symbols_lengths;
    bool symbols_flags = false;

    for (int i = 0; i < compress_string.length(); i++) {
        if (symbols_flags) {
            if (compress_string[i] >= '0' && compress_string[i] <= '9') {
                counts += compress_string[i];
            } else {
                int lens = std::stoi(counts);

                if (compress_pos.empty()) {
                    int starts = 1;
                    positions.push_back(starts);
                } else {
                    int starts = positions[positions.size() - 1] + symbols_lengths[symbols_lengths.size() - 1];
                    positions.push_back(starts);
                }

                symbols_lengths.push_back(lens);
                compress_pos.push_back(i - counts.length());

                symbols_flags = false;
                counts = "";
            }
        } else {
            if (compress_string[i] >= '0' && compress_string[i] <= '9') {
                counts += compress_string[i];
                symbols_flags = true;
            } else {
                int lens = 1;
                if (compress_pos.empty()) {
                    int starts = 1;
                    positions.push_back(starts);
                } else {
                    int starts = positions[positions.size() - 1] + symbols_lengths[symbols_lengths.size() - 1];
                    positions.push_back(starts);
                }

                symbols_lengths.push_back(lens);
                compress_pos.push_back(i - counts.length());
            }
        }
    }

    for (const auto& nums : numbers) {
        int array_len = positions.size();

        int starts = 0, ends = 0;
        bool is_starts = true, is_ends = true;

        int low_s = 0, low_e = 0;
        int high_s = array_len - 1, high_e = array_len - 1;

        while (is_starts || is_ends) {
            int mid_s = (low_s + high_s) / 2;
            int mid_e = (low_e + high_e) / 2;

            int section_s_s = positions[mid_s];
            int section_s_len = symbols_lengths[mid_s];

            if (is_starts) {
                if ((section_s_s + section_s_len) > nums[0] && section_s_s <= nums[0]) {
                    starts = mid_s;
                    is_starts = false;
                    if (!is_ends) {
                        break;
                    }
                } else if (section_s_s > nums[0]) {
                    high_s = mid_s - 1;
                } else {
                    low_s = mid_s + 1;
                }
            }

            int section_e_s = positions[mid_e];
            int section_e_len = symbols_lengths[mid_e];

            if (is_ends) {
                if ((section_e_s + section_e_len) > nums[1] && section_e_s <= nums[1]) {
                    ends = mid_e;
                    is_ends = false;
                    if (!is_starts) {
                        break;
                    }
                } else if (section_e_s > nums[1]) {
                    high_e = mid_e - 1;
                } else {
                    low_e = mid_e + 1;
                }
            }
        }

        if (nums[0] == nums[1]) {
            std::cout << 1 << std::endl;
            continue;
        }

        int first_cut_length = (positions[starts] + symbols_lengths[starts]) - nums[0];
        int last_cut_length = (nums[1] + 1 - positions[ends]);

        int difference = 0;
        if (positions[starts] == positions[ends]) {
            first_cut_length = (nums[1] - nums[0]) + 1;
            last_cut_length = 0;
        } else {
            difference = compress_pos[ends] - compress_pos[starts + 1];
        }

        int sum_len_starts = 1;
        if (first_cut_length != 1 && first_cut_length != 0) {
            sum_len_starts = std::to_string(first_cut_length).length() + 1;
        }

        int sum_len_ends = 1;
        if (last_cut_length != 1 && last_cut_length != 0) {
            sum_len_ends = std::to_string(last_cut_length).length() + 1;
        } else if (last_cut_length == 0) {
            sum_len_ends = 0;
        }

        int results = sum_len_starts + difference + sum_len_ends;
        std::cout << results << std::endl;
    }

    return 0;
}



