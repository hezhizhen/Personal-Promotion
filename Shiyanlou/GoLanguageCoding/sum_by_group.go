package main

import "fmt"

func sum(a []int, result chan int) {
	sum := 0
	for _, v := range a {
		sum += v
	}
	result <- sum // 若result是一个channel：将数据sum发送到result
}

func main() {
	a := []int{2, 3, 5, 6, 10, -5, 1, 0} // 声明了一个int类型的切片a
	result := make(chan int)             // 创建了一个int类型的channel
	go sum(a[:len(a)/2], result)         // 执行goroutine，计算切片a前半部分的和
	go sum(a[len(a)/2:], result)         // 执行goroutine，计算切片a后半部分的和
	x, y := <-result, <-result           // 若result是channel：从result中接收一个数据。main函数会阻塞至直到能从channel result中接收到数据

	fmt.Println(x, y, x+y)
}
