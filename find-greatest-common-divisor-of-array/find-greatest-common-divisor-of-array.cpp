class Solution {
public:
    int gcd(int a, int b){
        if(b == 0) return a;
        return gcd(b,a%b);
    }
    int findGCD(vector<int>& nums) {
        int smallest = *min_element(begin(nums), end(nums));
        int largest = *max_element(begin(nums), end(nums));
        return gcd(largest, smallest);
        
    }
};