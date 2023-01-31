## How to Install Chocolatey in windows 10
```
Steps to Install chocolatey/choco on Windows 10
Click Start and type “powershell“
Right-click Windows Powershell and choose “Run as Administrator“
Paste the following command into Powershell and press enter.

Set-ExecutionPolicy Bypass -Scope Process -Force; `
  iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))
Answer Yes when prompted

Close and reopen an elevated PowerShell window to start using choco
```

```
C:\>choco search hugo
Chocolatey v0.10.8
hugo 0.32.2 [Approved] Downloads cached for licensed users
pcwrunas 0.4.0.20161129 [Approved] Downloads cached for licensed users
lightworks 14.0.0.20171007 [Approved]
3 packages found.
```
