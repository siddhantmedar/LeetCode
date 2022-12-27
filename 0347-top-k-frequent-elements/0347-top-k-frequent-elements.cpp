class Solution {
public:
    static bool cmp(pair<int,int> &a, pair<int,int> &b){
            return a.second > b.second;
        }
    
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int,int> mp;
        
        for(auto ele:nums){
            if(mp.find(ele)==mp.end()){
                mp.insert(pair<int,int>(ele,1));
            }
            else{
                mp[ele]+=1;
            }
        }
        
        // vector<pair<int,int>> tmp;
        multimap<int,int,greater<int>> tmp;
        
        for(auto it:mp)
        {
            tmp.insert(make_pair(it.second,it.first));
        }
        
        // sort(begin(tmp),end(tmp),cmp);
        
        vector<int> result;
        
        for(auto x:tmp){
            if(result.size() == k){
                break;
            }
            result.emplace_back(x.second);
            // cout<<x.first<<" "<<x.second<<endl;
        }
        return result;
    }
};