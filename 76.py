'''
76. 最小覆盖子串
给你一个字符串 S、一个字符串 T，请在字符串 S 里面找出：包含 T 所有字符的最小子串。

示例：

输入: S = "ADOBECODEBANC", T = "ABC"
输出: "BANC"
说明：

如果 S 中不存这样的子串，则返回空字符串 ""。
如果 S 中存在这样的子串，我们保证它是唯一的答案。
'''

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left,right,m,n = 0,0,len(s),len(t)
        valid = 0
        need = {}
        mi = 99999
        ret = ""
        for k in t:
            if k in need:
                need[k]+=1
            else:
                need[k] = 1
        def iscontent():
            for _,value in need.items():
                if value>0:
                    return False
            return True
       
        while right<m:
            c = s[right]
            right+=1
            if c in need:
                need[c]-=1
                if need[c] == 0:
                    valid +=1
            print(left,right)
            while valid == len(need):
                if right-left <mi:
                    mi = right-left
                    ret = s[left:right]
                d = s[left]
                left+=1
                if d in need:
                    if need[d] == 0:
                        valid-=1
                    need[d] +=1
        return ret

s = Solution()
print(s.minWindow("a","a"))
            
                


