package main

import (
	"strings"

	"golang.org/x/tour/wc"
)

func WordCount(s string) map[string]int {
	ret := make(map[string]int)
	strs := strings.Fields(s)
	length := len(strs)
	for i := 0; i < length; i++ {
		ret[strs[i]]++
	}
	return ret
}

func main() {
	wc.Test(WordCount)
}
