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
    vector<vector<int>> levelOrderBottom(TreeNode* root) {
      vector<vector<int>> result;
        if(root == NULL) return result;
        vector<int> v;
        queue<TreeNode*> q;
        int levelCount = 0;
        
        q.push(root); levelCount++;
        TreeNode* current;
        
        while(!q.empty()){
            current = q.front(); q.pop(); levelCount--;
            v.push_back(current->val);
            if(current->left) q.push(current->left);
            if(current->right) q.push(current->right);
            
            if(levelCount == 0){
                result.push_back(v);
                v = vector<int>();
                levelCount = q.size();
            }
        }
        return vector<vector<int>>{rbegin(result), rend(result)};
    }
};