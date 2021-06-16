from deeppavlov import build_model
import json
with open('bert_api/data/model_config.json') as f:
  data = json.load(f)



def main():
    model = build_model(data)
    return model


#COMMANDS
#python -m deeppavlov riseapi bert_api/data/model_config.json -b 2
#curl -X POST "http://0.0.0.0:5000/model" -H "accept: application/json" -H "Content-Type: application/json" -d "{\"x\":[\" \"]}"