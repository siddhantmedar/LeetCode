class Solution {
public:
    bool isValid(string x) {
        if(x.size()== 0) return true;
        
        stack<char> s;
        
        for(int i=0;i<x.size();++i){
            if(x[i] == '(' || x[i] == '[' || x[i] == '{') s.push(x[i]);
            else{
                if(s.empty()) return false;
                else{
                    if(x[i] == ')'){
                        if(s.top() == '(') s.pop();
                            else return false;
                    }
                    
                    if(x[i] == ']'){
                        if(s.top() == '[') s.pop();
                            else return false;
                    }
                    
                    if(x[i] == '}'){
                        if(s.top() == '{') s.pop();
                            else return false;
                    }
                }
            }
        }
        return s.empty()?true:false;
    }
};