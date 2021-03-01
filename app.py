from flask import Flask, request, jsonify
from flask_cors import CORS
from .config import CONFIGS
from .extensions import db

def create_app(mode=None):
    # create and configure the app
    if not mode:
        mode = 'Default'

    app = Flask(__name__)
    app.config.from_object(CONFIGS[mode])
    CORS(app)

    # register dependencies
    register_extensions(app, mode)
    
    register_errorhandlers(app)
    return app

def register_extensions(app, mode):
    db.init_app(app)
    migrate.init_app(app)

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