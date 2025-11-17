# OrderPipeline (Lab 12)

Windows Forms demo implementing advanced event handling and custom EventArgs.

## Features implemented
- Custom `OrderEventArgs` and `ShipEventArgs` used to pass contextual data.
- Event chaining: `OrderCreated` → `ValidateOrder` which either raises `OrderRejected` or `OrderConfirmed`.
- Multicast subscribers: `DisplayOrderInfo` and `ValidateOrder` subscribe to `OrderCreated`.
- Dynamic subscriber management for `OrderShipped`: `NotifyCourier` is added only when `Express` is checked.
- Conditional event raising: `Ship Order` button only ships if the previous order was confirmed.

## Files
- `OrderPipeline.csproj` - project file.
- `Program.cs` - app entry.
- `MainForm.cs` - form logic and custom EventArgs classes.
- `MainForm.Designer.cs` - UI layout.

## Build & Run (dotnet CLI)
Open a Windows cmd prompt and run:

```cmd
cd "d:\Study\Sem 7\STT\Lab12\OrderPipeline"
dotnet restore
dotnet build
dotnet run
```

Alternatively open the folder in Visual Studio 2022 and run the project (recommended for WinForms designer).

## How to demonstrate required behaviors
1. Enter a customer name, select a product and quantity, then click `Process Order`.
   - If quantity &gt; 0: `lblStatus` shows `Validated`, a MessageBox shows order summary, then label shows `Order Processed Successfully for <Customer>`.
   - If quantity = 0: `lblStatus` shows `Order Invalid – Please retry`.
2. After a confirmed order, toggle the `Express` checkbox on/off and press `Ship Order`.
   - If `Express` is checked: `NotifyCourier` subscriber is dynamically attached and a MessageBox shows `Express delivery initiated!`; label shows `Product dispatched: <Product>`.
   - If unchecked: only the dispatch label update occurs (no courier notification).

## Screenshots to capture for lab report
- Code snippet showing delegate and event declarations (`MainForm.cs`).
- GUI state during express shipping (with MessageBox). 
- GUI state during regular shipping.
- Evidence of dynamic subscriber add/remove: run with Express checked then unchecked and note presence/absence of courier MessageBox.

If you want, I can:
- Run the app locally (if you let me run commands here).
- Add small unit tests or sample screenshots placeholders.
- Export this to a Visual Studio solution file (.sln).
