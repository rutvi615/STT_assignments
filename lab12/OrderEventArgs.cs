using System;

namespace OrderPipeline
{
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
}
