class Solution {
    public int findDuplicate(int[] nums) {
        int first=0;
        while(nums[first] != nums[nums[first]]){
            int temp=nums[nums[first]];
            nums[nums[first]]=nums[first];
            nums[first]=temp;
        }
        return nums[first];
    }
}