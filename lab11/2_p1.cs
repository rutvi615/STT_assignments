using System;
class NotifyEventArgs : EventArgs
{
public string Message { get; }
public NotifyEventArgs(string msg) => Message = msg;
}
class Notifier
{
public event EventHandler<NotifyEventArgs> OnNotify;
public void Trigger(string msg)
{
Console.Write("[Start]");
OnNotify?.Invoke(this, new NotifyEventArgs(msg));
Console.Write("[End]");
}
}
class Program
{
static void Main()
{
Notifier n = new Notifier();
n.OnNotify += (s, e) =>
{
Console.Write("{" + e.Message + "}");
};
n.OnNotify += (s, e) =>
{
Console.Write("(Nested)");
if (e.Message == "Ping")
((Notifier)s).Trigger("Pong");
};
n.Trigger("Ping");
}
}