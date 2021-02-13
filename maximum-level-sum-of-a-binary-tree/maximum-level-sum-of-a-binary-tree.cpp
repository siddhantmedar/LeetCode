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
public:
    int maxLevelSum(TreeNode* root) {
        vector<int> v;

        queue<TreeNode*> q;
        
        q.push(root);
        TreeNode* current;

        while(!q.empty()){
            int n = q.size();
            int temp = n;
            double sum = 0;
            while(n--){
            current = q.front(); q.pop();
            sum+= current->val;
            if(current->left) q.push(current->left);
            if(current->right) q.push(current->right);
            }
            v.push_back(sum);
        }
        return (max_element(begin(v), end(v)) - begin(v))+1;
    }
};