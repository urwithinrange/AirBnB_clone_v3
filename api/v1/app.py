#!/usr/bin/python3
"""this will be descriptive text"""
from flask import Flask
from models import storage
from api.v1.views import app_views
import os
app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def tear_down(self):
    """ tear down """
    storage.close()

if __name__ == "__main__":
    host = os.getenv("HBNB_API_HOST", "0.0.0.0")
    port = int(os.getenv("HBNB_API_PORT", 5000))
    app.run(host=host, port=port, threaded=True)
