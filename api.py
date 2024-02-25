from flask import Flask, request, jsonify
from geopy.geocoders import Nominatim

app = Flask(__name__)
geolocator = Nominatim(user_agent="my_geocoder")

@app.route('/api', methods=['GET'])
def get_coordinates():
    try:
        address = request.args.get('adresse')
        location = geolocator.geocode(address, timeout=30)
        if location:
            latitude, longitude = location.latitude, location.longitude
            return jsonify({"latitude": latitude, "longitude": longitude})
        else:
            return jsonify({"error": "Adresse introuvable"})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
