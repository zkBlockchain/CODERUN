#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

int permutate(int num, int pos_1, int pos_2) {
    string num_str = to_string(num);
    swap(num_str[pos_1], num_str[pos_2]);
    return stoi(num_str);
}

int main() {
    string number;
    cin >> number;
    int k;
    cin >> k;
    vector<int> divisors = {5, 6, 10};
    vector<pair<int, int>> indices;
    for (int i = 0; i < number.size(); i++) {
        for (int j = i + 1; j < number.size(); j++) {
            indices.push_back({i, j});
        }
    }
    vector<int> array_nums = {stoi(number)};
    for (int i = 0; i < k; i++) {
        vector<int> new_array;
        for (int n = 0; n < array_nums.size(); n++) {
            for (auto pair : indices) {
                int new_num = permutate(array_nums[n], pair.first, pair.second);
                new_array.push_back(new_num);
            }
        }
        array_nums.clear();
        array_nums = new_array;
    }
    int counts = 0;
    for (auto item : array_nums) {
        for (auto divisor : divisors) {
            if (item % divisor == 0) {
                counts++;
                break;
            }
        }
    }
    long double probability = (long double)counts / (long double)array_nums.size();
    cout.precision(18);
    cout << probability << endl;
    return 0;
}