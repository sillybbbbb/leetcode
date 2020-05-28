'''
示例:

输入: 4
输出: [
 [".Q..",  // 解法 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // 解法 2
  "Q...",
  "...Q",
  ".Q.."]
]

'''
import copy
class Solution:
    def solveNQueens(self, n: int):
        ans = []
        K = [-1]*n

        def printG(G):
            ground = [['.']*n for i in range(n)]
            for i in range(n):
                ground[i][G[i]]='Q'
                ground[i] = "".join(ground[i])
            return ground
#0241
        def isvalid(G,row):
            i = 0
            a = []
            b = []
            for i in range(row+1):
                if G[i]-i in a or (G[i] + i )in b:
                    return False
                else:
                    a.append(G[i]-i)
                    b.append(G[i]+i)
            for i in range(row+1):
                for j in range(i):
                    if G[i] == G[j] and G[i] > -1:
                        return False
            return True
        
        def backtrack(row,Q):
            if row == n:
                cop = copy.deepcopy(Q)
                ans.append(cop)
                return
            for i in range(n):
                Q[row] = i
                if isvalid(Q,row):
                    backtrack(row+1,Q)
                    Q[row] = -1
                else:
                    Q[row] = -1
        ret = []
        backtrack(0,K)
        print(ans)
        for i in ans:
            ret.append(printG(i))
        return ret


'''
位运算
void dfs(int n, int row, int col, int ld, int rd) {
        if (row >= n) { res++; return; }
        int bits = ~(col | ld | rd) & ((1 << n) - 1);   // 1
        while (bits > 0) {   // 2
            int pick = bits & -bits; // 3
            dfs(n, row + 1, col | pick, (ld | pick) << 1, (rd | pick) >> 1); //4
            bits &= bits - 1; // 5
        }
    }
'''
s=Solution()
s.solveNQueens(5)
st = "1245"