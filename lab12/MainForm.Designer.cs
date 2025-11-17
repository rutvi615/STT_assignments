namespace OrderPipeline
{
    partial class MainForm
    {
        private System.ComponentModel.IContainer? components = null;
        private System.Windows.Forms.TextBox txtCustomerName = null!;
        private System.Windows.Forms.ComboBox cmbProduct = null!;
        private System.Windows.Forms.NumericUpDown numQuantity = null!;
        private System.Windows.Forms.Button btnProcessOrder = null!;
        private System.Windows.Forms.Label lblStatus = null!;
        private System.Windows.Forms.CheckBox chkExpress = null!;
        private System.Windows.Forms.Button btnShipOrder = null!;

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















































}    }        }            this.PerformLayout();            this.ResumeLayout(false);            ((System.ComponentModel.ISupportInitialize)(this.numQuantity)).EndInit();            this.Text = "OrderPipeline";            this.Name = "MainForm";            this.MaximizeBox = false;            this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.FixedDialog;            this.Controls.Add(this.txtCustomerName);            this.Controls.Add(this.cmbProduct);            this.Controls.Add(this.numQuantity);            this.Controls.Add(this.btnProcessOrder);            this.Controls.Add(this.chkExpress);            this.Controls.Add(this.btnShipOrder);            this.Controls.Add(this.lblStatus);            this.ClientSize = new System.Drawing.Size(280, 220);            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;            this.AutoScaleDimensions = new System.Drawing.SizeF(7F, 15F);            //             // MainForm            //             this.lblStatus.Text = "Status";            this.lblStatus.TabIndex = 6;            this.lblStatus.Size = new System.Drawing.Size(38, 15);            this.lblStatus.Name = "lblStatus";            this.lblStatus.Location = new System.Drawing.Point(16, 176);            this.lblStatus.AutoSize = true;            //             // lblStatus            //             this.btnShipOrder.UseVisualStyleBackColor = true;            this.btnShipOrder.Text = "Ship Order";            this.btnShipOrder.TabIndex = 5;            this.btnShipOrder.Size = new System.Drawing.Size(112, 28);            this.btnShipOrder.Name = "btnShipOrder";            this.btnShipOrder.Location = new System.Drawing.Point(96, 132);            //             // btnShipOrder            //             this.chkExpress.UseVisualStyleBackColor = true;            this.chkExpress.Text = "Express";            this.chkExpress.TabIndex = 4;            this.chkExpress.Size = new System.Drawing.Size(63, 19);            this.chkExpress.Name = "chkExpress";            this.chkExpress.Location = new System.Drawing.Point(16, 136);            this.chkExpress.AutoSize = true;            //             // chkExpress            //             this.btnProcessOrder.UseVisualStyleBackColor = true;            this.btnProcessOrder.Text = "Process Order";            this.btnProcessOrder.TabIndex = 3;            this.btnProcessOrder.Size = new System.Drawing.Size(120, 28);            this.btnProcessOrder.Name = "btnProcessOrder";            this.btnProcessOrder.Location = new System.Drawing.Point(16, 96);            //             // btnProcessOrder            //             this.numQuantity.Minimum = 0;            this.numQuantity.TabIndex = 2;            this.numQuantity.Size = new System.Drawing.Size(64, 23);            this.numQuantity.Name = "numQuantity";            this.numQuantity.Location = new System.Drawing.Point(192, 56);            //             // numQuantity            //             this.cmbProduct.TabIndex = 1;            this.cmbProduct.Size = new System.Drawing.Size(160, 23);            this.cmbProduct.Name = "cmbProduct";            this.cmbProduct.Location = new System.Drawing.Point(16, 56);            this.cmbProduct.FormattingEnabled = true;            this.cmbProduct.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList;            //             // cmbProduct            //             this.txtCustomerName.PlaceholderText = "Customer Name";            this.txtCustomerName.TabIndex = 0;            this.txtCustomerName.Size = new System.Drawing.Size(240, 23);            this.txtCustomerName.Name = "txtCustomerName";            this.txtCustomerName.Location = new System.Drawing.Point(16, 16);            //             // txtCustomerName            //             this.SuspendLayout();            ((System.ComponentModel.ISupportInitialize)(this.numQuantity)).BeginInit();            this.btnShipOrder = new System.Windows.Forms.Button();            this.chkExpress = new System.Windows.Forms.CheckBox();            this.lblStatus = new System.Windows.Forms.Label();            this.btnProcessOrder = new System.Windows.Forms.Button();            this.numQuantity = new System.Windows.Forms.NumericUpDown();            this.cmbProduct = new System.Windows.Forms.ComboBox();            this.txtCustomerName = new System.Windows.Forms.TextBox();            this.components = new System.ComponentModel.Container();        {
n        private void InitializeComponent()        }            base.Dispose(disposing);            }                components.Dispose();            {            if (disposing && (components != null))        {n        protected override void Dispose(bool disposing)