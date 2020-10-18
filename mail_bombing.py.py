
# #-_-_-_-_-_-_-_-_-_ Mail Bombing script by Shahriar -_-_-_-_-_-_-_-_-_#
import smtplib as s
from random import randint
a=randint(100000,999999)
def sendmails(user):
    
    ob = s.SMTP("smtp.gmail.com",587)
    ob.starttls()
    ob.login("alice.jonathon@gmail.com" , "jjlalpekhlua")

    subject = "verifucking account"
    body = ("your verification code is ",a)
    messege = "Subject:{}\n\n{}".format(subject,body)

    listOfAddress = [user]

    ob.sendmail("alice.jonathon" , listOfAddress , messege)

    print("Your e-mail was sent successfully !!!")
    ob.quit()
print("Welcome to ishraqporn.com")
user = input("Enter your email address: ")
pw = input("Set a new password: ")
print("We'v sent a 6 digit code in your email.")
sendmails(user)
con_code = int(input("Enter the code we'v sent : "))
if con_code == a:
    print("Thank you for your bakchodi")
else:
    print("Sorry we couldn't verify you ,as you entered the wrong code..fuck off")




























