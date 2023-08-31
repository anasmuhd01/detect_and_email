import smtplib, ssl


def emailx():
    print("email send")

def send_mail():
    host = "smtp.gmail.com"
    port = 465

    username = "beerankutty1509@gmail.com"
    password = "sbbvdfarbygnwcwg"

    receiver = "beerankutty1509@gmail.com"

    context = ssl.create_default_context()

    message = """
    """

    with smtplib.SMTP_SSL(host , port, context=context)as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)