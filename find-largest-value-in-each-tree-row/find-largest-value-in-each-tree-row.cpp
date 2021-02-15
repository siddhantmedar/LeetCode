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
    vector<int> largestValues(TreeNode* root) {
        vector<int> result;
        if(root == NULL) return result;
        int max = INT_MIN;
        
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
                max = *max_element(begin(v), end(v));
                result.push_back(max);
                v = vector<int>();
                levelCount = q.size();
            }
        }
        return result;
    }
};