using System;
using System.Windows.Forms;

namespace OrderPipeline
{
    public partial class MainForm : Form
    {
        // Events for the order pipeline
        public event EventHandler<OrderEventArgs>? OrderCreated;
        public event EventHandler<OrderEventArgs>? OrderConfirmed;
        public event EventHandler<OrderEventArgs>? OrderRejected;
        public event EventHandler<ShipEventArgs>? OrderShipped;

        private bool lastOrderConfirmed = false;

        public MainForm()
        {
            InitializeComponent();

            // Wire up subscribers for order creation
            OrderCreated += ValidateOrder;
            OrderCreated += DisplayOrderInfo;
            OrderRejected += ShowRejection;
            OrderConfirmed += ShowConfirmation;

            // Shipping subscriber always present for dispatch display
            OrderShipped += ShowDispatch;

            // UI wiring
            btnProcessOrder.Click += BtnProcessOrder_Click;
            btnShipOrder.Click += BtnShipOrder_Click;
            chkExpress.CheckedChanged += ChkExpress_CheckedChanged;

            // Initialize controls
            cmbProduct.Items.AddRange(new object[] { "Laptop", "Mouse", "Keyboard" });
            if (cmbProduct.Items.Count > 0) cmbProduct.SelectedIndex = 0;
            numQuantity.Minimum = 0;
            lblStatus.Text = "Ready";
        }

        private void BtnProcessOrder_Click(object? sender, EventArgs e)
        {
            var customer = txtCustomerName.Text.Trim();
            var product = cmbProduct.SelectedItem?.ToString() ?? cmbProduct.Text;
            var quantity = (int)numQuantity.Value;

            var args = new OrderEventArgs(customer, product ?? string.Empty, quantity);

            // Reset confirmation flag until confirmed in the chain
            lastOrderConfirmed = false;

            // Raise the OrderCreated event (multicast)
            OrderCreated?.Invoke(this, args);
        }

        private void ValidateOrder(object? sender, OrderEventArgs e)
        {
            if (e.Quantity > 0)
            {
                lblStatus.Text = "Validated";
                // Chain order confirmed event when validation succeeds
                OrderConfirmed?.Invoke(this, e);
            }
            else
            {
                // Chain rejection when validation fails
                OrderRejected?.Invoke(this, e);
            }
        }

        private void DisplayOrderInfo(object? sender, OrderEventArgs e)
        {
            MessageBox.Show($"Order Summary:\nCustomer: {e.Customer}\nProduct: {e.Product}\nQuantity: {e.Quantity}", "Order Info");
        }

        private void ShowRejection(object? sender, OrderEventArgs e)
        {
            lblStatus.Text = "Order Invalid – Please retry";
        }

        private void ShowConfirmation(object? sender, OrderEventArgs e)
        {
            lblStatus.Text = $"Order Processed Successfully for {e.Customer}";
            lastOrderConfirmed = true;
        }

        // --- Shipping logic ---
        private void BtnShipOrder_Click(object? sender, EventArgs e)
        {
            if (!lastOrderConfirmed)
            {
                MessageBox.Show("Cannot ship: previous order not confirmed.", "Shipping Error");
                return;
            }

            var product = cmbProduct.SelectedItem?.ToString() ?? cmbProduct.Text;
            var express = chkExpress.Checked;

            // Manage dynamic subscriber: add NotifyCourier only if express is selected
            if (express)
            {
                // Ensure we don't double-subscribe
                OrderShipped -= NotifyCourier;
                OrderShipped += NotifyCourier;
            }
            else
            {
                // Remove notify if present
                OrderShipped -= NotifyCourier;
            }

            var shipArgs = new ShipEventArgs(product ?? string.Empty, express);
            OrderShipped?.Invoke(this, shipArgs);
        }

        private void ShowDispatch(object? sender, ShipEventArgs e)
        {
            lblStatus.Text = $"Product dispatched: {e.Product}";
        }

        private void NotifyCourier(object? sender, ShipEventArgs e)
        {
            if (e.Express)
            {
                MessageBox.Show("Express delivery initiated!", "Courier Notification");
            }
        }

        private void ChkExpress_CheckedChanged(object? sender, EventArgs e)
        {
            lblStatus.Text = chkExpress.Checked ? "Express selected" : "Regular shipping selected";
        }
    }

    // Custom EventArgs used in the app
    public class OrderEventArgs : EventArgs
    {
        public string Customer { get; }
        public string Product { get; }
        public int Quantity { get; }

        public OrderEventArgs(string customer, string product, int quantity)
        {
            Customer = customer;
            Product = product;
            Quantity = quantity;
        }
    }

    public class ShipEventArgs : EventArgs
    {
        public string Product { get; }
        public bool Express { get; }

        public ShipEventArgs(string product, bool express)
        {
            Product = product;
            Express = express;
        }
    }
}using System;
using System.Windows.Forms;
using System;
using System.Windows.Forms;

namespace OrderPipeline
{
    public partial class MainForm : Form
    {
        // Events for the order pipeline
        public event EventHandler<OrderEventArgs>? OrderCreated;
        public event EventHandler<OrderEventArgs>? OrderConfirmed;
        public event EventHandler<OrderEventArgs>? OrderRejected;
        public event EventHandler<ShipEventArgs>? OrderShipped;

        private bool lastOrderConfirmed = false;

        public MainForm()
        {
            InitializeComponent();

            // Wire up subscribers for order creation
            OrderCreated += ValidateOrder;
            OrderCreated += DisplayOrderInfo;
            OrderRejected += ShowRejection;
            OrderConfirmed += ShowConfirmation;

            // Shipping subscriber always present for dispatch display
            OrderShipped += ShowDispatch;

            // UI wiring
            btnProcessOrder.Click += BtnProcessOrder_Click;
            btnShipOrder.Click += BtnShipOrder_Click;
            chkExpress.CheckedChanged += ChkExpress_CheckedChanged;

            // Initialize controls
            cmbProduct.Items.AddRange(new object[] { "Laptop", "Mouse", "Keyboard" });
            if (cmbProduct.Items.Count > 0) cmbProduct.SelectedIndex = 0;
            numQuantity.Minimum = 0;
            lblStatus.Text = "Ready";
        }

        private void BtnProcessOrder_Click(object? sender, EventArgs e)
        {
            var customer = txtCustomerName.Text.Trim();
            var product = cmbProduct.SelectedItem?.ToString() ?? cmbProduct.Text;
            var quantity = (int)numQuantity.Value;

            var args = new OrderEventArgs(customer, product ?? string.Empty, quantity);

            // Reset confirmation flag until confirmed in the chain
            lastOrderConfirmed = false;

            // Raise the OrderCreated event (multicast)
            OrderCreated?.Invoke(this, args);
        }

        private void ValidateOrder(object? sender, OrderEventArgs e)
        {
            if (e.Quantity > 0)
            {
                lblStatus.Text = "Validated";
                // Chain order confirmed event when validation succeeds
                OrderConfirmed?.Invoke(this, e);
            }
            else
            {
                // Chain rejection when validation fails
                OrderRejected?.Invoke(this, e);
            }
        }

        private void DisplayOrderInfo(object? sender, OrderEventArgs e)
        {
            MessageBox.Show($"Order Summary:\nCustomer: {e.Customer}\nProduct: {e.Product}\nQuantity: {e.Quantity}", "Order Info");
        }

        private void ShowRejection(object? sender, OrderEventArgs e)
        {
            lblStatus.Text = "Order Invalid – Please retry";
        }

        private void ShowConfirmation(object? sender, OrderEventArgs e)
        {
            lblStatus.Text = $"Order Processed Successfully for {e.Customer}";
            lastOrderConfirmed = true;
        }

        // --- Shipping logic ---
        private void BtnShipOrder_Click(object? sender, EventArgs e)
        {
            if (!lastOrderConfirmed)
            {
                MessageBox.Show("Cannot ship: previous order not confirmed.", "Shipping Error");
                return;
            }

            var product = cmbProduct.SelectedItem?.ToString() ?? cmbProduct.Text;
            var express = chkExpress.Checked;

            // Manage dynamic subscriber: add NotifyCourier only if express is selected
            if (express)
            {
                // Ensure we don't double-subscribe
                OrderShipped -= NotifyCourier;
                OrderShipped += NotifyCourier;
            }
            else
            {
                // Remove notify if present
                OrderShipped -= NotifyCourier;
            }

            var shipArgs = new ShipEventArgs(product ?? string.Empty, express);
            OrderShipped?.Invoke(this, shipArgs);
        }

        private void ShowDispatch(object? sender, ShipEventArgs e)
        {
            lblStatus.Text = $"Product dispatched: {e.Product}";
        }

        private void NotifyCourier(object? sender, ShipEventArgs e)
        {
            if (e.Express)
            {
                MessageBox.Show("Express delivery initiated!", "Courier Notification");
            }
        }

        private void ChkExpress_CheckedChanged(object? sender, EventArgs e)
        {
            lblStatus.Text = chkExpress.Checked ? "Express selected" : "Regular shipping selected";
        }
    }

    // Custom EventArgs used in the app
    public class OrderEventArgs : EventArgs
    {
        public string Customer { get; }
        public string Product { get; }
        public int Quantity { get; }

        public OrderEventArgs(string customer, string product, int quantity)
        {
            Customer = customer;
            Product = product;
            Quantity = quantity;
        }
    }

    public class ShipEventArgs : EventArgs
    {
        public string Product { get; }
        public bool Express { get; }

        public ShipEventArgs(string product, bool express)
        {
            Product = product;
            Express = express;
        }
    }
}


























}    }
n        public ShipEventArgs(string p, bool ex) => (Product, Express) = (p, ex);        public bool Express { get; }        public string Product { get; }    {    public class ShipEventArgs : EventArgs    }
n        public OrderEventArgs(string customer, string product, int quantity) => (Customer, Product, Quantity) = (customer, product, quantity);        public int Quantity { get; }        public string Product { get; }        public string Customer { get; }    {    public class OrderEventArgs : EventArgs    // Custom EventArgs used in the app    }        }            lblStatus.Text = chkExpress.Checked ? "Express selected" : "Regular shipping selected";        {        private void ChkExpress_CheckedChanged(object? sender, EventArgs e)        }            }                MessageBox.Show("Express delivery initiated!", "Courier Notification");            {            if (e.Express)        {        private void NotifyCourier(object? sender, ShipEventArgs e)        }            lblStatus.Text = $"Product dispatched: {e.Product}";        {        private void ShowDispatch(object? sender, ShipEventArgs e)        }            OrderShipped?.Invoke(this, shipArgs);
n            var shipArgs = new ShipEventArgs(product ?? string.Empty, express);            }                OrderShipped -= NotifyCourier;                // Remove notify if present            {            else            }                OrderShipped += NotifyCourier;                OrderShipped -= NotifyCourier;                // Ensure we don't double-subscribe            {            if (express)
n            // Manage dynamic subscriber: add NotifyCourier only if express is selected            var express = chkExpress.Checked;
n            var product = cmbProduct.SelectedItem?.ToString() ?? cmbProduct.Text;            }                return;                MessageBox.Show("Cannot ship: previous order not confirmed.", "Shipping Error");            {            if (!lastOrderConfirmed)        {        private void BtnShipOrder_Click(object? sender, EventArgs e)        // --- Shipping logic ---        }            lastOrderConfirmed = true;            lblStatus.Text = $"Order Processed Successfully for {e.Customer}";        {        private void ShowConfirmation(object? sender, OrderEventArgs e)        }            lblStatus.Text = "Order Invalid – Please retry";        {        private void ShowRejection(object? sender, OrderEventArgs e)        }            MessageBox.Show($"Order Summary:\nCustomer: {e.Customer}\nProduct: {e.Product}\nQuantity: {e.Quantity}", "Order Info");        {        private void DisplayOrderInfo(object? sender, OrderEventArgs e)        }            }                OrderRejected?.Invoke(this, e);                // Chain rejection when validation fails            {            else            }                OrderConfirmed?.Invoke(this, e);                // Chain order confirmed event when validation succeeds                lblStatus.Text = "Validated";            {            if (e.Quantity > 0)        {        private void ValidateOrder(object? sender, OrderEventArgs e)        }            OrderCreated?.Invoke(this, args);
n            // Raise the OrderCreated event (multicast)            lastOrderConfirmed = false;
n            // Reset confirmation flag until confirmed in the chain
n            var args = new OrderEventArgs(customer, product ?? string.Empty, quantity);            var quantity = (int)numQuantity.Value;            var product = cmbProduct.SelectedItem?.ToString() ?? cmbProduct.Text;            var customer = txtCustomerName.Text.Trim();        {        private void BtnProcessOrder_Click(object? sender, EventArgs e)        }            lblStatus.Text = "Ready";            numQuantity.Minimum = 0;            cmbProduct.SelectedIndex = 0;            cmbProduct.Items.AddRange(new object[] { "Laptop", "Mouse", "Keyboard" });
n            // Initialize controls            chkExpress.CheckedChanged += ChkExpress_CheckedChanged;            btnShipOrder.Click += BtnShipOrder_Click;            btnProcessOrder.Click += BtnProcessOrder_Click;
n            // UI wiring            OrderShipped += ShowDispatch;
n            // Shipping subscriber always present for dispatch display            OrderConfirmed += ShowConfirmation;            OrderRejected += ShowRejection;            OrderCreated += DisplayOrderInfo;            OrderCreated += ValidateOrder;n            // Wire up subscribers for order creation