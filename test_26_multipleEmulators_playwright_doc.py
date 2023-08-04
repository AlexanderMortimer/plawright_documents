import json



path_of_devices = 'vevn\Lib\site-packages\playwright\driver\package\lib\server\deviceDescriptorsSource.json'
with open(path_of_devices) as json_deader:
    data = json.load(json_deader)
print(data)