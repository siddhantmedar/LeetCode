class Solution {
public:
    int specialArray(vector<int>& nums) {
        for(int i=0; i<=nums.size(); i++){
            if(i == count_if(begin(nums), end(nums), [i](int num){
                return num>=i;}))
            return i;
        }
        return -1;
    }
};