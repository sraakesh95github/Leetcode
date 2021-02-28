#include <stdio.h>
#include <iostream>
using namespace std;

struct ListNode {
  int val;
  ListNode *next;
  ListNode() : val(0), next(nullptr) {}
  ListNode(int x) : val(x), next(nullptr) {}
  ListNode(int x, ListNode *next) : val(x), next(next) {}
};

int getListLength(ListNode *head) {
  ListNode *node = NULL;
  node = new ListNode();
  node = head;
  int counter = 0;
  while(node!=NULL) {
    counter++;
    node = node->next;
  }
  return counter;
}

void printList(ListNode *head) {
  ListNode *node = NULL;
  node = new ListNode();
  node = head;
  while(node != NULL) {
    cout<<node->val<<", ";
    node = node->next;
  }
}

ListNode* swapNodes(ListNode *head, int k) {

  //Get the length of the linked list
  ListNode *node = NULL;
  ListNode *firstNode = NULL;
  ListNode *endNode = NULL;
  node = new ListNode();
  firstNode = new ListNode();
  endNode = new ListNode();
  node = head;
  int length = 0;
  while(node!=NULL) {
    if(length == k-1) {
      firstNode = node;
      endNode = head;
    }
    if(length >= k) {
      endNode = endNode->next;
    }
    length++;
    node = node->next;
  }

  swap(firstNode->val, endNode->val);
  return head;
}

int main() {
  ListNode *head = NULL;
  ListNode *second = NULL;
  ListNode *third = NULL;
  ListNode *fourth = NULL;

  fourth = new ListNode(7, NULL);
  third = new ListNode(5, fourth);
  second = new ListNode(3, third);
  head = new ListNode(1, second);

  ListNode *head2 = NULL;
  cout << "Initial Linked List"
       << "\n";
  printList(head);
  cout << "List after swap"
       << "\n";
  head2 = swapNodes(head, 2);
  printList(head2);
}