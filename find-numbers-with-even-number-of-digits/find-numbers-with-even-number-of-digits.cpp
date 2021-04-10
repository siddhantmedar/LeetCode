class Solution {
public:
    int findNumbers(vector<int>& nums) {
        int count = 0;
        
        for(int i=0; i<nums.size(); i++){
            int temp_count = 0;
            while (nums[i] > 0) {
		    nums[i] = nums[i] / 10;
		    temp_count++;
        }
        if(temp_count%2 == 0) count++;
    }
        return count;
    }
};

//[12,345,2,6,7896] output:2


//7896

// count = 4
    
// 7896/10 = 789
// 789/10 = 78
// 78/10 = 7
// 7/10 = 0