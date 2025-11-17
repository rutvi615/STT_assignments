using System;

namespace EventPlayground
{
    // Custom EventArgs to carry the selected color name
    public class ColorEventArgs : EventArgs
    {
        public string ColorName { get; }

        public ColorEventArgs(string colorName)
        {
            ColorName = colorName;
        }
    }
}
