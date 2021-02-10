bool compares(string a, string b){
        string l=a+b;
        string r=b+a;
        return l>r;
    }
class Solution {
public:
    string largestNumber(vector<int>& nums) {
        vector<string> result;
        for(int x: nums){
            result.push_back(to_string(x));
        }
        sort(begin(result), end(result), compares);
        string answer = "";
        for(string s: result){
            answer+=s;
        }
        return answer[0] == '0'?"0":answer;
    }
};