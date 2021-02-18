class Solution {
public:
    vector<vector<int>> permute(vector<int>& nums) {
        vector<vector<int>> result;
        sort(begin(nums), end(nums));
        do{
            result.push_back(vector<int>(begin(nums), end(nums)));
        }
        while(next_permutation(begin(nums),end(nums)));
        
        return result;
    }
};