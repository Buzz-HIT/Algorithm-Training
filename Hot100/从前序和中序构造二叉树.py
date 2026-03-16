class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def buildTree_(preBegin, preEnd, midBegin, midEnd, preOrder, midOrder):
    print("先根")
    for i in range(preBegin, preEnd):
        print(preOrder[i], end="-")
    print('\n')
    print("中根")
    for i in range(midBegin, midEnd):
        print(midOrder[i], end="-")
    print('\n')
    if preBegin >= preEnd:
        return None
    num = preOrder[preBegin]
    node = Node(num)
    midPos = 0
    for i in range(midBegin, midEnd):
        if num == midOrder[i]:
            midPos = i
            break
    leftLen = midPos - midBegin
    rightLend = midEnd - midPos
    node.left = buildTree_(preBegin + 1, preBegin + leftLen + 1, midBegin, midPos, preOrder, midOrder)
    node.right = buildTree_(preBegin + leftLen + 1, preEnd, midPos + 1, midEnd, preOrder, midOrder)
    return node
def buildTree(preOrder, midOrder):
    len_ = len(preOrder)
    root = buildTree_(0, len_, 0, len_, preOrder, midOrder)
    return root

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
buildTree(preorder, inorder)
