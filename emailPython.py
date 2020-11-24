import smtplib

gmail_user = 'me@gmail.com'
gmail_password = 'p@ssworb'

sent_from = gmail_user
to = ['jim@gmail.com', 'joe@gmail.com']
subject = 'python Message'
body = 'Hey, what\'s up?\n\n- You\n this is sent from my freakin python script!!!!! '

email_text = """\
From: %s
To: %s
Subject: %s

%s
""" % (sent_from, ", ".join(to), subject, body)

try:
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(gmail_user, gmail_password)
    server.sendmail(sent_from, to, email_text)
    server.close()

    print('Email sent!')
except:
    print('Something went wrong...')
################### tips ################
# Don't use system names like email.py
#