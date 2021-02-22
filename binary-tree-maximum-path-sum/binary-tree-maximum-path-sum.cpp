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
    int maxValue = INT_MIN;
public:
    int util(TreeNode* root, int& sum){
        if(!root) return 0;
        int left = util(root->left, sum);
        int right = util(root->right, sum);
        
        int max_single = max(max(left, right)+root->val, root->val);
        int max_top = max(max_single, left+right+root->val);
        sum = max(sum, max_top);
        return max_single;
    }
    int max(int a, int b){
        return a>b?a:b;
    }
    int maxPathSum(TreeNode* root) {
        int sum = INT_MIN;
        util(root, sum);
        return sum;
    }
};