class Solution {
public:
    vector<vector<int>> matrixReshape(vector<vector<int>>& matrix, int r, int c) {
        int m = matrix.size(), n = matrix[0].size(); 
        if(m*n < r*c) return matrix;
        
        vector<vector<int>> result;
        queue<int> temp;
        
        for(int i=0; i<matrix.size(); ++i){
            for(int j=0; j<matrix[0].size(); ++j){
                temp.push(matrix[i][j]);
            }
        }
        
        for(int i=0; i<r; ++i){
            vector<int> temp1;
            for(int j=0; j<c; ++j){
                int x = temp.front();
                temp1.push_back(x);
                temp.pop();
            }
            result.push_back(temp1);
            temp1.clear();
        }
    
        return result;
    }
};