# rpi-send-ip-ee250
 
### What is this?
This repository contains the script that will allow Raspberry Pis to connect to a flask server script running on eclipse.usc.edu.

### How do I use it?
Before using this repository make sure you've already configured your Raspberry Pi to automatically connect to Wifi on boot. We will need to modify the raspberry pi's rc.local file. The file rc.local gets run every time the RPi boots up so it's the perfect place to tell it to run our python script. 

To modify it run the command __sudo nano /etc/rc.local__ and on the last line of the file add the command __python3 /path_to_file/send_ip.py__. Once you have this done it should automatically run the script on startup and you will be able to see your updated ip address by visiting eclipse.usc.edu:10510/log or eclipse.usc.edu:10510/log/YOUR_HOSTNAME.

Additionally if you'd like to manually trigger this script or you'd just like to test if its working you can simply run it on your raspberry pi terminal session using the same command we put in the rc.local file.
