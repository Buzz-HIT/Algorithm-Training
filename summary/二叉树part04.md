# 代码随想录算法训练营74期|二叉树part04

## Leetcode题目
| 题目     | Leetcode地址 |
| ----------- | ----------- |
| 513.找树左下角的值| [力扣题目链接](https://leetcode.cn/problems/find-bottom-left-tree-value/description/)    |
| 112. 路径总和| [力扣题目链接](https://leetcode.cn/problems/path-sum/description/)      |
| 113. 路径总和II| [力扣题目链接](https://leetcode.cn/problems/path-sum-ii/description/)      |
| 106. 从中序与后序遍历序列构造二叉树| [力扣题目链接](https://leetcode.cn/problems/construct-binary-tree-from-inorder-and-postorder-traversal/description/)      |
| 105. 从前序与中序遍历序列构造二叉树| [力扣题目链接](https://leetcode.cn/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/)      |

下面是一段**清晰、结构化的总结**，概括你在调试 LeetCode 113「路径总和 II」过程中遇到的问题与最终解决方案。

---

# 📝 路径总和 II —— 调试总结

在实现 DFS + 回溯求解「路径总和 II」时，我遇到一个关键问题：**收集到的路径结果出现被覆盖的现象**。虽然打印显示每次找到的路径是正确的，但最终结果列表却只保存了最后一次的路径，或者多条完全相同的路径。

### ✔ 原因分析

问题的根源在于：

```python
self.result.append(path)
```

这里 append 的是 **同一个 path 列表对象的引用**。在 DFS 继续回溯、修改 path（例如 pop）时，`result` 中保存的路径也会同步被修改，导致最终所有保存的路径都变成了同一条。

### ✔ 本质原因（一句话）

> 你保存的是“指针”，不是“快照”。

### ✔ 解决方法

在保存路径时必须使用**深拷贝**：

```python
self.result.append(path[:])
```

这样每次加入 `result` 的都是一份全新的列表，不会受到后续回溯的影响。

### ✔ 收获与经验

* 回溯问题中，**path 必须在加入结果时复制**，否则所有结果都会共享同一份 path。
* DFS 时避免对同一个列表进行复用；如果要复用，务必在保存时深拷贝。
* 调试时多打印 path，能快速定位是否是引用问题(最后两道题也可以打印构造数组进行调试）

