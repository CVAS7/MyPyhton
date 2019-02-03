"""
Read passwd file and list all users mentioned in that file in ascending order of their user id.
Also mention the users real name and home directory in the output.
A sample passwd file is shown below :

header for passwd file heads:
Username:Password:User ID (UID):Group ID (GID):User ID Info:Home directory:Command/shell    
"""

#!/usr/bin/env python

FH = open("/etc/passwd", 'r')

dict1 = {}
for line in FH:
    value1 = line.strip().split(":")
    dict1[int(value1[2])] = value1[5]
FH.close()
print "User ID (UID)","=>","Home directory"
for u in sorted(dict1.keys()):
    print u,"=>",dict1[u]  
    
    
Output:
User ID (UID) => Home directory
0 => /root
1 => /bin
2 => /sbin
3 => /var/adm
4 => /var/spool/lpd
5 => /sbin
6 => /sbin
7 => /sbin
8 => /var/spool/mail
11 => /root
12 => /usr/games
14 => /var/ftp
29 => /var/lib/nfs
32 => /var/lib/rpcbind
42 => /var/lib/gdm
48 => /usr/share/httpd
59 => /dev/null
70 => /var/run/avahi-daemon
72 => /
74 => /var/empty/sshd
75 => /
81 => /
99 => /
107 => /
113 => /
171 => /var/run/pulse
172 => /proc
173 => /etc/abrt
192 => /
193 => /
978 => /var/lib/dnsmasq
986 => /run/gnome-initial-setup/
987 => /var/lib/setroubleshoot
988 => /
989 => /
990 => /run/saslauthd
991 => /var/lib/colord
992 => /var/lib/geoclue
993 => /var/run/pipewire
994 => /etc/openvpn
995 => /var/lib/chrony
996 => /run/gluster
997 => /
998 => /
999 => /
1000 => /home/suresh
