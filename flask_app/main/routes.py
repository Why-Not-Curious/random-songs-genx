from flask import abort, jsonify, render_template
import json
from main.api_requests import songs_list, InvalidInputException

def configure_routes(app):

    @app.errorhandler(404)
    def resource_not_found(e):
        return jsonify(error=str(e)), 404

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
            return render_template('out_of_range.html', title="page", response = response)

