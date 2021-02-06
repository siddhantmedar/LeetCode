class Solution {
public:
    vector<int> grayCode(int n) {
        if(n == 0){
            return vector<int>{0};
        }
        vector<int> result = grayCode(n-1);
        int numToAdd = 1<<(n-1);

        for(int i = result.size()-1; i>=0; i--){
            result.push_back(numToAdd+result[i]);
        }

        return result;
    }
};