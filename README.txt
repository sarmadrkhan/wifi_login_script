0. Download the chrome web driver for your system. For example I am using chrome-win64 since i have a 64 bit windows OS. Extract the chrome web driver folder in the root of this repository cloned on your PC

1. Download and install the latest stable version of python from https://www.python.org/downloads/. While installing, make sure to check the option of adding python to PATH environment variable

2. Press windows button and type cmd to open command prompt

3. Type "python --version" without the quotation marks and press enter to verify that python has been installed.

4. Open the terminal in the extracted folder by clicking on the address bar and typing cmd.

5. Type the following command and press enter "pip install -r required_packages.txt"

***TO CREATE A TASKBAR SHORTCUT FOR DOING EVERYTHING IN 1 CLICK DO THE FOLLOWING***

6. Right-click on your desktop or the desired location where you want to create the shortcut.

7. Select "New" and then choose "Shortcut". A "Create Shortcut" dialog box will appear.

8. In the "Type the location of the item" field, enter the following:
cmd.exe /c python "C:\path\to\login.py"

*Make sure to replace "C:\path\to\login.py" with the actual path to the Python script in the folder that you just extracted.

9. Click "Next".

10. Enter a name for the shortcut. This will be the name that appears on the shortcut icon.

11. Click "Finish".

12. Right-click on the shortcut and go to properties

13. In the "Shortcut" tab, select "Change Icon..." and select an icon of your choice(you can download any icon from google as well by looking for .ico files)

14. In the "Shortcut" tab,  click on the "Start in" field and enter the path of the extracted folder. You can click in the address bar and copy the path from there.

16. Click "Apply" and then "OK" to save the changes.

17. Finally, drag and drop this shortcut to taskbar or right click and "pin to taskbar". 

18. After every hour, wait for a couple of minutes for edisu server to restart and then click on the shortcut from the task bar, Internet will connect instantly.
Usually i click run the script after 3 minutes past every hour for example at 8:03, 9:03 and so on.