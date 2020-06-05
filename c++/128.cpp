#include <stdlib.h>
#include <vector>
#include <iostream>
#include <unordered_map>
#include <limits.h>
using namespace std;

class Solution
{
public:
    unordered_map<int,int> uf,cnt;
    int find(int x){
        return x == uf[x]? x: uf[x] = find(uf[x]);
    };
    int merge(int x,int y){
        int rx = find(x);
        int ry = find(y);
        if(rx == ry)return cnt[rx];
        uf[ry] = rx;
        cnt[rx]+=cnt[ry];
        return cnt[rx];
    }

    int longestConsecutive(vector<int> &nums)
    {
        int n = nums.size();
        if(!n)return 0;
        
        
        for (int i :nums)
        {
            uf[i] = i;
            cnt[i] = 1;
        }
        int ans = 1;
        for(int i :nums){
            int count = uf.count(i+1);
            if(i!=INT_MAX && uf.count(i+1)){
                ans = max(ans,merge(i,i+1));
            }
        }
        return ans;
    }
};

int main()
{
    vector<int> nums = {4,0,-4,-2,2,5,2,0,-8,-8,-8,-8,-1,7,4,5,5,-4,6,6,-3};
    Solution s;
    cout << s.longestConsecutive(nums);
}