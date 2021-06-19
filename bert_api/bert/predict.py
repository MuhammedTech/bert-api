from deeppavlov import build_model
from deeppavlov.utils.server import start_model_server

import json
with open('bert_api/data/model_config.json') as f:
  data = json.load(f)



def main():
    start_model_server(data, port=5001)