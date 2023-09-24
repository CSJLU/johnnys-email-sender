from flask import Flask, render_template, request

app = Flask(__name__, static_url_path='/static')

#home directory
@app.route('/')
def main():
    return render_template('index.html')


@app.route('/send_email', methods=['POST'])
def send_email():
    if request.method == 'POST':
        email = request.form['email']

    return render_template('success.html')

#create sqlite3 database and put email from request into database

#for each email in database, go through it and send email 

#function to send email, incorporate this with the above comment

#schedule email sender (use the function to send email to make it a daily automated email sender using a time schedule)


if __name__ == '__main__':
    app.run(debug=True)