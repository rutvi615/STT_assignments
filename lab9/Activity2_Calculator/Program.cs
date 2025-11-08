using System;

namespace Activity2_Calculator
{
    // Calculator class implementing OOP principles
    class Calculator
    {
        private double num1;
        private double num2;

        // Constructor
        public Calculator(double number1, double number2)
        {
            num1 = number1;
            num2 = number2;
        }

        // Method for addition
        public double Add()
        {
            return num1 + num2;
        }

        // Method for subtraction
        public double Subtract()
        {
            return num1 - num2;
        }

        // Method for multiplication
        public double Multiply()
        {
            return num1 * num2;
        }

        // Method for division
        public double Divide()
        {
            if (num2 == 0)
            {
                Console.WriteLine("Error: Division by zero!");
                return 0;
            }
            return num1 / num2;
        }

        // Method to check if sum is even or odd
        public void CheckSumEvenOdd()
        {
            double sum = Add();
            
            if (sum % 2 == 0)
            {
                Console.WriteLine($"The sum {sum} is EVEN.");
            }
            else
            {
                Console.WriteLine($"The sum {sum} is ODD.");
            }
        }

        // Method to display all results
        public void DisplayResults()
        {
            Console.WriteLine("\n===== Calculation Results =====");
            Console.WriteLine($"Number 1: {num1}");
            Console.WriteLine($"Number 2: {num2}");
            Console.WriteLine($"Addition: {num1} + {num2} = {Add()}");
            Console.WriteLine($"Subtraction: {num1} - {num2} = {Subtract()}");
            Console.WriteLine($"Multiplication: {num1} * {num2} = {Multiply()}");
            Console.WriteLine($"Division: {num1} / {num2} = {Divide()}");
            CheckSumEvenOdd();
            Console.WriteLine("================================\n");
        }
    }

    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("===== Object-Oriented Calculator =====\n");

            // Accept user input for two numbers
            Console.Write("Enter the first number: ");
            double number1 = Convert.ToDouble(Console.ReadLine());

            Console.Write("Enter the second number: ");
            double number2 = Convert.ToDouble(Console.ReadLine());

            // Create Calculator object
            Calculator calc = new Calculator(number1, number2);

            // Display all results
            calc.DisplayResults();

            Console.WriteLine("Press any key to exit...");
            Console.ReadKey();
        }
    }
}
