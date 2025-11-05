public class Institute
{
internal int i = 7;
public Institute()
{
Console.Write("1");
}
public virtual void info()
{
Console.Write("2");
}
}
public class IITGN:Institute
{
public int i = 8;
public IITGN()
{
Console.Write("3");
}
public IITGN(int i)
{
Console.Write("4");
}
public override void info()
{
Console.Write("5");
}
}
class Program
{
public static void Main(string[] args)
{
Console.Write("6");
Institute ins1 = new Institute();
ins1.info();
IITGN ab101 = new IITGN(3);
ab101 = new IITGN();
ab101.info();
Console.WriteLine();
Console.WriteLine(ab101.i);
Console.WriteLine(~(((Institute)ab101).i));
}
}