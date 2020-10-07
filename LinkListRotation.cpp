//  Rotate List

// https://leetcode.com/explore/challenge/card/october-leetcoding-challenge/559/week-1-october-1st-october-7th/3486/

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
    int getLength(ListNode* head){
        if (head == nullptr){
            return 0;
        }
        
        ListNode *itr = head;
        int len = 0;
        
        while (itr != nullptr){
            len++;
            itr = itr->next;
        }
        return len;
    }
    
    void displayList(ListNode *head){
        if (head == nullptr){
            return;
        }
        
        ListNode *itr = head;
        
        while (itr){
            cout<<itr->val<<"-->";
            itr = itr->next;
        }
        cout<<endl;
    }
    
    ListNode * deleteLast(ListNode * head){
        if (head == nullptr){
            return head;
        }
        
        ListNode *itr = head;
        ListNode *prev = nullptr;
        
        while (itr->next != nullptr){
            prev = itr;
            itr = itr->next;
        }
        
        prev->next = nullptr;
        
        return itr;        
    }
    
    ListNode * insertBeg(ListNode * head, ListNode * node) {
        node->next = head;
        head = node;        
        
        return head;
    }
    
    ListNode* rotateRight(ListNode* head, int k) {
        if (head == nullptr){
            return nullptr;
        }
        
        int length = getLength(head);
        
        if (length == 1){
            return head;
        }
        
        if (k >= length){
            k %= length;
        }
        
        for (int i=1; i<=k; i++){
            ListNode * last = deleteLast(head);
            head = insertBeg (head, last);
        }
     
        return head;
    }
};
