# config   
from flask import Flask 

    # factory
def create_app(): 
    app = Flask(__name__)

# index route
    @app.route('/')
    def hello(): 
        return 'Hello, this is PetFax!'

# register pet blueprint 
    from . import pet
    app.register_blueprint(pet.bp)

# pets index route
#    @app.route('/pets')
#    def pets(): 
#        return 'These are our pets available for adoption!'

    # return the app 
    return app
