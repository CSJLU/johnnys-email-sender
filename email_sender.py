import smtplib
import ssl
from email.message import EmailMessage
import random
import os

#obtain password from user directory
with open("sender_password.txt", "r", encoding="utf-8") as f:
    password = f.read()

#obtain sender email from user directory
with open("sender_email.txt", "r", encoding="utf-8") as f:
    email = f.read()

sender_email = email
app_password = password




#call to send email
def send_email(sender, recipient):
    #message contents
    msg = EmailMessage()
    body = "Here is an anime image"
    msg['Subject'] = "Here is your daily Johnny email!"
    msg['From'] = sender
    msg['To'] = recipient
    msg.set_content(body)
    
    image_path = "/home/csjlu/anime_images/"
    images = os.listdir(image_path)
    selected_image = random.choice(images)

    #read image data
    with open(os.path.join(image_path, selected_image), 'rb') as fp:
        img_data = fp.read()
        msg.add_attachment(img_data, maintype='image', subtype='jpg' and 'png')

    #send message
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(sender_email, app_password)
        smtp.send_message(msg)


