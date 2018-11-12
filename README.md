# PiMecha
PiMecha is a Raspberry Pi Humanoid Robot with 17 DOF

**Steps for PiMecha software installation:**
1. Open Terminal and download the code by writing:
```git clone https://github.com/sbcshop/PiMecha.git```

2. Your code will be downloaded to '/home/pi' directory. Use 'ls' command to check the list of directories.

3. Go to directory 'PiMecha' and run the command to change the permissions of 'configGUI' and 'controlGUI' python files:
   ```
   sudo chmod +x configGUI.py
   sudo chmod +x controlGUI.py
   ```
   You are now able to run these two softwares for your PiMecha. The control software is to control the movements of PiMecha, while the config software is to config the servo motor.

4. Click on the 'Servo Config' shortcut icon to configure your motor, or if you wish to give movements to PiMecha or control it, click on the 'PiMecha' shortcut icon.

5. You can also move these 2 icons to your desktop for your convinience.
