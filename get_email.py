#!/usr/bin/env python3
#
# Scrape a selected inbox's messages 
#
# Hexxend
# 2017
#
###############################################################################
# TODO;
#
# Pass argument for search criteria
#
#

import imaplib, os, getpass
from bs4 import BeautifulSoup
from sys import argv
from sys import platform

emailaddress = argv[1]
server = argv[2] 
mail_box = argv[3]
passwd = getpass.getpass()

help_info = 'usage: get_email.py emailaddress server mail_box\ndescription: \
             scrapes the messges in the specified inbox\n'

if len(argv) < 2 :
    print(help_info)

if platform == 'win32':
    new_line = '\r\n'
if platform == 'linux':
    new_line = '\n'

mail = imaplib.IMAP4_SSL(server)
mail.login(emailaddress, passwd)
mail.select(mail_box)
results, data = mail.search(None, 'All')

mail_ids = data[0]
id_list = mail_ids.split()

def get_inbox():
    for i in reversed(id_list):
        results, data = mail.fetch(i, '(RFC822)')

    data = str(data)
    soup = BeautifulSoup(data, 'lxml')
    divs = soup.find_all('div')

    for div in divs:
        div = div.text 
        as_fmt_string = '%s%s' % (div, new_line)
        with open('%s.%s' % (server, mail_box), 'a') as fmt_email_file:
            fmt_email_file.write(as_fmt_string)

get_inbox()
