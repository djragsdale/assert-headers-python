import json

def get_json_configuration(configuration_path):
    configuration = {}
    with open(configuration_path, "r") as file:
        configuration_str = file.read()
        configuration = json.loads(configuration_str)
        return configuration
