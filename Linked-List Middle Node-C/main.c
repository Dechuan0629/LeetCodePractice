#include <stdio.h>
#include <stdlib.h>

struct ListNode {
    int val;
    struct ListNode *next;
};


struct ListNode* middleNode(struct ListNode* head){
    struct ListNode *p;
    int count=0;
    p = head;
    while(p!=NULL){                             //单指针方法
        count++;                                //还可用双指针-快慢针方法，快指针每次走两步，慢指针每次走一步，当快指针到达尾节点时，慢指针必定在中间节点。
        p = p->next;
    }
    int i,mid = count/2+1;
    p = head;
    for(i=1;i<mid;i++){
        p = p->next;
    }
    return p;
}


void main()
{
    struct ListNode *head,*p,*q;
    int num;
    head = (struct ListNode *)calloc(1,sizeof(struct ListNode));
    p = head;
    printf("input the num of node:");
    scanf("%d",&num);
    for(int i=0;i<num;i++){
        printf("\ninput No.%d node:",i+1);
        scanf("%d",&p->val);
        if(i==num-1){
            p->next = NULL;
            break;
        }
        q = (struct ListNode *)calloc(1,sizeof(struct ListNode));
        p->next = q;
        p = q;
    }
    p = middleNode(head);
    while(p!=NULL){
        printf("%d ",p->val);
        p = p->next;
    }
}
