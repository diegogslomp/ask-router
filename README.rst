ask-router
==========

Synopsis
--------

A python script to get telnet command output from Enterasys routers/switches L3.

Code Examples
-------------

Print to stdout::

    $ python ask-router.py <target_ip> show port status
    $ python ask-router.py <target_ip> show vlan portinfo
    $ python ask-router.py <target_ip> router, configure, show running-config, exit, exit

Print to a file::

    $ python ask-router.py <target_ip> show port status > output_file.txt

License
-------

MIT
