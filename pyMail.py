import time
import urllib2
import re
import smtplib
import getpass
import os
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders
from bs4 import BeautifulSoup
from sys import platform

def clear_screen():
    if platform == "linux" or platform == "linux2" or platform == "darwin":
        os.system('clear')
    elif platform == "win32":
        os.system('cls')

def leaving_message():
    clear_screen()
    print "thanks for using pyMail!\n"
    quit()

clear_screen()
print "               ,--.   ,--.        ,--.,--."
print " ,---.,--. ,--.|   `.'   | ,--,--.`--'|  |"
print "| .-. |\  '  / |  |'.'|  |' ,-.  |,--.|  | \x1B[3mcreated by james\x1B[23m"
print "| '-' ' \   '  |  |   |  |\ '-'  ||  ||  |"
print "|  |-'.-'  /   `--'   `--' `--`--'`--'`--'"
print "`--'  `---'                               "
print "\n"

# lets gain some user info first
local_email = raw_input("type in your google email: ")
local_password = getpass.getpass(prompt="type in your google password: ")
print "\n\n"

# gather the site data
site = BeautifulSoup(urllib2.urlopen(raw_input("enter a sitename to scrape: ")), "html.parser").prettify()
print "\n\n"

# parsing the site data to find the emails
emails = list(set(re.findall('[\w\.-]+@[\w\.-]+', site))) # gathered emails
if not emails:
    print "pyMail didn't find any emails :("
    time.sleep(2)
    leaving_message()
else:
    print 'pyMail found this: ' + ' | '.join(emails) + '\n\n'
    send_email_question = raw_input("would you like to send a mass email? [Y|y] ")
    emails = ', '.join(emails)

def email(emails):
    msg = MIMEMultipart()
    msg['From'] = local_email
    msg['To'] = emails
    msg['Subject'] = raw_input("\n\ntype a subject: ")
    body = raw_input("type a body: ")
    msg.attach(MIMEText(body, 'plain'))
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(local_email, local_password)
    text = msg.as_string()
    server.sendmail(local_email, emails, text)
    print "\n\nthe mail has been sent"
    time.sleep(2)
    leaving_message()
    server.quit()

if send_email_question == "Y" or send_email_question == "y":
    email(emails)
else:
    leaving_message()
