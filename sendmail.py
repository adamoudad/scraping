# If using gmail, enable 2-step verification beforehand
# https://support.google.com/accounts/answer/185839

import smtplib
from getpass import getpass

def send_email(body, subject, sender, receiver):
  server = smtplib.SMTP('smtp.gmail.com', 587)
  server.ehlo()
  server.starttls()
  server.ehlo()

  password = getpass("Sender mail password:")
  server.login(sender, password)

  message = f"Subject: {subject}\n\n{body}"
  server.sendmail(
      sender,
      receiver,
      message
  )

if __name__ == "__main__":
  sender = input("Sender:")
  receiver = input("Receiver:")
  subject = input('Subject:') or "Hello !"
  body = input("Body:") or "Sample text."
  
  send_email(body, subject, sender, receiver)
  print("Email has been sent !")
