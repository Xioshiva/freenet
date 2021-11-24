import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import JSONResponse
from typing import List
from pydantic import BaseModel


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

@app.post("/train/")
def train(myRocky: Rocky):
    return {"kek"}

@app.post("/predict/")
def devine(myPepe: Pepe):
    return JSONResponse({"kek"})
