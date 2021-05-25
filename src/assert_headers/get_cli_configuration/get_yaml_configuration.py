import yaml

def get_yaml_configuration(configuration_path):
    configuration = {}
    with open(configuration_path, "r") as file:
        configuration = yaml.safe_load(file)
        return configuration
