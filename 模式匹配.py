'''
面试题 16.18. 模式匹配
你有两个字符串，即pattern和value。 pattern字符串由字母"a"和"b"组成，用于描述字符串中的模式。例如，字符串"catcatgocatgo"匹配模式"aabab"（其中"cat"是"a"，"go"是"b"），该字符串也匹配像"a"、"ab"和"b"这样的模式。但需注意"a"和"b"不能同时表示相同的字符串。编写一个方法判断value字符串是否匹配pattern字符串。

示例 1：

输入： pattern = "abba", value = "dogcatcatdog"
输出： true
示例 2：

输入： pattern = "abba", value = "dogcatcatfish"
输出： false
示例 3：

输入： pattern = "aaaa", value = "dogcatcatdog"
输出： false
示例 4：

输入： pattern = "abba", value = "dogdogdogdog"
输出： true
解释： "a"="dogdog",b=""，反之也符合规则
提示：

0 <= len(pattern) <= 1000
0 <= len(value) <= 1000
你可以假设pattern只包含字母"a"和"b"，value仅包含小写字母。
'''


class Solution:
    def patternMatching(self, pattern: str, value: str) -> bool:
        dic = {}
        def search(mem, pattern, value)-> bool:
            if len(pattern) + len(value)==0:
                return True
            if len(pattern)==0 and len(value)>0: 
                
                return False
            let = pattern[0]
            if let in mem:
                p = mem[let]
                if value.startswith(p):
                    
                    return search(mem,pattern[1:],value[len(p):])
                else:
                    return False

            else:
                for i in range(len(value)):
                    
                    if value[:i] not in mem.values():
                        mem[let] = value[:i]
                        if  search(mem,pattern[1:],value[i:]):
                            return True
                mem.pop(let)
                return False
        return search(dic,pattern,value)
s = Solution()
pattern = "abba"

value = "dogcatcatdog"
print(s.patternMatching(pattern,value))