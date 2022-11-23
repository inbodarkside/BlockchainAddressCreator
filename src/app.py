from flask import Flask, jsonify, request
import logging
import json
import os
import configparser
from addressCreator import createNewAddress

logging.basicConfig(level=logging.INFO)
dirname = os.path.dirname(__file__)
cfile = os.path.join(dirname, '../config.ini')

app = Flask(__name__)
config = configparser.ConfigParser()
config.read(cfile)


@app.route("/createAddress", methods=['POST'])
def createAddress():
    data = {}
    password = request.get_json()
    pkey, words, pukey = createNewAddress(config['BLOCKCHAIN']['MnemoLanguage'], config['BLOCKCHAIN']['Provider'],
                                          password['password'])
    logging.info("New Address created")


    return jsonify(PrivateKey=pkey, MnemonicPhrase=words, PublicKey=pukey)
