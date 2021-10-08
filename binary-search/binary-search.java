class Solution {
    public int searchHelper(int[] nums, int start, int end, int target){
        if(start <= end){
        int mid = (start+end)/2;
        if(nums[mid] == target) return mid;
        else if(nums[mid] > target) return searchHelper(nums,start,mid-1,target);
        else if(nums[mid] < target) return searchHelper(nums, mid+1, end, target);
        }
        return -1;
    }
    public int search(int[] nums, int target) {
        return searchHelper(nums, 0, nums.length-1, target);
    }
}