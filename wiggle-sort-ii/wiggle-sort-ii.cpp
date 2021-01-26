class Solution {
public:
    void wiggleSort(vector<int>& nums) {
        int n = nums.size();
        
        int mid = n/2;
        
        int small = (n%2)?mid:mid-1;
        
        int large = n-1;
        
        sort(nums.begin(), nums.end());
        
        vector<int> result(n);
        
        for(int i = 0; i<n; i+=2) result[i] = nums[small--];
        for(int i = 1; i<n; i+=2) result[i] = nums[large--];
        
        nums = result;
    }
};
