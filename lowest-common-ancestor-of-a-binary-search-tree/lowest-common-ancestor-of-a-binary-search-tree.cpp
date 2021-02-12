/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */

class Solution {
public:
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        int parentValue = root->val;
        int pNode = p->val, qNode = q->val;
        
        if(pNode > parentValue && qNode > parentValue) return lowestCommonAncestor(root->right, p, q);
        else if(pNode < parentValue && qNode < parentValue) return lowestCommonAncestor(root->left, p, q);
        else return root;
    }
};