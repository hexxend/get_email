#!/usr/bin/env python3
import imaplib
from bs4 import BeautifulSoup
from sys import argv

#usrname = ''
emailaddress = argv[1] #'%s%s' % (usrname, email_sufix)
passwd = argv[2]

mail = imaplib.IMAP4_SSL('imap.gmail.com')
mail.login(emailaddress, passwd)
mail.select('inbox')
results, data = mail.search(None, 'All')

mail_ids = data[0]
id_list = mail_ids.split()

for i in id_list:
    results, data = mail.fetch(i, '(RFC822)')
    file_name = 'email_dump.txt'
    dump_file = open(file_name, 'a')
    dump_file.write(str(data[0]))
dump_file.close()
dump_file = open(file_name, 'r') 
soup = BeautifulSoup(dump_file.read(), 'lxml')
divs = soup.find_all('div', dir='auto')
fmt_email = 'gmail_inbox'

for div in divs:
    fmt_email_file = open(fmt_email,'a')
    div = div.stddring 
    as_fmt_string = '%s\r\n' % div
    fmt_email_file.write(as_fmt_string)

fmt_email_file.close()
dump_file.close() 
