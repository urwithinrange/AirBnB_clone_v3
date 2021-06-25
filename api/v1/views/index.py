#!/usr/bin/python3
""" The index! """
from flask import jsonify
from api.v1.views import app_views


@app_views.route("/status", strict_slashes=False)
def status():
    """ Returns status OK """
    json_obj = {"status": "OK"}
    return jsonify(json_obj)
