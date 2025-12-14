# 代码随想录算法训练营74期|动态规划part06


## 题目
| 题目     | Leetcode地址 |
| ----------- | ----------- |
|322.零钱兑换| [力扣题目链接](https://leetcode.cn/problems/coin-change/description/)      |
|279.完全平方数| [力扣题目链接](https://leetcode.cn/problems/perfect-squares/)      |
|139.单词切分| [力扣题目链接](https://leetcode.cn/problems/word-break/description/)      |



### 322.零钱兑换

1. dp数组的含义： dp[j]表示满足容量为j的个数最少有dp[j]个
2. 递推关系式：拿第i个硬币来说：
   不放i就满足：有dp[j]个
   放i就满足：不放i前有dp[j - coin[i]] ,放i则+1，dp[j] = min(dp[j - coins[i]] + 1, dp[j]);
3. dp数组如何初始化：dp[0] = 0,其他为了能取到最小值，所以应该是取INT_MAX
4. 本题求钱币最小个数，那么钱币有顺序和没有顺序都可以，都不影响钱币的最小个数。所以本题并不强调集合是组合还是排列。**如果求组合数就是外层for循环遍历物品，内层for遍历背包。如果求排列数就是外层for遍历背包，内层for循环遍历物品。**。在01背包一位数组的时候，我们说，如果正序遍历内循环，会出现重复取的问题，而完全背包是允许重复取的，**所以内循环应该正序遍历**

### 139.单词切分

看到这道题目的时候，大家应该回想起我们之前讲解回溯法专题的时候，讲过的一道题目回溯算法：分割回文串 (opens new window)，就是枚举字符串的所有分割情况。
回溯算法：分割回文串 (opens new window)：是枚举分割后的所有子串，判断是否回文。本道是枚举分割所有字符串，判断是否在字典里出现过。

递归的过程中有很多重复计算，可以使用数组保存一下递归过程中计算的结果。这个叫做记忆化递归，这种方法我们之前已经提过很多次了。使用memory数组保存每次计算的以startIndex起始的计算结果，如果memory[startIndex]里已经被赋值了，直接用memory[startIndex]的结果。
```C++
class Solution {
private:
    bool backtracking (const string& s,
            const unordered_set<string>& wordSet,
            vector<bool>& memory,
            int startIndex) {
        if (startIndex >= s.size()) {
            return true;
        }
        // 如果memory[startIndex]不是初始值了，直接使用memory[startIndex]的结果
        if (!memory[startIndex]) return memory[startIndex];
        for (int i = startIndex; i < s.size(); i++) {
            string word = s.substr(startIndex, i - startIndex + 1);
            if (wordSet.find(word) != wordSet.end() && backtracking(s, wordSet, memory, i + 1)) {
                return true;
            }
        }
        memory[startIndex] = false; // 记录以startIndex开始的子串是不可以被拆分的
        return false;
    }
public:
    bool wordBreak(string s, vector<string>& wordDict) {
        unordered_set<string> wordSet(wordDict.begin(), wordDict.end());
        vector<bool> memory(s.size(), 1); // -1 表示初始化状态
        return backtracking(s, wordSet, memory, 0);
    }
};
```

背包问题：
单词就是物品，字符串s就是背包，单词能否组成字符串s，就是问物品能不能把背包装满。

拆分时可以重复使用字典中的单词，说明就是一个完全背包！

1. dp[j]:字符串长度为j的话，dp[j]为true，表示可以拆分为一个或多个在字典中出现的单词
2. 如果确定dp[j] 是true，且 [j, i] 这个区间的子串出现在字典里，那么dp[i]一定是true。（j < i ）。所以递推公式是 if([j, i] 这个区间的子串出现在字典里 && dp[j]是true) 那么 dp[i] = true。
3. dp数组如何初始化
从递推公式中可以看出，dp[i] 的状态依靠 dp[j]是否为true，那么dp[0]就是递推的根基，dp[0]一定要为true，否则递推下去后面都都是false了。那么dp[0]有没有意义呢？dp[0]表示如果字符串为空的话，说明出现在字典里。但题目中说了“给定一个非空字符串 s” 所以测试数据中不会出现i为0的情况，那么dp[0]初始为true完全就是为了推导公式。下标非0的dp[i]初始化为false，只要没有被覆盖说明都是不可拆分为一个或多个在字典中出现的单词。
4. 确定遍历顺序:题目中说是拆分为一个或多个在字典中出现的单词，所以这是完全背包。还要讨论两层for循环的前后顺序。如果求组合数就是外层for循环遍历物品，内层for遍历背包。如果求排列数就是外层for遍历背包，内层for循环遍历物品.而本题其实我们求的是排列数，为什么呢。 拿 s = "applepenapple", wordDict = ["apple", "pen"] 举例。

"apple", "pen" 是物品，那么我们要求 物品的组合一定是 "apple" + "pen" + "apple" 才能组成 "applepenapple"。

"apple" + "apple" + "pen" 或者 "pen" + "apple" + "apple" 是不可以的，那么我们就是强调物品之间顺序。

所以说，本题一定是 先遍历 背包，再遍历物品。

## 多重背包：

多重背包就是每个物品的数量有不确定件而且不同，可以将物品展开，按照01背包去做，但是展开的时候要由策略，否则展开会很耗时间。