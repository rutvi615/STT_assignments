using System;
public class Program
{
    static void Main(string[] args)
    {
        Main(["CS202"]);
    }
}

/*
EXPLANATION:
============

This program will cause a STACK OVERFLOW error!

Reason:
- The Main method calls itself recursively: Main(["CS202"])
- This is a recursive call with different parameters
- However, there is NO BASE CASE to stop the recursion
- Each call to Main(["CS202"]) will call itself again
- This creates infinite recursion
- Eventually, the call stack will be exhausted
- This leads to a StackOverflowException

Step by step:
1. Main(args) is called initially (args from command line)
2. It calls Main(["CS202"]) 
3. That call to Main executes and calls Main(["CS202"]) again
4. That call to Main executes and calls Main(["CS202"]) again
5. ... infinite recursion ...
6. Stack overflow!

Note: The syntax ["CS202"] is C# 12+ collection expression syntax for creating
a string array with one element "CS202".

EXPECTED OUTPUT:
The program will crash with:
System.StackOverflowException: Exception of type 'System.StackOverflowException' was thrown.

OR simply crash without a catchable exception (StackOverflowException cannot be caught
in a standard try-catch block in most cases).

BEHAVIOR:
The program will crash due to infinite recursion causing stack overflow.
You might see no output or just an error message depending on the runtime environment.
*/
