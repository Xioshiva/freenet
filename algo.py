from fastapi.encoders import jsonable_encoder
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import JSONResponse
from pydantic import BaseModel, main
import sys
import yaml
import requests


app = FastAPI()

orgn = ["*"]

app.parent = ""
app.neigh = []

app.add_middleware(
    CORSMiddleware,
    allow_origins=orgn,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Data(BaseModel):
    key: int
    sender: str
    text: str

class Answer(BaseModel):
    key: int
    sender: str
    text: str

@app.get("/")
def read_root():
    return {"I am root"}

@app.get("/ask")
def ask(data: Data):
    if containsKey(data.key):
        data.sender = app.node['address']
        data.text = "find"
        json_comp = jsonable_encoder(data)
        return JSONResponse(content=json_comp)
    if app.parent == "":
        app.parent = data.sender
        app.neigh = start_serv(data.key)
        for neigh in app.neigh:
            if neigh['address'] == data.sender:
                app.neigh.remove(neigh)
        for neigh in app.neigh:
            resp = sendToNeigh(data.key, neigh)
            print(resp)
            if resp['text'] == "find":
                app.parent = ""
                app.node['storage'].append({'key': resp['key'], 'address':resp['sender']})
                yamlWrite(sys.argv[1], app.node)
                json_comp = jsonable_encoder(resp)
                return JSONResponse(content=json_comp)
    else:
        data.text = "used"
    app.parent = ""
    json_comp = jsonable_encoder(data)
    return JSONResponse(content=json_comp)


def sendToNeigh(key, neigh):
    myobj = {'key': key, 'sender': app.node['address'],'text': "ask" }
    url = "http://" + neigh['address'] + ":8000/ask/"
    resp = requests.get(url, json=myobj)
    data = resp.json()
    return data

def containsKey(key):
    for storedKey in app.node['storage']:
        if storedKey['key'] == key:
            return True
    return False

def yamlWrite(filename,data):
    with open(filename, "w") as file:
        yaml.dump(data, file)

def yamlConvert(filename):
    nodes = None
    with open(filename,"r") as file:
        nodes = yaml.load(file, Loader=yaml.FullLoader)
    return nodes

def listOfNeigh(key):
    neigh = sorted(app.node["storage"], key = lambda i: abs(key - i['key']))
    dynamicLen = len(neigh)
    i = 0
    while i < dynamicLen:
        if neigh[i]['address'] == app.node['address']:
            neigh.pop(i)
            dynamicLen -= 1
        i += 1
    return neigh

def start_serv(key):
    key = key
    neigh = listOfNeigh(key)
    return(neigh)

app.node = yamlConvert(sys.argv[1])
if __name__ == "__main__":
    uvicorn.run("algo:app", host=app.node['address'], port=8000, log_level="info")
if len(sys.argv) < 3:
    print("Please executecode with:\n")
    print("algo.py file.yaml init/wait opt(val)\n")
    exit
if sys.argv[2] == "init":
    key = int(sys.argv[-1])
    if containsKey(key):
        print("Key is here")
    app.parent = "init"
    app.neigh = start_serv(key)
    for neigh in app.neigh:
        resp = sendToNeigh(key,neigh)
        if(resp['text'] == "find"):
            app.node['storage'].append({'key': resp['key'], 'address':resp['sender']})
            yamlWrite(sys.argv[1], app.node)
            break
        print("No key found")