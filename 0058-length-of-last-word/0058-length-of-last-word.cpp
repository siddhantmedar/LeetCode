class Solution {
public:
    int lengthOfLastWord(string s) {
        int i = 0, j = s.length()-1;
        
        while(s[i]  == ' '){i+=1;}
        while(s[j] == ' ') {j-=1;}
        
        s = s.substr(i,j-i+1);
        
        int res = 0;
        i = s.size()-1;
        
        while(i>=0 && s[i] != ' '){
            i-=1;
            res+=1;
        }
        
        return res;
    }
};

// a b c d e f 
// 0 1 2 3 4 5
    
//     2, 6-2

//    _  _ t h i s _ _
//    0  1 2 3 4 5 6 7