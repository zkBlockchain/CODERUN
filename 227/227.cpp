#include<iostream>

using namespace std;

// Failing with Time Limits 250 ms
int main()
{
	long library_books; cin >> library_books;
	long my_books; cin >> my_books;
	long week_day; cin >> week_day;

	long count = 0;
	long reads = 1;
	
	if ((week_day == 6 || week_day == 7) && (my_books == 0)){
		cout << 0;
		return 0;
	}

	if (week_day == 6 && (my_books == 1 || my_books == 2)) {
		cout << 1;
		return 0;
	}

	while (true) {
		if (week_day < 6) {
			my_books += library_books;
		}
		my_books = my_books - reads;

		if (my_books < 0) {
			break;
		}

		week_day = (week_day % 7) + 1;
		count++;
		reads++;
	}

	cout << count;
	return 0;
}


