package main

import (
    "fmt"
    "strconv"
)

func permutate(num int, pos_1 int, pos_2 int) int {
    numStr := strconv.Itoa(num)
    numArr := []rune(numStr)
    numArr[pos_1], numArr[pos_2] = numArr[pos_2], numArr[pos_1]
    newNumStr := string(numArr)
    newNum, _ := strconv.Atoi(newNumStr)
    return newNum
}

func main() {
    var number string
    fmt.Scan(&number)
    var k int
    fmt.Scan(&k)
    divisors := []int{5, 6, 10}
    indices := [][]int{}
    for i := 0; i < len(number); i++ {
        for j := i + 1; j < len(number); j++ {
            indices = append(indices, []int{i, j})
        }
    }
    arrayNums := []int{}
    num, _ := strconv.Atoi(number)
    arrayNums = append(arrayNums, num)
    for i := 0; i < k; i++ {
        newArray := []int{}
        for _, n := range arrayNums {
            for _, pair := range indices {
                newNum := permutate(n, pair[0], pair[1])
                newArray = append(newArray, newNum)
            }
        }
        arrayNums = newArray
    }
    counts := 0
    for _, item := range arrayNums {
        for _, divisor := range divisors {
            if item % divisor == 0 {
                counts += 1
                break
            }
        }
    }
    probability := float64(counts) / float64(len(arrayNums))
    fmt.Println(probability)
}