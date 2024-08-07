import pandas as pd
import smtplib
import datetime as dt
import random

MY_EMAIL = "email_address"
MY_PASS = "pass"

data = pd.read_csv("birthdays.csv")

now = dt.datetime.now()
month = now.month
day = now.day
today_tuple =(month, day)




new_data_dict = {(new_data.month,new_data.day): new_data for (index, new_data) in data.iterrows()}



if today_tuple in new_data_dict:
    birthday_person = new_data_dict[today_tuple]
    file_path = f"./letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        formatted = contents.replace("[NAME]",birthday_person["name"])
        
    with smtplib.SMTP("smtp-mail.outlook.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASS)
        connection.sendmail(
            from_addr=MY_EMAIL, 
            to_addrs=birthday_person["email"], 
            msg=f"Subject:Happy Birthday\n\n {formatted}"
        )






