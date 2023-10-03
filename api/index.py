
import os
from flask import Flask


#flask --app api run --debug
def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)

    # Configuration
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # Ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # Register Blueprints
    from . import  auth, db, blog
   
    app.register_blueprint(blog.bp)
    app.register_blueprint(auth.bp)

    # Add URL Rules
    app.add_url_rule('/', endpoint='index')

    # Initialize the database
    db.init_app(app)
    return app.run
   

