using System;
int a = 3;
int b = a++;
Console.WriteLine($"a is {+a++}, b is {-++b}");
int c = 3;
int d = ++c;
Console.WriteLine($"c is {-c--}, d is {~d}");


//output 
//a is 4, b is -4
//c is -4, d is -5