class Solution {
public:
    
    void mark(vector<vector<char>>& matrix, int m, int n, int r, int c){
            if(m<0 || m>=r || n<0 || n>=c || matrix[m][n] != '1') return;
        
            matrix[m][n] = 2;
            
            mark(matrix, m-1, n, r, c);
            mark(matrix, m+1, n, r, c);
            mark(matrix, m, n-1, r, c);
            mark(matrix, m, n+1, r, c);
        }
    
    int numIslands(vector<vector<char>>& grid) {
        
        int row = grid.size(), col = grid[0].size();
        if(grid.size() == 0) return 0;
        
        int count = 0;
        
        for(int i=0; i<row; ++i){
            for(int j=0; j<col; ++j){
                if(grid[i][j] == '1'){
                    mark(grid, i, j, row, col);
                    count++;
                }
            }
        }
        
        return count;
    }
};