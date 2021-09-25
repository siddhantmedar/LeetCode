class Solution {
    public char findTheDifference(String s, String t) {
        String temp = s+t;
        char res=0;
        for(int i=0; i<temp.length(); ++i){
            res^=temp.charAt(i);
        }
        return res;
    }
}