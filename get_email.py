#!/usr/bin/env python3
import imaplib, os, getpass
from bs4 import BeautifulSoup
from sys import argv
from sys import platform

emailaddress = argv[1]
server = argv[2] 
mail_box = argv[3]
passwd = getpass.getpass()

if platform == 'win32':
    new_line = '\r\n'
if platform == 'linux':
    new_line = '\n'

mail = imaplib.IMAP4_SSL(server)
mail.login(emailaddress, passwd)
mail.select(mail_box)
results, data = mail.search(None, mail_box)

mail_ids = data[0]
id_list = mail_ids.split()

def get_inbox():
    for i in reversed(id_list):
        results, data = mail.fetch(i, '(RFC822)')
        soup = BeautifulSoup(str(i), 'lxml')
        divs = soup.find_all('div')
        for div in divs:
            div = div.text 
            as_fmt_string = '%s%s' % (div, new_line)
            with open('%s.%s' % (server, mail_box), 'a') as fmt_email_file:
                fmt_email_file.write(as_fmt_string)
get_inbox()
