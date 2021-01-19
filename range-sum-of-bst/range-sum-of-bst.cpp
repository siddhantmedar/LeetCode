/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    int rangeSumBST(TreeNode* root, int L, int R) {
        if(root == NULL) return 0;
        
        int sum = 0;
        
        if(root->val >= L && root->val <= R) sum+= root->val;
        
        if(root->val<L){
            sum+=rangeSumBST(root->right, L, R);
        }
        else if(root->val>R){
            sum+=rangeSumBST(root->left, L, R);
        }
        else{
            sum+=rangeSumBST(root->left, L, R) + rangeSumBST(root->right, L, R);
        }
        
        return sum;
    }
};
