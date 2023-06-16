class Solution {
public:
    int majorityElement(vector<int>& nums) {
        int cand = nums[0], cnt = 1;
        
        for(int i=1;i<nums.size();i++){
            if(nums[i]==cand) cnt+=1;
            else{
                cnt-=1;
                if(cnt==0){
                    cand = nums[i];
                    cnt = 1;
                }
            }
        }
        return cand;
    }
};