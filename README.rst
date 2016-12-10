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

Installation
------------

Copy from github::

    $ git clone git@github.com:diegogslomp/ask-router.git
    $ cd ask-router

Motivation
----------

I made this to help diff config files from multiple targets, check port status from target, check routes, firmware version and so on.

License
-------

MIT
