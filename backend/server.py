from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/asr/upload_audio": {"origins": "*"}})


@app.route('/asr/upload_audio', methods=['GET', "POST", "OPTIONS"])
def upload_file():
    if request.method == 'OPTIONS':
        return '', 200
    elif request.method == 'POST':
        if 'file' not in request.files:
            return 'No file part'

        file = request.files['file']

        if file.filename == '':
            return 'Файл не выбран', 200


        file.save('./files/' + file.filename)

        text = "Ответ есть"

        return jsonify({'text': text})

    return 'NO RESPONSE', 200


if __name__ == '__main__':
    app.run(debug=True)
