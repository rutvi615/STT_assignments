using System;
using System.Windows.Forms;

namespace OrderPipeline
{
    public partial class MainForm : Form
    {
        private System.ComponentModel.IContainer? components = null;
        private TextBox txtCustomerName = null!;
        private ComboBox cmbProduct = null!;
        private NumericUpDown numQuantity = null!;
        private Button btnProcessOrder = null!;
        private Label lblStatus = null!;
        private CheckBox chkExpress = null!;
        private Button btnShipOrder = null!;

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
            this.txtCustomerName = new System.Windows.Forms.TextBox();
            this.cmbProduct = new System.Windows.Forms.ComboBox();
            this.numQuantity = new System.Windows.Forms.NumericUpDown();
            this.btnProcessOrder = new System.Windows.Forms.Button();
            this.chkExpress = new System.Windows.Forms.CheckBox();
            this.btnShipOrder = new System.Windows.Forms.Button();
            this.lblStatus = new System.Windows.Forms.Label();
            ((System.ComponentModel.ISupportInitialize)(this.numQuantity)).BeginInit();
            this.SuspendLayout();
            // 
            // txtCustomerName
            // 
            this.txtCustomerName.Location = new System.Drawing.Point(16, 16);
            this.txtCustomerName.Name = "txtCustomerName";
            this.txtCustomerName.PlaceholderText = "Customer Name";
            this.txtCustomerName.Size = new System.Drawing.Size(240, 23);
            this.txtCustomerName.TabIndex = 0;
            // 
            // cmbProduct
            // 
            this.cmbProduct.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList;
            this.cmbProduct.FormattingEnabled = true;
            this.cmbProduct.Location = new System.Drawing.Point(16, 56);
            this.cmbProduct.Name = "cmbProduct";
            this.cmbProduct.Size = new System.Drawing.Size(160, 23);
            this.cmbProduct.TabIndex = 1;
            // 
            // numQuantity
            // 
            this.numQuantity.Location = new System.Drawing.Point(192, 56);
            this.numQuantity.Name = "numQuantity";
            this.numQuantity.Size = new System.Drawing.Size(64, 23);
            this.numQuantity.TabIndex = 2;
            // 
            // btnProcessOrder
            // 
            this.btnProcessOrder.Location = new System.Drawing.Point(16, 96);
            this.btnProcessOrder.Name = "btnProcessOrder";
            this.btnProcessOrder.Size = new System.Drawing.Size(120, 28);
            this.btnProcessOrder.TabIndex = 3;
            this.btnProcessOrder.Text = "Process Order";
            this.btnProcessOrder.UseVisualStyleBackColor = true;
            // 
            // chkExpress
            // 
            this.chkExpress.AutoSize = true;
            this.chkExpress.Location = new System.Drawing.Point(16, 136);
            this.chkExpress.Name = "chkExpress";
            this.chkExpress.Size = new System.Drawing.Size(63, 19);
            this.chkExpress.TabIndex = 4;
            this.chkExpress.Text = "Express";
            this.chkExpress.UseVisualStyleBackColor = true;
            // 
            // btnShipOrder
            // 
            this.btnShipOrder.Location = new System.Drawing.Point(96, 132);
            this.btnShipOrder.Name = "btnShipOrder";
            this.btnShipOrder.Size = new System.Drawing.Size(112, 28);
            this.btnShipOrder.TabIndex = 5;
            this.btnShipOrder.Text = "Ship Order";
            this.btnShipOrder.UseVisualStyleBackColor = true;
            // 
            // lblStatus
            // 
            this.lblStatus.AutoSize = true;
            this.lblStatus.Location = new System.Drawing.Point(16, 176);
            this.lblStatus.Name = "lblStatus";
            this.lblStatus.Size = new System.Drawing.Size(38, 15);
            this.lblStatus.TabIndex = 6;
            this.lblStatus.Text = "Status";
            // 
            // MainForm
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(7F, 15F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(280, 220);
            this.Controls.Add(this.lblStatus);
            this.Controls.Add(this.btnShipOrder);
            this.Controls.Add(this.chkExpress);
            this.Controls.Add(this.btnProcessOrder);
            this.Controls.Add(this.numQuantity);
            this.Controls.Add(this.cmbProduct);
            this.Controls.Add(this.txtCustomerName);
            this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.FixedDialog;
            this.MaximizeBox = false;
            this.Name = "MainForm";
            this.Text = "OrderPipeline";
            ((System.ComponentModel.ISupportInitialize)(this.numQuantity)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();
        }
    }
}
