class MinStack {
private:
    stack<pair<int,int>> st;
public:    
    void push(int val) {
        if(!st.empty())
        {
            st.push(make_pair(val,min(st.top().second,val)));
        }
        else{
            st.push(make_pair(val,val));
        }
    }
    
    void pop() {
        if(!st.empty())
        {
            st.pop();
        }
    }
    
    int top() {
        if(!st.empty()){
            return st.top().first;
        }
        else{
            return INT_MIN;
        }
    }
    
    int getMin() {
        if(!st.empty()){
            return st.top().second;
        }
        else{
            return INT_MIN;
        }
    }
};

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack* obj = new MinStack();
 * obj->push(val);
 * obj->pop();
 * int param_3 = obj->top();
 * int param_4 = obj->getMin();
 */