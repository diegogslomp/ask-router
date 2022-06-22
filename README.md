# ask-router

Run telnet commands on routers/L3 switches. Tested on Enterasys S8, G3 and A4 series.

    ask-router 192.168.16.1 -u root -p 's3cr3t' show port status
    ask-router 192.168.16.1 show vlan portinfo > output.txt
    ask-router 192.168.16.1 router, show running-config, exit
    ask-router 192.168.16.1 -F ';' 'router; enable; show interface; exit; exit'