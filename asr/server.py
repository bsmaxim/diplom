import argparse
import json
import os
from pathlib import Path, PosixPath
import torch

import nemo.collections.asr as nemo_asr

from flask import Flask, jsonify, request
from flask_cors import CORS

asr_model = None
app = Flask(__name__)
CORS(app, resources={r"/asr/upload_audio": {"origins": "*"}})

MODEL_PATH = "./models/MyAcoustic.nemo"

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

        audio_path = './files/' + file.filename
        file.save(audio_path)

        transcript = decrypt(audio_path)

        if len(transcript) == 0:
            return jsonify({"text": "Ответ пуст"})

        return jsonify({'text': transcript})

    return 'NO RESPONSE', 200


def load_model(path: str):
    global asr_model
    asr_model = nemo_asr.models.EncDecCTCModel.restore_from(path)
    asr_model.cuda()


def decrypt(audio_path: str):
    global asr_model
    if asr_model == None:
        return ""
    return asr_model.transcribe(
        paths2audio_files=[audio_path], batch_size=20)[0]


if __name__ == '__main__':
    load_model(MODEL_PATH)
    app.run(debug=True)
    print("SERVER STARTED")
