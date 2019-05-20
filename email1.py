import smtplib
import time
import imaplib
import email
import getpass

email_user=input('email id: ')
email_pass=getpass.getpass("Enter your password: ")
Server="imap.gmail.com"
port=993
try:    
    mail = imaplib.IMAP4_SSL(Server,port)
    mail.login(email_user, email_pass)
    mail.select('inbox')
    typ, data = mail.search(None, 'ALL')
    mail_ids = data[0]
    id_list = mail_ids.split()
    for num in data[0].split():
        typ, data = mail.fetch(num, '(RFC822)' )
        raw_email = data[0][1]
        raw_email_string = raw_email.decode('utf-8').strip()
        email_message = email.message_from_string(raw_email_string)
        if email_message.is_multipart():
            for part in email_message.walk():
                ctype = part.get_content_type()
                cdispo = str(part.get('Content-Disposition'))

                # skip any text/plain (txt) attachments
                if ctype == 'text/plain' and 'attachment' not in cdispo:
                    body = part.get_payload(decode=False)  # decode
                    #print(body)
                    print(re.findall(r'(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)',body))
                    break
        else:
            print(email_message.get_payload())
except Exception as e:
    print(e)
