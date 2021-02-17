class MinStack {
public:
    long me;
    stack<long> s;
    /** initialize your data structure here. */
    MinStack() {
        me = -1;
    }
    
    void push(int x) {
        if(s.empty()) me = x;
        
        if(x < me){
            s.push((2l*x) - me);
            me=x;
        }
        else s.push(x);
        
    }
    
    void pop() {
        if(s.top() < me) me = 2*me-s.top();
            s.pop();
    }
    
    int top() {
        return max(me, s.top());
    }
    
    int getMin() {
        return me;
    }
};

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack* obj = new MinStack();
 * obj->push(x);
 * obj->pop();
 * int param_3 = obj->top();
 * int param_4 = obj->getMin();
 */