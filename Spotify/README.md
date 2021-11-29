After try many Spotify's clients on my Arm architecture, I found a good one called [librespot](https://github.com/plietar/librespot).

It works pretty well and there is a *tool* provided by David Cooper ([raspotify](https://github.com/dtcooper/raspotify)) to install and configure it in Raspberry.

To use use, you must follow these [steps](https://dtcooper.github.io/raspotify/#installation):

**1. Installation:**
```shellscript
    curl -sL https://dtcooper.github.io/raspotify/install.sh | sh
```
**2. Getting your username:**
Open [Spotify](https://www.spotify.com) website and select [Account overview](https://www.spotify.com/us/account/overview)

Copy your username:
![image](https://user-images.githubusercontent.com/6587538/143851387-0cdb5f60-fd33-4243-b708-a6ce75955ae1.png)

**3. Configuring your system:**
Edit configuration file and set your username and password:
```shellscript
sudo nano /etc/default/raspotify
```
You must edit the following line in the config file, replacing the USERNAME by your username (last step) and PASSWORD by your password:
```shellscript
OPTIONS="--username USERNAME --password PASSWORD"
```
**4. Restarting the service:**
```shellscript
sudo service raspotify restart
```

**5. Testing:**
Now, you can go to your cellphone and choose raspotify to play your music.

=)

***Notes:***

*I make no warranties, promises or other warranties on this tool. Use of this tool is at your own risk and expense.*

My Raspberry SD card is small (only 2GB) and read only to avoid problems when it is turned off due to lack of power.
Then I created a link to raspberry use the *tmp* folder as cache (it must be done only once).
```reaspberry
$ ln -vs /var/cache/raspotify /tmp/raspotify
/var/cache/raspotify -> /tmp/raspotify/
```
And changed the systemd's init script to create this temporary folder before start the *librespot*.

My configuration files are:
* [/etc/default/raspotify](default_raspotify)
* [/lib/systemd/system/raspotify.service](raspotify.service)
