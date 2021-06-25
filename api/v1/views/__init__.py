#!/usr/bin/python3
""" Initing the stuff """
from flask import Blueprint

app_views = Blueprint("app_views", __name__, uri_prefix="/api/v1") 
