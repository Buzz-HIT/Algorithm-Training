# 代码随想录算法训练营74期|二叉树part05

## Leetcode题目
| 题目     | Leetcode地址 |
| ----------- | ----------- |
| 654.最大二叉树| [力扣题目链接](https://leetcode.cn/problems/maximum-binary-tree/description/)    |
| 617. 合并二叉树| [力扣题目链接](https://leetcode.cn/problems/merge-two-binary-trees/description/)      |
| 700.二叉搜索树中的搜索| [力扣题目链接](https://leetcode.cn/problems/path-sum-ii/description/)      |
| 98.验证二叉搜索树| [力扣题目链接](https://leetcode.cn/problems/validate-binary-search-tree/description/)      |


验证二叉搜索树时，容易进入误区：只要当前节点的值大于左子节点且小于右子节点，就认为是合法的 BST。然而，这种局部判断无法覆盖整个树的结构，可能会遗漏一些全局不符合 BST 定义的情况。
---
所以，BST 的验证需要维护一个**全局的取值范围**，确保每个节点的值都在其允许的范围内，而不仅仅是与其直接子节点比较。具体来说：
二叉搜索树的中序遍历是一个严格递增的序列。因此，可以通过中序遍历来验证 BST 的合法性。如果在中序遍历过程中发现当前节点的值不大于前一个节点的值，则说明该树不是合法的 BST。
