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
    void flatten(TreeNode* root) {
        if(!root) return;
        
        TreeNode* l = root->left; 
        TreeNode* r = root->right;
        TreeNode* t = root;
        
        root->left = NULL;
        root->right = l;
        
        while(t->right){
            t=t->right;
        }
        t->right = r;
        
        flatten(root->right);
    }
};