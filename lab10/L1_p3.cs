public class A
{
public virtual void f1()
{
Console.WriteLine("f1");
}
}
public class B:A
{
public override void f1() => Console.WriteLine("f2");
}
class Program
{
static int i=0;
public event funcPtr handler;
public delegate void funcPtr();
public void destroy()
{
if (i == 6)
return;
else
{
Console.WriteLine(i++);
destroy();
}
}
public static void Main(string[] args)
{
Program p = new Program();
p.handler += new funcPtr((new A()).f1);
p.handler += new funcPtr((new B()).f1);
p.handler();
p.handler -= new funcPtr((new B()).f1);
p.handler -= new funcPtr((new A()).f1);
p?.destroy(); //check here8 about ?. operator
p = null;
i = -6;
p?.destroy();
(new Program())?.destroy();
}
}