#include <iostream> 
using namespace std; 

int main() 
{
    int sizeofarray;
    cin >> sizeofarray;

    int num_array[sizeofarray];
    for (int i = 0; i < sizeofarray; ++i)
    {
        cin >> num_array[i];
    }

    int unique = 0;
    for (int i = 0; i < sizeofarray; i++) {
        int flags = 0;
        for (int s = 0; s < sizeofarray; s++) {
            if (i != s && num_array[i] == num_array[s]) {
                flags = 1;
                break;
            }
        }
        if (flags == 0) {
            unique++;
        }
    }

    cout << unique;

    return 0;
}