import json

def save(data,filename):
    database = open(filename+".json", "wt")
    json_string = json.dumps(data, indent="     ")
    database.write(json_string)
    database.close()