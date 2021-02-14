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
    int sum(TreeNode* root){
        if(!root) return 0;
        return root->val + sum(root->left) + sum(root->right);
    }
public:
    int findTilt(TreeNode* root) {
        if(!root) return 0;
        
        int left = sum(root->left);
        int right = sum(root->right);
        
        root->val = abs(left-right);
        
        return root->val+findTilt(root->left)+findTilt(root->right);
    }
};