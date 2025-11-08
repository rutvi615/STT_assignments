@echo off
REM Quick Run Script for Lab 9 Activities
REM This script helps you run each activity easily

:menu
cls
echo ========================================
echo    Lab 9 - C# Console Applications
echo ========================================
echo.
echo Select an activity to run:
echo.
echo 1. Activity 1 - Hello World
echo 2. Activity 2 - Calculator (OOP)
echo 3. Activity 3 - Loops and Functions
echo 4. Activity 4 - Arrays (Sort, Matrix)
echo 5. Output Reasoning - Level 0 Example 1
echo 6. Output Reasoning - Level 1 Example 1
echo 7. Output Reasoning - Level 1 Example 2
echo 8. Output Reasoning - Level 2 Example 1
echo 0. Exit
echo.
set /p choice="Enter your choice (0-8): "

if "%choice%"=="1" goto activity1
if "%choice%"=="2" goto activity2
if "%choice%"=="3" goto activity3
if "%choice%"=="4" goto activity4
if "%choice%"=="5" goto level0_1
if "%choice%"=="6" goto level1_1
if "%choice%"=="7" goto level1_2
if "%choice%"=="8" goto level2_1
if "%choice%"=="0" goto end
goto menu

:activity1
cls
echo Running Activity 1 - Hello World...
echo.
cd Activity1_HelloWorld
dotnet run
cd ..
pause
goto menu

:activity2
cls
echo Running Activity 2 - Calculator...
echo.
cd Activity2_Calculator
dotnet run
cd ..
pause
goto menu

:activity3
cls
echo Running Activity 3 - Loops and Functions...
echo.
cd Activity3_LoopsAndFunctions
dotnet run
cd ..
pause
goto menu

:activity4
cls
echo Running Activity 4 - Arrays...
echo.
cd Activity4_Arrays
dotnet run
cd ..
pause
goto menu

:level0_1
cls
echo Running Output Reasoning - Level 0 Example 1...
echo.
echo Note: This will demonstrate post-increment operator
echo Expected Output: 0
echo.
csc /out:temp.exe Activity5_OutputReasoning\Level0_Example1.cs 2>nul
if exist temp.exe (
    temp.exe
    del temp.exe
)
pause
goto menu

:level1_1
cls
echo Running Output Reasoning - Level 1 Example 1...
echo.
csc /out:temp.exe Activity5_OutputReasoning\Level1_Example1.cs 2>nul
if exist temp.exe (
    temp.exe
    del temp.exe
)
pause
goto menu

:level1_2
cls
echo Running Output Reasoning - Level 1 Example 2...
echo.
csc /out:temp.exe Activity5_OutputReasoning\Level1_Example2.cs 2>nul
if exist temp.exe (
    temp.exe
    del temp.exe
)
pause
goto menu

:level2_1
cls
echo Running Output Reasoning - Level 2 Example 1...
echo.
echo WARNING: This program contains an infinite loop!
echo Press Ctrl+C to stop the program when it hangs.
echo.
pause
csc /out:temp.exe Activity5_OutputReasoning\Level2_Example1.cs 2>nul
if exist temp.exe (
    temp.exe
    del temp.exe
)
pause
goto menu

:end
cls
echo Thank you for using Lab 9 Activity Runner!
echo.
exit
