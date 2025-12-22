# 代码随想录算法训练营74期|单调栈part01

## 题目
| 题目     | Leetcode地址 |
| ----------- | ----------- |
| 739.每日温度| [力扣题目链接](https://leetcode.cn/problems/daily-temperatures/description/)      |
| 496.下一个更大元素 I| [力扣题目链接](https://leetcode.cn/problems/next-greater-element-i/description/)        |
| 503.下一个更大元素 II|[力扣题目链接](https://leetcode.cn/problems/next-greater-element-ii/description/)    |


### 503.下一个更大元素 II

本题和739题相同，需要注意的点在于循环怎么做，一种方法是把数组扩展一倍，然后result再切分为一个数组的长度，另一种方式是直接循环两边数组的长度，然后用取模运算获取下标。
