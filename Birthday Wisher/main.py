import smtplib
from secret_file import email, password, to_email

with smtplib.SMTP('smtp.mail.yahoo.com', 587) as connection:
    connection.starttls()
    connection.login(user=email, password=password)
    connection.sendmail(
        from_addr=email,
        to_addrs=to_email,
        msg="Subject:Happy Birthday!\n\n Happy Birthday Foo!")
