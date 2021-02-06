class Solution {
public:
    int largestRectangleArea(vector<int>& nums) {
        
        int n = nums.size();
        vector<int> left(n), right(n);
        
        stack<int> s;
        
        for(int i=0; i<n; i++){
            if(s.empty()){
                left[i] = 0; s.push(i);
            }
            else{
                while(!s.empty() && nums[s.top()] >= nums[i]) s.pop();
                
                left[i] = s.empty()?0: s.top()+1;
                s.push(i);
            }
        }
        
        while(!s.empty()) s.pop();
        
        for(int i=n-1; i>=0; i--){
            if(s.empty()){
                right[i] = n-1; s.push(i);
            }
            else{
                while(!s.empty() && nums[s.top()] >= nums[i]) s.pop();
                
                right[i] = s.empty()?n-1:s.top()-1;
                s.push(i);
            }
        }
        
        int maxarea = 0;
        for(int i=0; i<n; i++){
            maxarea = max(maxarea, nums[i]*(right[i]-left[i]+1));
        }
        
        return maxarea;
    }
};