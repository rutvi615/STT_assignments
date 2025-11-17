using System;

namespace OrderPipeline
{
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
