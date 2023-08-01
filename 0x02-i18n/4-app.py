#!/usr/bin/env python3
"""Basic Flask app to render a page"""
from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """Configuration class for Babel"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """Function to set the local language"""

    if 'locale' in request.args:
        user_lang = request.args['locale']
        if user_lang in Config.LANGUAGES:
            return user_lang
    return request.accept_languages.best_match(["en", "fr"])


@app.route('/', strict_slashes=False)
def index_fn():
    """Method to render the first template"""
    return render_template('4-index.html')


if __name__ == "__main__":
    app.run(port="5000", host="0.0.0.0", debug=True)
