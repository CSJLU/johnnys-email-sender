from flask import Flask, render_template, request
from flask_mail import Mail, Message

#obtain password from user directory
with open("password.txt", "r", encoding="utf-8") as f:
    password = f.read()

#obtain sender email from user directory
with open("sender_email.txt", "r", encoding="utf-8") as f:
    sender_email = f.read()


#important app information necessary to send emails
app = Flask(__name__)
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = sender_email
app.config['MAIL_PASSWORD'] = password
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
email = Mail(app)

app.app_context().push()
msg = Message("Test", sender = 'johnnysemailsender@gmail.com', recipients=['johnnylubleach@gmail.com'])
email.send(msg)



#UI user encounters upon entering website
@app.route('/home', methods=['GET', 'POST'])
@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)