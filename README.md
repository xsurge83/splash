SETUP crantab on OSX
 setup cron job or http://alvinalexander.com/mac-os-x/mac-osx-startup-crontab-launchd-jobs
 
Go to ~/Library/LaunchAgents
➜  LaunchAgents  launchctl unload acacia.plist
➜  LaunchAgents  launchctl load acacia.plist
check for errors 
➜  LaunchAgents  tail -f /var/log/system.log


TODO: 
- install command line tool 
 - https://github.com/architv/soccer-cli
 - http://nvie.com/posts/writing-a-cli-in-python-in-under-60-seconds/
    stuck on install pipse see script https://raw.githubusercontent.com/mitsuhiko/pipsi/master/get-pipsi.py
 - https://pythonhosted.org/an_example_pypi_project/setuptools.html
 - https://github.com/jkbrzt/httpie/blob/master/setup.py