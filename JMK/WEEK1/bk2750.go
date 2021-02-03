package main

import (
	"fmt"
	"os"
	"bufio"
	"strconv"
)

func bk2750()  {
	r := bufio.NewScanner(os.Stdin)
	w := bufio.NewWriter(os.Stdout)

	defer w.Flush()
	r.Scan()
	n, _ := strconv.Atoi(r.Text())

	arr := make([]int, n)
	// input value to array
	for i:= 0; i < n; i++{
		r.Scan()
		tmp, err := strconv.Atoi(r.Text())
		if err != nil {
			break
		}
		arr[i] = tmp
	}
	// bubble sort
	for i := 0; i < n-1; i++ {
		for j := 0; j < n-1-i; j++ {
			if arr[j] > arr[j+1] {
				arr[j], arr[j+1] = arr[j+1], arr[j]
			}
		}
	}
	// print
	for _, v := range arr {
		fmt.Fprintln(w, v)
	}

}