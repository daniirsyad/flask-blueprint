from flask import Blueprint

# Blueprint import
from .child import children

nested = Blueprint("nested", __name__, url_prefix="/nested")
nested.register_blueprint(children)

@nested.route("/")
def nested_page():
    return "This is Nested page"