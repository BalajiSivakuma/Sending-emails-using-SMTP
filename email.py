#SNEDING EMAILS USING SMTP

import smtplib
my_email="balajisy2005gmail.com"
password="Balaji@2005"

connection =smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=my_email , password=password)
connection.sendmail(from_addr=my_email,to_addrs="yasobalaji1980@gmail.com",
                    msg="Subject:Hello amma\n\n This the body of the mail")
connection.close()