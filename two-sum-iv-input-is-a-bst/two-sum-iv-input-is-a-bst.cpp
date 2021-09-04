/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    
    void inorder(TreeNode* root, vector<int>& temp){
        if(!root) return;
        inorder(root->left, temp);
        temp.push_back(root->val);
        inorder(root->right, temp);
    }
    bool findTarget(TreeNode* root, int k) {
        if(!root) return false;
        vector<int> temp;
        inorder(root, temp);
        
        int ptr_low = 0, ptr_high = temp.size()-1;
        while(ptr_low < ptr_high){
            if(temp[ptr_low]+temp[ptr_high] == k) return true;
            if(temp[ptr_low]+temp[ptr_high] < k) ptr_low++;
            else ptr_high--;
        }
        return false;
    }
};