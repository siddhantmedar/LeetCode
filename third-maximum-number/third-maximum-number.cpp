class Solution {
public:
    int thirdMax(vector<int>& nums) {
        if(nums.size() < 3) return *max_element(begin(nums), end(nums));
        vector<int> temp;
        for(int i=0; i<nums.size(); i++){
            if(find(begin(temp), end(temp), nums[i]) == temp.end()){
                temp.push_back(nums[i]);
            }
        }
        sort(begin(temp), end(temp), greater<int>());
        if(temp.size() < 3) return *max_element(begin(temp), end(temp));
        else{
            return temp[2];
        }
        return 0;
    }
};