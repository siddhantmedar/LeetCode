class Solution {
public:
    vector<int> nextGreaterElement(vector<int>& nums1, vector<int>& nums2) {
        unordered_map<int,int> mp;
        stack<int> st;
        vector<int> res(nums2.size(),-1);
        
        for(int i=nums2.size()-1;i>=0;i--){
            while(st.size()>0 and st.top()<=nums2[i]){
                st.pop();
            }    
            if(st.size()>0)
                res[i] = st.top();
            
            st.push(nums2[i]);
        }
        
        for(int i=0;i<nums2.size();i++){
            mp[nums2[i]] = res[i];
        }
        
        vector<int> result;
        
        for(auto &x:nums1){
            result.emplace_back(mp[x]);
        }
        
        return result;
    }
};