import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from config import CONFIGS
from extensions import db, migrate
from models.BaseModel import init_db
import logging
from logging import Formatter, FileHandler
from seeder import Seeder

def create_app(mode=None):
    # create and configure the app
    if not mode:
        mode = 'Default'

    app = Flask(__name__)
    app.config.from_object(CONFIGS[mode])
    CORS(app)

    # register dependencies
    register_errorhandlers(app)
    register_debug(app)
    register_extensions(app, mode)    
    register_blueprint(app)

    seed_db(app)
    

    return app

def register_blueprint(flask_app):
    # register notifications  blueprint
    from notifications import notifications
    flask_app.register_blueprint(notifications, url_prefix='/api')
    # print(app.url_map)


def register_extensions(flask_app, mode):
    # create db table
    migrate.init_app(flask_app, db)
    db.init_app(flask_app)
    

def register_errorhandlers(app):
    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            'success': False,
            'error': 404,
            'message': "Not found"
        }), 404

    @app.errorhandler(422)
    def unprocessible(error):
        return jsonify({
            'success': False,
            'error': 422,
            'message': "Unprocessible"
        }), 422

    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({
            'success': False,
            'error': 400,
            'message': "Bad Request"
        }), 400

    @app.errorhandler(405)
    def bad_request(error):
        return jsonify({
            'success': False,
            'error': 405,
            'message': "Method not found"
        }), 405

    @app.errorhandler(500)
    def internal_server(error):
        return jsonify({
            "success": False,
            "error": 500,
            "message": "server error"
        }), 500

def register_debug(flask_app):
    if flask_app.debug:
        file_handler = FileHandler('error.log')
        file_handler.setFormatter(
            Formatter(
                '%(asctime)s %(levelname)s:%(message)s [in %(pathname)s:%(lineno)d]')
        )
        flask_app.logger.setLevel(logging.INFO)
        file_handler.setLevel(logging.INFO)
        flask_app.logger.addHandler(file_handler)

def seed_db(app):
    @app.before_first_request
    def create_db_objects():
        # with app.app_context():
        seeder = Seeder()
        seeder.seed()

app = create_app(os.environ.get("FLASK_ENV"))
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)