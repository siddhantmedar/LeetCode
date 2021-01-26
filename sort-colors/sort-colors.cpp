class Solution {
public:
    void sortColors(vector<int>& nums) {
        
        int temp[3] = {0};
        
        for(int i=0; i<nums.size(); i++){
            if(nums[i] == 0) temp[0]++;
            if(nums[i] == 1) temp[1]++;
            if(nums[i] == 2) temp[2]++;
        }
        
        int i=0;
        
        while(temp[0]>0){
            nums[i] = 0; temp[0]--; i++;
            }
        while(temp[1]>0){
            nums[i] = 1; temp[1]--; i++;
            }
        while(temp[2]>0){
            nums[i] = 2; temp[2]--; i++;
            }
    }
};
