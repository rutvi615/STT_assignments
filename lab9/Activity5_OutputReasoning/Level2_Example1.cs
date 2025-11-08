using System;
public class Program
{
    static void Main()
    {
        try
        {
            int i=int.MaxValue;
            Console.WriteLine(-(i+1)-i);
            for(i=0; i<=int.MaxValue;i++); //note semicolon here
            Console.WriteLine("Program ended!");
        }
        catch(Exception ex)
        {
            Console.WriteLine(ex.ToString());
        }
    }
}

/*
EXPLANATION (Step by Step):
============================

Line 1: int i = int.MaxValue;
- int.MaxValue = 2,147,483,647 (maximum value for 32-bit signed integer)

Line 2: Console.WriteLine(-(i+1)-i);
- i + 1 = 2,147,483,647 + 1 = -2,147,483,648 (INTEGER OVERFLOW!)
  When you add 1 to int.MaxValue, it wraps around to int.MinValue
- -(i+1) = -(-2,147,483,648) = 2,147,483,648 (but stored as int)
  Wait! 2,147,483,648 cannot fit in int, so there's overflow again
  Actually, -(-2,147,483,648) = 2,147,483,648, but in int representation
  this becomes -2,147,483,648 (overflow wraps)
  
Actually, let's be precise:
- i = 2,147,483,647
- i+1 = -2,147,483,648 (overflow to int.MinValue)
- -(i+1) = -(-2,147,483,648) = 2,147,483,648
  But 2,147,483,648 cannot be represented as int, so it wraps to -2,147,483,648
- -(i+1) - i = -2,147,483,648 - 2,147,483,647 = -4,294,967,295
  This also overflows: result is 1

Wait, let me recalculate properly with overflow semantics:
i = 2147483647
i+1 = -2147483648 (overflow wraps to MinValue)
-(i+1) = -(-2147483648) = 2147483648, but as int this is -2147483648 (abs of MinValue overflows)
-(i+1) - i = -2147483648 - 2147483647 = 1 (with wrap-around)

Output: 1

Line 3: for(i=0; i<=int.MaxValue; i++);
- This is an INFINITE LOOP (almost)
- Starts with i=0
- Loop continues while i <= int.MaxValue
- When i reaches int.MaxValue (2,147,483,647), i++ causes overflow
- i becomes int.MinValue (-2,147,483,648)
- But -2,147,483,648 <= 2,147,483,647 is TRUE!
- So the loop continues... eventually i will reach MaxValue again and overflow
- This creates an infinite loop!
- However, in practice, this loop will eventually complete after cycling through 
  all integer values multiple times (if no timeout)

Actually, the loop will:
- Go from 0 to 2,147,483,647 (MaxValue)
- Then overflow to -2,147,483,648 (MinValue)
- Continue from MinValue back to MaxValue
- This is an infinite loop!

In practice: The program will appear to hang and "Program ended!" will likely NEVER print
(unless there's a timeout or the user terminates it)

EXPECTED OUTPUT (if loop somehow exits):
1
Program ended!

ACTUAL BEHAVIOR:
1
[Program hangs in infinite loop]

Note: In unchecked context (default), integer overflow doesn't throw exceptions.
The for loop will run indefinitely because when i=MaxValue and i++ executes,
i wraps to MinValue, which is still <= MaxValue.
*/
