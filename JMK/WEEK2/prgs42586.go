package main

import (
	"container/list"
	"fmt"
)

func main() {
	progresses := []int{95, 90, 99, 99, 80, 99}
	speeds := []int{1, 1, 1, 1, 1, 1}
	dayList := list.New()
	for i := 0; i < len(progresses); i++ {
		remainWrk := 100 - progresses[i]
		day := remainWrk / speeds[i]
		if remainWrk%speeds[i] != 0 {
			day++
		}
		dayList.PushBack(day)
	}
	var result []int
	for dayList.Len() > 0 {
		e := dayList.Front().Value.(int)
		count := 0

		for dayList.Len() > 0 {
			element := dayList.Front()
			tmpDay := element.Value.(int)
			if tmpDay-e <= 0 {
				count++
				dayList.Remove(element)
			} else {
				break
			}
		}
		result = append(result, count)
	}

	fmt.Println(result)
}
