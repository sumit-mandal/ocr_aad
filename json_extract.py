import json
input_file = open('info.json','r')
json_decode = json.load(input_file)

print(json_decode)

jsonData = json_decode["ID Type"]
print(jsonData)
