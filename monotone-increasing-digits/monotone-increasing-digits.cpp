class Solution {
public:
    int monotoneIncreasingDigits(int N) {
        
        string temp = to_string(N);
        
        const int n = temp.size();
        int k = n;
        
        for(int i= k-1; i>0; i--){
            if(temp[i]<temp[i-1]){
                temp[i-1]--;
                k = i;
            }
        }
            
        for(int i=k; i<n; i++){
             temp[i] = '9';
        }
​
        return stoi(temp);
    }
};
