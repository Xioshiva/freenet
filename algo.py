import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import JSONResponse
from typing import List
from pydantic import BaseModel, main
import sys
import requests
import yaml


app = FastAPI()

orgn = ["*"]



app.add_middleware(
    CORSMiddleware,
    allow_origins=orgn,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Rocky(BaseModel):
    canvas: List[int]
    number: int

class Pepe(BaseModel):
    canvas: List[int]


@app.get("/")
def read_root():
    return {"I am root"}

@app.post("/ask/")
def train(myRocky: Rocky):
    return {"kek"}

@app.post("/ans/")
def devine(myPepe: Pepe):
    return JSONResponse({"kek"})

def init(key):
    url = node["storage"]
    print(url)
    myobj = {"key": 50}
    #resp = requests.post(url, data = myobj)

def yamlConvert(filename):
    nodes = None
    with open(filename,"r") as file:
        nodes = yaml.load(file, Loader=yaml.FullLoader)
    return nodes

if len(sys.argv) < 3:
    print("Please executecode with:\n")
    print("algo.py file.yaml init/wait opt(val)\n")
    exit
node = yamlConvert(sys.argv[1])
print(node)
print(node['address'])
if __name__ == "__main__":
    uvicorn.run("algo:app", host=node['address'], port=8000, log_level="info")
if sys.argv[-2] == "init":
    init(sys.argv[-1])