# 代码随想录算法训练营74期|字符串part01

| 题目     | Leetcode地址 |
| ----------- | ----------- |
|344.翻转字符串 | [力扣题目链接](https://leetcode.cn/problems/reverse-string/description/)      |
|541.翻转字符串II| [力扣题目链接](https://leetcode.cn/problems/reverse-string-ii/)      |
|54.替换数字| [卡玛网](https://kamacoder.com/problempage.php?pid=1064)      |

题目较为简单，需要注意的是看输入的类型和返回的类型，如果是str类型的就需要进行str和列表之间的转换
```python
s = "123456"
sList = list(s)
s = ''.join(sList)
```

s.extend(' ' for _ in range(numberNum * 5)),扩充s的大小

## ACM输出
输入和输出需要自己进行定义：
```python
if __name__ == "__main__":
    solution = Solution()

    while True:
        try:
            s = input()
            result = solution.subsitute_numbers(s)
            print(result)
        except EOFError:
            break
```