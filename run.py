from flask import Flask
from routes import Routes

app = Flask(__name__)

if __name__ == "__main__":
    Routes.set(app)
    app.run(debug=True)
