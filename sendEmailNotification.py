import smtplib

listOfEmail = ['firstemail', 'secondemail', 'andsoon']
import  random
import config
fromaddr = 'YourEmailAddress'

server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(config.username, config.password)
toaddrs = listOfEmail[random.randint(0, len(listOfEmail)-1)]

msg = "Dump garbage this week!"

server.sendmail(fromaddr, toaddrs, msg)

server.quit()

