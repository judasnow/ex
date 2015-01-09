#!/usr/bin/env python
# coding=utf-8

class M(type):
    
    def __new__(cls, name, bases, classdict):

        for attr in classdict.get('__slots__', ()):
            if not attr.startswith('_'):
                def getter(self, attr=attr):
                    return getattr(self, attr)

                classdict['get' + attr] = getter

        return type.__new__(cls, name, bases, classdict)


class Point(object):
    __metaclass__ = M
    __slots__ = ['x', 'y']


if __name__ == "__main__":
    p = Point()
    print p.getx()


""" 要理解元类 就需要理解 py 程序运行的时候 对象系统的初始化 也就是 class
    对象的构建过程 
    
    拥有 <type 'type'> 类型的 对象在 py 中可以作为其他对象的 类型存在，换句话说就是 可以作为其他 对象 type 的
    对象 称之为 metaclass py 根据 metaclass 来构造 class 对象 也就是说 普通的 class 对象是 metaclass 对象经过
    实例化进行创建的
    
    type 表示的是一种 is_instanceof 的关系 和 __class__ 的效果相同
    
    object 是 type 对象的实例 type 对象继承自 object 对象
    
    对于内置 type 对象中 tp_dict 的填充 完成了 type 对象到 class 对象的转换。
    
    而 tp_dict 是一个 dict_proxy 
    
    type 对象的初始化 过程
    
    1   尝试获取 基类信息
    2   如果基类还没有经过初始化 则 初始化基类 (判断是否存在 tp_dict)
    3   设置 type 信息
    
    具体分析:
    
    1   type 对象的基类就是 object 
"""






