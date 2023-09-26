from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__, static_url_path='/static')

def get_db_connection():
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()
    return connection, cursor

#all_emails = c.fetchall()


#home directory
@app.route('/')
def main():
    return render_template('index.html')


@app.route('/put_email', methods=['GET', 'POST'])
def put_email():
    if request.method == 'POST':
        email = request.form['email']
        #Connects to database and creates cursor
        connection, cursor = get_db_connection()
        #Create emails table
        cursor.execute("CREATE TABLE IF NOT EXISTS emails (email TEXT UNIQUE)")
        #Put all emails into existing emails database table
        cursor.execute("INSERT OR IGNORE INTO emails VALUES (?)", (email,))
        cursor.execute("SELECT * FROM emails")
        #cursor.execute("DELETE FROM emails")
        connection.commit()
        connection.close()

    return render_template('success.html')


#create sqlite3 database and put email from request into database

#for each email in database, go through it and send email 

#function to send email, incorporate this with the above comment

#schedule email sender (use the function to send email to make it a daily automated email sender using a time schedule)


if __name__ == '__main__':
    app.run(debug=True)