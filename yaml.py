import yaml
import socket
import threading
import json
import sys


def yamlConvert(filename):

    nodes = None

    with open(filename,"r") as file:
        nodes = yaml.load(file, Loader=yaml.FullLoader)
    return nodes




    