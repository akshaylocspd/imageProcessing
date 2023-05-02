import base64
import json

# Read the PNG files
with open('A.jpg', 'rb') as f:
    a_png = f.read()
with open('B.jpg', 'rb') as f:
    b_png = f.read()

# Encode the PNG files to Base64 strings
a_base64 = base64.b64encode(a_png).decode('utf-8')
b_base64 = base64.b64encode(b_png).decode('utf-8')

# Write the Base64 strings to a JSON file
data = {'a': a_base64, 'b': b_base64}
with open('data.json', 'w') as f:
    json.dump(data, f)
