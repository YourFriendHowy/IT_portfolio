> [!important|left-small] Important User Files
> cat /etc/passwd: shows users on system
> cat /etc/shadow: Shows user password hash
> cat /etc/group: shows users groups

yourfriendhowy:x:1000:1000:Howy:/home/yourfriendhowy:/bin/bash

| yourfriendhowy | x        | 1000    | 1000     | Howy | /home/yourfriendhowy | /bin/bash     |
| -------------- | -------- | ------- | -------- | ---- | -------------------- | ------------- |
| user account   | password | user ID | Group ID | Name | home directory       | default shell |


## User ID(UID)
Most Linux distros with a GUI wont show users on the login screen with a UID under 1000.

numerical representation of a user