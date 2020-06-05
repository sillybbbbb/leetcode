/*
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. 
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. 
You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input:
11110
11010
11000
00000

Output: 1
Example 2:

Input:
11000
11000
00100
00011

Output: 3

*/



#include <stdlib.h>
#include <vector>
#include <iostream>
using namespace std;
class unionfind
{
private:

    vector<int> parent;
    vector<int> rank;
    int count = 0;
public:
    unionfind(vector<vector<char>>& grid);
    int find(int i);
    void unite(int x,int y);
    int getcount();
};

unionfind::unionfind(vector<vector<char>>& grid)
{
    int m = grid.size();
    int n = grid[0].size();
    for(int i = 0; i<m;i++)
    {
        for(int j =0 ;j<n;j++)
        {
            if(grid[i][j] == '1')
            {
                parent.push_back(i*n+j);
                count++;

            }
            else
            {
                parent.push_back(-1);
            }
            rank.push_back(0);
        }
    }
}
int unionfind::find(int x)
{
    if (parent[x] != x)parent[x] = find(parent[x]);
    return parent[x];
}
void unionfind::unite(int x,int y)
{
    int rootx = find(x);
    int rooty = find(y);
    if(rootx!=rooty){
        if(rank[rootx]<rank[rooty]){
            swap(rootx,rooty);
        }
        parent[rooty] = rootx;
        if(rank[rootx]==rank[rooty]){
            rank[rootx]++;  
        }
        count--;
    }
}
int unionfind::getcount(){
    return count;
}
class Solution {
public:
    int numIslands(vector<vector<char>>& grid) {
        int m = grid.size();
        
        if(m == 0){
            return 0;
        }
        int n = grid[0].size();
        unionfind nf(grid);
        for(int i = 0;i<m;++i){
            for(int j = 0;j<n;++j){
                if(grid[i][j]=='1'){
                    grid[i][j] = '0';
                    if(i-1>=0&&grid[i-1][j] == '1' ) nf.unite((i-1)*n+j,i*n+j);
                    if(i+1<m&&grid[i+1][j] == '1' ) nf.unite((i+1)*n+j,i*n+j);
                    if(j-1>=0&&grid[i][j-1] == '1' ) nf.unite((i)*n+j-1,i*n+j);
                    if(j+1<n&&grid[i][j+1] == '1' ) nf.unite((i)*n+j+1,i*n+j);
                }
            }
        }
        return nf.getcount();

    }
};

int main()
{

    Solution s;
    //vector<vector<char> > grid(4 ,vector<int>(5));
    vector<vector<char> > grid= {{'1','1','1','1','0'},{'1','1','0','1','0'},{'1','1','0','0','0'},{'0','0','0','0','0'}};
   
  
    cout<<s.numIslands(grid);
    
    return 0;
}