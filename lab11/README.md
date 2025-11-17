# EventPlayground

Windows Forms demo for Lab 11: Events and Delegates (C#)

Project structure:

- `EventPlayground/` - project directory
  - `EventPlayground.csproj` - project file
  - `Program.cs` - application entry
  - `MainForm.cs` / `MainForm.Designer.cs` - form implementation
  - `ColorEventArgs.cs` - custom EventArgs used by ColorChangedEvent

Features implemented:
- Custom delegates and events declared in `MainForm.cs`.
- `ColorChangedEvent` uses custom `ColorChangedHandler` delegate and `ColorEventArgs` to pass selected color name.
- `ColorChangedEvent` has two subscribers: `UpdateLabelColor()` and `ShowNotification()` (demonstrates multicast).
- `TextChangedEvent` updates the label text to current date/time.

Running the project

Open in Visual Studio 2022:

1. Open `EventPlayground.sln` if you create one, or open the folder in Visual Studio.
2. Build and run (F5).

OR using dotnet CLI (requires .NET SDK installed):

Command prompt (cmd.exe):
```
cd "d:\Study\Sem 7\STT\Lab11\EventPlayground"
dotnet build
dotnet run
```

Notes for the lab submission:
- Include screenshots of the source showing delegate/event declarations and the running GUI demonstrating correct behavior.
