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
    int count = 0;
    void traverse(TreeNode* root, int max){
        if(!root) return;
        
        if(root->val >= max){
            count++;
            max = root->val;
        }
        
        traverse(root->left, max);
        traverse(root->right, max);
    }
public:
    int goodNodes(TreeNode* root) {
        if(!root) return 0;
        
        traverse(root->left, root->val);
        traverse(root->right, root->val);
        
        return count+1;
    }
};