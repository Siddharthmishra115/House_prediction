from flask import Flask, request, jsonify
# from flask_cors import CORS  # ← import this
import util


app = Flask(__name__)
# CORS(app, resources={r"/*": {"origins": "*"}}, supports_credentials=True)

### Task one :- To return the location
@app.route('/get_location_names', methods = ['GET'])
def get_location_names():
    response = jsonify({
        'locations': util.get_location_names()
    })

    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/predict_home_price', methods = ['GET', 'POST'])
def predict_home_price():
    total_sqft = float(request.form['total_sqft'])
    locations = request.form['location']
    bhk = int(request.form['bhk'])
    bath = int(request.form['bath'])

    response = jsonify({
        'estimated_price': util.get_estimated_price(locations, total_sqft, bhk, bath)
    })

    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


if __name__ == "__main__":
    print("Starting python Flask Server for house price prediction.......")
    util.load_saved_artifacts()
    app.run()
