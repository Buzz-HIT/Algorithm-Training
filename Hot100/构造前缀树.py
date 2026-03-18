class TreeNode():
    def __init__(self, val="", isEnd=False):
        self.val = val
        self.isEnd = isEnd
        self.chiledren = [None] * 26
class Trie(object):

    def __init__(self):
        self.root = TreeNode()

    def print_trie(self):
        def dfs(node, depth):
            if not node:
                return

            # 根节点特殊处理
            if node.val == "":
                print("ROOT")
            else:
                indent = "  " * depth
                end_flag = " (END)" if node.isEnd else ""
                print(f"{indent}{node.val}{end_flag}")

            for child in node.chiledren:
                if child:
                    dfs(child, depth + 1)

        dfs(self.root, 0)

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        if self.search(word):
            return
        else:
            cur = self.root
            for i in word:
                # print(i)
                index = ord(i) - ord('a')
                if cur.chiledren[index] == None:
                    # print(i)
                    cur.chiledren[index] = TreeNode(i)
                    cur = cur.chiledren[index]
                else:
                    # print(i)
                    cur = cur.chiledren[index]
            cur.isEnd = True
        # self.print_trie

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        cur = self.root
        for i in word:
            print(cur.val)
            cur = cur.chiledren[ord(i) - ord('a')]
            if cur == None:
                break
        if cur == None or cur.isEnd == False:
            return False
        else:
            return True

    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        cur = self.root
        for i in word:
            print(cur.val)
            cur = cur.chiledren[ord(i) - ord('a')]
            if cur == None:
                return False

        return True



obj = Trie()
word = "apple"
obj.insert(word)
obj.print_trie()
obj.insert("app")
print(obj.search(word))
print(obj.startsWith("app"))
print(obj.search("app"))