import smtplib

listOfEmail = ['firstemail', 'secondemail', 'andsoon']
msg = "Dump garbage this week!" # or whatever your duty is
fromaddr = 'YourEmailAddress'


import  random
import config

server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(config.username, config.password)
toaddrs = listOfEmail[random.randint(0, len(listOfEmail)-1)]

server.sendmail(fromaddr, toaddrs, msg)

server.quit()

