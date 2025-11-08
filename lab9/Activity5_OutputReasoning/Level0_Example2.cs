using System;
class Program
{
    public void Main(string[] args)
    {
        int a = 0;
        Console.WriteLine(a++);
    }
}

/*
EXPLANATION:
============
This program will NOT RUN and will cause a COMPILATION/RUNTIME ERROR.

Reason:
- The Main method is declared as 'public void' instead of 'public static void'
- In C#, the entry point Main() method must be static
- Without the static keyword, the CLR (Common Language Runtime) cannot find 
  the entry point to start the application
- The program will not compile or run properly

ERROR: The Main method must be static to be used as an entry point.

To fix: Change 'public void Main' to 'public static void Main'
*/
