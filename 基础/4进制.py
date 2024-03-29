#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2022/12/27 17:18
# @Author : puchen
# @File : 4进制.py

'''
二进制：0 1
八进制： 01234567
十进制： 0-9
十六进制 0-9 A-F

十进制转二进制
10 -->  取余数 1010

十进制转八进制   除8求余数 反着写


'''

# 转二进制
n = 149
result = bin(n)  # binary
print(result)

# 转八进制
result = oct(n)
print(result)

# 转十六进制  --221

c = 221
result = hex(c)
print(result)

# 前缀 ：0b 二进制 bin()  0o 八进制  oct() 0x 十六进制 hex()

a = 0x558

print(int(a))
print(bin(a))  # 十六进制  向二进制转换  无论当前参数是几进制
print(oct(a))

# 0x 558 #--> 二进制
# 0x558
#     5    5    8
# ob 1101 0101 1000

# 已知二进制转成十六进制，将二进制从右侧开始4位一组  最后不足一位补0就可以了
# 已知二进制转成八进制，将二进制从右侧开始3位一组  最后不足一位补0就可以了


'''
针对二进制的运算  1为真 0为假  都是二进制上下运算
& 按位与运算符  类似 and 
| 按位或运算符  类似 or
^ 按位异或运算符  相同为假 不同为真
~ 按位取反运算符
<< 左移运算符
>> 右移运算符
'''

n1 = 0b0110
n2 = 0b0010

print(n1 & n2)  # 0b 0010  上下进行与运算   最终结果会转成10进制

print(5 & 9)
print(5 | 9)
print(5 ^ 9)

print(~n1)

# 1byte  = 8bit  整形占4个字节  32个bit位

n = 2  # 占32个bit位

# 二进制的负数怎么表示

# 原码  0110
# 反码  1001
# 补码  1010

'''

1 已知十进制的负数，求二进制负数
    1 正数的原码  2原码取反  3 加1  --->得到的二进制的就是负数的二进制
    -7的进制
        步骤
        1。先求+7的二进制： 0000 0111 原码
        2。反码 1111 1000
        3.补码  1111 1001
        -7的二进制就是：1111 1001 
2 已知二进制的负数，判断是否是负数的二进制的依据，看二进制的最高位，  1111 1010 ，  最高位位1则为负数，最高位位0则为正数
已知求对应的的十进制
        1 二进制（负数）  2 二进制减1 3  取反  4 原码 将原码转成十进制，在十进制的前面添加负号-
3 ~5 ---> 就是将5的二进制取反
'''
print(bin(7))
print(bin(~7))
print(bin(~-7))

# 位运算的移动  都是针对二进制说的

n = 12

# 0000 1100 n<<2  往左边移动两位 0011 0000  就是48  n>>2  往右边边移动两位 0000 0011  就是3

print(n << 2)
print(n >> 2)

##boolean在算术运算符里面按照0来处理
