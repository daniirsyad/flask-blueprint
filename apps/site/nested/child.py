from flask import Blueprint

children = Blueprint("child", __name__)

@children.route("/child")
def child_page():
    return "This is Children page of neted folder"