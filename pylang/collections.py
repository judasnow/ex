#!/usr/bin/env python
#coding=utf-8

from collections import Counter

# 分割单词
# re.findall(r'\w+', "word is word")

"""
Counter 接受一个 iterable-or-mapping 统计每一个 item 出现的次数 返回一个 dict

"""

cnt = Counter()
for word in ['red', 'blue', 'red', 'green', 'blue', 'blue']:
    cnt[word] += 1


# 分割单词
# re.findall(r'\w+', "word is word")

print cnt

# 双端队列
# 有序 dict