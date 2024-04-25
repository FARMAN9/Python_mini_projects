import smtplib

to=input("enter the email of recipient:")

content=input("Enter the email content:")



def send_email(to, content):
    servser=smtplib.SMPT('smpt.gmail.com',589)
    servser.ehlo
    servser.starttls()
    servser.login('saeedfarmanwrhiuwGmail.com','hydegfiuiiuheikk')
    servser.sendmail('saeedfarmfjhfjh9@gmail.com',to,content)
    servser.close()
    
    
send_email(to,content)    