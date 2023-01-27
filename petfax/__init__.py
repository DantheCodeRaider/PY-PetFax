# config   
from flask import Flask
from flask_migrate import Migrate  

# factory
def create_app(): 
    app = Flask(__name__)

    # database config 
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:%24d8e3k99SA%25@127.0.0.1:5432/petfax'
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