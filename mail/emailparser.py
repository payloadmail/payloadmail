from . import parsed_email
import mailbox
from email.utils import parseaddr


def check_emails(useremail=None):
	emails = []
	mbox = mailbox.Maildir('/home/mailuser/Maildir')
	for msg in mbox.values():
		parsed_sender = parseaddr(msg['From'])[1].split('@')[0]
		if parsed_sender == useremail:
			emails.append(parsed_email.Email(msg))
	emails.sort(key=lambda x: x.date, reverse=True)
	return emails

def delete_emails(useremail=None):
	emails = []
	mbox = mailbox.Maildir('/home/mailuser/Maildir')
	for key, msg in mbox.items():
		parsed_sender = parseaddr(msg['From'])[1].split('@')[0]
		if parsed_sender == useremail:
			try:
				mbox.discard(key)
			except KeyError:
				continue


if __name__ == '__main__':
	for mail in check_emails():
		print(mail.getall())
