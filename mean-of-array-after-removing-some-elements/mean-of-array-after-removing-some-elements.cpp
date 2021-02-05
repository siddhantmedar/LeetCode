class Solution {
public:
    double trimMean(vector<int>& arr) {
        
        sort(begin(arr), end(arr));
        
        auto offset = arr.size()/20;
        
        int sum = accumulate(arr.begin()+offset, arr.end()-offset, 0);
        
        return static_cast<double> (sum) / (arr.size()-(2*offset));
    }
};