class Solution {
    public int helperBinarySearch(int[] nums, int start, int end, int target){
        if(start<=end){
            int mid = (start+end)/2;
            if(nums[mid] == target) return mid;
            else if(nums[mid] > target) return helperBinarySearch(nums, start, mid-1, target);
            else if(nums[mid] < target) return helperBinarySearch(nums, mid+1, end, target);
        }
        return -1;
    }
    public int search(int[] nums, int target) {
        return helperBinarySearch(nums, 0, nums.length-1, target);
    }
}