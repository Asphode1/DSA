#include <stdio.h>
#include <string.h>

typedef struct Node
{
  char name[256];
  struct Node *leftChild;
  struct Node *right;
} Node;

Node *add(char *name)
{
  Node *cur;
  strcpy(cur->name, name);
  return cur;
}

Node *find(Node *root, char *name)
{
  if (strcmp(root->name, name))
    return root;
  Node *temp = root->leftChild;
  while (temp)
  {
    if (strcmp(temp->name, name))
      return temp;
    temp = temp->right;
  }
  return find(root->leftChild, name);
}

int main()
{
  Node *root;
  strcpy(root->name, "david");
  root->leftChild = add("jame");
  Node *cur = root->leftChild;
  cur->right = add("peter");
  cur->leftChild = add("mike");
  cur = cur->right;
  cur->leftChild = add("mary");
  Node *temp = cur->leftChild;
  cur->right = add("john");
  cur = root->leftChild;
  cur = cur->leftChild;
  cur->right = temp;
  temp->right = add("daisy");
}