using System;
class Program
{
static void Main()
{
int[] nums = {0, 1, 0, 3, 12};
int pos = 0;
for (int i = 0; i < nums.Length; i++)
{
if (nums[i] != 0)
{
int temp = nums[pos];
nums[pos] = nums[i];
nums[i] = temp;
pos++;
}
}
Console.WriteLine(string.Join(", ", nums));
}
}