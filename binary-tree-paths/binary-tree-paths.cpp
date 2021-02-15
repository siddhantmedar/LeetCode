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
    void path(TreeNode* root, vector<string>& result, string str){
        if(!root->left and !root->right){
            result.push_back(str);
            return;
        }
        if(root->left) path(root->left, result, str+"->"+to_string(root->left->val));
        if(root->right) path(root->right, result, str+"->"+to_string(root->right->val));
    }
public:
    vector<string> binaryTreePaths(TreeNode* root) {
        vector<string> result;
        
        if(!root) return result;
        
        path(root, result, to_string(root->val));
        return result;
    }
};