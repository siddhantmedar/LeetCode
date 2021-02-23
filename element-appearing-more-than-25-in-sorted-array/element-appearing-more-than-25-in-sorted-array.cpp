class Solution {
public:
    int findSpecialInteger(vector<int>& arr) {
        unordered_map<int, int> m;
        for(int i=0; i<arr.size(); i++){
            m[arr[i]]++;
        }
        for(auto x:m){
            if(x.second > 0.25*arr.size()) return x.first;
        }
        return 0;
    }
};