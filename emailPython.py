#!/usr/bin/env python
# # import smtplib
########################################################################

# do sth every second - periodically
# import sched, time
# s = sched.scheduler(time.time, time.sleep)
# def do_something(sc): 
#     print("Doing stuff...")
#     # do your stuff
#     s.enter(1, 1, do_something, (sc,))

# s.enter(1, 1, do_something, (s,))
# s.run()
########################################################################
import winsound
frequency = 1000 # Set Frequency To 2500 Hertz
duration = 5000 # Set Duration To 1000 ms == 1 second
winsound.Beep(frequency, duration)
winsound.Beep(frequency, duration)
# winsound.Beep(frequency, duration)
########################################################################

# import requests

# url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/v2/get-financials"

# querystring = {"symbol":"appl","region":"US"}

# headers = {

#     }

# response = requests.request("GET", url, headers=headers, params=querystring)

# print(response.text)
##################################################################################



# gmail_user = '@gmail.com'
# gmail_password = 'kkk'

# sent_from = gmail_user
# to = ['70@gmail.com', 'joe@gmail.com']
# subject = 'python Message'
# body = 'Hey, what\'s up?\n\n- You\n this is sent from my freakin python script!!!!! \n\
# This is supposed to be a fun trip \
# so maybe a new crew should accompany us'

# email_text = """\
# From: %s
# To: %s
# Subject: %s

# %s
# """ % (sent_from, ", ".join(to), subject, body)

# try:
#     server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
#     server.ehlo()
#     server.login(gmail_user, gmail_password)
#     server.sendmail(sent_from, to, email_text)
#     server.close()

#     print('Email sent!')
# except:
#     print('Something went wrong...')
# ################### tips ################
# # Don't use system names like email.py
# #