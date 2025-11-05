using System;
class Program
{
int age;
Program() => age=age==0?age+1:age-1;
static void Main()
{
int k = "010%".Replace('0','%').Length;
Console.Write("[" + (k<<++new Program().age).ToString() + "]");
Console.Write("[" + "010%".Split('1')[1][0] + "]");
Console.Write("[" + "010%".Split('0')[1][0] + "]");
Console.Write("[" + int.Parse(Convert.ToString("123".ToCharArray()[~-1])) + "]");
}
}