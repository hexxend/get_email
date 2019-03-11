#!/usr/bin/env python3
#
# Scrape a selected inbox's messages 
#
# 2017
#
###############################################################################
# TODO;
#
# Pass argument for search criteria
#
# Requires Python3.x, and BeautifulSoup
#
#Copyright (C) 2019  HexXend
#
#    This program is free software; you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation; either version 2 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License along
#    with this program; if not, write to the Free Software Foundation, Inc.,
#    51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
#
#hexxend@protonmail.com


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
