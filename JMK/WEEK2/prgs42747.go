package main

import (
	"fmt"
	"sort"
)

func main() {
	s := []int{20, 19, 18, 17}
	// Reverse sorting
	sort.Sort(sort.Reverse(sort.IntSlice(s)))
	count := 0
	for i, v := range s {
		// index(count) >= element --
		if i < v {
			count++
		} else {
			break
		}
	}
	fmt.Println(count)
}
