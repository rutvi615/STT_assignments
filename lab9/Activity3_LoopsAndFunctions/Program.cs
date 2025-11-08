using System;

namespace Activity3_LoopsAndFunctions
{
    class LoopOperations
    {
        // Method to demonstrate for loop
        public void ForLoopDemo()
        {
            Console.WriteLine("\n===== For Loop (1 to 10) =====");
            for (int i = 1; i <= 10; i++)
            {
                Console.Write(i + " ");
            }
            Console.WriteLine();
            Console.WriteLine("==============================\n");
        }

        // Method to demonstrate foreach loop
        public void ForEachLoopDemo()
        {
            Console.WriteLine("===== Foreach Loop (1 to 10) =====");
            int[] numbers = { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 };

            foreach (int num in numbers)
            {
                Console.Write(num + " ");
            }
            Console.WriteLine();
            Console.WriteLine("==================================\n");
        }

        // Method to demonstrate do-while loop
        public void DoWhileLoopDemo()
        {
            Console.WriteLine("===== Do-While Loop =====");
            Console.WriteLine("Enter text (type 'exit' to quit):");

            string input;
            do
            {
                Console.Write("> ");
                input = Console.ReadLine();

                // Treat Ctrl+Z (EOF) as an exit
                if (input is null)
                {
                    Console.WriteLine("(No input detected - exiting loop.)");
                    break;
                }

                input = input.Trim();

                if (!input.Equals("exit", StringComparison.OrdinalIgnoreCase))
                {
                    if (input.Length == 0)
                    {
                        Console.WriteLine("(Empty input - type text or 'exit' to quit.)");
                    }
                    else
                    {
                        Console.WriteLine($"You entered: {input}");
                    }
                }
            } while (!string.Equals(input, "exit", StringComparison.OrdinalIgnoreCase));

            Console.WriteLine("Exiting do-while loop...");
            Console.WriteLine("=========================\n");
        }

        // Static method to calculate factorial (safe with overflow check)
        public static long CalculateFactorial(int n)
        {
            if (n < 0)
            {
                Console.WriteLine("Factorial is not defined for negative numbers.");
                return -1;
            }

            long factorial = 1;
            try
            {
                checked
                {
                    for (int i = 2; i <= n; i++)
                    {
                        factorial *= i;
                    }
                }
            }
            catch (OverflowException)
            {
                Console.WriteLine("Overflow: The factorial is too large to fit in a 64-bit integer. Try a smaller n (<= 20).");
                return -1;
            }

            return factorial;
        }
    }

    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("===== Loops and Functions Demo =====\n");

            // Create object for loop demonstrations
            LoopOperations loopOps = new LoopOperations();

            // Demonstrate for loop
            loopOps.ForLoopDemo();

            // Demonstrate foreach loop
            loopOps.ForEachLoopDemo();

            // Demonstrate do-while loop
            loopOps.DoWhileLoopDemo();

            // Factorial calculation with robust input parsing
            Console.WriteLine("===== Factorial Calculation =====");
            int number = PromptForInt("Enter a non-negative integer (recommended 0..20) to calculate its factorial: ", 0);

            long result = LoopOperations.CalculateFactorial(number);
            if (result != -1)
            {
                Console.WriteLine($"Factorial of {number} = {result}");
            }
            Console.WriteLine("=================================\n");

            PauseIfInteractive();
        }

        private static int PromptForInt(string prompt, int minInclusive)
        {
            while (true)
            {
                Console.Write(prompt);
                var line = Console.ReadLine();

                if (line is null)
                {
                    Console.WriteLine("(No input detected - defaulting to 0.)");
                    return 0;
                }

                line = line.Trim();
                if (int.TryParse(line, out int value))
                {
                    if (value < minInclusive)
                    {
                        Console.WriteLine($"Please enter an integer >= {minInclusive}.");
                        continue;
                    }
                    return value;
                }
                Console.WriteLine("Invalid number. Please enter a valid integer.");
            }
        }
        private static void PauseIfInteractive()
        {
            try
            {
                if (!Console.IsInputRedirected)
                {
                    Console.WriteLine("Press any key to exit...");
                    Console.ReadKey(true);
                }
            }
            catch
            {
                // Non-interactive environment; skip pause
            }
        }
    }
}
