package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
	"strings"
)

func main() {
	r := bufio.NewReader(os.Stdin)
	w := bufio.NewWriter(os.Stdout)
	defer w.Flush()

	str, _ := r.ReadString('\n')
	strToken := strings.Fields(str)
	nums := make([]int, len(strToken))

	for i := 0; i < len(strToken); i++ {
		nums[i], _ = strconv.Atoi(strToken[i])
	}

	sort.Ints(nums)
	min, max := nums[0], nums[len(nums)-1]
	s := strconv.Itoa(min) + " " + strconv.Itoa(max)
	fmt.Fprintln(w, s)
}
