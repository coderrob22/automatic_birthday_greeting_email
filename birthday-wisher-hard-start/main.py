import datetime as dt
import smtplib
import random
import pandas

my_email = 'app.production02@gmail.com'
my_password = 'ksigssggokzhrzmf'

now = dt.datetime.now()
month = now.month
date = now.day
today = (month, date)

data = pandas.read_csv('birthdays.csv')

birthday_dict = {(data_row['month'], data_row['day']): data_row for (index, data_row) in data.iterrows()}
if today in birthday_dict:
    birthday_person = birthday_dict[today]
    file_path = f'letter_templates/letter_{random.randint(1,3)}.txt'
    
    with open(file_path) as letter_file:
            content = letter_file.read()
            content = content.replace("[NAME]", birthday_person['name'])

    with smtplib.SMTP('smtp.gmail.com', 587) as connection:
          connection.starttls()
          connection.login(my_email, my_password)
          connection.sendmail(
                from_addr=my_email,
                to_addrs=birthday_person['email'],
                msg=f'Subject:Birthday Greetings\n\n{content}'
          )