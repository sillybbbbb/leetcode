'''
564. 寻找最近的回文数
给定一个整数 n ，你需要找到与它最近的回文数（不包括自身）。

“最近的”定义为两个整数差的绝对值最小。

示例 1:

输入: "123"
输出: "121"
注意:

n 是由字符串表示的正整数，其长度不超过18。
如果有多个结果，返回最小的那个。
'''
# # 
# n= "123456"
# length = len(n)
# k = int((length+1)/2)
# c2 = n[:k-1] +str(int(n[k-1])-1)+str(int(n[k-1])-1) + n[:k-1][::-1]
# print(c2)
class Solution:
    def nearestPalindromic(self, n: str) -> str:
        length = len(n)
        k = int((length+1)/2)
        #print(int(n[1:]))
        if length ==1:
            return str(int(n)-1)
        if n[0]=='1' and length >=2 and int(n[1:])==0:
                return str(int(n)-1)
        if n=='11':
            return '9'
        i = 0
        while n[i]=='9':
            i+=1
            if i ==length:
                return str(int(n)+2)
        
        if length%2 ==1:
            #t = n[:k]+n[:k-1][::-1]
            half = str(int(n[:k]))
            t1 =half +half[:k-1][::-1]
            half = str(int(n[:k])-1)
            t2 =half +half[:k-1][::-1]
            half = str(int(n[:k])+1)
            t3 = half +half[:k-1][::-1]
            t = self.nearest(n,t1,t2,t3)
            return t
        else:
            c1 = n[:k]+n[:k][::-1]
            half = n[:k]

            c2 = str(int(half)-1)+str(int(half)-1)[::-1]
            c3 = str(int(half)+1)+str(int(half)+1)[::-1]
            final = self.nearest(n,c1,c2,c3)
            return final
    def nearest(self,n,c1,c2,c3):
        n = int(n)
        #t = min(abs(int(c1)-n),abs(int(c2)-n),abs(int(c3)-n))
        a1 = abs(int(c1)-n)
        a2 = abs(int(c2)-n)
        a3 = abs(int(c3)-n)

        if a1 == 0:
            a1=a1+a2+a3
        
        if a2<=a1 and a2<=a3:
            return c2
        if a1<=a3 and a1<a2:
            return c1
        if a3<a1 and a3<a2:
            return c3
s = Solution()
print(s.nearestPalindromic('230'))
