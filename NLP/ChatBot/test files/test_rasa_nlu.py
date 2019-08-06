from rasa_nlu.model import Interpreter
import json
interpreter = Interpreter.load("./models/nlu/default/restaurantnlu")
message = "I want to find a restaurant in Mumbai"
result = interpreter.parse(message)
print(json.dumps(result, indent=2))
print('******************')
message = "can you find me a restaurant in chennai"
result = interpreter.parse(message)
print(json.dumps(result, indent=2))