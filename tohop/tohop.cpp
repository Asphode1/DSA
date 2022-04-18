#include <iostream>
#include <chrono>
using namespace std;

long long dequykonho(int k, int n)
{
  if (k == 0 || k == n)
    return 1;
  return dequykonho(k, n - 1) + dequykonho(k - 1, n - 1);
}

long long dequyconho(int k, int n, long long d[][100])
{
  if (k == 0 | k == n)
    return 1;
  if (d[k][n] != 0)
    return d[k][n];
  d[k][n] = dequyconho(k, n - 1, d) + dequyconho(k - 1, n - 1, d);
  return d[k][n];
}

int main()
{
  long long d[100][100];
  for (int i = 0; i < 100; i++)
    for (int j = 0; j < 100; j++)
      d[i][j] = 0;
  int ck[] = {10, 20, 20, 30, 40};
  int nk[] = {20, 35, 40, 50, 60};
  for (int i = 1; i < 2; i++)
  {
    auto start = std::chrono::system_clock::now().time_since_epoch();
    auto nss = std::chrono::duration_cast<std::chrono::nanoseconds>(start);
    cout << dequykonho(ck[i], nk[i]) << "  ";
    auto end = std::chrono::system_clock::now().time_since_epoch();
    auto nse = std::chrono::duration_cast<std::chrono::nanoseconds>(end);
    cout << (nse.count() - nss.count()) << endl;
  }
}