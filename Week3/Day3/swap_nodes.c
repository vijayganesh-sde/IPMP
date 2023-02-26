#include<stdio.h>
struct ListNode{
  int val;
  struct ListNode *next;
};
struct ListNode* swapPairs(struct ListNode* head){
    struct ListNode *temp;
    struct ListNode *first = NULL;
    struct ListNode *second = NULL;
    temp=head;
    if(head==NULL) return head;
    else{
        first=temp;
        if(head->next==NULL){
        return head;
        }
        second=temp->next;
        head=second;
        while(second!=NULL){
        first->next=second->next;
        second->next=first;
        if(first->next!=NULL){
            second=first->next;
            if (second->next==NULL){
            return head;
            }
            first->next=second->next;
            first=second;
            second=second->next;
        }
        else{
            return head;
        }
        } 
    }
    return head;
}