using System;
class AlertEventArgs : EventArgs
{
public string Info { get; }
public AlertEventArgs(string info) => Info = info;
}
class Sensor
{
public event EventHandler<AlertEventArgs> ThresholdReached;
public void Check(int value)
{
Console.Write("[Check]");
if (value > 50)
ThresholdReached?.Invoke(this, new AlertEventArgs("High"));
Console.Write("[Done]");
}
}
class Program
{
static void Main()
{
Sensor s = new Sensor();
s.ThresholdReached += (sender, e) =>
{
Console.Write("{" + e.Info + "}");
if (e.Info == "High")
((Sensor)sender).Check(30);
};
s.ThresholdReached += (sender, e) =>
Console.Write("(Alert)");
s.Check(80);
}
}