class Solution {
    public int nextNumber(int n){
        int sum=0;
        while(n>0){
            sum+=Math.pow(n%10,2);
            n/=10;
        }
        return sum;
    }
    public boolean isHappy(int n) {
        HashSet<Integer> h = new HashSet<>();
        while(n != 1 && !h.contains(n)){
            h.add(n);
            n= nextNumber(n);
        }
        return n==1;
    }
}