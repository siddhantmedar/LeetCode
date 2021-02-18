class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        auto it =find(begin(nums), end(nums), target);
        if(it != end(nums)) return it-begin(nums);
        else if(it == end(nums)){
            return (lower_bound(begin(nums), end(nums), target)-begin(nums));
        }
        
        return 0;
    }
};