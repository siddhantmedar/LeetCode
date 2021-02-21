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
    bool isLeaf(TreeNode* root){
        if(!root) return false;
        else if(!root->left && !root->right) return true;
        return false;
    }
    int util(TreeNode* root){
        int sum=0;
        if(root){
            if(isLeaf(root->left)) sum+=root->left->val;
            else sum+=util(root->left);
            sum+=util(root->right);
            }
        return sum;
    }
    int sumOfLeftLeaves(TreeNode* root) {
        return util(root);
    }
};