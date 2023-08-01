#!/usr/bin/env python3
"""Basic Flask app to render a page"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    """Method to render the first template"""
    return render_template('0-index.html')