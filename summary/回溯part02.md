# 代码随想录算法训练营74期|回溯part02

## 题目

| 题目     | Leetcode地址 |
| ----------- | ----------- |
| 39.组合总和 | [力扣题目链接](https://leetcode.cn/problems/combination-sum/)      |
| 40.组合总和 II | [力扣题目链接](https://leetcode.cn/problems/combination-sum-ii/)      |
| 131.分割回文串 | [力扣题目链接](https://leetcode.cn/problems/palindrome-partitioning/)      |



### 39.组合总和

不变的数组的长度，变的是加和的值
因为可以重复取值，那么startIndex就不需要+1，为什么不从0开始取值呢？因为会有重复解，从i开始取可以保证i之前的数都不会再取到，从而避免重复解。
同时，这样的取值要加一个>target的判断。否则会无限递归下去。