using System;
class LimitEventArgs : EventArgs
{
public int CurrentValue { get; }
public LimitEventArgs(int val) => CurrentValue = val;
}
class Counter
{
public event EventHandler<LimitEventArgs> LimitReached;
public event EventHandler<LimitEventArgs> MilestoneReached;
private int value = 0;
public void Increment()
{
value++;
Console.Write(">" + value);
// Fire Milestone event every 2nd increment
if (value % 2 == 0)
MilestoneReached?.Invoke(this, new LimitEventArgs(value));
// Fire Limit event every 3rd increment
if (value % 3 == 0)
LimitReached?.Invoke(this, new LimitEventArgs(value));
}
}
class Program
{
static void Main()
{
Counter c = new Counter();
// Subscribers for LimitReached
c.LimitReached += (s, e) => Console.Write("[L" + e.CurrentValue + "]");
c.LimitReached += (s, e) => Console.Write("(Reset)");
// Subscribers for MilestoneReached
c.MilestoneReached += (s, e) =>
{
Console.Write("[M" + e.CurrentValue + "]");
if (e.CurrentValue == 4)
Console.Write("{Alert}");
};
for (int i = 0; i < 6; i++)
c.Increment();
}
}