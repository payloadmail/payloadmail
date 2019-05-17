# PayloadMail
Lightweight email receiving client for testing purposes.

This is an email client that provides a test environment for email sending. PayloadMail will collect emails based on the sender instead of the recipient, unlike the typical emails. This software is not an email server, it requires Postfix-based email server running on Ubuntu (other Linux distros may work as well). The original configuration used Postfix + Dovecot to receive emails, then it used virtual aliases to forward all incoming emails to a specific mailuser. PayloadMail uses pam authentication to log in with your Ubuntu user. While all emails are forwarded to one user, the web client of PayloadMail will only display those emails where you (your ubuntu username with any domain, for example mailuser(at)anydomain.com) were the sender. This was created for specific testing purposes where emails are sent from other softwares.

**Prerequisites**

A working email server configured in Linux environment, either physical or virtual.
Technically you only need to have a mailbox in Maildir format located in /home/user/Maildir for PayloadMail to work.

Python 3 (3.6.7)

[pip](https://pip.pypa.io/en/stable/)

`apt-get install python3-pip`

[Django](https://www.djangoproject.com/)

`pip3 install django`

[python-pam](https://pypi.org/project/python-pam/)

`pip3 install python-pam`


**Installation and usage**

Clone repository into your system

Start PayloadMail from root of the repository with command:
'sudo python3 manage.py runserver 0.0.0.0:80'

sudo is needed to grant access for the pam module to work.
You can replace ip or port of the last parameter. You can also leave it blank, if you're just planning to run it locally.

Your can now access PayloadMail from your browser by typing the ip of the server it is running from; for example localhost:80


