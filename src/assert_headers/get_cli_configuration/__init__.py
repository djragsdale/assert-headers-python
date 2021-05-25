#!/usr/bin/env python
# -*- coding: utf-8 -*-


from .get_json_configuration import get_json_configuration
from .get_yaml_configuration import get_yaml_configuration

def get_cli_configuration(configuration_path):
    # if file ends in .yml or .yaml
    if configuration_path.endswith(".yml") or configuration_path.endswith(".yaml"):
        return get_yaml_configuration(configuration_path)
    
    return get_json_configuration(configuration_path)
