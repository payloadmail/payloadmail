# PayloadMail
Lightweight email receiving client for testing purposes

This is a email client with the purpose of providing test environment for email sending. PayloadMail will collect mails based on the sender instead of recipient, unlike typical emails. This software is not an email server, it requires Postfix based email server running on Ubuntu (other Linux distros may work as well). The original configuration used Postfix + Dovecot to receive email, then used virtual aliases to forward all incoming mail to specific mailuser. PayloadMail uses pam authentication to log in with your Ubuntu user. While all emails are forwarded to one user, PayloadMail will show in web client all those mails where you (your ubuntu username with any domain, for example mailuser(at)anydomain.com) have been as sender. This was created for a specific testing purposes of sending email from other software.

**Prerequisites**

A working email server configured in Linux environment, either physical or virtual.
Technically you only need to have mailbox in Maildir format located in /home/user/Maildir for PayloadMail to work

Python 3 (3.6.7)

[pip](https://pip.pypa.io/en/stable/)

`apt-get install python3-pip`

[Django](https://www.djangoproject.com/)

`pip install django`

[python-pam](https://pypi.org/project/python-pam/)

`pip3 install python-pam`


**Installation and usage**

Clone repository onto your system

Start PayloadMail from root of the repo with command:
'sudo python3 manage.py runserver 0.0.0.0:80'

sudo is needed to grant access for pam module to work.
You can replace ip or port of the last parameter. You can also leave it blank if you're just planning to run it locally.

Your can now access PayloadMail from your browser by typing the ip of the server its running from, for example localhost:80


