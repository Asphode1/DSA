// Mai Trung Kiên
// 20200301
// https://github.com/Asphode1/DSA/tree/master/tree/BTVN-14-6.cpp

#include <iostream>
#include <string>
#include <stack>
using std::cout;
using std::stack;
using std::string;

std::string signs = "+-*/";

int priority(char chr)
{
  if (chr == '+' || chr == '-')
    return 1;
  if (chr == '*' || chr == '/')
    return 2;
  return 0;
}

int calc(char opr, int x1, int x2)
{
  if (opr == '+')
    return x1 + x2;
  if (opr == '-')
    return x1 - x2;
  if (opr == '*')
    return x1 * x2;
  if (opr == '/')
    return x1 / x2;
  return 0;
}

string convert(string expression)
{
  stack<char> val;
  string postFix = "";
  for (auto &chr : expression)
  {
    if (chr == ' ')
      continue;
    if (chr - '0' >= 0 && chr - '0' <= 9)
      postFix += chr;
    if (chr == '(')
      val.push(chr);
    if (chr == ')')
    {
      while (val.top() != '(')
      {
        postFix += val.top();
        val.pop();
      }
      val.pop();
    }
    else if (signs.find(chr) != string::npos)
    {
      while (!val.empty() && priority(chr) <= priority(val.top()))
      {
        postFix += val.top();
        val.pop();
      }
      val.push(chr);
    }
  }
  while (!val.empty())
  {
    postFix += val.top();
    val.pop();
  }
  return postFix;
}

int eval(string postFix)
{
  stack<int> val;
  for (auto &chr : postFix)
  {
    if (chr - '0' >= 0 && chr - '0' <= 9)
      val.push(chr - '0');
    if (signs.find(chr) != string::npos)
    {
      int x1 = val.top();
      val.pop();
      int x2 = val.top();
      val.pop();
      val.push(calc(chr, x1, x2));
    }
  }
  return val.top();
}

int main()
{
  string inFixExpression = "5+((1+2)*4)+3";
  string postFix = convert(inFixExpression);
  cout << postFix << std::endl;
  cout << eval(postFix);
  return 0;
}