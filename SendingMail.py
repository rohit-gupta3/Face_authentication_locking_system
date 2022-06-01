import smtplib

gmail_user = 'Your Email Address'
gmail_password = 'You email app password'#Refer any youtube video How to generate App password in your google account

sent_from = gmail_user
to = ['Email which needed to be sent']
subject = 'Generated mail using python'
body = 'Confirmed that code is working'

email_text = """\
From: %s
To: %s
Subject: %s

%s
""" % (sent_from, ", ".join(to), subject, body)

try:
    smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    smtp_server.ehlo()
    smtp_server.login(gmail_user, gmail_password)
    smtp_server.sendmail(sent_from, to, email_text)
    smtp_server.close()
    print ("Email sent successfully!")
except Exception as ex:
    print ("Something went wrong….",ex)
