DumpGarbageDuptyRotation
========================

For home use only. 

##Install:

In your terminal, do

'''
cd ~
git clone git@github.com:oeddyo/DumpGarbageDuptyRotation.git
cd DumpGarbageDuptyRotation
'''

Then paste
'''open config.py'''

replace your gmail username and password to it

paste
'''open sendEmailNotification.py'''

add your destination emails to listOfEmail
change fromaddr to your email addres like "garbage@gmail.com"

change msg to the message you would like to send out


Finally, in terminal, do: 

$ crontab -e

Add 
```
1 15 * * 4 python ~/DumpGarbageDuptyRotation/sendEmailNotification.py
```


