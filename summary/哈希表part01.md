# 代码随想录算法训练营74期|哈希表part01 
## [哈希表理论基础](https://programmercarl.com/%E5%93%88%E5%B8%8C%E8%A1%A8%E7%90%86%E8%AE%BA%E5%9F%BA%E7%A1%80.html#%E5%93%88%E5%B8%8C%E5%87%BD%E6%95%B0)
### 哈希表
哈希表也称散列表，**一般用来快速判断一个元素是否出现在在集合里面**（通过关键索引即可通过O（1）的时间复杂度去映射对应的元素
### 哈希函数
有些哈希表查找的值并不是哈希表的直接索引，需要一个函数来进行映射，这种函数为哈希函数
### 哈希碰撞
哈希表有时候会出现同一个index对应多个值的情况，这种情况被称为哈希碰撞
为了解决哈希碰撞，目前主流的有两种方法：
1.拉链法：
每一个哈希索引后面跟着一整个链表
![alt text](image.png)
拉链法的关键在于选择适当的哈希表的大小，从而保证既不会因为数组空值浪费大量内存，也不会因为链表太长是时间复杂度退化到O(n)
2.线性探测法
一定要保证tablesize>datasize, 即利用空位去放置哈希碰撞的元素对应哈希表的三种结构
一般会选择数组，集合，字典（map，映射）来使用哈希法，这三种实现的底层逻辑不同：
### 总结
当遇到在集合中快速判断或者选择一个元素时，就要考虑哈希表（空间换时间）

## 哈希表题目

| 题目     | Leetcode地址 |
| ----------- | ----------- |
| 242.有效字母的异位词| [力扣题目链接](https://leetcode.cn/problems/valid-anagram/)      |
| 383.赎金信| [力扣题目链接](https://leetcode.cn/problems/ransom-note/)      |
| 49.字母异位词分组| [力扣题目链接](https://leetcode.cn/problems/find-all-anagrams-in-a-string/description/)      |
| 438.找到字符串中所有字母的异位词| [力扣题目链接](https://leetcode.cn/problems/find-all-anagrams-in-a-string/)      |
| 349.两个数组的交集| [力扣题目链接](https://leetcode.cn/problems/intersection-of-two-arrays/description/)      |
| 350.两个数组的交集II| [力扣题目链接](https://leetcode.cn/problems/intersection-of-two-arrays-ii/)      |
| 202.快乐数| [力扣题目链接](https://leetcode.cn/problems/happy-number/)      |
| 1.两数之和| [力扣题目链接](https://leetcode.cn/problems/two-sum/)      |

### 题目总结

除了第438题外基本上没有什么题目思路上的问题，438题一开始的思路是滑动窗口，快指针先动，满足条件后，慢指针再动，找到最小的窗口，后来发现题目要求是**求异位词子串，而不是包含所有字符的子串，也就是说异位词子串长度应该是相等的**，所以窗口长度固定即可，就更为简单

### python数据结构使用指南

今天更多地学到了python数据结构的一些用法，正好最近也在选python，正好做一下总结：
python的基本数据结构为list，set，dict，tuple,
其中，list和dict可做映射，set可做不重复元素的统计。
dict初始化可以使用get函数，即
```python
dict[index] = dict.get(index, 0) + 1
```
除了上述的四种基本数据结构，在collection类中还定义了其他数据结构：
namedtuple()：创建具有命名字段的元组子类的工厂函数。
```python
from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(11, y=22)
print(p.x + p.y) # 输出: 33
```
deque：类似列表的容器(双向队列)，支持在两端快速添加和弹出元素。
```python
from collections import deque
d = deque('ghi') # 创建带有三个元素的deque
for elem in d: # 遍历deque的元素
   print(elem.upper())
```
ChainMap：类似字典的类，用于创建多个映射的单个视图。
```python
from collections import ChainMap
baseline = {'music': 'bach', 'art': 'rembrandt'}
adjustments = {'art': 'van gogh', 'opera': 'carmen'}
combined = ChainMap(adjustments, baseline)
print(combined['art']) # 输出: 'van gogh'
```
Counter：用于计数可哈希对象的字典子类。
```python
from collections import Counter
cnt = Counter()
for word in ['red', 'blue', 'red', 'green', 'blue', 'blue']:
   cnt[word] += 1
print(cnt) # 输出: Counter({'blue': 3, 'red': 2, 'green': 1})
```
OrderedDict：记住元素添加顺序的字典子类。
```python
from collections import OrderedDict
od = OrderedDict()
od['a'] = 1
od['b'] = 2
od['c'] = 3
od['d'] = 4
for key, value in od.items():
   print(key, value)
```
defaultdict：在查询缺失键时调用工厂函数提供默认值的字典子类。
```python
from collections import defaultdict
s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
d = defaultdict(list)
for k, v in s:
   d[k].append(v)
print(sorted(d.items()))
```
此外，UserDict、UserList、UserString：分别围绕字典、列表、字符串对象的包装器，便于子类化。
