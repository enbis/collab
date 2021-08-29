import yaml
import logging
from flask import Flask, jsonify

#read config as cfg
with open("configs/config.yml", "r") as ymlfile:
    cfg = yaml.load(ymlfile, Loader=yaml.FullLoader)
#flask application instance
app = Flask(__name__)

@app.route('/add')
def value():
    response = jsonify({'response': 'ok'})
    response.status_code = 200
    return response

if __name__ == "__main__":
    logger = logging.basicConfig(level=logging.INFO)
    logging.info('Launching webserver...')
    app.run(host=cfg["webserver"]["host"], port=cfg["webserver"]["port"])