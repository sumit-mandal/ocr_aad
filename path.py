import json
input_file = open('info.json','r')
json_decode = json.load(input_file)

jsonData = json_decode["Adhaar Number"]
