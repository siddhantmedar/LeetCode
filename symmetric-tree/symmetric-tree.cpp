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
    bool util(TreeNode* x, TreeNode* y){
        if(x == NULL && y == NULL) return true;
        
        if((x == NULL && y != NULL) || (x != NULL && y == NULL) || (x->val != y->val)) return false;
        
        return util(x->left,y->right) && util(x->right, y->left);
    }
public:
    bool isSymmetric(TreeNode* root) {
        if(!root) return true;
        return util(root->left, root->right);
    }
};