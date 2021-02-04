class Solution {
public:
    int largestAltitude(vector<int>& gain) {
        int answer = 0, current = 0;
        
        for(auto x: gain)
        {
            answer = max(answer, current+=x);
        }
        
        return answer;
    }
};