支持RE的工具：vi、grep、awk、sed等

## 特殊符号

- [:alnum:] 代表英文大小写字母及数字
- [:alpha:] 代表英文大小写字母
- [:blank:] 代表空格和tab键
- [:cntrl:] 键盘上的控制按键，如CR、LF、TAB、DEL
- [:digit:] 代表数字
- [:graph:] 代表空白字符以外的其他
- [:lower:] 小写字母
- [:print:] 可以被打印出来的任何字符
- [:punct:] 代表标点符号
- [:upper:] 大写字母
- [:space:] 任何会产生空白的字符，如空格、tab、CR等
- [:xdigit:]代表16进制的数字类型

## 使用实例

- grep -n '[[:lower:]]' regular_express.txt # 查找小写字母(-n显示行号)
- grep -n '[[:digit:]]' regular_express.txt # 查找数字

## 语系

使用[A-Z]时，C语系的结果为大写字母A-Z，zh_CN语系的结果为所有字母

我们使用C语系(LANG=C)

## ls应用

- ls a* # 打印以a开头的文件或目录
- ls \*a # 打印以a结尾的文件或目录

## grep应用

- grep -n 'the' regular_express.txt # 查找字符串the
- grep -in 'the' regular_express.txt # -i忽略大小写
- grep -vn 'the' regular_express.txt # -v反向选择，显示没有字符串the的那一行

字符组匹配([]内)

- [abc] # a或b或c
- [0-9] # 0-9中任一数字
- [\u4e00-\u9fa5] # 任一汉字
- [^a1<] # 除a、1、<之外的任一字符
- [^a-z] # 除小写字母外的任一字符

实例

- grep -n 't[ae]st' regular_express.txt # 查找tast或test字符串
- grep -n '^#' regular_express.txt
- grep -n '[^go]oog' regular_express.txt # 查找oog字符串，前面的字符非g或者o
- grep -n '^the' regular_express.txt # 查找行首为the
- grep -n '^[A-Z]' regular_express.txt # 以大写字母开头
- grep -n '[^A-Z]' regular_express.txt # 除了大写字母之外的所有字符中的任一一个
- grep -n 'd$' regular_express.txt # 以d结尾
- grep -n '^$' regular_express.txt # 查找空行
- grep -v '^\$' regular_express.txt | grep -v '\^\#' # '^\$'过滤空行，'^\#'过滤以\#开头的注释行

任意字符与重复字符

- .(小数点)表示任一字符
- \*表示重复前面0或多个字符
- e* 表示具有空字符或者1个以上e字符
- ee* 表示第一个e必须存在，后面是空字符或者1个以上e字符

限定连续字符范围{}

- {}可限制一个范围区间内的重复字符数(在shell中需用转义字符)
- grep -n 'o\\{2\\}' regular_express.txt # 查找连续的2个o，效果同'ooo*'
- grep -n 'go\\{2,5\\}g' regular_express.txt # 查找g后面有2-5个o字符再接g的字符串
- {n,} # 表示n个以上

## sed应用

- nl regular_express.txt | sed '2,5d' # 将regular_express.txt内容打印并显示行号，其中将2-5行删除
- nl regular_express.txt | sed '3d' # 删除第3行
- nl regular_express.txt | sed '3,$d' # 删除第3行到最后一行
- sed -i '1d' regular_express.txt # 在原文件中删除第1行
- nl regular_express.txt | sed '2a test' # 在第2行后添加test字符串
- nl regular_express.txt | sed '2i test' # 在第2行前添加test字符串
- nl regular_express.txt | sed '2a test \n test' # 在第2行后添加两行test
- nl regular_express.txt | sed '2,5c No 2-5 number' # 将2-5行内容替换为No 2-5 number (mac上不行)
- nl regular_express.txt | sed -n '5,7p' # 复制5-7行
- sed 's/被替换字符串/新字符串/g'
- /sbin/ifconfig en0 | grep 'inet ' #空格不能少，获取本机ip的行
- /sbin/ifconfig en0 | grep 'inet ' | sed 's/.inet...://g' | sed 's/..:.\*$//g'

## 扩展RE

- egrep -v '^\$|^#' regular_express.txt # 效果同 grep -v '^\$' regular_express.txt | grep -v '^#'
- grep -E 相当于 egrep
- egrep -n 'go+d' regular_express.txt # grep -n 'goo*d' regular_express.txt (+表示重复一个或多个前一个字符)
- egrep -n 'go?d' regular_express.txt # ？表示重复0或1个前一个字符
- egrep -n 'gd|good' regular_express.txt # 表示用或的方式找出整个字符串
- egrep -n 'g(la|oo)d' regular_express.txt # 搜寻glad或good
- echo 'AxyzxyzxyzxyzC' | egrep 'A(xyz)+C' # 找开头为A结尾为C中间有一个以上xyz的字符串
