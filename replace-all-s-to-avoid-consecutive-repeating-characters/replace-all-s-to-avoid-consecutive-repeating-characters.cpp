class Solution {
public:
    
    char difference(char a, char b){
        for(auto i = 'a'; i<='z'; i++){
            if(i!=a && i != b) return i;
        }
        return ' ';
    }
    string modifyString(string s) {
        string answer;
        char previous = ' ';
        
        for(int i=0; i<s.size()-1; i++){
            if(s[i] == '?'){
                answer += difference(previous, s[i+1]);
                previous = answer.back();
            }
            else{
                answer+=s[i];
                previous = s[i];
            }
        }
        if(s.back() == '?'){
            answer+= difference(previous, ' ');
        }
        else{
            answer+=s.back();
        }
        
        return answer;
    }
};