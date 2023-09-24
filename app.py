from flask import Flask, render_template

app = Flask(__name__)

#home directory
@app.route('/')
def main():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)