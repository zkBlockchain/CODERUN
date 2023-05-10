#include <iostream>
#include <algorithm>
#include <vector>
#include <cmath>
using namespace std; 

// Time Limits (Easy but long Solution)
int main() 
{
    long summary = 0;
    long sizeofarray;
    cin >> sizeofarray;

    vector <long> num_array;
    for (long i = 0; i < sizeofarray; ++i)
    {
        long temp_value;
        cin >> temp_value;
        num_array.emplace_back(temp_value);
    }
    
    for (long i = 1; i < sizeofarray + 1; i++) {
        vector <long> elem_lists;
        for (long s = 0; s < i; s++) {
            elem_lists.emplace_back(num_array[s]);
        }

        sort(elem_lists.begin(), elem_lists.end());
        summary += elem_lists[(long)(ceil(i / 2.0) - 1)];
    }

    cout << summary << "\n";
    return 0;
}



