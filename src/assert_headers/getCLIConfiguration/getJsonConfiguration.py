import json

def getJsonConfiguration(configurationPath):
    configuration = {}
    with open(configurationPath, "r") as f:
        configurationStr = f.read()
        configuration = json.loads(configurationStr)
        return configuration
