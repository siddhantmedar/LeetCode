class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        if(matrix.empty() || matrix[0].empty()) return false;
        
        const int m = matrix.size(), n = matrix[0].size();
        
        int r = 0, c = matrix[0].size()-1;
        
        while(r<m && c>=0){
            if(matrix[r][c] == target) return true;
            if(matrix[r][c] > target) c-=1;
            else if(matrix[r][c] < target) r+=1;
        }
        return false;
    }
};