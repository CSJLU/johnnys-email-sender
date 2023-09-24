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


if __name__ == '__main__':
    app.run(debug=True)