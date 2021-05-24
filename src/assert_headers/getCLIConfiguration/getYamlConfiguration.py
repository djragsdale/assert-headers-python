import yaml

def getYamlConfiguration(configurationPath):
    configuration = {}
    with open(configurationPath, "r") as f:
        configuration = yaml.safe_load(f)
        return configuration
