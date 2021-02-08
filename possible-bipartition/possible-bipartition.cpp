class Solution {
public:
    
    bool isBiPartite(vector<vector<int>> adj, int N, int node, vector<int>& colors){
        queue<int> q;
        q.push(node);
        colors[node] = 1;
        
        while(!q.empty()){
            int current = q.front();
            q.pop();
            for(auto x: adj[current]){
                if(colors[x] == colors[current]) return false;
                if(colors[x] == -1){
                    colors[x] = 1-colors[current];
                    q.push(x);
                }
            }
        }
        return true;
    }
    bool possibleBipartition(int N, vector<vector<int>>& nums) {
        vector<vector<int>> adj(N+1);
        
        for(int i=0; i<nums.size(); i++){
            adj[nums[i][0]].push_back(nums[i][1]);
            adj[nums[i][1]].push_back(nums[i][0]);
        
        }
        
        vector<int> colors(N+1, -1);
        
        for(int i=1; i<=N; i++){
            if(colors[i] == -1){
                if(!isBiPartite(adj, N, i, colors))
                    return false;
            }
        }
        return true;
    }
};