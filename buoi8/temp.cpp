#include <iostream>
using namespace std;

void print(int a[], int n)
{
  for (int i = 0; i < n; i++)
  {
    cout << a[i];
  }
  cout << " ";
}

void G(int lev, int a[], int n)
{
  if (lev == n)
    print(a, n);
  for (a[lev] = lev; a[lev] < n; a[lev]++)
    G(lev + 1, a, n);
}

int main()
{
  int a[3] = {1, 2, 3};
  G(0, a, 3);
  return 0;
}