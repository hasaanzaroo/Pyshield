from flask import Flask, render_template

from config import Config

from database.db import db

import database.models


app = Flask(__name__)

app.config.from_object(Config)

db.init_app(app)


@app.route("/")
def dashboard():
    return render_template("dashboard.html")


with app.app_context():
    db.create_all()


if __name__ == "__main__":
    app.run(debug=True)