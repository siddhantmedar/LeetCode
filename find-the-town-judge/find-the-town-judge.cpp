class Solution {
public:
    int findJudge(int N, vector<vector<int>>& trust) {
        
        vector<pair<int,int>> result(N+1, {0,0});
        
        for(int i=0; i<trust.size(); i++){
            result[trust[i][0]].first += 1;
            result[trust[i][1]].second += 1;
        }
        
        for(int i=1; i<=N; i++){
            if(result[i].second == N-1 && result[i].first == 0)
               {
                   return i;
               }
        }
        
        return -1;
    }
};
