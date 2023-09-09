import smtplib
from email.message import EmailMessage
import imghdr

sender = "beerankutty1509@gmail.com"
password = "sbbvdfarbygnwcwg"
receiver = "beerankutty1509@gmail.com"
def emailx(image_path):
    email_message = EmailMessage()
    email_message["Subject"] = "Alert :: "
    email_message.set_content("Some object detected :: ")

    with open(image_path, "rb") as file:
        content = file.read()

    email_message.add_attachment(content, maintype="image",  subtype=imghdr.what(None, content))
    gmail = smtplib.SMTP("smtp.gmail.com", 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(sender, password)
    gmail.sendmail(sender, receiver, email_message.as_string())
    gmail.quit()

if __name__ == "__main__":
    emailx("images/33.png")