class Solution {
public:
    void swap(vector<int>& nums, int i, int j){
        int temp = nums[i];
        nums[i] = nums[j];
        nums[j] = temp;
        
    }
    
    void reverse(vector<int>& nums, int start, int end){
        while(start < end){
            swap(nums, start, end);
                start++; end--;

        }
    }
    
    void nextPermutation(vector<int>& nums) {
        if(nums.size() == 0 || nums.size() == 1) return;
        
        if(nums.size() == 2){
            swap(nums, 0, 1); return;
        }
        
        int dec = nums.size()-2;
        
        while(dec>=0 && nums[dec]>=nums[dec+1])
            dec--;
        
        if(dec == -1){
            sort(nums.begin(), nums.end()); return;
        }
        reverse(nums, dec+1, nums.size()-1);
        
        int next_number = dec + 1;
        
        while(next_number < nums.size() && nums[next_number] <= nums[dec]){
            next_number+=1;
        }
        
        swap(nums, next_number, dec);
    }
};