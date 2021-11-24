import yaml
import socket
import threading
import json
import sys


def yamlConvert(filename):

    nodes = None

    with open(filename,"r") as file:
        nodes = yaml.load(file, Loader=yaml.FullLoader)

    test = []

    for node in nodes:
        nouveau = Node(node["id"],None,node["address"])
        for neighbour in node["neighbours"]:
            nouveau.addNeighbour(Neighbour(neighbour["id"],neighbour["address"]))
        test.append(nouveau)

    return test