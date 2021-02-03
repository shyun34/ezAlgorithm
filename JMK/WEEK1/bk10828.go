package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	s "strings"
)

func main() {
	r := bufio.NewScanner(os.Stdin)
	w := bufio.NewWriter(os.Stdout)
	defer w.Flush()
	r.Scan()
	n, _ := strconv.Atoi(r.Text())

	arr, count := make([]string, n), 0
	for i := 0; i < n; i++ {
		r.Scan()
		str := r.Text()
		strToken := s.Split(str, " ")

		switch strToken[0] {
		case "push":
			arr[count] = strToken[1]
			count++
		case "pop":
			count--
			if count == -1 {
				fmt.Fprintln(w, "-1")
				count++
			} else {
				fmt.Fprintln(w, arr[count])
				arr[count] = ""
			}
		case "top":
			count--
			if count == -1 {
				fmt.Fprintln(w, "-1")
				count++
			} else {
				fmt.Fprintln(w, arr[count])
				count++
			}
		case "size":
			fmt.Fprintln(w, count)
		case "empty":
			if count == 0 {
				fmt.Fprintln(w, 1)
			} else {
				fmt.Fprintln(w, 0)
			}
		}
	}
}
