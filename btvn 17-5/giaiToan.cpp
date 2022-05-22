// Họ và Tên: Mai Trung Kiên
// MSV: 20200301

#include <iostream>
#include <stack>
#include <string>

std::string signs = "+-*/";

int priority(char chr)
{
  if (chr == '+' || chr == '-')
    return 1;
  if (chr == '*' || chr == '/')
    return 2;
  return 0;
}

int calc(int a, int b, char chr)
{
  switch (chr)
  {
  case '+':
    return a + b;
  case '-':
    return a - b;
  case '*':
    return a * b;
  case '/':
    return a / b;
  }
}

bool check(std::string str)
{
  std::stack<char> stk;
  for (auto &chr : str)
  {
    if (chr == '{' || chr == '(' || chr == '[')
    {
      stk.push(chr);
    }
    else if (chr == '}')
    {
      if (stk.top() != '{')
        return false;
      stk.pop();
    }
    else if (chr == ']')
    {
      if (stk.top() != '[')
        return false;
      stk.pop();
    }
    else if (chr == ')')
    {
      if (stk.top() != '(')
        return false;
      stk.pop();
    }
  }
  if (!stk.empty())
    return false;
  return true;
}

void solve(std::string str)
{
  std::stack<int> number;
  std::stack<char> opr;
  if (!check(str))
  {
    std::cout << "Wrong expression\n";
    return;
  }
  for (auto &chr : str)
  {
    if (chr == '(')
      opr.push(chr);
    else if (chr >= '0' && chr <= '9')
      number.push(chr - '0');
    else if (chr == ')')
    {
      while (!opr.empty() && opr.top() != '(')
      {
        int n1 = number.top();
        number.pop();
        int n2 = number.top();
        number.pop();
        char sign = opr.top();
        opr.pop();
        number.push(calc(n2, n1, sign));
      }
      if (!opr.empty())
        opr.pop();
    }
    else
    {
      while (!opr.empty() && priority(opr.top()) >= priority(chr))
      {
        int n1 = number.top();
        number.pop();
        int n2 = number.top();
        number.pop();
        char sign = opr.top();
        opr.pop();
        number.push(calc(n1, n2, sign));
      }
      opr.push(chr);
    }
  }
  while (!opr.empty())
  {
    int n1 = number.top();
    number.pop();
    int n2 = number.top();
    number.pop();
    char sign = opr.top();
    opr.pop();
    number.push(calc(n2, n1, sign));
  }
  std::cout << number.top() << std::endl;
  return;
}

int main()
{
  std::string bieuthuc1 = "1+2*(5-6/3)+2";
  std::string bieuthuc2 = "(2*3+1-2)-(2+4)/3";
  std::string bieuthuc3 = "(2*3+1-2)-((2+4)/3";
  solve(bieuthuc1); // 9
  solve(bieuthuc2); // 3
  solve(bieuthuc3); // Wrong expression
  return 0;
}