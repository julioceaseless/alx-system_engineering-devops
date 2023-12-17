## ALX::Command line for the win

This CMD CHALLENGE is a pretty cool game challenging you on Bash skills. Everything is done via the command line and the questions are becoming increasingly complicated. It’s a good training to improve your command line skills!

After taking the screenshots of the milestones, the images are transfered to the sandbox from local machine via SFTP and later pushed to github. 

These are the steps followed to use the SFTP command-line tool. 

### SFTP Process

_Step 1: Connect SFTP to the sandbox environment_

Using the SFTP credentials (username, hostname, and password) on the intranet, I connected to the sandox via the terminal of my Ubuntu Machine

command: `sftp username@hostname`

_Step 2: Navigate to the remote directory_

Once connected to the sandbox environment, I navigated to the remote directory where I want to upload the files.

command: `cd root/alx-system_engineering-devops/command_line_for_the_win/`

_Step 3: Navigate to the local directory_

Use the cd command to navigate to the local directory where the screenshot files are.

command: `lcd Pictures/Screenshots`

_Step 4: Upload the files to the remote directory_

I use the put command to upload the screenshot files to the sandbox environment

command: 
```
put 0-first_9_tasks.png
put 1-next_9_tasks.png
put 2-next_9_tasks.png
```
_Step 5: Exit_

Exit SFTP with `exit` command
