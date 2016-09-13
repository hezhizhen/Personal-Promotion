package main // 表明当前源文件属于main包

import ( // 导入的包。若导入的包没有使用，则编译失败
	"fmt"
	"os"
)

func main() {
	target := "World"     // 声明并初始化
	if len(os.Args) > 1 { /*os.Args是一个参数切片 */
		target = os.Args[1]
	}
	fmt.Println("Hello", target)
}
