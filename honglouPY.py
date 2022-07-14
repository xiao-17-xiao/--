# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 12:23:37 2022

@author: XIAOWENYUN
"""
'''
def cf(list1):
    for i in list1:
        counts=list1.count(i)
        if counts > 1:
            return True
    return False
list2=list(input('输入列表元素'))
if cf(list2) == True:
    print("有重复元素")
else:
    print("无重复元素")
'''
'''
def jh(list1):
    list2=set(list1)
    if len(list1)>len(list2):
        return True
    else:
        return False
list2=list(input('输入列表元素'))
if jh(list2) == True:
    print("有重复元素")
else:
    print("无重复元素")
'''
import jieba
excludes={"什么","一个","我们","那里","如今","你们","说道","知道","这里","起来","姑娘","出来","他们","众人","自己","一面",
          "两个","只见","没有","怎么","不是","不知","这个","听见","这样","进来","咱们","太太","告诉","就是","东西","回来","大家",
          "只是","只得","丫头","不敢","这些","出去","所以","不过","姐姐","不好","鸳鸯","过来","不能","的话","一时","心里",
          "银子","如此","今日","几个","二人" ,"答应","还有","一回","只管","那边","这么","说话","不用","外头","自然","打发",
          "小丫头","屋里","罢了","今儿","那些","听说","这话","如何","人家","问道","看见","妹妹"}
txt=open("红楼梦.txt","r",encoding='utf-8').read()
words =jieba.lcut(txt)
counts ={}
for word in words:
    if len(word)==1:
        continue
    elif  word=="奶奶" or word=="老太太":
        rword="贾母"
    elif word=="王夫人" or word=="凤姐儿":
        rword="凤姐"
    else:
        counts[word]=counts.get(word,0)+1
for word in excludes:
    del(counts[word])
items=list(counts.items())
items.sort(key=lambda x:x[1],reverse=True)
for i in range(20):
    word,count=items[i]
    print("{0:<10}{1:>5}".format(word,count))
        
    
