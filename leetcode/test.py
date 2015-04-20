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

