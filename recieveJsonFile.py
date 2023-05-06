import base64
import json
from getImageCoordinates import getCoordinates
from encodeDecode import encrypt_message
from lionsFileUtils import deleteFolder,deleteFile,renameFile,createFolder,getCurrentDirPath
from flask import *  
from databaseConnection import getDataFromUniqueValueFromDataBase,countValueMatch,countMatches,insertSingleRecord,update,updateArray,getSingleDataFromDataBase,getAllDataFromDataBase,deleteData,parse_json
app = Flask(__name__)   

def getCoordinatesInDecodedFormate(data):
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

@app.route('/uploadFile', methods = ['POST'])  #
def upload():  
    if request.method == 'POST':  
        responce={}
        tokenId =request.headers.get('Tokenid')
        if countMatches('63e12748f9ad14b21cd15e7f',tokenId) == 1:
            file = request.files['file']
            data=json.load(file)
            responce= getCoordinatesInDecodedFormate(data)
        return responce
        
if __name__=='__main__':
    app.run(host="0.0.0.0")