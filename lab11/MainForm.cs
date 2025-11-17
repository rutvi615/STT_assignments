using System;
using System.Drawing;
using System.Windows.Forms;

namespace EventPlayground
{
    public partial class MainForm : Form
    {
        // Custom delegate declarations (visible in source for the lab submission)
        public delegate void ColorChangedHandler(object sender, ColorEventArgs e);
        public delegate void TextChangedHandler(object sender, EventArgs e);

        // Custom events using the delegates
        public event ColorChangedHandler ColorChangedEvent;
        public event TextChangedHandler TextChangedEvent;

        public MainForm()
        {
            InitializeComponent();

            // Populate ComboBox with color options
            cmbColors.Items.AddRange(new string[] { "Red", "Green", "Blue" });
            cmbColors.SelectedIndex = 0;

            // Subscribe multiple methods to the ColorChangedEvent (multicast)
            this.ColorChangedEvent += UpdateLabelColor;
            this.ColorChangedEvent += ShowNotification;

            // Subscribe to TextChangedEvent
            this.TextChangedEvent += UpdateLabelText;

            // Wire control clicks to raise the custom events (we do not rely solely on built-in Click behavior)
            btnChangeColor.Click += BtnChangeColor_Click;
            btnChangeText.Click += BtnChangeText_Click;
        }

        private void BtnChangeColor_Click(object sender, EventArgs e)
        {
            var selected = cmbColors.SelectedItem?.ToString() ?? "Red";
            // Invoke custom ColorChangedEvent with ColorEventArgs
            ColorChangedEvent?.Invoke(this, new ColorEventArgs(selected));
        }

        private void BtnChangeText_Click(object sender, EventArgs e)
        {
            // Invoke custom TextChangedEvent
            TextChangedEvent?.Invoke(this, EventArgs.Empty);
        }

        // Subscriber: Updates the label's ForeColor
        private void UpdateLabelColor(object sender, ColorEventArgs e)
        {
            var color = Color.FromName(e.ColorName);
            if (color.IsKnownColor || color.IsNamedColor)
            {
                lblMessage.ForeColor = color;
            }
        }

        // Subscriber: Shows a notification message box (demonstrates multiple subscribers)
        private void ShowNotification(object sender, ColorEventArgs e)
        {
            MessageBox.Show(this, $"Selected color: {e.ColorName}", "Color Changed", MessageBoxButtons.OK, MessageBoxIcon.Information);
        }

        // Subscriber: Updates the label text with current date/time
        private void UpdateLabelText(object sender, EventArgs e)
        {
            lblMessage.Text = $"Current date and time: {DateTime.Now}";
        }
    }
}
