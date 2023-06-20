from flask import Flask

app = Flask(__name__)

@app.get('/programming_languages')
def list_programming_languages():
    return "oi"

if __name__ == '__main__':
    app.run(host='0.0.0.0')
