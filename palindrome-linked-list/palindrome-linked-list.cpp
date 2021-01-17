/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    bool isPalindrome(ListNode* head) {
        
        stack<int> s;
        
        ListNode* temp = head;
        
        if(temp == NULL) return true;
        
        while(temp != NULL){
            s.push(temp->val);
            temp = temp->next;
        }
        
        ListNode* temp1 = head;
    
        while(!s.empty() && temp1){
            if(temp1->val != s.top()) return false;
            s.pop(); temp1 = temp1->next;
            }
        return true;
    }
};
