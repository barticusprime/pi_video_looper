# pi_video_looper
Application to turn your Raspberry Pi into a dedicated looping video playback device, good for art installations, information displays, or just playing cat videos all day.

Run these commands

```
sudo apt-get install git
git clone https://github.com/ADNewsom09/pi_video_looper.git
```

wait for the install to complete

```
cd pi_video_looper
sudo ./install.sh
```

To Stop: Press Esc or from ssh
`sudo supervisorctl stop video_looper`

To permanently disable video looper, i.e. to prevent it from ever starting on boot again, you can run a small script included with the video looper code.  Connect to the Raspberry Pi in a terminal/SSH session and navigate to the folder where video_looper was downloaded.  If you followed the installation in this guide then run:

`cd pi_video_looper`
Now run the disable script by executing:

`sudo ./disable.sh`

Don't worry if you see an error message displayed that video looper is already stopped (this might happen if video looper isn't running when its disabled).  After running the script above video looper will be disabled and should not run on boot.

To disable lightning bolt error

`avoid_warnings=1`

to your /boot/config.txt
