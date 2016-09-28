package main

import (
	"golang.org/x/tour/pic"
)

func Pic(dx, dy int) [][]uint8 {
	ret := make([][]uint8, dy) // length: dy
	for i := 0; i < dy; i++ {
		ret[i] = make([]uint8, dx)
		for j := 0; j < dx; j++ {
			ret[i][j] = uint8(i * j) // 计算每个像素的灰度值，这里选用i*j
		}
	}
	return ret
}

func main() {
	pic.Show(Pic)
}
