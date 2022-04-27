from flask import abort, jsonify
from main.api_requests import songs_list

def configure_routes(app):

    @app.errorhandler(404)
    def resource_not_found(e):
        return jsonify(error=str(e)), 404

    @app.route('/random_songs/<int:number>', methods=['GET'])
    def random_songs(number):
        response = songs_list(number)
        if response is None:
            abort(404, description="Something went wrong")
        return response

    @app.route('/hello')
    def hello():
        return 'hello'