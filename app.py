from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///locations.db'
db = SQLAlchemy(app)

class Location(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    latitude = db.Column(db.String(50), nullable=False)
    longitude = db.Column(db.String(50), nullable=False)
    timestamp = db.Column(db.String(50), nullable=False)

@app.route('/api/track', methods=['POST'])
def track():
    data = request.json
    new_location = Location(latitude=data['latitude'], longitude=data['longitude'], timestamp=data['timestamp'])
    db.session.add(new_location)
    db.session.commit()
    return jsonify(success=True)

@app.route('/api/locations', methods=['GET'])
def get_locations():
    locations = Location.query.all()
    return jsonify([{'latitude': loc.latitude, 'longitude': loc.longitude, 'timestamp': loc.timestamp} for loc in locations])

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Создание всех таблиц
    app.run(debug=True, host='0.0.0.0', port=5000)
