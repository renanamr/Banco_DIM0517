from flask import Flask
from .services.banco import operations
app = Flask(__name__)


app.register_blueprint(operations)



if __name__ == '__main__':
    app.run(host='0.0.0.0')
