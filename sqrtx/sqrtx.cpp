class Solution {
public:
    
    int binarySearch(int n, int left, int right){
        
        if(left > right) return right;
        
        long long mid = left+(right-left)/2;
        

        if(mid*mid < n) return binarySearch(n, mid+1, right);

        else if(mid*mid > n) return binarySearch(n, left, mid-1);
        
        else return mid;

        return -1;
    }
    int mySqrt(int x) {
        if(x<=1) return x;
        return binarySearch(x, 1, x);
    }
};