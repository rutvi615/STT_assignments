using System;
class Program
{
    int f;
    public static void Main(string[] args)
    {
        Console.WriteLine("run 1");
        Program p = new Program(new int() + "0".Length);
        for (int i = 0, _ = i; i < 5 && ++p.f >= 0; i++, Console.WriteLine(p.f++)) ;
        {
            for (; p.f == 0;) ;
            {
                Console.WriteLine(p.f);
            }
        }
        Console.WriteLine("\nrun 2");
        p = new Program(p.f);
        Console.WriteLine(p.f);
        Console.WriteLine("\nrun 3");
        p = new Program();
        Console.WriteLine(p.f);
    }
    Program() => f = 0;
    Program(int x) => f = x;
}

