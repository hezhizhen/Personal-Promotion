package main

import (
	"fmt"
)

// 通过\uhhhh的方式创建Unicode字符
func main() {
	t0 := "\u6B22\u8FCE\u6765\u5230" // 欢迎来到
	t1 := "\u5B9E\u9A8C\u697C"       //实验楼
	t2 := t0 + t1
	for index, char := range t2 { // 通过range对Unicode字符串t2中的每一个unicode字符依次操作
		fmt.Printf("%-2d    %U    '%c'    %X    %d\n",
			index, char, char, []byte(string(char)), len([]byte(string(char)))) // 每个字符在t2中的位置，每个字符的Unicode码值，每个字符的字面量，每个字符的16进制值，每个字符的字节长度
	}
	fmt.Printf("length of t0: %d, t1: %d, t2: %d\n", len(t0), len(t1), len(t2))
	fmt.Printf("content of t2[0:2] is %X\n", t2[0:2])
}
