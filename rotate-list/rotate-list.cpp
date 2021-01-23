class Solution {
public:
    ListNode* rotateRight(ListNode* head, int k) {
        
        if(head == NULL || k == 0) return head;
        
        int length = 0;
        ListNode* temp = head;
        
        
        while(temp->next != NULL){
            temp = temp->next; length++;
        }
        length++; temp->next = head;
        
        
        int rotate = length - k % length;
        
        temp = head; 
        
        while(rotate > 1){
            temp = temp->next; rotate--;
        }
​
        head = temp->next;
        temp->next = NULL;
        
        return head;
    }
};
