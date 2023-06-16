class Solution {
public:
    vector<int> replaceElements(vector<int>& arr) {
        vector<int> res(arr.size(),-1);
        stack<int> st;
        
        for(int i=arr.size()-1; i>=0; i--){
            if(st.size() > 0){
                res[i] = st.top();
                if(arr[i] > st.top()){
                    st.pop();
                    st.push(arr[i]);
                }
            }   
            else{
                st.push(arr[i]);
            }
        }
        return res;
    }
};