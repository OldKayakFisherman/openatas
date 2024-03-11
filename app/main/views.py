from . import main
from flask import render_template
from flask_login import confirm_login


@main.route("/secret", methods=['GET'])
def secret():
    return "<html lang='en'><body>Secret!</body></html>"

@main.route("/", methods=['GET', 'POST'])
def index():
    return render_template("index.jinja")



