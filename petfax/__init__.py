# config   
from flask import Flask
from flask_migrate import Migrate
from dotenv import load_dotenv
import os

# factory
def create_app(): 
    app = Flask(__name__)

    # database config
    load_dotenv()
    URI = os.getenv("URI")
    app.config['SQLALCHEMY_DATABASE_URI'] = URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    from . import models 
    models.db.init_app(app)
    migrate = Migrate(app, models.db)              

# index route
    @app.route('/')
    def index(): 
        return 'Hello, this is PetFax!'

    # register pet blueprint 
    from . import pet 
    app.register_blueprint(pet.bp)

    # register fact blueprint 
    from . import fact
    app.register_blueprint(fact.bp)

    # return the app 
    return app