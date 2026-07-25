from app import app

from database.db import db

from database.models import AppSettings


with app.app_context():

    if AppSettings.query.first() is None:

        settings = AppSettings(
            default_policy="ALLOW",
            capture_interface="Default"
        )

        db.session.add(settings)

        db.session.commit()

        print("Default settings created.")

    else:

        print("Settings already exist.")