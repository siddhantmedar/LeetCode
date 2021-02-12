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
    int search(vector<int>& inorder, int data, int l, int r){
        for(int i = l; i<= r; i++){
            if(inorder[i] == data) return i;
        }
        return -1;
    }
    TreeNode* Solve(vector<int>& preorder, vector<int>& inorder, int& preIndex, int l, int r){
        if(l > r) return NULL;
        
        TreeNode* node = new TreeNode(preorder[preIndex++]);
        
        int mid = search(inorder, node->val, l, r);
        
        node->left = Solve(preorder, inorder, preIndex, l, mid-1);
        node->right = Solve(preorder, inorder, preIndex, mid+1, r);
        
        return node;
    }
public:
    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
        int preIndex = 0;
        int n = preorder.size();
        TreeNode* result = Solve(preorder, inorder, preIndex, 0, n-1);
        return result;
    }
};