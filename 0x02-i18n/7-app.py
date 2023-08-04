#!/usr/bin/env python3
"""Basic Flask app to render a page"""
from flask import Flask, render_template, request, g
from flask_babel import Babel
from pytz import timezone
from pytz import exceptions

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


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

    if g.user:
        if g.user['locale'] and g.user['locale'] in Config.LANGUAGES:
            return g.user['locale']

    user_lang2 = request.headers.get('locale', None)
    if user_lang2 in Config.LANGUAGES:
        return user_lang2

    return request.accept_languages.best_match(["en", "fr"])


@babel.timezoneselector
def get_timezone():
    """Get the timezone in params, user settings or use UTC"""
    try:
        if 'timezone' in request.args:
            tz = request.args['timezone']
            new_tz = timezone(tz)
            return new_tz

        elif g.user and g.user['timezone']:
            tz = g.user['timezone']
            new_tz = timezone(tz)
            return new_tz

    except exceptions.UnknownTimeZoneError:
        return timezone('UTC')


def get_user(user_id=None):
    """A function that returns the user details if loginas"""
    if user_id and user_id in users:
        return users[user_id]
    return None


@app.before_request
def before_request():
    """Find the user details given the login deets"""
    if 'login_as' in request.args:
        user_id = int(request.args.get('login_as'))
        g.user = get_user(user_id)
    else:
        g.user = None


@app.route('/', strict_slashes=False)
def index_fn():
    """Method to render the first template"""
    return render_template('7-index.html')


if __name__ == "__main__":
    app.run(port="5000", host="0.0.0.0", debug=True)
