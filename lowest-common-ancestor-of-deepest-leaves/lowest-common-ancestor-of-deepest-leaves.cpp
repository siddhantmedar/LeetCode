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
    int depthOfTree(TreeNode* root){
        if(!root) return 0;
        if(root->left == NULL && root->right == NULL) return 1;
        else return(max(depthOfTree(root->left), depthOfTree(root->right)))+1;
    }
    void findNode(TreeNode* root, TreeNode*& result){
        if(!root) return;
        
        int left = depthOfTree(root->left);
        int right = depthOfTree(root->right);
        
        if(left > right){
            findNode(root->left, result);
        }
        else if(right > left){
            findNode(root->right, result);
        }
        else{
            result = root;
            return;
        }
    }
public:
    TreeNode* lcaDeepestLeaves(TreeNode* root) {
        TreeNode* result = NULL;
        findNode(root, result);
        return result;
    }
};