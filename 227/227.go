package main

import "fmt"
// (Just for Fun)
// Failing with Time Limits 250 ms (Just for Fun)
func main() {
    var library_books int64
    fmt.Scan(&library_books)
    var my_books int64
    fmt.Scan(&my_books)
    var week_day int64
    fmt.Scan(&week_day)
    count := 0
    reads := int64(1)
    for {
        if week_day < 6 {
            my_books += library_books
        }
        my_books -= reads
        if my_books < 0 {
            break
        }
        week_day = (week_day % 7) + 1
        count++
        reads++
    }
    fmt.Println(count)
}

