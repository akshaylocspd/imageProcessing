from flask import Flask, request, jsonify
import base64
import json
from getImageCoordinates import getCoordinates
from encodeDecode import encrypt_message
app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return "Api...."


@app.route('/post_json_data', methods=['POST'])
def post_json_data():
    # Get the JSON data from the request
    data = request.get_json()
    base64_string_a = data['a']
    base64_string_b = data['b']

    # Decode base64 strings to bytes
    img_data_a = base64.b64decode(base64_string_a)
    img_data_b = base64.b64decode(base64_string_b)
    center=getCoordinates(img_data_a,img_data_b)
    print(center)
    msg="x="+str(center[0])+" y="+str(center[1])
    msg=encrypt_message(message=msg)
    # Return a JSON response
    response = {'message': msg}
    return jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)