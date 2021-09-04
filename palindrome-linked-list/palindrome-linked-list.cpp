/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    bool isPalindrome(ListNode* head) {
        if(!head || head->next == NULL) return true;
        vector<int> v;
        while(head){
            v.push_back(head->val);
            head = head->next;
        }
        vector<int> reverseList = v;
        reverse(begin(reverseList), end(reverseList));       
        return v==reverseList?true:false;
    }
};