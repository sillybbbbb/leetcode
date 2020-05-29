'''
删除最小数量的无效括号，使得输入的字符串有效，返回所有可能的结果。

说明: 输入可能包含了除 ( 和 ) 以外的字符。

示例 1:

输入: "()())()"
输出: ["()()()", "(())()"]
示例 2:

输入: "(a)())()"
输出: ["(a)()()", "(a())()"]
示例 3:

输入: ")("
输出: [""]


'''
class Solution:
    def isvalid(self,s):
        cnt = 0
        for c in s:
            if c == "(": cnt += 1
            elif c == ")": cnt -= 1
            if cnt < 0: return False  # 只用中途cnt出现了负值，你就要终止循环，已经出现非法字符了
        return cnt == 0

#
    def removeInvalidParentheses(self, s: str):
        ans = set()
        Q = [(s,0)]
        while len(Q):
            size = len(Q)
            flag = 0
            for i in range(size):
                t,index = Q.pop(0)
                if self.isvalid(t):
                    #t = t.replace('#','')
                    ans.add(t)
                    flag = 1
                else:
                    for j in range(index,len(t)):
                        if t[j] == '(' or t[j] == ')' :
                            tmp = t[:j]+t[j+1:]

                            Q.append((tmp,j))
            if flag:
                return ans   
        #优化==========================================
    def removeInvalidParentheses1(self, s: str):
   
        level = {s}
        
        while True:
            valid = list(filter(self.isvalid,level))
            if len(valid):
                return valid
            next_level = set()
            for i in level:
                for j in range(len(i)):
                    next_level.add(i[:j]+i[j+1:])
            level = next_level
s = Solution()
print(s.removeInvalidParentheses1(")))())("))