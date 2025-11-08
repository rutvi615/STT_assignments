using System;

namespace Activity4_Arrays
{
    class ArrayOperations
    {
        // Method to implement Bubble Sort
        public void BubbleSort(int[] arr)
        {
            int n = arr.Length;
            
            Console.WriteLine("\nArray before sorting:");
            PrintArray(arr);

            // Bubble Sort Algorithm
            for (int i = 0; i < n - 1; i++)
            {
                for (int j = 0; j < n - i - 1; j++)
                {
                    if (arr[j] > arr[j + 1])
                    {
                        // Swap arr[j] and arr[j+1]
                        int temp = arr[j];
                        arr[j] = arr[j + 1];
                        arr[j + 1] = temp;
                    }
                }
            }

            Console.WriteLine("Array after sorting:");
            PrintArray(arr);
        }

        // Method to print 1D array
        public void PrintArray(int[] arr)
        {
            foreach (int element in arr)
            {
                Console.Write(element + " ");
            }
            Console.WriteLine();
        }

        // Method to convert 2D array to 1D array in Row Major Order
        public int[] ConvertToRowMajor(int[,] arr2D)
        {
            int rows = arr2D.GetLength(0);
            int cols = arr2D.GetLength(1);
            int[] arr1D = new int[rows * cols];
            int index = 0;

            for (int i = 0; i < rows; i++)
            {
                for (int j = 0; j < cols; j++)
                {
                    arr1D[index++] = arr2D[i, j];
                }
            }

            return arr1D;
        }

        // Method to convert 2D array to 1D array in Column Major Order
        public int[] ConvertToColumnMajor(int[,] arr2D)
        {
            int rows = arr2D.GetLength(0);
            int cols = arr2D.GetLength(1);
            int[] arr1D = new int[rows * cols];
            int index = 0;

            for (int j = 0; j < cols; j++)
            {
                for (int i = 0; i < rows; i++)
                {
                    arr1D[index++] = arr2D[i, j];
                }
            }

            return arr1D;
        }

        // Method to print 2D array
        public void Print2DArray(int[,] arr)
        {
            int rows = arr.GetLength(0);
            int cols = arr.GetLength(1);

            for (int i = 0; i < rows; i++)
            {
                for (int j = 0; j < cols; j++)
                {
                    Console.Write(arr[i, j] + "\t");
                }
                Console.WriteLine();
            }
        }

        // Method to multiply two matrices
        public int[,] MatrixMultiplication(int[,] A, int[,] B)
        {
            int rowsA = A.GetLength(0);
            int colsA = A.GetLength(1);
            int rowsB = B.GetLength(0);
            int colsB = B.GetLength(1);

            // Check if multiplication is possible
            if (colsA != rowsB)
            {
                Console.WriteLine("Matrix multiplication not possible!");
                Console.WriteLine($"Columns of A ({colsA}) must equal rows of B ({rowsB})");
                return null;
            }

            // Result matrix C will be of size rowsA x colsB
            int[,] C = new int[rowsA, colsB];

            // Perform multiplication
            for (int i = 0; i < rowsA; i++)
            {
                for (int j = 0; j < colsB; j++)
                {
                    C[i, j] = 0;
                    for (int k = 0; k < colsA; k++)
                    {
                        C[i, j] += A[i, k] * B[k, j];
                    }
                }
            }

            return C;
        }
    }

    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("===== Array Operations Demo =====\n");

            ArrayOperations arrayOps = new ArrayOperations();

            // ===== Bubble Sort =====
            Console.WriteLine("===== 1. Bubble Sort =====");
            int[] arr = { 64, 34, 25, 12, 22, 11, 90 };
            arrayOps.BubbleSort(arr);
            Console.WriteLine();

            // ===== 2D to 1D Array Conversion =====
            Console.WriteLine("===== 2. 2D to 1D Array Conversion =====");
            int[,] arr2D = {
                { 1, 2, 3 },
                { 4, 5, 6 },
                { 7, 8, 9 }
            };

            Console.WriteLine("\nOriginal 2D Array:");
            arrayOps.Print2DArray(arr2D);

            Console.WriteLine("\n(i) Row Major Order:");
            int[] rowMajor = arrayOps.ConvertToRowMajor(arr2D);
            arrayOps.PrintArray(rowMajor);

            Console.WriteLine("\n(ii) Column Major Order:");
            int[] colMajor = arrayOps.ConvertToColumnMajor(arr2D);
            arrayOps.PrintArray(colMajor);
            Console.WriteLine();

            // ===== Matrix Multiplication =====
            Console.WriteLine("===== 3. Matrix Multiplication =====");
            
            int[,] matrixA = {
                { 1, 2, 3 },
                { 4, 5, 6 }
            };

            int[,] matrixB = {
                { 7, 8 },
                { 9, 10 },
                { 11, 12 }
            };

            Console.WriteLine("\nMatrix A:");
            arrayOps.Print2DArray(matrixA);

            Console.WriteLine("\nMatrix B:");
            arrayOps.Print2DArray(matrixB);

            int[,] matrixC = arrayOps.MatrixMultiplication(matrixA, matrixB);

            if (matrixC != null)
            {
                Console.WriteLine("\nMatrix C (A × B):");
                arrayOps.Print2DArray(matrixC);
            }

            Console.WriteLine("\nPress any key to exit...");
            Console.ReadKey();
        }
    }
}
