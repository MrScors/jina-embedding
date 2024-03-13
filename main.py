import os
import torch
import socket

from transformers import AutoModel
from array import array
from flask import Flask, request

# cos_sim = lambda a: norm(a)

app = Flask(__name__)
model = AutoModel.from_pretrained('./model/jina-embeddings-v2-base-en', trust_remote_code=True)


@app.route('/get-embedding', methods=['POST'])
def add_income():
    text = request.get_json()['text']
    value = array('f', model.encode([text]).tolist()[0])
    print(text)
    print(value.__len__())
    print(value.tolist())
    return value.tolist(), 200

app.run(debug=True, host='localhost', port=8080)



