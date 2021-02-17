package main

import (
	"fmt"
	"sort"
	"strconv"
)

type Pair struct {
	Key   string
	Value int
}

type PairList []Pair

func (p PairList) Len() int           { return len(p) }
func (p PairList) Less(i, j int) bool { return p[i].Value < p[j].Value }
func (p PairList) Swap(i, j int)      { p[i], p[j] = p[j], p[i] }

func main() {
	genres := []string{
		"classic",
		"pop",
		"classic",
		"pop",
		"classic",
		"classic",
	}
	plays := []int{400, 600, 150, 600, 500, 500}

	fmt.Println(solutions(genres, plays))
}

func solutions(genres []string, plays []int) []int {
	m := make(map[string]int)
	// Genres total
	for i := 0; i < len(genres); i++ {
		genre := genres[i]
		play := m[genre]
		m[genre] = play + plays[i]
	}
	// sort genres
	genresTotalSort := descendingOrderMap(m)

	result := []int{}

	for i := 0; i < genresTotalSort.Len(); i++ {
		tmp := make(map[string]int)
		// get index, element for each genre
		for j := 0; j < len(genres); j++ {
			if genresTotalSort[i].Key == genres[j] {
				str := strconv.Itoa(j)
				tmp[str] = plays[j]
			}
		}
		// sort
		genreSort := descendingOrderMap(tmp)
		// get 0, 1
		if genreSort.Len() > 1 {
			for x := 0; x < 2; x++ {
				tmpValue, _ := strconv.Atoi(genreSort[x].Key)
				result = append(result, tmpValue)
			}
		} else {
			tmpValue, _ := strconv.Atoi(genreSort[0].Key)
			result = append(result, tmpValue)
		}
	}
	return result
}

// Map sort through Value
func descendingOrderMap(pairMap map[string]int) PairList {
	pl := make(PairList, len(pairMap))
	i := 0

	for k, v := range pairMap {
		pl[i] = Pair{k, v}
		i++
	}
	sort.Sort(sort.Reverse(pl))
	return pl
}
