#include <stdio.h>
#include <string.h>
#include <stdlib.h>

struct Node
{
  int dat;
  struct Node *next;
};

struct DoublyLinkedList
{
  char Hoten[100];
  int namSinh;
  int diem;
  struct DoublyLinkedList *prev;
  struct DoublyLinkedList *next;
};
typedef struct DoublyLinkedList *lk;

void printDS(int c, lk tail)
{
  do
  {
    if (2021 - tail->namSinh > c && 2021 - tail->namSinh % 2 == 1)
      printf("%s\n%d\n", tail->Hoten, tail->diem);
    tail = tail->prev;
  } while (tail->prev != NULL);
}

typedef struct Node *node;

node merge(node l1, node l2)
{
  node cur1 = l1;
  node cur2 = l2;
  node l;
  node cur = l;
  node tmp = cur;
  while (cur1->next != NULL || cur2->next != NULL)
  {
    if (cur1->dat > cur2->dat)
    {
      cur->dat = cur1->dat;
      cur1 = cur1->next;
    }
    else
    {
      cur->dat = cur2->dat;
      cur2 = cur2->next;
    }
    cur = cur->next;
  }
  return l;
}
