using System;
delegate int Calc(int x, int y);
class Program
{
static int Add(int a, int b) { Console.Write("A"); return a + b; }
static int Mul(int a, int b) { Console.Write("M"); return a * b; }
static int Sub(int a, int b) { Console.Write("S"); return a - b; }
static void Main()
{
Calc c = Add;
c += Mul;
c += Sub;
c -= Add;
int res = c(2, 3);
Console.Write(":" + res);
}
}