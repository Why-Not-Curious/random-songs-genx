from flask import abort, jsonify, render_template
import json
from main.api_requests import songs_list, InvalidInputException

def configure_routes(app):

    @app.errorhandler(404)
    def not_found(e):
        response = {'error': 'Page not found',
            'details': str(e)}
        jsonify(response)
        return render_template('error.html', title="page", response = response), 404

    @app.route('/random_songs/<int:number>', methods=['GET'])
    def random_songs(number):
        try:
            response = songs_list(number)
            jsonify(response)
            return render_template('random_songs.html', title="page", response = response)
        except InvalidInputException:
            response = {'error': 'Invalid request',
            'details': 'Please enter intiger from 5 to 20.'}
            jsonify(response)
            return render_template('error.html', title="page", response = response)

