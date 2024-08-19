from flask import Flask
from routes import Routes

app = Flask(__name__)

app.secret_key = "64466794546dasdadaf87f98sdf46a54fe4wf6as7f65465we44"

if __name__ == "__main__":
    Routes.set(app)
    app.run(debug=True)
