class Solution {
public:
    vector<pair<int,int>> dir = {{-1,0},{1,0},{0,-1},{0,1}};
    
    void dfs(vector<vector<char>> &grid, int i, int j, int m, int n){
        if(i<0 or i>=m or j<0 or j>=n or grid[i][j]=='0')
            return;
        
        grid[i][j] = '0';
        
        for(auto &z:dir){
            int x = z.first+i;
            int y = z.second+j;
            
            dfs(grid,x,y,m,n);
        }
    }
    
    void bfs(vector<vector<char>> &grid, int i, int j, int m, int n){
        queue<pair<int,int>> q;
        
        q.push({i, j});
        grid[i][j] = '0';
        
        while(!q.empty()){
            int size = q.size();
            
            for(int i=0;i<size;i++){
                pair<int,int> loc = q.front();
                q.pop();
                
                for(auto &z:dir){
                    int x = z.first+loc.first;
                    int y = z.second+loc.second;
                    
                    if(x<0 or x>=m or y<0 or y>=n or grid[x][y]=='0')
                        continue;
                    
                    grid[x][y] = '0';
                    
                    q.push({x,y});
                }
            }
        }
    }

    int numIslands(vector<vector<char>>& grid) {
        int m = grid.size(), n = grid[0].size();
        int cnt = 0;
        
        for(int i=0;i<m;i++){
            for(int j=0;j<n;j++){
                if(grid[i][j]=='1'){
                    cout<<i<<" "<<j<<endl;
                    bfs(grid,i,j,m,n);
                    cnt+=1;
                }
            }
        }
        return cnt;
    }
};