def levelOrder(root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        from collections import deque
        result = []
        que = deque()
        if root == None:
            return result
        que.append(root)
        que.append(None)
        path = []
        while que:
            cur = que.popleft()
            if cur == None:
                if que:
                    que.append(None)
                    result.append(path[:])
                    path = []
                else:
                    result.append(path[:])
                    path = []
                    continue
            else:
                path.append(cur.val)
                if cur.left:
                    que.append(cur.left)
                if cur.right:
                    que.append(cur.right)
        return result