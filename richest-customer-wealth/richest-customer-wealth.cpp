class Solution {
public:
    int maximumWealth(vector<vector<int>>& accounts) {
        
        int answer = 0;
        
        for(const vector<int>& x: accounts){
            answer = max(answer, accumulate(begin(x), end(x), 0));
        }
        
        return answer;
    }
};