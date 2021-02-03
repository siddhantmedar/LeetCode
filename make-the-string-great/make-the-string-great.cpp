class Solution {
public:
    string makeGood(string s) {
        
        string answer;
        
        for(char c:s){
            if(answer.size() && abs(answer.back() - c) == abs('a' - 'A'))
                answer.pop_back();
            else answer.push_back(c);
        }
        return answer;
    }
};