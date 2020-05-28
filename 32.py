'''
32. 最长有效括号
给定一个只包含 '(' 和 ')' 的字符串，找出最长的包含有效括号的子串的长度。

示例 1:

输入: "(()"
输出: 2
解释: 最长有效括号子串为 "()"
示例 2:

输入: ")()())"
输出: 4
解释: 最长有效括号子串为 "()()"
'''
 #dp[i] 为以s[i]为最后一位的最长有效字串
class Solution:
    def longestValidParentheses(self, s):
        n = len(s)
        dp = [0]*n 
        for i in range(1,n,1):
            if s[i] == ')' and i-dp[i-1]>0 and s[i-dp[i-1]-1]=='(' :
                dp[i] = dp[i-1]+2 + dp[i-dp[i-1]-2]
        return max(dp)
    def stackmethod(self,s):
        stack = [-1]
        length = 0
        ml = 0
        for i in range(len(s)):
            if s[i] =='(':
                stack.append(i)
            elif stack[-1]!=-1 and s[stack[-1]]=='(':
                length = i-stack.pop()+1
                if length >ml:
                    ml = length
            
        return ml

                
s = Solution()
string = ")()())"
print(s.longestValidParentheses(string)    )      
print(s.stackmethod(string) ) 

        
