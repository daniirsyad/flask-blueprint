from flask import Blueprint

about = Blueprint("about", __name__)

@about.route("/about")
def about_page():
    return "This is about Page"