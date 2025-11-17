## [二叉树的基本概念、种类、遍历方法](https://programmercarl.com/%E4%BA%8C%E5%8F%89%E6%A0%91%E7%90%86%E8%AE%BA%E5%9F%BA%E7%A1%80.html#%E4%BA%8C%E5%8F%89%E6%A0%91%E7%9A%84%E7%A7%8D%E7%B1%BB)

## 递归方法论

### Leetcode题目
| 题目     | Leetcode地址 |
| ----------- | ----------- |
| 144.二叉树的前序遍历| [力扣题目链接](https://leetcode.cn/problems/binary-tree-preorder-traversal/description/)      |
|145.二叉树的后序遍历| [力扣题目链接](https://leetcode.cn/problems/binary-tree-postorder-traversal/)        |
|94.二叉树的中序遍历|[力扣题目链接](https://leetcode.cn/problems/binary-tree-inorder-traversal/)    |

确定递归三要素：
1. **确定递归函数的参数和返回值**：确定哪些参数是递归的过程中需要处理的，那么就在递归函数里加上这个参数， 并且还要明确每次递归的返回值是什么进而确定递归函数的返回类型。
2. **确定终止条件**：写完了递归算法, 运行的时候，经常会遇到栈溢出的错误，就是没写终止条件或者终止条件写的不对，操作系统也是用一个栈的结构来保存每一层递归的信息，如果递归没有终止，操作系统的内存栈必然就会溢出。
3. **确定单层递归的逻辑**：确定每一层递归需要处理的信息。在这里也就会重复调用自己来实现递归的过程。（这个时候可以想象最简单的情况，即不需要更深的处理的情况，思路会更清晰）

e.g. 以前序遍历为例：
1. **确定递归函数的参数和返回值**:前序遍历不需要返回值，参数就是当前遍历到的树节点和用来存储答案的vector数组
```C++
void traversal(TreeNode* cur, vector<int>& vec)
```
2.**确定终止条件**：当前节点为空的时候，就说明遍历到位了,就需要返回了
```python
if cur == None:
    return
```
3.**确定单层递归的逻辑**：（假设二叉树的只有三个节点）前序遍历顺序为中左右，中的值放到答案中，再遍历左子树，最后遍历右子树
```python
ans.append(cur.val)
traversal(cur.left)
traversal(cur.right)
```
自此一个递归程序就写完了
而中序遍历和后序遍历就比较简单了

## 迭代（用栈来模拟递归）

前序遍历，很简单，先处理节点，在将右左节点入栈（因为出栈的顺序是和入栈的顺序相反的）
后序遍历，左右中-》前序是中左右-》前序可以变成中右左-》然后将答案倒序即可
中序遍历就比较复杂了，因为加入节点的顺序和处理节点的顺序完全不一致，因此就会比较复杂

于是就会有一种统一的迭代法，即通过对每个节点加一个flag标签，来判断是否被处理过，这样就能实现遍历处理两不误

拿最复杂的中序遍历来说
```python
def preorderTraversal(self, root):
    result = []
    st = [(root, False)] if root else []
    while st:
        node, visited= st.pop()
        if visited:
            result.append(node.val)
            continue
        if node.right:
            st.append((node.right, False))
        st.append((node, True))
        if node.left:
            st.append((node.left))
    return result
```
同理，前序和后序就改变一下进栈的顺序即可

## 层次遍历（广搜，用队列）
层次遍历指针法，由于python没有do-while结构，因此会少一次循环
### Leetcode题目
| 题目     | Leetcode地址 |
| ----------- | ----------- |
| 102.二叉树的层序遍历| [力扣题目链接](https://leetcode.cn/problems/binary-tree-level-order-traversal/description/)      |