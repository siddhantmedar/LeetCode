class Solution {
public:
    vector<int> majorityElement(vector<int>& nums) {
        unordered_map<int, int> m;
        vector<int> result;
        for(int i=0; i<nums.size(); ++i){
            m[nums[i]]++;
        }
        vector<pair<int, int>> temp;
        for(auto& x:m){
            temp.emplace_back(x);
        }
        sort(begin(temp), end(temp), [](const auto& x, const auto& y){
            return x.second>y.second;
        });

        for(auto& x:temp){
            if(x.second > nums.size()/3){
                result.push_back(x.first);
            }
        }
        return result;
    }
};