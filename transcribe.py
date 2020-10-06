from flask import Flask, request
from PIL import Image
import pytesseract
import os
import urllib.request
import uuid

app = Flask(__name__)

@app.route('/health')
def health():
    return 'Health is wealth'

@app.route('/transcribe', methods=['GET'])
def get_transcription():
    url = request.form.get('image_url')
    filename = str(uuid.uuid4()) + '.jpg'
    urllib.request.urlretrieve(url, filename)
    text = pytesseract.image_to_string(Image.open(filename))
    os.remove(filename)
    return text

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
# urllib.request.urlretrieve('https://imgur.com/gallery/h2KlKTJ', 'test.jpg')

# print(pytesseract.image_to_string(Image.open('test.jpg')))
