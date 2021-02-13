class MyStack {
public:
    /** Initialize your data structure here. */
    queue<int> q1, q2;
    int current_size = 0;
    MyStack() {
        current_size = 0;
    }
    
    /** Push element x onto stack. */
    void push(int x) {
        current_size++;
        q2.push(x);
        
        while(!q1.empty()){
            q2.push(q1.front());
            q1.pop();
        }
        
        queue<int> temp = q1;
        q1 = q2;
        q2 = temp;
    }
    
    /** Removes the element on top of the stack and returns that element. */
    int pop() {
        if(q1.empty()) return -1;
        int temp = q1.front();
        q1.pop();
        current_size--;
        return temp;
    }
    
    /** Get the top element. */
    int top() {
        if(q1.empty()) return -1;
        else return q1.front();
        
    }
    
    /** Returns whether the stack is empty. */
    bool empty() {
        return current_size == 0;
    }
};

/**
 * Your MyStack object will be instantiated and called as such:
 * MyStack* obj = new MyStack();
 * obj->push(x);
 * int param_2 = obj->pop();
 * int param_3 = obj->top();
 * bool param_4 = obj->empty();
 */