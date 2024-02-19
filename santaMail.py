import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

yourEmail = "your.email@gmail.com"
yourPassword = "your password"

def send_emails(santaData, santaPairs):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()

    server.login(yourEmail, yourPassword)

    for santa in santaData:
        gifter = santa
        giftee = santaPairs[gifter]
        gifterEmail = santaData[gifter]['email']

        message = MIMEMultipart()
        message['Subject'] = 'Secreta Santa 20XX'
        message['From'] = yourEmail
        message['To'] = gifterEmail
        body = f'''
        Hey {gifter}!

        You have been assigned {giftee} for Secret Santa this year!

        FILL FILL FILL FILL FILL
        '''
        message.attach(MIMEText(body, 'plain'))
        server.sendmail(yourEmail, gifterEmail, message.as_string())
    
    server.quit()
    
    print("Emails sent :)")