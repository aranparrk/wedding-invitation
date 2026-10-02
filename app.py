from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Wedding Invitation Service"

if __name__ == '__main__':
    app.run(debug=True)