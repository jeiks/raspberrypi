# Update raspberry datetime

Sometimes, the *ntpdate* does not work on my raspberry and it is necessary to set manually the datetime.
Then I built this tool to solve that. =)

*Obs.: I make no warranties, promises or other warranties on this tool. Use of this tool is at your own risk and expense.*

### Manual Installation

Download the files, copy them to the right place and set the permissions:
```shellscript
sudo cp update-clock /etc/init.d/update-clock
sudo chmod 755 /etc/init.d/update-clock

sudo cp update_clock.py /usr/local/bin/update_clock.py
sudo chmod 755 /usr/local/bin/update_clock.py
```

Include the script (*/etc/init.d/update-clock*) at system boot process:
```shellscript
sudo update-rc.d update-clock defaults
```

Insert the following lines at the end of **/etc/crontab**:
```
# This example updates the clock every 5 minutes.
*/5 *  * * *  root service update-clock restart
```

Restart the *cron* service:
```shellscript
sudo systemctl restart cron.service
sudo systemctl status cron.service
```
