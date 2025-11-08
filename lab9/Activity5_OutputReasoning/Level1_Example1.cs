class Program
{
    public static void Main(string[] args)
    {
        int a = 0;
        int b = a++;
        Console.WriteLine(a++.ToString(),++a,-a++);
        Console.WriteLine((a++).ToString() + (-a++).ToString());
        Console.WriteLine(~b);
    }
}

/*
EXPLANATION (Step by Step):
============================

Initial State:
- a = 0
- int b = a++;  → b = 0 (post-increment), then a = 1

After line 2:
- a = 1, b = 0

Line 3: Console.WriteLine(a++.ToString(), ++a, -a++);
- a++.ToString() → "1" (uses a=1, then a becomes 2)
- ++a → 3 (pre-increment, a becomes 3 first, then uses 3)
- -a++ → -(3) = -3 (uses a=3, then a becomes 4)
- However, Console.WriteLine with multiple arguments only prints the first argument
- The format string is "1" but there are extra parameters that are ignored
- Prints: 1
- After this line: a = 4

Line 4: Console.WriteLine((a++).ToString() + (-a++).ToString());
- (a++).ToString() → "4" (uses a=4, then a becomes 5)
- (-a++).ToString() → "-5" (uses a=5, then a becomes 6)
- String concatenation: "4" + "-5" = "4-5"
- Prints: 4-5
- After this line: a = 6

Line 5: Console.WriteLine(~b);
- b = 0
- ~0 (bitwise NOT) = -1 (in two's complement representation)
- Prints: -1

FINAL OUTPUT:
1
4-5
-1

Note: The bitwise NOT operator (~) inverts all bits. For 0:
Binary: 00000000 00000000 00000000 00000000
After ~: 11111111 11111111 11111111 11111111 (which is -1 in two's complement)
*/
