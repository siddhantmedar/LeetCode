class Solution {
public:
    vector<vector<int>> construct2DArray(vector<int>& nums, int m, int n) {
        if(m*n != nums.size())
            return vector<vector<int>>{};
        
        if(m==1 and n==nums.size())
            return vector<vector<int>>{nums};
        vector<vector<int>> res(m,vector<int>(n,0));
        
        for(int i=0;i<nums.size();i++){
            // cout<<i<<" "<<i/m<<" "<<i%n<<endl;
            res[i/n][i%n] = nums[i];
        }
        return res; 
    }
};