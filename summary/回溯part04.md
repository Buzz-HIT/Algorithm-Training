# 代码随想录算法训练营74期|回溯part04
## 题目
| 题目     | Leetcode地址 |
| ----------- | ----------- |
|491.递增子序列 | [力扣题目链接](https://leetcode.cn/problems/increasing-subsequences/)      |
|46. 全排列 | [力扣题目链接](https://leetcode.cn/problems/permutations/)      |
|47. 全排列 II | [力扣题目链接](https://leetcode.cn/problems/permutations-ii/)      |



## 491.递增子序列

本题和子集II类似，也是需要去重的题目，但是不能通过排序去重，所以就要使用set来去重，或者使用used数组来标记

## 46.全排列

本题为什么不能使用startIndex以及used数组为什要传入下一层参数呢，因为全排列，需要的是，没有选取过得元素去进行下一层递归，而不是从startIndex开始选取元素，所以，需要传入used数组来标记选取过的元素，同时，本层选取后，要将used重置。归根结底，还是应该理解在递归搜索树中哪个是本层的变量，哪个是递归的变量，就会迎刃而解。

## 47.全排列 II
本题需要去重，去重的条件是：
(i > 0 and nums[i] == nums[i - 1] and not used[i - 1]):
重点要注意的是，去重的条件中，used[i - 1]必须是False，**表示同一树层中，前一个元素没有被使用过，**才进行去重，如果used[i - 1]是True，表示前一个元素被使用过了，那么本层就可以使用当前元素（已经进入下一层了）。这里需要理解