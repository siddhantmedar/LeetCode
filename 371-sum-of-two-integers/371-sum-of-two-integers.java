class Solution {
    public int getSum(int a, int b) {
        while(b!=0){
            int xor = a^b;
            int carry = (a&b) << 1;
                
            a = xor;
            b = carry;
        }
        
        return a;
    }
}