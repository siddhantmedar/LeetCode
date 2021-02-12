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
    vector<int> inOrder(TreeNode* root, vector<int>& v){
        if(root == NULL) return v;
        inOrder(root->left, v);
        v.push_back(root->val);
        inOrder(root->right, v);
        return v;
    }
public:
    int kthSmallest(TreeNode* root, int k) {
        vector<int> temp;
        vector<int> result = inOrder(root, temp);
        return result[k-1];       
    }
};