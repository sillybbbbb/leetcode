'''
给定两个单词（beginWord 和 endWord）和一个字典 wordList，找出所有从 beginWord 到 endWord 的最短转换序列。转换需遵循如下规则：

每次转换只能改变一个字母。
转换过程中的中间单词必须是字典中的单词。
说明:

如果不存在这样的转换序列，返回一个空列表。
所有单词具有相同的长度。
所有单词只由小写字母组成。
字典中不存在重复的单词。
你可以假设 beginWord 和 endWord 是非空的，且二者不相同。
示例 1:

输入:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

输出:
[
  ["hit","hot","dot","dog","cog"],
  ["hit","hot","lot","log","cog"]
]
示例 2:

输入:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

输出: []

解释: endWord "cog" 不在字典中，所以不存在符合要求的转换序列。

'''
import copy
class Solution:
    

    def findLadders(self, beginWord: str, endWord: str, wordList):
        G = {}
        ret = []
        if endWord not in wordList:
            return []
        n = len(wordList)
        if beginWord not in wordList:
            wordList.append(beginWord)
            ibegin = n
        else:
            ibegin = wordList.index(beginWord)
        iend = wordList.index(endWord)
        INF = 999999
        cost = [INF]*(len(wordList))
        def compare(a,b):
            cnt = 0
            for i in range(len(a)):
                if a[i] != b[i]:
                    cnt+=1
                if cnt > 1:
                    return False
            if cnt == 1:
                return True
        def graph():
            for i in range(len(wordList)):
                for j in range(i+1,len(wordList)):
                    if compare(wordList[i],wordList[j]):
                        if i in G:

                            G[i].append(j)
                        else:
                            G[i] = [j]
                        if j in G:

                            G[j].append(i)
                        else:
                            G[j] = [i]
        # wordList.append(beginWord)
        # wordList.append(endWord)
        graph()
        if ibegin not in G:
            return []
        
        def bfs():
            queue = []
            queue.append([ibegin])
            cost[ibegin] = 0
            while(len(queue)):
                now = queue.pop(0)
                last = now[-1]
                if last == iend:
                    tmp = []
                    for i in now:
                        tmp.append(wordList[i])
                    ret.append(tmp)
                else:
                    for to in G[last]:
                        if cost[last] + 1 <= cost[to]:
                            cost[to] = cost[last] + 1
                            tmp = copy.deepcopy(now)
                            tmp.append(to)
                            queue.append(tmp)
        bfs()

        return ret
        
s = Solution()
beginWord = "talk"
endWord ="tail"

wordList =["talk","tons","fall","tail","gale","hall","negs"]
print(s.findLadders(beginWord,endWord,wordList))