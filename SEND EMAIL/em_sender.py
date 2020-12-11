import stdiomask
import smtplib
import time

sender_email = str(input("enter sender's email ID: "))
rec_email = str(input("enter reciver's email ID: "))
password =stdiomask.getpass(prompt='PLS ENTER UR PASSWORD: ')
message = str(input("what is the msg u want to send:"))

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(sender_email, password)
print("Login success")
server.sendmail(sender_email, rec_email, message)
print("Email has been sent to ", rec_email)
