from deeppavlov import build_model
from deeppavlov.utils.server import start_model_server

import json
with open('bert_api/data/model_config.json') as f:
  data = json.load(f)



def main():
    start_model_server(data)


#COMMANDS
#python -m deeppavlov riseapi bert_api/data/model_config.json -b 2 or #poetry run script
#curl -X POST "http://0.0.0.0:5000/model" -H "accept: application/json" -H "Content-Type: application/json" -d "{\"x\":[\" \"]}"