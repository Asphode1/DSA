#include <iostream>
#include <cstdlib>
#include <math.h>
#include <time.h>
using namespace std;

int randint(int start, int end)
{
  double rnd = static_cast <int> (floor(rand() * (start - end + 1)) + end);
  return (int)rnd;
}

int sumArr(int *arr, int i, int j)
{
  int sum = 0;
  for (int k = i; k <= j; k++)
    sum += arr[k];
  return sum;
}

int bruteForce(int *arr)
{
  int l = sizeof(arr) / sizeof(arr[0]);
  int max = 0;
  for (int i = 0; i < l; i++)
  {
    for (int j = i; j < l; j++)
    {
      int sum = sumArr(arr, i, j);
      if (sum > max)
        max = sum;
    }
  }
  return max;
}

int betterBruteForce(int *arr)
{
  int l = sizeof(arr) / sizeof(arr[0]);
  int max = 0;
  for (int i = 0; i < l; i++)
  {
    int sum = 0;
    for (int j = i; j < l; j++)
    {
      sum += arr[j];
      if (sum > max)
        max = sum;
    }
  }
  return max;
}

int dynamic(int *arr)
{
  int l = sizeof(arr) / sizeof(arr[0]);
  int s = arr[0];
  int e = arr[0];
  for (int i = 1; i < l; i++)
  {
    e = (arr[i] > e + arr[i]) ? arr[i] : (e + arr[i]);
    s = (s > e) ? s : e;
  }
  return s;
}

int main()
{
  const int l = 100;
  int arr[l];
  for (int i = 0; i < l; i++)
  {
    arr[i] = randint(-1000, 1000);
  }
  for (int i = 0; i < l; i++)
    cout << arr[i] << endl;
  clock_t start, end;
  start = clock();
  ios_base::sync_with_stdio(false);
  cout << bruteForce(arr);
  end = clock();
  cout << double(end - start) / double(CLOCKS_PER_SEC);
  return 0;
}