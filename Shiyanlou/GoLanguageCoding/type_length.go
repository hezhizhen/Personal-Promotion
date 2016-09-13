package main

import (
	"fmt"
	"unsafe" // unsafe包含了用于获取Go语言类型信息的方法
)

func main() {
	a := 12
	fmt.Println("length of a: ", unsafe.Sizeof(a))
	var b = 12
	fmt.Println("length of b(int): ", unsafe.Sizeof(b))
	var c int8 = 12
	fmt.Println("length of c(int8): ", unsafe.Sizeof(c))
	var d int16 = 12
	fmt.Println("length of d(int16): ", unsafe.Sizeof(d))
	var e int32 = 12
	fmt.Println("length of e(int32): ", unsafe.Sizeof(e))
	var f int64 = 12
	fmt.Println("lenght of f(int64): ", unsafe.Sizeof(f))
}
