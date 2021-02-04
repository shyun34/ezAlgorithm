package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	r := bufio.NewScanner(os.Stdin)
	w := bufio.NewWriter(os.Stdout)
	defer w.Flush()

	r.Scan()
	str := r.Text()
	strToken := strings.Split(str, " ")
	n, _ := strconv.Atoi(strToken[0])
	k, _ := strconv.Atoi(strToken[1])

	originArr := []string{}
	for i := 0; i < n; i++ {
		originArr = append(originArr, strconv.Itoa(i+1))
	}

	point := 0
	newArr := []string{}
	// origin Array 크기 자체에 대한 변화 없이 작성. -- O(n^2). time complexity < memory complexity
	/* for i := 0; i < n; i++ {
		count := k
		for count > 0 {
			if originArr[point] != "" {
				count--
			}
			point++
			point %= n
		}
		point--
		if point == -1 {
			point = n - 1
		}

		newArr[i] = originArr[point]
		originArr[point] = ""
	} */

	// origin array 길이 조절. -- O(n) time complexity > memory complexity
	for len(originArr) > 0 {
		point = (point + k - 1) % len(originArr)
		newArr = append(newArr, originArr[point])
		originArr = append(originArr[:point], originArr[point+1:]...)
	}

	fmt.Fprintf(w, "<"+strings.Join(newArr, ", ")+">")
}
