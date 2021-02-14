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
    pair<int, int> util(TreeNode* root){
        if(!root) return make_pair(0,0);
        pair<int, int> left = util(root->left);
        pair<int, int> right = util(root->right);
        
        int internal_path = max(left.second, right.second);
        
        if(left.first+ right.first+1 > internal_path){
            internal_path = left.first+right.first+1;
        }
        return make_pair(max(left.first, right.first)+1, internal_path);
    }
public:
    int diameterOfBinaryTree(TreeNode* root) {
        if(!root) return 0;
        pair<int, int> result = util(root);
        return max(result.first, result.second)-1;
    }
};