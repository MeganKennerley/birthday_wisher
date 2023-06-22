import smtplib
import datetime as dt
import pandas

MY_EMAIL = YOUR_EMAIL
PASSWORD = YOUR_PASSWORD
SUBJECT = "HAPPY BIRTHDAY"

now = dt.datetime.now()
today_tuple = (now.month, now.day)

birthdays = pandas.read_csv("birthdays.csv")
birthday_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in birthdays.iterrows()}

if today_tuple in birthday_dict:

    person = birthday_dict[today_tuple]
    with open("letter.txt") as letter:
        my_letter = letter.read().replace("[NAME]", person["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=person["email"],
            msg=f"Subject:{SUBJECT}\n\n{my_letter}"
        )
