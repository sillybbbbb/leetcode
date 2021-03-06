'''
给你两个单词 word1 和 word2，请你计算出将 word1 转换成 word2 所使用的最少操作数 。

你可以对一个单词进行如下三种操作：

插入一个字符
删除一个字符
替换一个字符
 

示例 1：

输入：word1 = "horse", word2 = "ros"
输出：3
解释：
horse -> rorse (将 'h' 替换为 'r')
rorse -> rose (删除 'r')
rose -> ros (删除 'e')
示例 2：

输入：word1 = "intention", word2 = "execution"
输出：5
解释：
intention -> inention (删除 't')
inention -> enention (将 'i' 替换为 'e')
enention -> exention (将 'n' 替换为 'x')
exention -> exection (将 'n' 替换为 'c')
exection -> execution (插入 'u')

'''
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        l1 = len(word1)
        l2 = len(word2)
        dp = [[None]*(l2+1) for i in range(l1+1)]
        for i in range(l1+1):
            dp[i][0] = i
        for i in range(l2+1):
            dp[0][i] = i
        # if word1 == "":
        #     return len(word2)
        # elif word2 == "":
        #     return len(word1)
        #dp[0][0] = 0 if word1[0] == word2[0] else 1
        for i in range(1,l1+1):
            for j in range(1,l2+1):
                s1 = dp[i-1][j-1] if word1[i-1] ==word2[j-1] else dp[i-1][j-1]+1
                s2 = dp[i-1][j] + 1
                s3 = dp[i][j-1] + 1
                dp[i][j] = min(s1,s2,s3)
        return dp[l1][l2]
s = Solution()
print(s.minDistance('horse','ros'))