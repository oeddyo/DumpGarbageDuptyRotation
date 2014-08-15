import smtplib

# Import the email modules we'll need
from email.mime.text import MIMEText

# Open a plain text file for reading.  For this example, assume that
# the text file contains only ASCII characters.
# Create a text/plain message
msg = MIMEText("Dump garbage this week!")

# me == the sender's email address
# you == the recipient's email address
msg['Subject'] =  msg
msg['From'] = "GarbageNotification"


listOfEmail = ['oeddyo@gmail.com', 'jinfu.leng@gmail.com', 'illdian1989@gmail.com']

import  random
import config
fromaddr = 'garbagenotification@gmail.com'

server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(config.username, config.password)
toaddrs = listOfEmail[random.randint(0, 2)]

toaddrs = "oeddyo@gmail.com"

msg = "Dump garbage this week!"
server.sendmail(fromaddr, toaddrs, msg)

server.quit()

