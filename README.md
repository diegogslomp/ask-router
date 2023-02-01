# ask-router

Run telnet commands on routers/L3 switches. Tested on Enterasys S8, G3 and A4 series.

    cd ask-router
    python ask-router.py 192.168.16.1 -u root -p 's3cr3t' show port status
    python ask-router.py 192.168.16.1 show vlan portinfo > output.txt
    python ask-router.py 192.168.16.1 router, show running-config, exit
    python ask-router.py 192.168.16.1 -F ';' 'router; enable; show interface; exit; exit'
