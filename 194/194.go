package main

import (
	"bufio"
	"fmt"
	"os"
)

func bfs(graph [][][2]int, color []int, maxWeight int, vertex int) bool {
	queue := []int{vertex}
	color[vertex] = 1
	l := 0
	for l != len(queue) {
		v := queue[l]
		l++
		for _, uw := range graph[v] {
			u, w := uw[0], uw[1]
			if w > maxWeight {
				continue
			}
			if color[u] == 0 {
				color[u] = 3 - color[v]
				queue = append(queue, u)
			} else if color[v] == color[u] {
				return false
			}
		}
	}
	return true
}

func check(graph [][][2]int, maxWeight int) bool {
	color := make([]int, len(graph))
	for i := range graph {
		if color[i] == 0 && !bfs(graph, color, maxWeight, i) {
			return false
		}
	}
	return true
}

func main() {
	var n, m int
	fmt.Scan(&n, &m)
	edges := make([][3]int, m)
	scanner := bufio.NewScanner(os.Stdin)
	for i := 0; i < m; i++ {
		scanner.Scan()
		fmt.Sscanf(scanner.Text(), "%d %d %d", &edges[i][0], &edges[i][1], &edges[i][2])
	}
	graph := make([][][2]int, n)
	maxWeight := 0
	for _, edge := range edges {
		v, u, w := edge[0]-1, edge[1]-1, edge[2]
		graph[v] = append(graph[v], [2]int{u, w})
		graph[u] = append(graph[u], [2]int{v, w})
		if w > maxWeight {
			maxWeight = w
		}
	}
	if check(graph, maxWeight) {
		fmt.Println(maxWeight)
		return
	}
	left := 0
	right := maxWeight + 1
	for right-left > 1 {
		mid := (left + right) / 2
		if check(graph, mid) {
			left = mid
		} else {
			right = mid
		}
	}
	fmt.Println(right)
}
