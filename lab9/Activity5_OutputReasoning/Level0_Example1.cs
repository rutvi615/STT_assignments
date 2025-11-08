using System; //namespace
class Program //default visibility is 'internal' if not specified
{
    public static void Main(string[] args)
    {
        int a = 0; //default visibility is 'private' (in a class)
        Console.WriteLine(a++);
    }
}

/*
EXPLANATION:
============
This program will output: 0

Reason:
- Variable 'a' is initialized to 0
- The expression a++ is a post-increment operator
- In post-increment, the current value is used first, then incremented
- So Console.WriteLine(a++) will print 0 (the current value)
- After printing, 'a' becomes 1 (but this is not printed)

OUTPUT: 0
*/
