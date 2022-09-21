## 
```
Run a batch file at loading of Windows 8 and 10
Create a shortcut to the batch file.
How to create a Windows shortcut.
Once the shortcut is created, right-click the shortcut file and select Cut.
Press Start, type Run, and press Enter.
In the Run window, type shell:startup to open the Startup folder.
Once the Startup folder is opened, click the Home tab at the top of the folder. Then, select Paste to paste the shortcut file into the Startup folder.
Run a batch file at loading of Windows 98, XP, NT, 2000, Vista, and 7
Create a shortcut to the batch file.
How to create a Windows shortcut.
Once the shortcut is created, right-click the shortcut file and select Cut.
Click Start, then Programs or All Programs. Find the Startup folder and right-click that folder, then select Open.
Once the Startup folder is opened, click Edit in the menu bar, then Paste to paste the shortcut file into the Startup folder. If you do not see the menu bar, press the Alt to make the menu bar visible.
Any shortcuts in the Startup folder automatically run each time the user logs in to Windows.

Run a batch file at loading of Windows 95, 3.x, and MS-DOS
The autoexec.bat file is in the root directory of the C: drive (C:\autoexec.bat). Place a line in your autoexec.bat that calls the batch file each time you want to boot the computer, as shown below.

CALL C:\myfile.bat
```
