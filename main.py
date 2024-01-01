import smtplib
import datetime as dt
from random import choice

email = 'sender_email@provider.com'
pwd = 'password_of_sender'

now = dt.datetime.now()
today = now.weekday()

with open('quotes.txt') as data_file:
    data = data_file.readlines()
    quote = choice(data)


with smtplib.SMTP('smtp.gmail.com') as connection:
    connection.starttls()
    connection.login(user=email, password=pwd)
    if today == 0:
        connection.sendmail(from_addr=email, to_addrs='receiver_email@provider.com',
                            msg=f'Subject:Monday Motivation\n\n{quote}'
                            )
