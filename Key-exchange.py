from random import randint
import smtplib


	# Both the persons will be agreed upon the
    # 	# public keys G and P
	# A prime number P is taken
P = 23
	
	# A primitive root for P, G is taken
G = 9
	
	
print('The Value of P is :%d'%(P))
print('The Value of G is :%d'%(G))
	
	# Alice will choose the private key a
a = 4
print('The Private Key a for Alice is :%d'%(a))
	
	# gets the generated key
x = int(pow(G,a,P))
	
	# Bob will choose the private key b
b = 3
print('The Private Key b for Bob is :%d'%(b))
	
	# gets the generated key
y = int(pow(G,b,P))
	
	
	# Secret key for Alice
ka = int(pow(y,a,P))
	
	# Secret key for Bob
kb = int(pow(x,b,P))
kb = str(kb)
    

gmail_user = 'guptarohitkumar2580@gmail.com'
gmail_password = 'ettldvgzpohrdmnw'

sent_from = gmail_user
to = ['guptarohitkumar2580@gmail.com', 'rohit.vitofficial@gmail.com']
subject = 'Generated mail using python'
body = 'The random key generated to lock is ' + kb

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

	

