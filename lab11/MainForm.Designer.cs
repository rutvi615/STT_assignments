namespace EventPlayground
{
    partial class MainForm
    {
        private System.ComponentModel.IContainer components = null;
        private System.Windows.Forms.Button btnChangeColor;
        private System.Windows.Forms.Button btnChangeText;
        private System.Windows.Forms.Label lblMessage;
        private System.Windows.Forms.ComboBox cmbColors;

        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        private void InitializeComponent()
        {
            this.components = new System.ComponentModel.Container();
            this.btnChangeColor = new System.Windows.Forms.Button();
            this.btnChangeText = new System.Windows.Forms.Button();
            this.lblMessage = new System.Windows.Forms.Label();
            this.cmbColors = new System.Windows.Forms.ComboBox();
            this.SuspendLayout();
            // 
            // btnChangeColor
            // 
            this.btnChangeColor.Location = new System.Drawing.Point(30, 110);
            this.btnChangeColor.Name = "btnChangeColor";
            this.btnChangeColor.Size = new System.Drawing.Size(120, 30);
            this.btnChangeColor.TabIndex = 0;
            this.btnChangeColor.Text = "Change Color";
            this.btnChangeColor.UseVisualStyleBackColor = true;
            // 
            // btnChangeText
            // 
            this.btnChangeText.Location = new System.Drawing.Point(170, 110);
            this.btnChangeText.Name = "btnChangeText";
            this.btnChangeText.Size = new System.Drawing.Size(120, 30);
            this.btnChangeText.TabIndex = 1;
            this.btnChangeText.Text = "Change Text";
            this.btnChangeText.UseVisualStyleBackColor = true;
            // 
            // lblMessage
            // 
            this.lblMessage.AutoSize = false;
            this.lblMessage.Font = new System.Drawing.Font("Segoe UI", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point);
            this.lblMessage.Location = new System.Drawing.Point(30, 30);
            this.lblMessage.Name = "lblMessage";
            this.lblMessage.Size = new System.Drawing.Size(480, 21);
            this.lblMessage.TabIndex = 2;
            this.lblMessage.Text = "Welcome to Events Lab";
            // 
            // cmbColors
            // 
            this.cmbColors.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList;
            this.cmbColors.FormattingEnabled = true;
            this.cmbColors.Location = new System.Drawing.Point(30, 70);
            this.cmbColors.Name = "cmbColors";
            this.cmbColors.Size = new System.Drawing.Size(460, 23);
            this.cmbColors.TabIndex = 3;
            // 
            // MainForm
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(7F, 15F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(540, 170);
            this.Controls.Add(this.cmbColors);
            this.Controls.Add(this.lblMessage);
            this.Controls.Add(this.btnChangeText);
            this.Controls.Add(this.btnChangeColor);
            this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.FixedDialog;
            this.MaximizeBox = false;
            this.Name = "MainForm";
            this.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen;
            this.Text = "EventPlayground - Events & Delegates";
            this.ResumeLayout(false);
            this.PerformLayout();
        }
    }
}
