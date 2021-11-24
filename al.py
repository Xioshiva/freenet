import yaml
import socket
import threading
import json
import sys


def yamlRead(filename):

    nodes = None

    with open(filename,"r") as file:
        nodes = yaml.load(file, Loader=yaml.FullLoader)
    return nodes

def yamlWrite(filename,data):
    with open(filename, "w") as file:
        yaml.dump(data, file)
        

    
if __name__ == "__main__":
  
    a = yamlRead("d.yaml")
    print(a)
    a['address'] = "127.0.0.4"
    yamlWrite("d.yaml", a)
    print(a)
    a = yamlRead("d.yaml")
    print(a)