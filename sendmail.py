import smtplib
from getpass import getpass

def send_email(body, subject):
  server = smtplib.SMTP('smtp.gmail.com', 587)
  server.ehlo()
  server.starttls()
  server.ehlo()

  password = getpass("Your mail password: ")
  server.login('myemail@gmail.com', password)

  msg = f"Subject: {subject}\n\n{body}"
  server.sendmail(
      'myemail',
      'mysecondemail',
      msg
  )
  
  print("Email has been sent !")

subject = 'Interesting product from craigslist'
body = 'Check craigslist link : ' + URL

send_email(body, subject)
