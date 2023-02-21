import smtplib as s
ob = s.SMTP('smtp.gmail.com',587)
ob.ehlo()
ob.starttls()
ob.login("amityadav1214@gmail.com","smitamit1214")
subject = "This is a test mail sent from python"
body = "This is a test mail sent from python"
message = "Subject:{}\n\n{}".format(subject,body)
to = ["amityadav1214@gmail.com"]
ob.sendmail(amityadav1214@gmail.com,to,message)
print("Mail sent")
ob.quit()
