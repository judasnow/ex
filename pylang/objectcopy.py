#!/usr/bin/env python
#coding=utf-8

import copy

class Foo: pass

a = [Foo(), Foo()]
b = copy.copy(a)

# 普通的 copy 没有递归的处理 list 中的元素
print map(lambda x: id(x), a)
print map(lambda x: id(x), b)

# 深度 copy 引用的 object 全部重建
c = copy.deepcopy(a)
print map(lambda x: id(x), c)

print a == b
print a is b


# 不可变对象没有必要存在副本
# 因此 copy 对其是没有意义的

d = "123"
f = copy.copy(d)

print id(d), id(f)

# lisp 切片可以造成浅 copy
q = [1,2,4]
r = q[:]
s = list(q)

print id(q), id(r), id(s)

# 还是一个隐藏的引用问题
mul = [[0] * 5] * 3
mul[0][0] = "1024"
print mul

mul2 = [[0] * 5 for row in range(10)]
mul[0][0] = "1024"
print mul2

