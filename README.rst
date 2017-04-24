ask-router
==========

A script to get telnet command output routers/switches layer 3. Tested on Enterasys S8, G3 and A4 series. 

::

    $ python ask-router.py <target_ip> -u admin -p 'admin_pass' show port status
    $ python ask-router.py <target_ip> show vlan portinfo > output.txt
    $ python ask-router.py <target_ip> router, show running-config, exit
    $ python ask-router.py <target_ip> -F ';' 'router; enable; show interface; exit; exit'

License
-------

MIT
