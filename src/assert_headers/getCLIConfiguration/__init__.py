#!/usr/bin/env python
# -*- coding: utf-8 -*-


from .getJsonConfiguration import getJsonConfiguration
from .getYamlConfiguration import getYamlConfiguration

def getCLIConfiguration(configurationPath):
    # if file ends in .yml or .yaml
    if configurationPath.endswith(".yml") or configurationPath.endswith(".yaml"):
        return getYamlConfiguration(configurationPath)
    else:
        return getJsonConfiguration(configurationPath)
