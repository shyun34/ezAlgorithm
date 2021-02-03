package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
	s "strings"
)

func bk7785() {
	r := bufio.NewScanner(os.Stdin)
	w := bufio.NewWriter(os.Stdout)
	defer w.Flush()

	r.Scan()
	n, _ := strconv.Atoi(r.Text())

	m := make(map[string]string)
	for i := 0; i < n; i++ {
		r.Scan()
		str := r.Text()
		strToken := s.Split(str, " ")
		m[strToken[0]] = strToken[1]
	}
	arr := make([]string, n)
	count := 0
	for key, val := range m {
		if val == "enter" {
			arr[count] = key
			count++
		}
	}

	s := arr[:count]
	sort.Slice(s, func(i, j int) bool {
		return s[i] > s[j]
	})

	for _, v := range s {
		fmt.Fprintln(w, v)
	}
}
