ask-router
==========

Get telnet response from routers/switches. Tested on Enterasys S8, G3 and A4 series. 

::

    $ python ask-router.py <host> -u <user> -p <pass> show port status
    $ python ask-router.py <host> show vlan portinfo > output.txt
    $ python ask-router.py <host> router, show running-config, exit
    $ python ask-router.py <host> -F ';' 'router; enable; show interface; exit; exit'

