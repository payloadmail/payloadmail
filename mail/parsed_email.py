import mailbox
import base64
import email
import email.header
import email.utils
import datetime
import re

class Email:
	def __init__(self, mail):
		self.raw = mail.as_string()
		self.attachments = []
		self.sender = email.header.make_header(email.header.decode_header(mail['From']))
		self.recipient = email.header.make_header(email.header.decode_header((str)(mail['To'])))
		d = email.utils.parsedate(mail['Date'])
		self.date = datetime.datetime(d[0],d[1],d[2],d[3],d[4],d[5])
		self.filename = mail.get_filename()
		self.subject = email.header.make_header(email.header.decode_header(str(mail['Subject'])))
		self.replyto = email.header.make_header(email.header.decode_header(str(mail['Reply-To'])))
		self.state = mail.get_subdir()
		self.message = self.handle_message(mail)



	def getall(self):
		return vars(self)

	def cleanhtml(self, raw_html):
		cleanr = re.compile('<.*?>')
		cleantext = re.sub(cleanr, '', raw_html)
		return cleantext

	def handle_message(self, mail):
		body = ""

		if mail.is_multipart():
			for part in mail.walk():
				if part.is_multipart():
					for subpart in part.get_payload():
						if subpart.is_multipart():
							for subsubpart in subpart.get_payload():
								body = subsubpart.get_payload().decode('utf-8')
						else:
							ptype = subpart.get("Content-Type", None).split(";")[0]
							if ptype == "text/plain":
								body = subpart.get_payload(decode=True).decode('utf-8')
							elif ptype == "text/html":
								body = subpart.get_payload(decode=True).decode('utf-8')
							else:
								content = subpart.get("Content-Type", None).split(";")
								encoding = subpart.get("Content-Transfer-Encoding", "base64")
								content_type = content[0]
								filename = email.header.make_header(email.header.decode_header(subpart.get_filename()))
								self.attachments.append((content_type, filename, encoding, subpart.get_payload()))
		else:
			body = mail.get_payload(decode=True).decode('utf-8')

		return body




