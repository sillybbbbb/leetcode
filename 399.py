'''
给出方程式 A / B = k, 其中 A 和 B 均为用字符串表示的变量， k 是一个浮点型数字。根据已知方程式求解问题，并返回计算结果。如果结果不存在，则返回 -1.0。

示例 :
给定 a / b = 2.0, b / c = 3.0
问题: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ? 
返回 [6.0, 0.5, -1.0, 1.0, -1.0 ]

输入为: vector<pair<string, string>> equations, vector<double>& values, vector<pair<string, string>> queries(方程式，方程式结果，问题方程式)， 其中 equations.size() == values.size()，即方程式的长度与方程式结果长度相等（程式与结果一一对应），并且结果值均为正数。以上为方程式的描述。 返回vector<double>类型。

基于上述例子，输入如下：

equations(方程式) = [ ["a", "b"], ["b", "c"] ],
values(方程式结果) = [2.0, 3.0],
queries(问题方程式) = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ]. 
输入总是有效的。你可以假设除法运算中不会出现除数为0的情况，且不存在任何矛盾的结果。

'''


class Solution:
    def calcEquation(self, equations, values, queries):
        def get_route(a,b,c,visited):
            #visited = set()
            #ans = -1
            if a==b:
                return 1.0
            visited.add(a)
            for item,v in graph[a]:
                if item == b:
                    return c*v
                if item not in visited:
                    visited.add(item)
                    ans =  get_route(item,b,c*v,visited)
                    if ans!=-1:
                        return ans
            return -1

        graph = {}
        ret = []
        
        for i in range(len(equations)):
            if equations[i][0] in graph:
                graph[equations[i][0]].append((equations[i][1],values[i]))            
            else:
                graph[equations[i][0]] = [(equations[i][1],values[i])]
            if equations[i][1] in graph:
                graph[equations[i][1]].append((equations[i][0],1/values[i]))            
            else:
                graph[equations[i][1]] = [(equations[i][0],1/values[i])]
        for q in queries:
            if q[0] not in graph or q[1] not in graph:
                ret.append(-1.0)
                continue
            #visited = set()
            ret.append(get_route(q[0],q[1],1,set()))
        return ret
s = Solution()


equations = [["x1","x2"],["x2","x3"],["x1","x4"],["x2","x5"]]

values = [3.0,0.5,3.4,5.6]
queries = [["x2","x4"],["x1","x5"],["x1","x3"],["x5","x5"],["x5","x1"],["x3","x4"],["x4","x3"],["x6","x6"],["x0","x0"]]

print(s.calcEquation(equations,values,queries))