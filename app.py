from flask import Flask
# Blueprint
from apps.site.home import home
from apps.site.about import about
from apps.site.nested import nested

app = Flask(__name__)

if __name__ == '__main__':
    # Register Blueprint
    app.register_blueprint(home)
    app.register_blueprint(about)
    app.register_blueprint(nested)

    app.run(debug=True)