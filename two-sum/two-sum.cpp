class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int left= 0, right = numbers.size()-1;
        
        for(int i=0; i<numbers.size()-1; i++){
            for(int j = i+1; j<numbers.size(); j++){
                if(numbers[i]+numbers[j] == target) return vector<int>{i,j};
            }
        }
        
        return vector<int>{};
    }
};
