using System;
/*you can also write top level code outside of a class. C# takes
care of this by providing internal entry point Main*/
Console.WriteLine("int x = 3;");
Console.WriteLine("int y = 2 + ++x;");
int x = 3; //default visibility is 'internal' (outside a class)
int y = 2 + ++x;
Console.WriteLine($"x = {x} and y = {y}");
Console.WriteLine("x = 3 << 2;");
Console.WriteLine("y = 10 >> 1;");
x = 3 << 2;
y = 10 >> 1;
Console.WriteLine($"x = {x} and y = {y}");
x = ~x;
y = ~y;
Console.WriteLine($"x = {x} and y = {y}");

/*
EXPLANATION (Step by Step):
============================

This uses C# 9.0+ top-level statements feature.

Line 1-2: Prints literal strings
Output: int x = 3;
        int y = 2 + ++x;

Line 3-4: Variable initialization
- x = 3
- y = 2 + ++x → ++x makes x = 4 first (pre-increment), then y = 2 + 4 = 6

Line 5: Prints interpolated string
Output: x = 4 and y = 6

Line 6-7: Prints literal strings
Output: x = 3 << 2;
        y = 10 >> 1;

Line 8-9: Bitwise shift operations
- x = 3 << 2 (left shift)
  Binary: 3 = 0011
  Shift left by 2: 1100 = 12
  x = 12
  
- y = 10 >> 1 (right shift)
  Binary: 10 = 1010
  Shift right by 1: 0101 = 5
  y = 5

Line 10: Prints interpolated string
Output: x = 12 and y = 5

Line 11-13: Bitwise NOT operations
- x = ~x → ~12
  Binary: 12 = 00000000 00000000 00000000 00001100
  After ~:    11111111 11111111 11111111 11110011 = -13 (two's complement)
  
- y = ~y → ~5
  Binary: 5 =  00000000 00000000 00000000 00000101
  After ~:     11111111 11111111 11111111 11111010 = -6 (two's complement)

Line 14: Prints interpolated string
Output: x = -13 and y = -6

FINAL OUTPUT:
int x = 3;
int y = 2 + ++x;
x = 4 and y = 6
x = 3 << 2;
y = 10 >> 1;
x = 12 and y = 5
x = -13 and y = -6
*/
